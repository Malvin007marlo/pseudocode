print("enter marks")
a=int(input())
b= int(input())
k=int(input())
s=int(input())
d=int(input())
total= a+b+k+s+d
avg=(a+b+k+s+d)/5
print (total)
print (avg)
if avg>=70and avg<=100:
  print("grade A")
elif avg>60 and avg<=69:
    print("b")
elif avg>=50 and avg <=59:
    print("b")
elif avg>=40 and avg <49:
    print("e")