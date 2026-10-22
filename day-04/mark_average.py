#printing average
total = 0
count = 0

mark = int(input("Enter a mark (-1 to stop): "))

while mark != -1:

    if mark >= 0 and mark <= 100:
        total = total + mark
        count = count + 1
    else:
        print("Reject", mark)

    mark = int(input("Enter a mark (-1 to stop): "))

if count == 0:
    print("No valid marks entered.")
else:
    average = total / count
    print("Average: {:.2f}".format(average))
