# Lists 
marks = []

mark = int(input("Enter mark or -1 to stop:"))
i = 0
while mark!= -1:
    marks.append(mark)
    mark = int(input("Enter mark or -1 to stop:"))

print (f"Our list has {len(marks)} elements:")

for x in range(len(marks)):
    print(marks[x])