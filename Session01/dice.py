from random import randint

num = 100
out = {1:0,2:0,3:0,4:0,5:0,6:0}
for i in range(num):
    n = randint(1,6)
    out[n] += 1
for i, j in out.items():
    print(i,"==>",j)