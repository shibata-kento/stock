import os
from settings import Settings

dir_path = os.path.join(os.path.dirname(__file__))
filename = 'brand_list.csv'
dfilename = 'detail_info.csv'
csv_path = f'{dir_path}\{filename}'
tmp = ','.join(csv_path)
tmp = tmp.replace('\\', '/')
csv_path = tmp.replace(',', '')


class DetailedInfomation():
    setting = Settings()
    
    def stock_data(self):
        stock_list = self.setting.csv_reader(csv_path)
        stock_data = []
        for stock_number in stock_list[1:]:
            base_url = f'https://minkabu.jp/stock/{stock_number}/'
            html = self.setting.bs_settings(base_url)
            dd = html.find_all('dd')
            stock = [stock_number]
            for cnt, data in enumerate(dd[:-1]):
                stock.append(data.get_text())
                if data.get_text() != '---' and cnt == 11:
                    stock = self.stock_holder(base_url, stock)
            stock_data.append(stock)
            stock = []
            # print(f'{stock_number}finished.')
        self.setting.csv_writer2(dfilename, stock_data)

    def stock_holder(self, base_url, stock):
        total = 0.0
        url = f'{base_url}yutai'
        html = self.setting.bs_settings(url)
        td = html.find_all('td', class_='tar')
        for ydata in td[1:3]:
            ydata = ydata.get_text().replace('\n', '')
            stock.append(ydata)

            try:
                total += float(ydata[:-1])
            except ValueError:
                pass

        stock.append(f'{total:.2f}%')
        print(f'{total:.2f}%')
        for ydata in td[4:6]:
            ydata = ydata.get_text().replace('\n', '')
            stock.append(ydata)

        return stock

                

if __name__ == "__main__":
    stock = DetailedInfomation()
    stock.stock_data()