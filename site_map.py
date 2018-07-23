import json
import os
class site_map:
    def ___init__(self, path, filename):
        #ファイルのあるフォルダまでのパスを取得
        __name = str(os.path.dirname(os.path.abspath(__name__)))
        #変換対象のjsonファイルまでのパスを作成
        __path = __name + '/' + path + '/' + filename
        #絶対パスに変換
        __abspath = os.path.normpath(__path)

        #jsonファイルを開く
        self.f = open(__abspath, 'r')
        self.jsonData = json.load(self.f)

        #目次を取得
        __indexlist = self.jsonData.keys()
        #dick_keyをリストに変換
        self.indexList = list(__indexlist)

    def get_index(self):
        return self.indexList

    def get_url(self, index):
        #戻り値となるリストを作成
        self.urlList = []
        __secIndex = list(self.jsonData[index].keys())
        for __key in __secIndex:
            #サイトマップに含まれるURLを一つづつ取得
            __url = self.jsonData[index][__key]

            #urlを生成してリストに
            self.urlList.append(__url)
        return self.urlList

    def __del__(self):
        self.f.close()

a = site_map("target", "siteMap.json")
b = a.get_index()
print(b)
print(a.get_url(b[0]))



            

