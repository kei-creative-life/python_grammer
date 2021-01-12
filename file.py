# ファイルの内容を表示①
# f = open("test.txt","r",encoding="utf-8")
# s = f.read()
# print(s)
# f.close

# ファイルの内容を1行ずつ表示②
# f = open("test.txt","r",encoding="utf-8")
# for line in f:
# 	print(line,end =" ")

# ファイルに書き込む
s = "hello"
f_read = open("test.txt","r",encoding="utf-8")
print(type(f_read))
# f = open("test.txt","w",encoding="utf-8")
# f.write(s)
# f.close()