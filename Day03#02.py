#練習：將字串當中的 not that poor 換成 good 。

❏ Requirements：

1. 輸入一個包含「not that poor 」的字串

2. 在程式中 not that poor 換成 good 後輸出

❏ Sample Input： The company is not that poor! ← 使用者輸入

❏ Sample Output： The company is good! ← 畫面輸出

s = input("") # The company is not that poor!

s =s.replace("not that poor","good")

print(s) # The company is good!

