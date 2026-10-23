# Lists 
marks = []

mark = int(input("Enter mark or -1 to stop:"))

while mark!= -1:
    marks.append(mark)
    mark = int(input("Enter mark or -1 to stop:"))

print (f"Our list has {len(marks)} elements:")

for x in range(len(marks)):
    print(marks[x])
    
#get the sum of all marks
    sum = 0
    for x in range (len(marks)):
        mark = marks[x]
        sum = sum + mark
        
print(f'The sum of all marks = {sum}')

# get the average of all marks
total = 0
for x in range(len(marks)):
    mark = marks[x]
    total = total + mark
    
avg = total/ len(marks)
print(f'The average of all marks = {avg}')