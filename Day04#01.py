1. 請問 List 是 Python 中常見的容器型態，他跟一般的 int、float 這類型態有什麼不同嗎？

列表是一種可變的有序容器，其中的元素可以是不同的資料型態，包括數字、字串、布林值、甚至是其他的列表;int用來宣告整數值,float用來宣告浮點數一次只能放1個數值都是固定不變的

2. 試著解釋 list 底下的 append 用法是什麼？

在列表的末尾添加一個新的元素

3. 請問 list 當中的 append(...) 跟 extend(...) 有什麼不一樣的地方？

append:指在列表的末尾添加一個新的元素;extend:將一個列表中的元素添加到另一個列表的末尾。

4. 請問 list 當中的 reverse(...) 跟 [::-1] 有什麼一樣和不一樣的地方？

reverse:可以將列表中的元素倒序排列。

list[::-1]是一種列表切片（slicing）語法，用於將列表（list）倒序（reverse）。 輸出它會建一個從列表的最後一個元素到第一個元素的新列表。

5. 請問如果直接用以下方法複製 List，可能會存在什麼疑慮嗎？

a = [1, 2, 3, 4, 5] 
b = a


把a串列的元素指定給b,當a的元素變動時b也會跟著變
a = [1, 2, 3, 4, 5]

b = a

b=a.copy()

print(b) # [1, 2, 3, 4, 5]
