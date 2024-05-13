# write a program to check a number enter by user is even or odd.
# User_number=int(input("Enter a number to check whether it is Evern or Odd:\n"))
# if User_number%2==0:
#     print(User_number,"is Even number.")
# else:
#     print(User_number,"is Odd number")


# write a program to find greatest of 3 number entered by user.

# def find_greatest(num1, num2, num3):
#     return max(num1, num2, num3)

# User_num1=int(input("Enter the first number:\n"))
# User_num2=int(input("Enter the second number:\n"))
# User_num3=int(input("Enter the third number:\n"))

# Greatest = find_greatest(User_num1, User_num2, User_num3)
# print(Greatest, "is the greatest among the all")



# swap two numbers without using 3rd veriable
# case 1:
# User_num1=int(input("Enter the number 1:\n"))
# User_num2=int(input("Enter the number 1:\n"))
# User_num1 , User_num2 = User_num2 ,User_num1
# print(User_num1,"\n",User_num2 )

# case 2:
# User_num1=int(input("Enter the number 1:\n"))
# User_num2=int(input("Enter the number 1:\n"))
# User_num1=User_num1+User_num2
# User_num2=User_num1-User_num2
# User_num1=User_num1-User_num2
# print(User_num1,"\n",User_num2 )


# find factorial of a given number.
# def Find_Fact(n):
#     if n<0:
#         return 0
#     if n==0:
#         return 1
#     else:
#         return n* Find_Fact(n-1)

# User_num=int(input("Enter a number to find factorial:\n"))
# fact=Find_Fact(User_num)
# print(fact,"is the factorail of ",User_num,"!")


# Check the number is prime or not.
# def check(num):
#     c=0
#     for i in range(1,num+1):
#         if (num%i==0):
#             c=c+1
#     return c

# User_num=int(input("Enter the number:\n"))
# ans=check(User_num)
# if ans == 2:
#     print(User_num," is prime")
# else:
#     print(User_num," is not prime")
    

# program to print triangle 
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("\n")


# program for next triangle pattern   
# for i in range(1,6):
#     print("* "*i,end=" ")
#     print("\n")


# program for another pattern
# for i in range(1,6):
#     print(" "*(5-i),end=" ")
#     print("* "*i,end=" ")
#     print("\n")



""" 
write a program to find the grade of students in 5 different subjects along with    marks to
illustrate the usage of default constructor , constant value and inheritance.
"""
class Student:
  PASS_MARK = 40  #Constant value

  def __init__(self, name): #default constructor to add student 
    self.name = name
    self.subjects = []

  def add_subject(self, subject, marks): #function to add subject  
    self.subjects.append((subject, marks))

  def calculate_grade(self, subject): #to calculate the grade of student
    for sub, marks in self.subjects:
      if sub == subject and marks >= self.PASS_MARK:
        return "Pass"
    return "Fail"

  def calculate_overall_grade(self):
    """
    Calculates the overall grade (Pass/Fail) based on all subjects.
    (Simple implementation assuming passing all subjects is required)
    """
    for sub, marks in self.subjects:
      if marks < self.PASS_MARK:
        return "Fail"
    return "Pass"

class HighSchoolStudent(Student):
  """
  This class inherits from Student and adds functionality specific to high school students.
  """

  def __init__(self, name, grade_level):
    """
    Inherits from Student's constructor and adds grade level.
    """
    super().__init__(name)  # Call the base class constructor
    self.grade_level = grade_level

  def calculate_overall_grade(self):
    # Call the base class method to check subject pass/fail
    base_grade = super().calculate_overall_grade()
    if base_grade == "Pass" and self.grade_level == 12:  # Assuming grade 12 requires more credits
      return "Graduated"
    return base_grade  

# Create student objects
student1 = Student("Ravi")
student2 = HighSchoolStudent("Riya", 11)  # High school student with grade level

# Add subjects and marks
student1.add_subject("Math", 85)
student1.add_subject("Science", 78)
student1.add_subject("English", 90)
student1.add_subject("History", 65)
student1.add_subject("Art", 95)

student2.add_subject("Math", 35)
student2.add_subject("Science", 82)
student2.add_subject("English", 70)
student2.add_subject("History", 88)
student2.add_subject("Art", 80)

# Print student information and grades
print("Student Name:", student1.name)
for subject, marks in student1.subjects:
  print(f"{subject}: {marks} ({student1.calculate_grade(subject)})")
print(f"Overall Grade: {student1.calculate_overall_grade()}\n")

print("Student Name:", student2.name)
for subject, marks in student2.subjects:
  print(f"{subject}: {marks} ({student2.calculate_grade(subject)})")
print(f"Overall Grade: {student2.calculate_overall_grade()}")
