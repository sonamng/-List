# # accending

a=[3,12,4,5,76,87]
i=0
while i<len(a):
     j=0
     while j<len(a):
          if a[i]<a[j]:
               d=a[i]
               a[i]=a[j]
               a[j]=d
          j=j+1
     i=i+1
print("acending",a)


