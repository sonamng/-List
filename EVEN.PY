# even number and odd number

a= [2,5,6,7,9,4,8,3]
i=0
odd=[]
even=[]
while i<len(a):
     if a[i]%2==0:
          even.append(a[i])
     else:
          odd.append(a[i])
     i=i+1
print("even",even)
print("odd",odd)          




