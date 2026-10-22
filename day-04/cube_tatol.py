#cube
total = 0
n=int(input("Enter your  number:"))
for num in range(1, n+1):
    cube=num**3
    
    print(cube,end=",")
    total = total + cube
print("The total is:", total)