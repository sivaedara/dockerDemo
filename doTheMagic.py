import robin_stocks.robinhood as rh
import pandas as pd
import yfinance as yf
import numpy as np
from yahoo_fin import stock_info as si


def loginToRH():
    #login
    login = rh.login('username','password')

# Login and get top stocks at this point of time
def getTopStocks():

    loginToRH()

    # get topmovers from robinhood
    df= pd.DataFrame(rh.get_top_movers())
    #df= pd.DataFrame(rh.get_top_100())                     # to get top 

    #print (df)

    # wtite data to a csv file if required
    df.to_csv("output.csv")

    # Decide the +ve retutn and -ve return stocks
    df['result'] = np.where((df['last_trade_price'].astype(float)-df['previous_close'].astype(float))>0, "good", "bad")

    #seperate all +ve return stocks to new dataframe
    df=df[df["result"]=="good"]

    # Fetch only required columns
    df=df[["symbol","previous_close","last_trade_price","result"]]

    # Calculate return of inverstment in percentage
    df = calCurInvestmentReturn(df)

    df=df.sort_values(by='returnInvestment',ascending=False)

    #df=df.sort_values(by='last_trade_price',ascending=False)

    # Print the final DF
    #print (df)

    processData(df)


def processData(df):
    try:
        print ("Processing data" + '\n')
        
        # Less than 5 
        lessThan5df=df[df["previous_close"].astype(float)<=5.0]
        printDfWithMsg(lessThan5df,"Stocks with less than 5$ today")
        
        # less than 10 and greater than 5 
        lessThan10df=df[(df["previous_close"].astype(float)>5.0) & (df["previous_close"].astype(float)<=10.0)]
        printDfWithMsg(lessThan10df,"Stocks with greater than 5$ and less than 10$")

        # less than 15 and greater than 10 
        lessThan15df=df[(df["previous_close"].astype(float)>10.0) & (df["previous_close"].astype(float)<=15.0)]
        printDfWithMsg(lessThan15df,"Stocks with greater than 10$ and less than 15$")


    except Exception as e:
        print ("Cmg to exception")
        print (str(e))


def printDfWithMsg(df,msg):
    print (msg)
    print (df)
    print ('\n')

def findProfitTest(df,stockNumber):
    """ This is an sample calculator """

    

def calCurInvestmentReturn(df):
    """ Calculate current investment return based on yesterdays closing""" 
    df["returnInvestment"]=  ((df["last_trade_price"].astype(float) - df["previous_close"].astype(float))/df["previous_close"].astype(float))*100
    return df
    

def getMyCurrentStocks():
    loginToRH()
    totallistOfStocks=pd.DataFrame(rh.get_all_open_stock_orders())
    totallistOfStocks.to_csv("totalstocks.csv")


def setLimit():
    loginToRH()

def printStockHistory():
    # Column is regularMarketOpen
    result=si.get_quote_data('BKD')
    for key, value in result.items():
        if key == "regularMarketOpen":
            print(value)


def main():
    getTopStocks()
    #getMyCurrentStocks()
    #printStockHistory()

if __name__ == "__main__":
    main()


