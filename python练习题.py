
'''
# 1.给定一个梯形如下图，求梯形的圆形，打印出结果。(梯形面积公式:s = (a+c)*h/2)
a = int(input("梯形的上长 a: "))
c = int(input("梯形的下长 c: "))
h = int(input("梯形的高 h: "))
s = (a+c)*h/2
print('梯形面积为：{}'.format(int(s)))
'''

'''
# 2.创建一个0~100，只包含偶数的列表。如[0,2,4,6,.....98,100]
a = [each for each in range(101) if not (each % 2 == 1)]
print(a)
##老师的方法
li = list(range(0,101,2))
print(li)
'''

'''
# 3.统计字符串 ’keep on going never give up’ 中所有字符出现的次数。打印出结果.(需要加入set()集合排序，不然会有问题)
b = 'keep on going never give up'
print("统计：")
for i in set(b):
    print("%s:%d" %(i,b.count(i)))
'''
    


'''
# 4. 找出两个10以内的数字，满足公式 x2 + y2 = 50，打印出所有组合。如x:1 y:7
for x in range(1,11):
    for y in range(1,11):
        if (x * x + y * y ) == 50:
            print(f"x:{x},y:{y}")

##使用pow()函数

for x in range(1,11):
    for y in range(1,11):
        if pow(x,2)+pow(y,2) == 50:
            print(f"x:{x},y:{y}")



# 5.一个字符串由单词和空格组成0
#，将字符串逆序，单词不变。
d = "i am iron man"
# # print(''.join(reversed(list(d)))        ##reversed反转，对于数字可以，字母不咋行。
d_list = d.split(" ")
# print(d_list[3],d_list[2],d_list[1],d_list[0])

for i in range(0,4)[::-1]:    # for i in range(3,-1,-1)
    print(d_list[i],end=" ")

##老师的方法
i = "i am iron man"
li1 = i.split(" ")
li2 = list(reversed(li1))
print(" ".join(li2))






# 6.找到字符串A在另一个字符串B中的位置的下标，如果不存在，返回-1。不可使用内置函数
a = "hello"
b = "1q2wh3ehellonm"
print(b.find(a))

##老师的方法
a = "hello"
b = "1q2wh3ehellonm"
lt = b.split(a,1)
if len(lt) == 1:
    print('-1')
else:
    print(len(lt[0]))





# 7.对角线遍历
# 给定一个含有3 x 3 个元素的矩阵，请以对角线遍历的顺序返回这个矩阵中的所有元素。
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = (len(A))
li = []
for x in range(n + n - 1):
    for y in range(x + 1):
        k = x - y
        if k < n and k >= 0 and y < n:
            li.append(A[y][k])
print(li)




# 8.移动非0元素到头部
# 给定一个数组 [0,1,0,3,12]，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 输出[1, 3, 12, 0, 0]
# 要求：必须在原数组上操作，不能拷贝额外的数组。
# 陆炜杰的做法
arrlist = [0, 1, 0, 3, 12]
def move():
    for i in arrlist:
        if i == 0:
            arrlist.remove(0)
            arrlist.append(0)
    print(arrlist)
move()

'''







'''
# 1.输入文件名称，例如：“test.txt”，输出文件的扩展名。
filename = input('filename: ')
print(filename.split(".")[-1])


# 2.定义一个变量并查看变量在内存中的地址。
test = 'hellow word'
print(id(test))

'''

# 3.输入一个数字，判断是奇数还是偶数。



# 4.使用while循环打印出 1 2 3 4 5 6 8 9 10。



# 5.输入一个数字 n，输出 n、nn、nnn 之和。




# 6.字典test_dic={‘k1’:“v1”,“k2”:“v2”,“k3”:“v3”}，请循环输出所有的 key。





# 7.输入一连串数字（数字用英文逗号分隔），然后以元组和列表形式输出。




# 8.请写出一段Python代码实现删除一个list里面的重复元素，并打印出处理后的list首尾两个元素。




# 9.请写出一段Python代码实现计算字符串"I am a student,we are students,she is a student"中"student"出现的次数。




# 10.给一个正整数，例如12345。求它是几位数，并逆序打印出各位数字。




# 11.编写一个程序，可以找到所有这些数字，可被7整除，但不是5的倍数，2021年至2100年(包括在内)。顺序打印出得到的年份数字。




# 12.一球从1000米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？
a = 1000
course = 1000
for i in range(1,11):
    course += a
    a = a/2
print(course-2*a)

##老师做的
sum = 0
h = 500
for x in range(1,10):
    sum = sum + (h * 2)
    h = h / 2
sum += 1000
print(sum)






# 13.2020年51OpenLab平台培训学员5千人，每年增长80%，请问按此增长速度，到哪一年培训学员人数将达到5万人?请写出一段Python代码计算出预期年份。

students = 5000
year = 2020

while students <= 50000:
    students = students + students * 0.8
    year = year + 1
print(year)
print(students)









