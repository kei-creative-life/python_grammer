# from random import randint
# num = randint(0,3)

# def pickup_name(num):
# 	members = ["John","Mary","Alice","Amanda"]
# 	print("あなたの運命の人は...")
# 	return print(members[num])

# pickup_name(num)

# # ディクショナリー（＝ハッシュ）
# def convert_num(num):
#     english_nums = {1:"one",2:"two",3:"three",4:"four"}
#     if num in english_nums:
#         return english_nums[num]
#     else:
#         return "見つかりません"
# convert_num(2)

# # ディクショナリー（＝ハッシュ）② ループ
# info = {"nickname":"ほげ","age":26,"height":175}
# for key in info:
# 	print(key,info[key])

# # FizzBuzz
# num = 1
# while num <= 100:
#     if num%3 == 0 and num%5 == 0:
#         print("FizzBuzz")
#     elif num%3 == 0:
#         print("Fizz")
#     elif num%5 == 0:
#         print("Buzz")
#     else:
#         print(num)
#     num += 1

# # ジャンケンプログラム
# from random import randint
# hands={0:"グー",1:"チョキ",2:"パー"}
# rules = {(0,0):"アイコ",(0,1):"勝ち",(0,2):"負け",(1.0):"負け",(1,1):"アイコ",(1,2):"勝ち",(2,0):"勝ち",(2,1):"負け",(2,2):"アイコ"}

# while True:
#     pc_hand = randint(0,2)
#     user_hand_str = input("0:グー 1:チョキ 2:パー 3:やめる")
#     if user_hand_str == "3":
#         break
#     if user_hand_str not in ("0","1","2"):
#         continue
#     user_hand = int(user_hand_str)
#     print("あなた："+hands[user_hand]+"、　コンピュータ："+hands[pc_hand])
#     print(rules[(user_hand,pc_hand)])

# # デフォルト引数
# def say_hello(count =10, name="太郎",message="愛している"):
# 	for count in range(1,count):
# 		print("私は"+name+"を"+message)
# 		count+=1
# say_hello()

# # メソッドを作る場合
# def find_index(the_list,target):
#     idx = 0
#     for item in the_list:
#         if target == item:
#             return idx
#         idx+= 1
# names = ["Jogn","Mary","Mike"]
# find_index(names,"Mary")

# # 組み込みのメソッドを使う場合
# names.index("Mary")

# # splitとjoin
# str_speeds = "38 42 20 40 39"
# speeds = str_speeds.split()
# csep_speeds = ",".join(speeds)
# csep_speeds

# # formatによる挿入
# link = '<a href="{}">{}</a>'
# for i in ['http://hoge1.com','http://hoge2.com','http://hoge3.com']:
# 	print(link.format(i,i.replace('http://','')))

# # formatによる挿入：キーワード引数
# "{food1}{food2}".format(food1='Banana',food2='Apple')

# # formatによる挿入：ディクショナリも挿入可能
# info = {'name':'John','age':28}
# "{0[name]}は{0[age]}歳です。".format(info)

# # 文字列と変数を結合：f文字列
# name = "Kengo"
# f"{name} loves Python."

# # リストの並び替え
# array=[158,186,100,90]
# array.sort()
# print(array)

# sortの引数を指定する
data =[("太郎",20,30,40),("次郎",30,0,20),("三郎",10,50,10)]
def evaluate_data(array):
	for i in range(0,len(array)):
		return array[i][1] + array[i][2] + array[i][3]
		i+=1
	data.sort(key=evaluate_data,reverse=True)
	print(array)

evaluate_data(data)

# アンパック代入（分割代入みたいなもの？）
a = 1
b = 2
x,y = a,b
print(x,y)

# ディクショナリーのキーを使う。
line = "a b c d e"
wordcount = {"a":"hello","e":"goodbye","f":"no thanks"}
for word in line.split():
    if word in wordcount:
        print(f"{word}に対応する{wordcount[word]}が見つかりました。")
    else:
        print("見つかりませんでした。")

# クラスの定義の基本：Rubyとほぼ一緒なので楽勝！！
class Prism:
	def __init__(self,width,height,depth):
			self.width = width
			self.height = height
			self.depth = depth

	def content(self):
			return self.width * self.height * self.depth

prism = Prism(width =100,height =175,depth =50)
print(prism.content())

print(prism.width)
print(prism.height)
print(prism.depth)

# クラスの継承:class 小クラス(スーパークラス)
class Prism:
    def __init__(self,width,height,depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content(self):
        return self.width * self.height * self.depth

prism = Prism(width =100,height =175,depth =50)
print(f"幅は{prism.width}")
print(prism.height)
print(prism.depth)
print(prism.content())


class Cube(Prism):
    def __init__(self,length):
        self.width = self.height = self.depth = length

cube = Cube(20)
print(cube.width)
print(cube.height)
print(cube.depth)
print(cube.content())

# アトリビュートの追加を制限するスロット
# ↓heightを追加しようとしてエラーが出る！！
class Member:
    __slots__ = ['name','age']
    def __init__(self):
        self.name = "太郎"
member = Member()
print(member.name)

member.age = 24
print(member.age)

member.height = 175
print(member.height)

# ゲッターとセッター
# xの部分はRubyでいうattribute_accessor :xみたいなもの？
class Prop:
    def __init__(self):
        self.__x = 0
    def getx(self):
        return self.__x
    def setx(self):
        self.__x = x
    x = property(getx,setx)

prop = Prop()
prop.x
