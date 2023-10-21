1. 回想看看到目前為止，你曾經遇到過哪些錯誤發生？
大部分都是Syntax Error、IndentationError、NameError、TypeError、ZeroDivisionError、ValueError、IndexError


2. 試著解釋什麼是「例外處理」，並且說明在哪些情況適合使用？
在Python編程中，當程式運行出現錯誤時，會產生一種稱為「例外(exception)」的事件。這可能是因為程式碼中有錯誤、運行環境出現問題，或是由於不可預測的外部事件而引起的。如果未處理這些例外，程序將停止運行並拋出錯誤信息。
為了解決這些問題，Python提供了一種稱為「例外處理(exception handling)」的機制。這個機制允許開發人員在出現錯誤時處理它們，而不是直接終止程序。
3. 請問以下程式碼的「變數 e」代表的意義是什麼？
try:
x = input() / input()
except Exception as e:
print(e)
在這個程式碼中，變數 e 是一個 Exception 物件，表示異常的詳細內容訊息。except Exception as e: 表示將發生的異常內容儲存在 e 變數中。

4. 請問以下程式碼的「raise」跟「finally」的用法為何？
try:
raise Exception('spam', 'eggs')
except Exception as e:
print(e)
finally:
print('done')
在try語句塊中，我們使用raise語句引發了自定義的例外。在except語句塊中，我們捕獲了這個例外，並且打印了它的錯誤信息。

不管try語句塊中的代碼是否引發了例外，finally語句塊中的代碼都會被執行。
