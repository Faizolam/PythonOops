class Student:
    def __init__(self, student_id, name):
        self.student_id=student_id
        self.name=name
        self.enrolled_courses=[]

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)


    def drop(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)

    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"
    
    def display_courses(self):
        pass

class Course:
    def __init__(self, course_id, title, capacity):
        self.course_id = course_id
        self.title = title
        self.capacity = capacity
        self.enrolled_students = []

    def add_student(self, student): #→ Adds a student to the course if there is space
        if student not in self.enrolled_students and self.capacity > 0:
            self.enrolled_students.append(student)
            print(self.enrolled_students, student)
            self.capacity -= 1
            print(f"student added to {self.course_id}")

    def remove_student(self, student): # → Removes the student
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            self.capacity += 1
            print(f"Student Droped")
        else:
            print(f"Student dose not exists")

    def __str__(self):
        return f"{self.title} (ID: {self.course_id})"
    
class University:
    def __init__(self, name):
        self.name = name
        self.students=[]
        self.courses=[]

    def add_student(self, student:Student):
        if self.find_student_by_id(student.student_id) is None:
            self.students.append(student)
            print(f"Student {student.name} and id {student.student_id} registered successfully!")



    def add_course(self, course:Course):
        if self.find_course_by_id(course.course_id) is None:
            self.courses.append(course)
            print(f"Course {course.title} with id {course.course_id} added")


    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def enroll_student(self, student_id, course_id):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)

        if student and course:
            course.add_student(student)
            student.enroll(course)
        else:
            print("Sorry, No student")

    def drop_student(self, student_id, course_id):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)

        if student and course:
            course.remove_student(student)
            student.drop(course)
        else:
            print(f"There is no {student.name}")

    def display_all_courses(self):
        print(f"{self.name}'s Courses:")
        for course in self.courses:
            print(f"- {course.title} ")

    def display_all_students(self):
        print(f"{self.name}'s Courses:")
        for student in self.students:
            print(f"- {student.name}")


# create Students
student1 = Student(1, "Faiz")
student2 = Student(2, "Maaz")
student3 = Student(3, "Masnoon")

# Create Courses
course1 = Course(101, "Physics", 5)
course2 = Course(102, "Mathematics", 4)
course3 = Course(103, "Chemistry", 4)

# Create University
uni = University("Aliah University")

# Add Courses First
uni.add_course(course1)
uni.add_course(course2)
uni.add_course(course3)

# Add Students
uni.add_student(student1)
uni.add_student(student2)
uni.add_student(student3)

# Enroll Students in Courses
uni.enroll_student(1, 101)
uni.enroll_student(2, 101)
uni.enroll_student(3, 102)
uni.enroll_student(3, 103)


