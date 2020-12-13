import requests
from bs4 import BeautifulSoup
import csv


class Crawler:

    def __init__(self):
        pass

    def brand_name_get(self):
        all_stock = []
        for page in range(100):
            brand_url = f'http://www.morningstar.co.jp/StockInfo/sec/list?code=1000&code_detail=&page={page}'
            brand_filename = 'brand_list.csv'
            req, soup, html = self.bs_settings(brand_url)
            req = requests.get(brand_url)
            html = BeautifulSoup(req.content, 'html.parser')
            data = html.find_all('td', class_='tac')
            stock = []
            for tmp in data:
                if len(stock) < 3:
                    stock.append(tmp.get_text())
                else:
                    all_stock.append(stock)
                    stock = []
                    stock.append(tmp.get_text())

        print(all_stock)
        self.csv_writer(brand_filename, all_stock)

    
    def stock_data(self, ):
        pass

    def bs_settings(self, url):
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        html = BeautifulSoup(req.content, 'html.parser')

        return req, soup, html


    def csv_writer(self, filename, all_stock):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['Brand Number', 'Brand Name', 'Stock Market'])
            for single_stock in all_stock:
                writer.writerow(single_stock)





if __name__ == '__main__':

    crawler = Crawler()
    word = crawler.brand_name_get()

