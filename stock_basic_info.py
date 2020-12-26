import os
from settings import Settings

filename = 'brand_list.csv'

class BasicInfomation():
    setting = Settings()

    def brand_name_get(self):
        all_stock = []
        for page in range(100):
            brand_url = f'http://www.morningstar.co.jp/StockInfo/sec/list?code=1000&code_detail=&page={page}'
            html = self.setting.bs_settings(brand_url)
            data = html.find_all('td', class_='tac')
            stock = []
            for tmp in data:
                if len(stock) < 3:
                    stock.append(tmp.get_text())
                else:
                    all_stock.append(stock)
                    stock = []
                    stock.append(tmp.get_text())

        self.setting.csv_writer(filename, all_stock)

if __name__ == "__main__":
    stock = BasicInfomation()
    stock.brand_name_get()
    
    