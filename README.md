# 🕷🕸 Funpay Parser

## Star the Project
If you find this project useful, please consider giving it a star on GitHub. This helps to raise awareness of the project and encourage more people to use and contribute to it.

## Description
The Funpay Spider is a web scraper built with Scrapy that extracts information about lots on the [https://funpay.com/](https://funpay.com/) marketplace. The spider prompts the user to enter the URL of the lot they want information about and then scrapes data from the lot's page, including the username of the seller, the price of the lot, the unit of the price, the amount of items the seller has for sale, the description of the lot, the number of 5-star ratings the seller has received, and whether the seller is on-site or off-site.

## Stack:
[![Python 3.10](https://img.shields.io/badge/Python%203.9-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-0E67df?style=for-the-badge&logo=scrapy&logoColor=white)](https://scrapy.org/)

## Installation
To use the Funpay Spider, you must first clone the repository from GitHub:
```
git clone https://github.com/chyornyy/funpay-parser.git
```
Create a virtualenv:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip3 install --upgrade pip
```
Install Scrapy and tqdm. You can do this by running the following command in your terminal:
```
pip3 install -r requirements.txt
```

## Usage
```
cd funpay
```
To use the Funpay Spider, run the following command in your terminal:
```
scrapy crawl funpay
```
The spider will prompt you to enter the URL of the lot you want information about. Once you enter the URL, the spider will scrape the data and print it to your terminal. If you want to save the data to a file, you can use the following command:
```
scrapy crawl funpay -O funpay.json
```
This will save the data in JSON format to a file called output.json.

## Contributing
If you want to contribute to the Funpay Spider, feel free to submit a pull request or open an issue on GitHub.
Or you can contact me in telegram: [@chyornxx](t.me/chyornxx)

## License
Project is released under the MIT license.

## Development Team:
#### [Aleksandr Chyornyy](https://github.com/chyornyy) - Backend