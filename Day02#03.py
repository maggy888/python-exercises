#練習：請輸入兩個整數存入變數 a, b ，利用程式將兩個變數當中的數值進行交換。

❏ Requirements：

1. 輸入兩個正整數存入變數 a, b

2. 請輸出 a, b 變數內容交換後的結果（不是輸出順序交換而已）

3. 程式當中不可以使用 if 或 loop

❏ Sample Input： 5 10 ← 使用者輸入

❏ Sample Output： 10 5 ← 畫面輸出

w = input("w=")

s = input("s=")

print(w,s)

w,s = s,w

print(w,s)

