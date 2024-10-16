class Vehicle:
	name = ""
	kind = "car"
	color = ""
	value = 100.00
	def description(self):
		desc_str = "%s is a %s %s worth $%.2f."%(self.name,self.color,self.kind,self.value)
		return desc_str

car1 = Vehicle()
car1.name = 'Serena the Fast'
car1.color = 'red'
car1.kind = 'convertible'
car1.value = 10000000000000000
print(car1.description())

class person:
        name = ''
        age = 0
        birthday = ''
        favorite_food = ''
        grade = 0
        def description(self):
                desc_str = ("So your name is %s and you are %s years old and your birthday is %s. You are in %sth grade and your favorite food is %s. Nice, %s!" % (self.name,self.age,self.birthday,self.grade,self.favorite_food,self.name))
                return desc_str

serena = person()
serena.name = "serena".title()
serena.age = 14
serena.favorite_food = 'cHicken'.lower()
serena.grade = 8
serena.birthday = 'October 17th'
print(serena.description())
