# -*- coding: utf-8 -*-
# @Author: linguowei
# @Date:   2017-06-22 10:13:40
# @Last Modified by:   linguowei
# @Last Modified time: 2017-06-22 11:10:40

message = 'hello_world'
for item in range(1,20):
	print(item)
print(message.title())

list = [1,2,3,4]
event_number = list(range(2,20,4))
print(event_number)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

# 找出列表最大最小值和值
digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1,20)]
print(squares)

# 切片
players = ['charles', 'martina', 'mivhael', 'florece', 'eli']
print(players[0:3])

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[2:]:
	print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)



















