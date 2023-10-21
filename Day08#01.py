❏ Requirements：

1. 利用迴圈讓使用者可以重複輸入一個數字 n

2. 利用程式計算 1! + 2! + 3! + ... + n! 的總和

3. 每一個回合請將階乘總和的結果印出

❏ Sample Input： 4 ← 使用者輸入

❏ Sample Output： 33 ← 畫面輸出

x = int(input()) # 4

Q = 1

sum = 0

for i in range(1, x+1):

Q*= i

sum += Q

print(sum) # 33

