# Databases-Advanced

This scraper is made to use on a Ubuntu 20.04 system (VM)
We need python and some libraries to be able to run this script. Python3 (version 3.8.5) should be installed by default on this Ubuntu version.

To be able to run this script use this commands in your terminal to install the right libraries:

to install pip3:

	sudo apt install python3-pip

to install bs4:

	pip3 install bs4
	
to install numpy:

	pip3 install numpy
	
to install pandas:

	pip3 install pandas
	
to install lxml:

	pip3 install lxml

to install pymongo
	pip3 install pymongo
	
this script will scrape BTC transactions from blockchain every minute and pushes the largest transaction to a log file (results.txt).
to stop the script press CTRL + C. 
