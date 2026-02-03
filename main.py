import numpy as np 
class Students:
    name :str
    roll_no :str
    total_marks :int
    avg_marks :int
    status :bool
    marks :object
    
s = []
while(True):
    print("Wellcom to Student Performance Analysis System")
    x = input(("press 1: to store student data\npress 2: to calculate total marks\npress 3: to see avg marks\npress 4: to check student pass or fail\npress 5: to find max and min marks of student\npress 6: to find topper of class\npress b: to exit : "))

    match x:
        case "1":
            s1 = Students()
            s1.name = input("Enter students name : ")
            s1.roll_no = input("Enter roll number of students : ")
            l = []
            for i in range(0,5):
                l.append(int(input(f"Enter marks of sunject {i+1} : ")))
            s1.marks = np.array(l)
            s.append(s1)
        case "2":
            roll = input("Enter roll number of student : ")
            f = False
            for i in s:
                if(i.roll_no==roll):
                    i.total_marks = i.marks.sum()
                    print(f"Total marks obtain by {i.name} is : {i.total_marks}")
                    f = True
                    break
            if not f:
                print("Student not found ")
        case "3":
            roll = input("Enter roll number of student : ")
            f = False
            for i in s:
                if(i.roll_no==roll):
                    i.avg_marks = i.marks.mean()
                    print(f"Avg amrks of {i.name} is : {i.avg_marks}")
                    f = True
                    break
            if not f:
                print("Student not found ")
        case "4":
            roll = input("Enter roll number of student : ")
            f = False
            for i in s:
                if(i.roll_no==roll):
                    f = True
                    i.avg_marks = i.marks.mean()
                    status = i.avg_marks>33
                    print(f"{i.name} is {'pass' if status else 'fail'}")
                    break
            if not f:
                print("Student not found ")
        case "5":
            roll = input("Enter roll number of student : ")
            f = False
            for i in s:
                if(i.roll_no==roll):
                    f = True
                    max_marks = i.marks.max()
                    min_marks = i.marks.min()
                    
                    print(f"{i.name} obtain maximum marks is {max_marks}")
                    print(f"{i.name} obtain minimum marks is {min_marks}")
                    break
            if not f:
                print("Student not found ")
        case "6":
            if(len(s)==0):
                print("Students records not available ")
                continue
            topper = s[0]
            topper.avg_marks = topper.marks.mean()
            for i in s:
                i.avg_marks = i.marks.mean()
                if(i.avg_marks > topper.avg_marks):
                    # topper.avg_marks = i.marks.mean()
                    topper = i
            print("\n--Class Topper--")
            print("------------------")
            print(f"Name: {topper.name}")
            print(f"Roll No: {topper.roll_no}")
            print(f"Average Marks: {topper.avg_marks}")

        case "b":
            print("Thanks for visiting ")
            break
        case _:
            print("Please Enter a valid option\n")