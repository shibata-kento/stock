import requests
from bs4 import BeautifulSoup
import csv
import json


class Settings:

    def bs_settings(self, url):
        req = requests.get(url)
        html = BeautifulSoup(req.content, 'html.parser')

        return html

    def csv_reader(self, csv_path):
        with open(csv_path) as f:
            reader = csv.reader(f)
            stock_number = [row[0] for row in reader]

        return stock_number

    def csv_writer(self, filename, all_stock):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['Brand Number', 'Brand Name', 'Stock Market'])
            for single_stock in all_stock:
                writer.writerow(single_stock)

    def csv_writer2(self, dfilename, stock_data):
        header = ['stock_number', 'open_price', 'high_price', 'low_price', 'dividend_yield', 'share_unit_number', 'per', 'psr', 'pbr', 'volume', 'market_capitalization', 'number_os_issued_shares', 'stockholder', 'preferential_yield', 'diviidend_yield', 'minumum_stock', 'vesting_month', 'vesting_day']
        with open(dfilename, 'w', newline='') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(header)
            for data in stock_data:
                writer.writerow(data)

