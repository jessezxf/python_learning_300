"""
Date:2026/4/4 14:31
Author:Jesse

需求：给定一个简单列表，对其元素进行排序。
简单列表：元素类型不是复合类型（列表/元组/字典）。
示例：
-形式1:[20,50,10,40,30]
-形式2:[bb','ee','aa','dd','cc']
"""


list1 = [20,50,10,40,30]

#对列表进行排序（原地排序）,改变原列表的顺序
# sort(key=None,reverse=False)
#key（可选）：接收一个函数作为参数。该函数会在每个元素上调用，其返回值将作为排序的依据。如果未提供，
#reverse（可选）：接收一个布尔值。如果设置为True，则列表将以降序排
list1.sort(reverse=True)
print("list1:",list1)


print("\n")
print("#"*100)

list1 = [20,50,10,40,30]
#对列表进行排序（不改变原列表顺序）
# sorted(iterable,key=None,reverse=False)
#iterable：想要排序的可迭代对象
#key（可选）：接收一个函数作为参数。该函数会在每个元素上调用，其返回值将作为排序的依据。如果未提供，则直接比较
#reverse（可选）：接收一个布尔值。如果设置为True，则列表将以降序排列：如果设置为False或未提供，则列表将以升序
print(list1)
list2 = sorted(list1)
print(list2)


