


#some python tricky

#56. 按照要求来排序列表里的列表

a = cmp()






#https://blog.csdn.net/qwe1257/article/details/83272340
# collections.Counter

from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print (dict(c))
#{'red': 2, 'blue': 3, 'green': 1}



# filter函数
# 起到过滤作用，把需要过滤的东西储存到b中
a = [11, 20, 4, 5, 16, 28]
b = filter(lambda x: x % 2 != 0, a)



