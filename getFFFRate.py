from time import sleep
from modules import XMLProcess
from modules import get_url
import sqlite3


class GetFFRate:
    # アクセスマップの入ったファイルを指定
    def __init__(self, path, filename, index):
        # アクセスするURLのリストを取得
        __scr = get_url.site_map(path, filename)
        self.url_list = __scr.get_url(index)

    # 日付取得用の関数
    def get_date(self):
        __XML = XMLProcess.XMLProcess(self.url_list[0])
        __str_date = __XML.get_cut_data("dc:date", 0, 10)
        __XML = None
        return __str_date

    def get_rate(self, url):
        __XML = XMLProcess.XMLProcess(url)
        __rate = __XML.get_float_data("cb:value")
        __XML = None
        return __rate

    # urlのリストに基づいてデータを取得していく
    def get_list(self):
        __rate_list = list([])
        # 日付をリストに入れる(主キー)
        __rate_list.append(self.get_date())

        for __url in self.url_list:
            __rate = self.get_rate(__url)
            __rate_list.append(__rate)
            # 1秒待つ
            sleep(1)

        __XML = None
        return __rate_list


a = get_url.site_map("target", "FFRate.json")
b = a.get_index()

for idx in b:
    # 満期ごとに表示
    ff = GetFFRate("target", "FFRate.json", idx)

print(ff.get_list())
