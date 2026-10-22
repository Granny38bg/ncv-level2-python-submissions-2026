
# Program to find the Highest Common Factor (HCF)
# We declare variable num1 and num2, then assign them to the inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# The hcf is asigned to 1
hcf = 1
# The for loof and the formula that calcultes the highest commom factor 
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
#Display the highest common factor 
print("The HCF is:", hcf)
