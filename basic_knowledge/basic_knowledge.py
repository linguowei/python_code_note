# -*- coding: utf-8 -*-
# @Author: linguowei
# @Date:   2017-06-22 10:13:40
# @Last Modified by:   linguowei
# @Last Modified time: 2017-06-27 14:18:24

message = 'hello_world'
for item in range(1,20):
	print(item)
print(message.title())

# 列表
items = [1,2,3,4]
event_number = list(range(2,20,4))
print(items)
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

# 元组(不可变列表)
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组
for dimension in dimensions:
	print(dimension)

# 字典
alien_0 = {
	'color': 'green', 
	'points': 5
}
print(alien_0['color'])
print(alien_0['points'])

# 删除字典中的值
del alien_0['color']
print(alien_0)

# 遍历字典
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}
for key,value in user_0.items():
	print("\nKey:"+key)
	print("Value:"+value)

# 遍历字典中的键
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

for name in favorite_languages.keys():
	print(name)

#接收用户输入
# message = input("请输入一些内容并按回车试试")
# print(message)

# 定义函数
def green_user():
	""" 这里的注释被称为文档字符串的注释,Python使用它们来生成有关程序中函数的文档 """
	print('Hello!')

green_user()

# 位置实参
def describe_pet(animal_type, pet_name):
	""" 显示宠物信息 """
	print("\nI have a" + animal_type + ".")
	print("My" + animal_type  +"'s name is" +  pet_name.title()+".")

describe_pet('hamster','harry')

# 关键字实参
def descript_pet(animal_type,pet_name):
	""" 显示宠物信息 """
	print("\nI have a" + animal_type + ".")
	print("My" + animal_type  +"'s name is" +  pet_name.title()+".")

descript_pet(animal_type="hamster", pet_name="harry")

# 函数参数默认值
def descript_pet(pet_name, animal_type="dog"):
	""" 显示宠物信息 """
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type  +"'s name is" +  pet_name.title()+".")

descript_pet(pet_name="willie")

# 类class
class Dog():
	def __init__(self,name,age):
		""" 初始化属性name和age """
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + "is now sitting")
	def roll_over(self):
		print(self.age.title() + "rolled over!")

my_dog = Dog('willie',6)
print(my_dog.name,my_dog.age)

# 继承
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + '' + self.make + '' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def unpdate_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an dometer!")

	def increment_odometer(self,miles):
		self.odometer_reading += miles

	def fill_gas_tank(self):
		print("This car doesn't need a gas tank!")

class ElectricCar(Car): 
	def __init__(self, make, model, year): 
		""" 初始化父类的属性"""
		super().__init__(make, model, year)
		self.battery_size = 70

	""" 定义子类的方法 """
	def descript_battery(self):
		print("This car has a " + str(self.battery_size))

	""" 重写父类的方法 """
	def fill_gas_tank(self):
		print("Rewrite")

my_tesla = ElectricCar(" tesla ","model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.descript_battery()
my_tesla.fill_gas_tank()

# 读取文件
with open('read.txt') as file_object:
	contents = file_object.read()
	print(contents)

# 逐行读取
with open('read.txt') as file_object:
	for line in file_object:
		# rstrip方法可以删除字符串末尾的空白
		print(line.rstrip())

# 写入文件
with open('write.txt', 'w') as file_object:
	file_object.write("I lova programming")

# 异常处理
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide zero!")




























