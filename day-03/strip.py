name = input("Enter your name:")
staff_number = input("Enter your Staff number:")
level = input("Enter your level:")

while not name.strip():
    print("That's a blank space. Please enter a proper name.")
    name = input("Enter your name: ")
    
#part = name.split()

if name.isalpha():
   print("Accepted")
else:
   print("Rejected")
   
if staff_number.isdigit():
   print("Accepted")
else:
   print("Rejected")
   
if level.isalpha():
   print("Rejected")
else:
   print("Accepted")