❏ Requirements：

1. 讓使用者可以輸入一個網址

2. 利用程式取出網址當中的 domain 後輸出

❏ Sample Input： https://www.facebook.com/dscareer ← 使用者輸入

❏ Sample Output： www.facebook.com ← 畫面輸出

s = "http://www.facebook.com/dscareer"

s1 =s.split("/")

print(s1[2]) # www.facebook.com
