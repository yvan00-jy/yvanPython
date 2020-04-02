#coding:utf-8

# 布尔类型可以当成int来处理  True为1  False为0
print(True+True)
print(False*True)
################################################################################################
# 字符串转int  如果字符串转化为数值是浮点型，则转化为int时会报错，如：print(int("56.1"))
print(int("56"))

# 浮点型转int,截断处理，不会四舍五入
print(int(5.99))

# float把字符转化为浮点型
print(float("5.99"))
print(float(666))

# str转字符串
print(str(5.99))
print(str(4e5))
################################################################################################
# 使用type函数获取类型
print(type("123"))  # 结果： <type 'str'>
print(type(123))    # 结果：<type 'int'>
print(type(123.4))  # 结果：<type 'float'>
print(type(True))   # 结果：<type 'bool'>

# 使用isinstance判断值是否与指定的类型相符
print(isinstance(456,int))

print(isinstance(1,bool))
print(isinstance(True,bool))

print(isinstance(456,float))

print(isinstance(456,str))
print(isinstance("456",str))