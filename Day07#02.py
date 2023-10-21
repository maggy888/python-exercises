#練習：n! 階乘代表 1 * 2 * 3 ... * n 的乘積總和，請用 Python 程式實現 n! 計算。

❏ Requirements：

1. 讓使用者可以自行輸入一個數字 n，請檢查 n 是否為合法數字否則回傳錯誤訊息

2. 利用程式計算 n! 的結果並且印在畫面上

❏ Sample Input #01： 4 ← 使用者輸入

❏ Sample Output #01： 24 ← 畫面輸出

❏ Sample Input #02： a ← 使用者輸入

❏ Sample Output #02： a 是一個不合法的輸入，無法運算 ← 畫面輸出

x = input("請輸入一個整數：")

if x.isdigit():

n = int(x)

result = 1

for i in range(1, n + 1):

result *= i

print(f"{n}! = {result}")

else:

print(f"{x}是一個不合法的輸入，無法運算。")
