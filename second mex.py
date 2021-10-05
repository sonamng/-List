

list=[50, 40, 23, 70, 56, 12, 5, 10, 7]
max=list[0]
i=0
while i<len(list):
     if list[i]>max:
          max=list[i]
     i=i+1
list.remove(max)
i=0
secoend=list[0]
while i<len(list):
     if list[i]>secoend:
          secoend=list[i]
     i=i+1
print(secoend)
