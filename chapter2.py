# -*- coding: utf-8 -*-

# 2-1 什麼是變數
print("3 6 18")

print("3 6")

print("3 18")


a = 3
b = 6
c = 18

print(a,b,c)

print(a,b)

print(a,c)

# 同時指定
a,b,c = 3,6,18


# 2-2 運算子與運算式
x = 1

print(x)

x = x + 1

print(x)

y = 1

print(y)

y += 1

print(y)

x = 10

y = 3.125

result = x + y * 2

int_result = int(result)

str_result = str(result)


round_result = round(result, 1)

expression = "x + y * 2"

eval_result = eval(expression)

print("運算式結果：", result)
print("整數型態轉換結果：", int_result)
print("字串型態轉換結果：", str_result)
print("四捨五入的結果：", round_result)
print("eval函數計算結果：", eval_result)

# 語法錯誤
x = 5
#print(x  遺失了右括號 程式會報錯

# 邏輯錯誤
radius = 5
area = 2 * 3.14 * radius  # 此處計算的應為圓周長而非面積
print("圓的半徑：", radius)
print("圓的面積：", area)

# 執行時錯誤
x = 1
y = 0
answer = x / y   

# 2-4 小練習
import math

radius = 5
PI = math.pi

# 計算圓的周長
circumference = 2  * radius * PI

# 計算圓的面積
area = radius**2 * PI

print("圓的周長：", round(circumference, 2))  # 使用 round 函數四捨五入到小數點後兩位
print("圓的面積：", round(area, 2))  # 使用 round 函數四捨五入到小數點後兩位
