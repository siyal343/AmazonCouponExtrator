# Amazon Coupon Scrapper

## Intro
### This script scrapes coupons from Amazon using the product ASINs.

## Setup
### 1. You need to have following
- A Widnows Operating System.
- Python (version 3.11) installed.
- Microsoft Edge webdrivers (version of the webdrivers will be correspond to Edge Browser version) i.e. You can find the Edge browser version in the burger menu *About*.
- Get Edge webdrivers from (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- Place the webdrives in somewhere you have full permission
- Add the webdriver exe. in the Path Enviornment Variable.

Thats it the setup to Run the script is complete.

## Script Running and Confuguration
Before running the script you have to do the following.

- Place your ASIN list in .csv formate in the same directory as the script.
- Make sure data in your .csv file is layed out the same way as the "url_data.csv". The "url_data.csv" file is shared for reference.
- After placing your .csv file rename it to "url_data.csv" and the old "url_data.csv" to something else.
- Open a Terminal (PowerShell, CMD etc.) and navigate to the script directory.
- run the following command.
    
    `python --version`

- If there is an error, please install and setup the Python (you may have to add it to the path). 
- If it returns with a python version like below, you are good to go.

    `Python 3.11.1`

- Next Run the following command into your Terminal. This command will install all the required dependencies.
    
    `pip install -r requirements.txt`

- When the installations of the dependencies simply run following command in your Terminal.

    `python .\AmazonCoupons_working.py`

- This will start the script and automate the Edge browser to open the Amazon.com and start scraping(Do not close the terminal or the Edge Windows).

- When the Script finish its scraping it will show the following message in the Terminal.

    `Finished Scraping! You can see the coupons in the Coupons.csv file.`

- Now you can close both the Edge Browser window and the Terminal.


