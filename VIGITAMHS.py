import os
import time
print('hello to my tools')
time.sleep(2)
print("LODING...")
time.sleep(2)
os.system ('clear')
print("\033[1;33m=============\033[01;31m=========\033[01;35m=============\033[01;34m==========\033[01;32m==============\033[01;31mwelcom  t>
n1 = int(input('enter number 1==> '))
n2 = int(input('enter number 2==> '))
x = int(input('1.[+]\n2.[-]\n3.[×]\n4.[/]\n5.[%]\n===> '))
time.sleep(1)
print("please wiat...")
time.sleep(2)
if x == 1:
    print(n1 + n2)
elif x == 2:
    print(n1 - n2)
elif x == 3:
    print(n1 * n2)
elif x == 4:
    print(n1 / n2)
elif x == 5:
    print(n1 % n2)
else:
    print('sorry not found!!')

print("\033[1;33m=============\033[01;31m=========\033[01;35m=============\033[01;34m==========\033[01;32m==============\033[01;31mwelcom  t>
