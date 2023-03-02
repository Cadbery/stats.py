import statistics
list=[]
num=0
while num!="":
  num=input("Enter your list of numbers:")
  if num=="":
    break
  else:
    list.append(int(num))

print(list)

sort=list.sort()

print("Sorted List is: " + str(sort))
print("Median is "+str(statistics.median(list)))
print("Mean is "+str(statistics.mean(list)))
print("Mode is "+str(statistics.mode(list)))
