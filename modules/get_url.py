import json
import os


class site_map:
    def __init__(self, path, filename):
        # ファイルのあるフォルダまでのパスを取得
        __name = str(os.path.dirname(os.path.abspath(__name__)))
        # 変換対象のjsonファイルまでのパスを作成
        __path = __name + '/' + path + '/' + filename
        # 絶対パスに変換
        __abs_path = os.path.normpath(__path)

        # jsonファイルを開く
        self.f = open(__abs_path, 'r')
        self.jsonData = json.load(self.f)

        # 目次を取得
        __index_list = self.jsonData.keys()
        # dick_keyをリストに変換
        self.index_list = list(__index_list)

    def get_index(self):
        return self.index_list

    def get_url(self, index):
        # 戻り値となるリストを作成
        self.url_list = list([])
        __secIndex = list(self.jsonData[index].keys())
        for __key in __secIndex:
            # サイトマップに含まれるURLを一つづつ取得
            __url = self.jsonData[index][__key]

            # urlを生成してリストに
            self.url_list.append(__url)
        return self.url_list

    def __del__(self):
        self.f.close()


# a = site_map("target", "FFRate.json")
# b = a.get_index()
# print(b)
# print(a.get_url(b[0]))
