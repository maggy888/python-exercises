Task #07 作業 01【簡答題】流程控制（上）
1. 請簡單描述程式中必備的三種結構，以及他們的運作流程為何？
循序的 (Sequential)
程式會按照順序執行每一條指令，一行一行地運行。當一行指令執行完畢後，才會執行下一行指令。
條件判斷 (Conditional)
當條件成立時，執行一段程式碼；當條件不成立時，則跳過該段程式碼，繼續執行下一段程式碼。常用的條件判斷語句有 if、else 和 elif。
重複迴圈 (Loop)
常用的重複迴圈語句有 while 和 for。while 語句是在滿足某個條件時，重複執行一段程式碼；for 語句則是在一個序列中逐一取出元素，對每個元素進行一定的操作。

2. 請問以下描述會回傳什麼結果？
x = 6
y = 5
z = 7

print((x > y )and (y > z) or (y - z % 2 > x) or (z + x*6 > y**2))
True
3. 請問下方程式碼會回傳什麼結果？
a = 10
while a:
a = a - 1
print(a)
9~0
4. 請問下方程式碼會回傳什麼結果？
a = list(range(6))
while a:
a.pop()
print(len(a))
5~0
