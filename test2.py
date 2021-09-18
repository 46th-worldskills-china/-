
# 1.给定一个梯形如下图，求梯形的圆形，打印出结果。

'''
# 2.创建一个0~100，只包含偶数的列表。如[0,2,4,6,.....98,100]
a = [each for each in range(101) if not (each % 2 == 1)]
print(a)

# 3.统计字符串 ’keep on going never give up’ 中所有字符出现的次数。打印出结果
b = 'keep on going never give up'
print("统计：")
for i in b:
    print("%s:%d" %(i,b.count(i)))



# 4. 找出两个10以内的数字，满足公式 x2 + y2 = 50，打印出所有组合。如x:1 y:7
z = 0
for i in range(1,11):
    for a in range(1,11):
        if (i * i + a * a ) == 50:
            print(f"x:{i},y:{a}")


# 5.一个字符串由单词和空格组成0
#，将字符串逆序，单词不变。
d = "i am iron man"
# # print(''.join(reversed(list(d)))        ##reversed反转，对于数字可以，字母不咋行。
d_list = d.split(" ")
# print(d_list[3],d_list[2],d_list[1],d_list[0])

for i in range(0,4)[::-1]:    # for i in range(3,-1,-1)
    print(d_list[i],end=" ")


# 6.找到字符串A在另一个字符串B中的位置的下标，如果不存在，返回-1。不可使用内置函数
a = "hello"
b = "1q2wh3ehellonm"
print(b.find(a))
'''

