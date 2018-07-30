import urllib.request as req
from bs4 import BeautifulSoup


def get_date():
    _url = "https://www.federalreserve.gov/feeds/Data/H15_H15_RIFLGFCY30_N.B.XML"
    _res = req.urlopen(url)
    _soup = BeautifulSoup(_res, "lxml")
    d = _soup.item
    return d.find("dc:date").string


date_str = get_date()
date_str = date_str[0:10]
print(str)


class XMLProcess:
    raw_data: str

    def __init__(self, _url):
        self.res = req.urlopen(_url)
        self.soup = BeautifulSoup(self.res, "lxml")
        self.data = self.soup.item

    # 加工してないデータを入手
    def get_raw_data(self, tag):
        # tag:検索対象のタグ
        return self.data.find(tag).string

    # start文字目からend文字目まで切り取る。
    def get_cut_data(self, tag, start, end):
        # start:N文字目から切り取りたい場合、startにはN-1が入ることに注意。
        # end:同様。M-1文字目まで切り取る
        self.raw_data = self.get_raw_data(tag)
        self.cut_data = self.raw_data[start:end]
        return self.cut_data

    def get_float_data(self, tag):
        # float型に直したデータを取得
        self.raw_data = self.get_raw_data(tag)
        self.num_data = float(self.raw_data)
        return self.num_data


url = "https://www.federalreserve.gov/feeds/Data/H15_H15_RIFLGFCY30_N.B.XML"
XML = XMLProcess(url)
raw_date = XML.get_raw_data("dc:date")
print(raw_date)
str_date = XML.get_cut_data("dc:date", 0, 10)
print(str_date)
interest_rate = XML.get_float_data("cb:value")
print(interest_rate)
XML = None
