                                        Saucedemo Test Automation 

                                                 Overview
The repository contains an automated test suite for the Saucedemo application using Playwright with Python. The test suite can be used for assessing both manual and automation testing experience through a variety of tests for example, sorting products, ordering by price, and checking out.

                                                Prerequisites
Before you can run the test suite, please ensure you have the following installed:

Python 3.7 or higher 
Pip (Python package installer)
Node.js (required by Playwright)
 
                                      Install the required packages with pip

Terminal
pip install -r requirements.txt

                                                 Configuration

if you need to, please edit the config/config.py file to add the test credentials that you would like to use for the testing and the base url as needed. 

                                               Running Test Cases

To Run in Headless Mode set headless=True(In All the Script)
Use "pytest  -v -s --alluredir=allure-results tests/" (It will run all the Test Cases Present in test suite)
To View the Report "allure serve allure-results" --> after that also enter "allure generate --clean allure-results -o allure-report" in Terminal (Prerequisites - Java and Allure has to be configured in Environmental variables)
Navigate to "allure-reports" find "index.html" Open in Browser

