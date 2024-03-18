from time import gmtime, strftime
a=6
b=4
print(a+b)

formatted_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print("date and time:", formatted_time)