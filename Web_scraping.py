#To incorporate automation and schedule the script to run at specific intervals, you can use the `schedule` library in Python. Here's an example of how you can modify your code to schedule the script to run daily:


import requests
from bs4 import BeautifulSoup
import csv
import schedule
import time

def scrape_data():
    # Send a GET request to the URL
    url = "https://www.audi.de/de/brand/de/neuwagen.html"
    response = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the car elements on the page
    car_elements = soup.find_all('div', class_='CardStyles__StyledCard-sc-z3urmd-0 fPmAQa')
    # Create a CSV file to store the extracted data
    csv_file = open('car_data.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Car Name', 'Price', 'Image Website'])

    # Extract the name, price, and image website for each car
    for car_element in car_elements:
        name = car_element.find('p').text.strip()
        print(name)
        try:
            price = car_element.find('p', class_="auir-85a2d0c-StyledText-auir-85a2d0c-j31299 hFtWmx").text.strip()
        except:
            print('not available')
            price='not found'
        print(price)
        image_website = car_element.find('img')['src']
        csv_writer.writerow([name, price, image_website])

    # Close the CSV file
    csv_file.close()

# Schedule the script to run daily at a specific time
schedule.every().day.at("08:00").do(scrape_data)

while True:
    schedule.run_pending()
    time.sleep(1)


