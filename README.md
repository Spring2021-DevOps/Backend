# Uber-Python
Repository for Python Application

Steps to install mongodb on MacOS
brew tap mongodb/brew
brew install mongodb-community@4.4
brew services start mongodb-community@4.4
mongo
use Uber
gunicorn -w 4 -b 0.0.0.0:5000 booking:app