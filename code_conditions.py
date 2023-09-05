#compare minimum marks of the students
minMarks = 30
compareStudents = (float(input('input your value: ')))

if compareStudents >= minMarks:
    print("You are eligible")
elif compareStudents >= 25:
    print("You are not eligible but have been put into a waiting list")
else: print("You are not eligible!")
    