import smtplib
import argparse
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders

"""
Configuration parameters
"""

# List of recipients is passed from Jenkins as command line parameter.  
parser = argparse.ArgumentParser()
parser.add_argument('-e','--email', type=str, help='Emails of user to whom config should be sent separated with space', required=True)

args = parser.parse_args()

def sendMail(sender, recievers, message):
    s = smtplib.SMTP(host='aws.smtp.trans.ge.com', port=25) 
    emailBody = MIMEMultipart()
    emailBody['Subject'] = 'Cluster config'
    emailBody['From'] = sender
    emailBody['To'] = ','.join(recievers)
    emailBody['CC'] = 'armando.paz1@ge.com'
    
    body = MIMEText(message)

    emailBody.attach(body)

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("/etc/kubernetes/admin.conf", "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="admin.conf"')

    emailBody.attach(part)

    s.sendmail(sender, recievers, emailBody.as_string())
    print("Successfully sent email")



def main(): 
    emails = args.email.split(',')
    resultData = 'Attached is the configuration file for cluster that was ordered by you through automated Jenkins job.\nAt the time email is recieved cluster should be operational. Worker nodes might still be creating and should be ready in few minutes.\nIf you have not requested this cluster, please contact infra admin of your team immediately.\n\nHave fun,\nInfrastructure team'
    sendMail('armando.paz1@ge.com@ge.com', emails, resultData)

main()
