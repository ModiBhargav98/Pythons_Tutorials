"""birth_year = input('birth year:  ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(age)
print(type(age))"""


"""Ask a user their Weight(in pounds),converts it to kilograms and print an the terminal
Weight_lbs = input('weight (lbs): ')
Weight_kg = int(Weight_lbs) * 0.45
print(Weight_kg)"""


"""course = "python's for Beginners"
print(course)
print(course[0])
print(course[-1])"""


"""name = 'bhargav'
print(name[1:-1])
first = 'john'
msg = f'{first} [{last}] is coder'
print(message)"""


"""price = 100000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")"""


"""has_good_credit = False
has_high_income = False
if has_high_income or has_good_credit:
     print("Eligiable for loan")"""



"""weight = int(input('weight: '))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pound")"""



"""i = 1
while i<= 5:
    print( i)
    i = i+1
print("Done") """


"""i = 1
while i<= 5:
     print('*' * i)
    i = i+1
print("Done") """


"""secret_number = 9
uess_count = 0
guess_limit = 3
while guess_count < guess_limit:
      guess = int(input('guess: '))
      guess_count += 1
      if guess == secret_number:
          print('you win!')
          break  """

"""command = ""
started = False
while True:
      command = input("> ").lower()
      if command == "start":
         if started:
              print("car is already started!")
         else:
              started = True
              print("car started....")
         if not started:
              print("car is already stopped!")
          else:
               started = False
               print("car stoped.")
      elif command == "help":
          print("
          start - to start the car
          stop - to stop the car
          quit - to quit
          ")
      elif command == "quit":
           break
      else:
           print("sorry, I do not understand!")"""



"""for var in [1,5,7,9]:
       print(var)"""

"""for var in range(10):
       print(var)"""

"""prices = [20,50,60]
total = 0
for var in prices:
    total += var
print(f"Total: {total}")"""

"""for x in range(4):
     for y in range(3):
          print(f"({x},{y})")"""

"""number = [5,3,2,4,8]
for x_count in number:
    print("x" * x_count)
numbers = [15,10,4,7,6,2]
max = numbers[2]
for number in numbers:
     if number>max:
         max = number
print(max)"""


"""matrix = [
   [5,4,8],
    [9,6,1],
]
print(matrix)
for row in matrix:
      print(col)"""


"""number = [5,4,9,7,3,2,5,8,9]
uniques = []
for number2 in number:
    if number2 not in uniques:
         uniques.append(number2)
print(uniques)"""


"""phone = input("Phone: ")
dict = {
    "1":"one",
    "2":"Two",
    "3":"Three",
    "4":"For"
}
output = ""
for var in phone:
     output += dict.get(var,"!") + " "
print(output)"""

"""try:
    age = int(input("age:"))
    print(age)
except ValueError:
    print('invalid value')"""


"""class point:
     def move(self):
         print("hi modi")
     def drow(self):
         print('hello')

p = point()
p.move()
p.drow()"""


"""class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
         print("hi modi")
    def drow(self):
         print('hello')

p = point(10,20)
p.x = 11
print(p.x)"""


"""class person:
     def __init__(self,name):
         self.name = name
     def talk(self):
         print(f"hi, I am {self.name}")
p = person('modi')
print(p.name)
p.talk()

b = person('hello')
b.talk()"""


"""class Mammal:
     def walk(self):
         print("walking")
class Dog(Mammal):
    pass
class cat(Mammal):
     def be_annoying(self):
         print("annoying")
dog1 = Dog()
dog1.walk()
cat1 = cat()
cat1.be_annoying()"""


