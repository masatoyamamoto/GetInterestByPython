import urllib.request as req
from bs4 import BeautifulSoup

class XMLprocess:
    def __init__(self,url):
        self.res=req.urlopen(url)
        self.soup=BeautifulSoup(self.res,"lxml")
        self.data=self.soup.item

    #加工してないデータを入手
    def get_intactData(self,tag):
        #tag:検索対象のタグ
        return self.data.find(tag).string

    #start文字目からend文字目まで切り取る。
    def get_cutedData(self,tag,start,end):
        #start:N文字目から切り取りたい場合、startにはN-1が入ることに注意。
        #end:同様。M-1文字目まで切り取る
        self.intactdata=self.get_intactData(tag)
        self.cutedData=self.intactdata[start:end]
        return self.cutedData

    def get_floatData(self,tag):
        #float型に直したデータを取得
        self.intactdata=self.get_intactData(tag)
        self.numericalData=float(self.intactdata)
        return self.numericalData

url="https://www.federalreserve.gov/feeds/Data/H15_H15_RIFLGFCY30_N.B.XML"
XML=XMLprocess(url)
intactdate=XML.get_intactData("dc:date")
print(intactdate)
strdate=XML.get_cutedData("dc:date",0,10)
print(strdate)
rate=XML.get_floatData("cb:value")
print(rate)
XML=None
