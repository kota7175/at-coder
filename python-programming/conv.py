#正規表現のインポート
import re
# クリップボードにコピーのモジュールインポート
import pyperclip

#変換用にファイルの読み込み
with open("proto.py", mode="r") as prot, open("answer.py", mode="w") as answ:
    #ローカル環境の読み込み
    for line in prot:
        #ローカル開発環境専用のキーワードを標準入力のものに置き換え
        tmp = line.replace('inp =  open("input.txt", mode="r")','')\
                 .replace('inp.readline()','input()')\
                 .replace('inp.close()','')
        #コメントの削除
        tmp = re.sub(r'#.*','',tmp)
        #空白行以外書き出し
        if tmp != '\n':
            answ.write(tmp)

#回答をクリップボードコピー用に読み込み
with open("answer.py", mode="r") as answ:
    pyperclip.copy(answ.read())
