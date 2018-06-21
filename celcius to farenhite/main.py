import time
num=int(input("enter the number of elements to be changed from celcius to farenheit"))
cel=[]
for i in range(num):
    lis=int(input("enter the number\n"))
    cel.append(lis)
print(cel)
faren = [((9/5)*temp + 32) for temp in cel ]
print(faren)
time.sleep(20)
