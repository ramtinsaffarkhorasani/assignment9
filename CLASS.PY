a=input("enter your name?")
b=int(input("how old are you?"))
c=input("whats your favorite food?")
d=input("whats your job?")
e=input("whats your favorite car?")
class Person:
  def __init__(self, name, age,favoritefood,job,car):
    self.favoritefood=favoritefood
    self.name = name
    self.age = age
    self.job=job
    self.car=car

px = Person(a,b,c,d,e)
print("your information card is here")
print("Name:",px.name,"Age:",px.age,"Favorite food:",px.favoritefood,"Job:",px.job,"Favorite car:",px.car)

