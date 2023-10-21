1. 解釋看看你心中的「函式」是什麼？為什麼要使用「函式」？
在 Python 中，函式是一個可重複使用的程式碼區塊，可以接受參數並且返回值。有效運用函式可以讓程式更加模組化，使得程式碼的可讀性更好，並且能夠避免重複編寫程式碼。

2. 試著說明以下程式的「執行順序」，執行的順序會長怎樣（盡可能地拆分為運算的最小單位）？
def f(a, b):a
if a > b:
return a
return b

max = f(3, 5)
max = f(6, f(3, 5))
max = f(max, f(1, 2))
n定義了一個函式f(a,b)，該函式比較兩個數字a和b，並返回較大的數字。

1. max = f(3, 5)：在這一步，函式f被呼叫，傳入參數3和5。由於3不大於5，所以返回值為5，然後將max變數賦值為5。
2. max = f(6, f(3, 5))：這一步中，函式f再次被呼叫兩次。首先，內部的呼叫f(3, 5)會返回之前計算過的5。接著，f(6, 5)會將6和5進行比較，返回較大的數字6，然後將max變數更新為6。
3. max = f(max, f(1, 2))：最後一步，又是兩次函式呼叫。第一個內部呼叫f(1, 2)會返回2，然後外部呼叫f(6, 2)會將6和2進行比較，返回較大的數字6。最終，max變數保持為6。
所以，經過這一系列的操作，最後max變數的值是6，這是由於不斷地將函式的返回值和之前的max值進行比較，取其中的較大者。

3. 以下程式可以會傳 a, b 的最大值，如何改寫成可以接收 f(a, b), f(a, b, c), f(a, b, c, ...) 等不同個數輸入的最大值函式可以怎麼做？
def f(a, b):
if a > b:
return a
return b

f(3, 5) # O
f(3, 4, 5) # X
f(3, 4, 5, 6, 7) # X
def f(*args):
max_value = float('-inf') # 初始化最大值為負無限大
for num in args:
if num > max_value:
max_value = num
return max_value

print(f(3, 5)) # 輸出: 5
print(f(3, 4, 5)) # 輸出: 5
print(f(3, 4, 5, 6, 7)) # 輸出: 7

4. 請問下方程式碼會回傳什麼結果？
a = 'A'

def f(b):
a = 'AAA'
c = 'C'
print(a)
print(b)
print(c)
return b

print(a)
print(f('B'))
print(a)

A
AAA
B
C
B
A

5. 請問下方程式碼會回傳什麼結果？
a = 'A'

def f(b):
c = 'C'
print(a)
a = 'AAA'
print(b)
print(c)
return b

print(a)
print(f('B'))
print(a)
UnboundLocalError: local variable 'a' referenced before assignment
