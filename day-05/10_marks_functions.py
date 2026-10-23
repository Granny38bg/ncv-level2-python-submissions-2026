# Lists and functions

def getMarks():
    marks = []
    mark = int(input("Enter mark or -1 to stop: "))

    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark or -1 to stop: "))

    return marks


def print_list_size(marks):
    print(f"Our list has {len(marks)} elements.")


def print_marks(marks):
    for x in range(len(marks)):
        print(marks[x])


def get_sum_of_marks(marks):
    total = 0
    for x in range(len(marks)):
        mark = marks[x]
        total = total + mark
    return total


def determine_highest(marks):
    if len(marks) == 0:
        print("No marks have been entered.")
    else:
        highest = marks[0]

        for i in range(len(marks)):
            current_mark = marks[i]
            if current_mark > highest:
                highest = current_mark

        print("The highest mark is:", highest)


# Menu
menu = (
    "Press 1: Capturing marks\n"
    "Press 2: To check number of marks\n"
    "Press 3: To calculate sum of marks\n"
    "Press 4: To find highest mark\n"
    "Press -1: To exit"
)

entered_marks = []

while True:
    print("\n" + menu)
    choice = int(input("Make your choice: "))

    if choice == 1:
        entered_marks = getMarks()
        print("Entered marks:", entered_marks)

    elif choice == 2:
        print_list_size(entered_marks)

    elif choice == 3:
        calc_sum = get_sum_of_marks(entered_marks)
        print("Sum of all marks:", calc_sum)

    elif choice == 4:
        determine_highest(entered_marks)

    elif choice == -1:
        print("Exiting program...")
        break

    else:
        print("Not on the menu. Please try again.")
        choice = int(input(':Make your choice (-1 to exit)'))