# coding: UTF-8
#ローカル実行環境の作成
#ファイルのオープン

inp =  open("input.txt", mode="r")

#1行1データの場合
#date = inp.readline().rstrip() #rstripは右端の空白、改行の削除

#1行複数データの場合
#date = inp.readline().rstrip().split(' ') #splitにより空白区切でリスト化
#a,b,c,d = map(int, (inp.readline().rstrip().split()))

#data = input()
#x, a, b = map(int, (input().split()))

#----ここからプログラム----
N = int(inp.readline().rstrip())
A = list(map(int, inp.readline().rstrip().split(' ')))
rect_long = 0
rect_small = 0
while A != []:
    long_max = max(A)
    if A.count(long_max) >= 2:
        rect_long += long_max
        A.remove(long_max)
        A.remove(long_max)
        break
    A.remove(long_max)

while A != []:
    small_max = max(A)
    if A.count(small_max) >= 2:
        rect_small += small_max
        break
    A.remove(small_max)

print(rect_long * rect_small)



#----ここまでプログラム----

#ファイルのクローズ
inp.close()