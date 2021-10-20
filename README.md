# dockerDemo
Pre-req: Vagrant boxes already set up in your local machines or any linux machine

Note:We are installing docker only in our build server, rest of servers we are going to use ansible playbooks
https://github.com/sivaedara/vagrantBoxes

To run some commans vagrant user might not be good enough so make sure to switch to root user

*su root*

## Steps to install docker:
-- This will fetch docker packages and dependencies from redhat and install docker

*yum install docker -y*

-- This command will start docker

*systemctl start docker*

-- This command will ensure docker to start after any system restarts.

*systemctl enable docker*

-- To view and tail docker logs

*journalctl -f -u docker*

## Docker commands
-- To list docker images

*docker images*

-- to list all docker containers

*docker ps -a*

### Make sure you have soem basic understanding about these concepts
Why Docker

Adavantages

Docker Images and tags

Docker Containers

what is DockerFile

How to write Dockerfile (layers)

DockerHub and localReistry

Volumes

Delete Images and containers


