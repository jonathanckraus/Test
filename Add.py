from time import strftime
a=6
b=4
sum=0
print(f"The sum is  {a+b}") 

# Create a list of 100 items (for demonstration purposes)

my_list = ('Acai','Ackee','Apple','Apricot','Avocado','Babaco','Banana','Bilberry','Blackberry','Blackcurrant','Blood Orange','Blueberry','Boysenberry','Breadfruit','Brush Cherry','Canary Melon','Cantaloupe','Carambola','Casaba Melon','Cherimoya','Cherry','Clementine','Cloudberry','Coconut','Cranberry','Crenshaw Melon','Cucumber','Currant','Curry Berry','Custard Apple','Damson Plum','Date','Dragonfruit','Durian','Eggplant','Elderberry','Feijoa','Finger Lime','Fig','Gooseberry','Grapes','Grapefruit','Guava','Honeydew Melon','Huckleberry','Italian Prune Plum','Jackfruit','Java Plum','Jujube','Kaffir Lime','Kiwi','Kumquat','Lemon','Lime','Loganberry','Longan','Loquat','Lychee','Mammee','Mandarin','Mango','Mangosteen','Mulberry','Nance','Nectarine','Noni','Olive','Orange','Papaya','Passion fruit','Pawpaw','Peach','Pear','Persimmon','Pineapple','Plantain','Plum','Pomegranate','Pomelo','Prickly Pear','Pulasan','Quine','Rambutan','Raspberries','Rhubarb','Rose Apple','Sapodilla','Satsuma','Soursop','Star Apple','Star Fruit','Strawberry','Sugar Apple','Tamarillo','Tamarind','Tangelo','Tangerine','Ugli','Velvet Apple','Watermelon')

for item in(my_list):
    print(item)
# print(my_list[6])
# Enumerate through the list and print each item along with its index
for index, item in enumerate(my_list):
    sum += index    
    print(f"Item at index {index}: {item} sum {sum}")
formatted_time = strftime("%m-%d-%Y %H:%M:%S")
print("date and time:", formatted_time)