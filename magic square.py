magic_squre=[ [8,3,4],
              [1,5,9],
              [1,6,2] 
]
i=0
s1=0
while i<len(magic_squre):
     a=0
     while a<len(magic_squre):
          s1=s1+magic_squre[i][a]
          a=a+1
     i=i+1
print(s1)
j=0
s2=0
while j<len(magic_squre):
     b=0
     while b<len(magic_squre):
          s2=s2+magic_squre[j][b]
          b=b+1
     j=j+1     
print(s2)
k=0
s3=0
while k<len(magic_squre):
     c=0
     while c<len(magic_squre):
          s3=s3+magic_squre[k][c]
          c=c+1
     k=k+1
     print(s3)
if s2==s2==s3:
     print("it is magic_squre") 
else:
     print("not") 