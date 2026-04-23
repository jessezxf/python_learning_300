# 需求：有四个数字：1、2、3、4，统计能组成多少个互不相同且无重复数字的三位数？各是多少？


count = 0

for b in range(1,5):
    for s in range(1, 5):
        for g in range(1, 5):
            #三个数字各不相同
            if b != s and b != g and s !=g:
                print(b,s,g)
                #将当前个数加一
                count += 1
print(f"可以组成{count}个互不相同的数")
