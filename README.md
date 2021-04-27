# Uber-Python
Repository for Python Application

##Steps to install mongodb on MacOS
##brew tap mongodb/brew
##brew install mongodb-community@4.4
##brew services start mongodb-community@4.4
##sudo vi /etc/mongod.conf -> net bindIP 0.0.0.0
##brew services restart mongodb-community@4.4
##Open TCP 27017 on EC2
##mongo
##use Uber

##gunicorn -w 4 -b 0.0.0.0:5000 booking:app

--

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
ubuntu 18
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update -y
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl status mongod
sudo vi /etc/mongod.conf
sudo systemctl restart mongod


Adding new instance
sudo apt-get update
sudo apt install npm

sudo apt-get install python3
sudo apt install python3-pip
sudo apt install gunicorn
sudo apt-get install python3-venv
python3 -m venv env
source env/bin/activate
 
 
 
 
Python Flask Backend:

To test locally : 
pip3 install -r requirements.txt
python3 wsgi.py


Local Unit tests:

"python3 -m pytest ./tests"

The application can be run on an AWS instance using the terraform script

Setup Python backend on AWS:
​

Pre-requisite
Follow the readme in https://github.com/Spring2021-DevOps/Terraforms/EKS to setup initial resources​

Setup EKS cloudbuild i. Go to AWS 

ii. Select the AWS Codebuild service 

iii. Create Build Project

iv. Select "Connect using OAuth", and click Connect to Github and allow access to GitHub repo for Backend

v. Set a timeout of 10 minutes, and setup AWS_ACCOUNT_ID and AWS_REGION

vi. Setup the environment to use Ubuntu along with the service role created for codebuild

vii. Select "Use a Buildspec file" to use the buildspec.yml file that is in the root folder, and start the build

viii. The codebuild CI/CD will make the deployment

Copy the load balancer address that is created, and add it to the Dockerfile for the frontend, to be able to access through the ENV variable.
To test the /health endpoint, copy the load balancer Address, and check the /health endpoint. 
