#練習：定義一個計算質數的函數。

❏ Requirements：

1. 讓使用者輸入一個整數 n

2. 請分別定義兩個 Function: isPrime(n) 回傳 n 是否為質數、primes(n) 回傳小於 n 質數

❏ Sample Input： 20 ← 使用者輸入

❏ Sample Output： 2, 3, 5, 7, 11, 13, 17, 19 ← 畫面輸出

def isPrime(n):
if n > 1:
for i in range(2,n):
if n % i== 0:
return False #能被整除非質數，回傳false
break;
else:
return True #沒能被其他數整除，為質數，回傳True
else:
print("1 is not prime") #1的特例
return False

def primes(n):
Prime_list= []
for i in range(2,n):
if isPrime(i):
Prime_list.append(i)
return Prime_list

isPrime(x)
print("小於",x,"的質數有",primes(x))

