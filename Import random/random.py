import random

value = random.random()   
print(value) 
# გამოაქვს ყველა შესაძლო რიცხვი რაც კი არსებობს 0-1 შორის. float-ებში.      example: 0.239962705010406

value = random.uniform(1, 10)   
print(value) 
# გამოაქვს ყველა შესაძლო რიცხვი რაც კი არსებობს 1-10 შორის. float-ებში.     example: 5.239962705010406

value = random.randint(1, 10)   
print(value) 
# გამოაქვს ყველა შესაძლო რიცხვი რაც კი არსებობს 1-10 შორის. string-ებში.     example: 6

greetings = ["Hello", "gamarjoba", "ola", "hey", "hi"]
name = input("enter your name: ")

value = random.choice(greetings)
print(value, name)

# random.choice-ი, ცვლად greetings-იდან ირჩევს რენდომულად მნიშვნელობას და პრინტავს.


colors = ["red", "green", "blue", ]

value = random.choices(colors, k=2)
print(value)

# random.choice და random.choices ერთი და იგივეა უბრალოდ random.choices-ს ემატება 1 ატრიბუტი k, რისი მეშვეობითაც ვირჩევთ რამდენი მნიშვნელობა დავპრინტოთ

deck = list(range(1, 50))

random.shuffle(deck)
print(deck)

# random.shuffle ურევს ლისტში რიცხვებს