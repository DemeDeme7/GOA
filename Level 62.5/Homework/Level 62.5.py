# 1
counter = 0
while counter < 20:
    print("hello world!")
    counter += 1

# 2
user_list = input("Input a list:").split()
for element in user_list:
    print(element)

# 3
# მსგავსებები:
# - ყველა არის მონაცემთა სტრუქტურა.
# - ყველა ინახავს ელემენტებს.
# განსხვავებები:
# - set: არ აქვს რიგი, არის ცვალებადი, არ ინახავს დუბლიკატებს.
# - dictionary: ინახავს key-value წყვილებს, არის ცვალებადი, key-ები უნიკალურია.
# - tuple: აქვს რიგი, არის უცვლელი, ინახავს დუბლიკატებს.

# 4
# immutable ნიშნავს, რომ ობიექტი შექმნის შემდეგ ვერ შეიცვლება (მაგ. tuple, string).
# mutable ნიშნავს, რომ ობიექტი შექმნის შემდეგ შეიძლება შეიცვალოს (მაგ. list, dictionary).

# 5
# კონკატენაცია ნიშნავს ორი ან მეტი სტრინგის შეერთებას.
# მაგალითი: "Hello" + " " + "World" = "Hello World"

# 6
# დეკლარირება ნიშნავს ცვლადის ან ფუნქციის განსაზღვრას პროგრამაში.
# მაგალითი: x = 10 (აცხადებს ცვლადს x მნიშვნელობით 10)

# 7
# and ოპერატორის მაგალითები:
print(True and True)
print(True and False)
print(5 > 3 and 2 < 4)
print(5 > 3 and 2 > 4)
print("ა" in "ვაშლი" and "ბ" in "ბანანი")

# or ოპერატორის მაგალითები:
print(True or False)
print(False or False)
print(5 > 3 or 2 > 4)
print(5 < 3 or 2 < 4)
print("ა" in "ვაშლი" or "ბ" in "ბანანი")