name=str(input("请输入你的名字："))
print("你好，", name)

x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end="," )
print(y)
print(x,y)




# 循环语句

sites = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for site in sites:
    if site == "c":
        print("找到了目标数据："+site)
        break
    print("正在查找 " + site)
else:
    print("没有找到目标数据!")
print("完成循环!")


 
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   age=20
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )