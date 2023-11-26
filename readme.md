Python Script for Web Scraping and Automation

Purpose of the Script:
The purpose of this script is to scrape data from the Audi website and extract information about new cars. It retrieves the name, price, and link for website of image for each car and stores the data in a CSV file in order to organize it !


To run the script, you need to follow these steps:

1)Install the necessary dependencies:

requests: This library is used to send HTTP requests to the website. You can install it by running the following command:
pip install requests

BeautifulSoup: This library is used to parse the HTML content of the website. You can install it by running the following command:
pip install beautifulsoup4

csv: This library is used to write data to a CSV file. It is a built-in library in Python and does not require installation.

schedule: This library is used to schedule the script to run at a specific time. You can install it by running the following command:
pip install schedule

2)Import the required libraries:

requests
BeautifulSoup
csv
schedule
time


2)Define the scrape_data function:

This function sends a GET request to the Audi website and retrieves the HTML content.
It then creates a BeautifulSoup object to parse the HTML.
Next, it finds all the car elements on the page using the specified class name.
It creates a CSV file to store the extracted data and writes the column headers.
It iterates over each car element n the car_elements list. 
For each car_element, it extracts the name, price, and website link for the image by using the find method of the car_element object. 
If the price is not displayed on the website(this is the case for many cars on the audi website),  it sets the price to 'not found'.
The extracted data is then written to the CSV file using the csv_writer.writerow m .
Finally, the CSV file is closed.

3)Schedule the script to run daily at a specific time:

The script uses the schedule library to schedule the scrape_data function to run daily at 8:00 AM.
The while True loop ensures that the script keeps running and checks for scheduled tasks to execute.
The schedule.run_pending() function checks if there are any pending tasks to run.
The time.sleep(1) function adds a delay of 1 second between each iteration of the loop.

4)Save the script in a Python file with a .py extension, for example, web_scraping.py or car_scraper.py.

Open a terminal or command prompt and navigate to the directory where the script is saved.

Run the script by executing the following command:
python car_scraper.py

The script will start running and will scrape the data from the Audi website daily at 8:00 AM.

