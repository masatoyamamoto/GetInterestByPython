import json
import os

# 共通部分のインデックス
idx0 = "static"
# 個別の組み合わせ部分
idx1 = "combination"
# 前半の共通部分
prefix = "prefix"
# 後半の共通部分
suffix = "suffix"


class scrape_url:
    def __init__(self, filename):
        # __変数で擬似ローカル変数になる
        # ファイルのあるフォルダまでのパスを取得
        __name = os.path.dirname(os.path.abspath(__name__))
        # 変換対象のjsonファイルまでのパスを作成
        __path = __name + '/target/' + filename
        # 絶対パスに変換
        __abspath = os.path.normpath(__path)

        # jsonファイルを開く
        __f = open(__abspath, 'r')
        __jsonData = json.load(__f)

        # urlの前半と後半の共通部分を取得
        __prefix = __jsonData[idx0][prefix]
        __suffix = __jsonData[idx0][suffix]

        # 個別項のインデックスを取得

        __indexList = __jsonData[idx1].keys()
        # dict_keyをリストに変換
        __indexList = list(__indexList)

        # 戻り値となるリストを作成
        self.urlList = []

        for __index in __indexList:
            # インデックスごとの値を取得
            __text = __jsonData[idx1][__index]

            # FFRateのurlは"SP"+"FF"
            __part = __text + __index
            # urlを生成してリストに
            self.urlList.append(__prefix + __part + __suffix)
        __f.close()

    def get_url(self):
        return self.urlList

# TODO 3のURL自動生成をやる。
