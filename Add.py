from time import gmtime, strftime
a=6
b=4
sum=0
print(f"The sum is  {a+b}")
# Create a list of 20 items (for demonstration purposes)
my_list = list(range(1, 21))

# Enumerate through the list and print each item along with its index
for index, item in enumerate(my_list):
    sum += int(item)    
    print(f"Item at index {index}: {item} sum {sum}")
formatted_time = strftime("%m-%d-%Y %H:%M:%S")
print("date and time:", formatted_time)