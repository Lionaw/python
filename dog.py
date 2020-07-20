# -*- coding: gbk -*- 
print("hello,world!")   # by Lionaw
class Dog():
	"""一次模拟小狗的简单尝试"""
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name.title()+" is now sitting.")
	
	def roll_over(self):
		print(self.name.title()+" rolled over!")
		
my_dog = Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('川普',10)
print("My dog's name is "+your_dog.name.title()+".")
print("My dog is "+str(your_dog.age)+" years old.")
your_dog.sit()
your_dog.roll_over()

class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self,make,model,year):
	    self.make = make
	    self.model = model
	    self.year = year
	    self.odometer_reading = 50
	def get_descriptive_name(self):
		long_name = str(self.year)+' '+self.make +' '+self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")
	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
		    self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer")
	def increment_odometer(self,miles):
		self.odometer_reading += miles
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading=60
my_new_car.read_odometer()	
my_new_car.update_odometer(40)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()




