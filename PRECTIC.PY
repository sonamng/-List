
# # three meximun  frist and secoend and third meximum



a=[10,20,30,40,50,60]
max=a[0]
i=0
while i<len(a):
     if a[i]>max:
          max=a[i]
     i=i+1
print(max,"first maximum")
a.remove(max)
secoend=a[0]
i=0
while i<len(a):
     if a[i]>secoend:
          secoend=a[i]
     i=i+1
print(secoend,"secoend maximum")
a.remove(secoend)
third_max=a[0]
i=0
while i<len(a):
     if a[i]>third_max:
          third_max=a[i]
     i=i+1
print(third_max,"third maximum") 





# a=["a","a","b","c","d","b"]
# i=0
# count=0
# while i<len(a):
#      i=i+1
#      count=count+1
# print(count)

# a=[1,1,2,3,3,4,5,4,5,6]
# i=0
# c=[]
# while i<len(a):
#      b=a[i]
#      if b not in a:
#           c.append(b)
#      i=i+1
#      print(c)


