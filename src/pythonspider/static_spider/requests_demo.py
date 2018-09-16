import requests, sys
from bs4 import BeautifulSoup


class Downloader:
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []  # 章节名称
        self.urls = []  # 章节连接
        self.nums = []  # 章节数

    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html, features="html.parser")
        divs = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(divs[0]), features="html.parser")
        all_a = a_bf.find_all('a')
        self.nums = len(all_a[15:])
        for each in all_a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        # print(target)
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html,features="html.parser")
        texts = bf.find_all('div', class_='showtxt')
        text = texts[0].text.replace('\xa0' * 8, '')
        # print(text)
        return str(text)

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'w', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n')


if __name__ == '__main__':
    dl = Downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
        print("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        # sys.stdout.flush()
    print("《一年永恒》下载完成")
