Here’s your next **Python OOP challenge** with a mix of **Pandas tasks** to keep things interesting and to help you practice both OOP concepts and data manipulation skills.

---

## **Challenge Title: Library Management System**

### **Overview**
Build a **Library Management System** using Python OOP principles. The system should allow libraries to manage books, members, and borrowing records. Additionally, use **Pandas** to analyze borrowing data for insights.

---

### **Requirements**

#### **1. Core Classes and Their Responsibilities**
1. **Book**:
   - Attributes: `book_id`, `title`, `author`, `copies_available`.
   - Methods:
     - `lend_copy()`: Decrease `copies_available` by 1.
     - `return_copy()`: Increase `copies_available` by 1.

2. **Member**:
   - Attributes: `member_id`, `name`, `borrowed_books` (list of borrowed book IDs).
   - Methods:
     - `borrow_book(book_id)`: Add a book ID to the member's borrowed list.
     - `return_book(book_id)`: Remove a book ID from the borrowed list.

3. **Library**:
   - Attributes: `library_name`, `books` (list of `Book` objects), `members` (list of `Member` objects).
   - Methods:
     - `add_book(book: Book)`: Add a new book to the library.
     - `add_member(member: Member)`: Add a new member to the library.
     - `lend_book(member_id, book_id)`: Lend a book to a member.
     - `return_book(member_id, book_id)`: Process the return of a borrowed book.
     - `display_books()`: Show all books in the library with availability status.

---

#### **2. Pandas Data Analysis Tasks**
1. **Generate Borrowing Records**:
   - After implementing the library system, simulate borrowing and returning events.
   - Store these events in a Pandas DataFrame with columns:
     - `event_id`, `member_id`, `book_id`, `event_type` (`borrow` or `return`), `timestamp`.

2. **Insights to Analyze**:
   - Find the **most borrowed book**.
   - Identify the **top borrowing members**.
   - Calculate the **total number of borrowing events** over time.
   - List books that have **never been borrowed**.

---

### **Constraints and Hints**
- Use unique IDs for books and members.
- Validate all operations (e.g., check if a book is available before lending, ensure members exist before borrowing).
- Leverage **Pandas** for efficient data manipulation and analysis.

---

### **Deliverables**
- Fully functional `LibraryManagementSystem` program in Python.
- Example usage with at least 5 books, 3 members, and multiple borrowing/returning events.
- Pandas analysis output for insights.

---

### **Stretch Goals**
1. Add functionality to export the borrowing records to a CSV file.
2. Implement a `search_book_by_title()` method to find books by keywords.
3. Visualize the borrowing trends over time using Matplotlib or Seaborn.

---

### **Next Steps**
- Start by defining the `Book`, `Member`, and `Library` classes.


---

Great! Since you want to focus on practicing only Python OOP, here’s your next challenge:

---

### 🧩 **Challenge: University Course Enrollment System**

You need to model a basic course enrollment system using OOP principles.

#### 🏫 Classes to Implement:

1. **Student**
   - Attributes:
     - `student_id`
     - `name`
     - `enrolled_courses` (List of `Course` objects)
   - Methods:
     - `enroll(course)` → Adds a course to the student's list
     - `drop(course)` → Removes a course
     - `display_courses()` → Shows all enrolled courses

2. **Course**
   - Attributes:
     - `course_id`
     - `title`
     - `capacity`
     - `enrolled_students` (List of `Student` IDs)
   - Methods:
     - `add_student(student)` → Adds a student to the course if there is space
     - `remove_student(student)` → Removes the student

3. **University**
   - Attributes:
     - `name`
     - `students` (list of all registered students)
     - `courses` (list of all available courses)
   - Methods:
     - `add_student(student)`
     - `add_course(course)`
     - `enroll_student(student_id, course_id)`
     - `drop_student(student_id, course_id)`
     - `display_all_courses()`
     - `display_all_students()`

---

### 🧠 Focus Concepts:
- Composition (e.g., Student has many Courses, Course has many Students)
- Encapsulation (use of private attributes if necessary)
- Clear method responsibilities
- Validation (e.g., course capacity check, valid student ID)

---

Awesome! Here's your **next Python OOP challenge**, and it's going to level you up with **inheritance**, **method overriding**, and **composition**.

---

## 🚗 Vehicle Rental System

You're tasked with building a basic vehicle rental system.

### 🎯 Objectives:
1. Use **inheritance** for different types of vehicles.
2. Track availability and rent/return status.
3. Use **composition** by associating rentals with users.

---

### 👨‍👩‍👦 Classes You Need to Create:

#### ✅ `Vehicle` (Base Class)
- Attributes:
  - `vehicle_id`
  - `brand`
  - `model`
  - `is_available` (default: `True`)
- Methods:
  - `rent()`: sets `is_available` to `False`
  - `return_vehicle()`: sets `is_available` to `True`
  - `__str__()`: nicely format vehicle info

---

#### ✅ `Car` (inherits from `Vehicle`)
- Extra Attribute:
  - `num_doors`
- Override `__str__()` to include type and doors info.

---

#### ✅ `Bike` (inherits from `Vehicle`)
- Extra Attribute:
  - `type` (e.g., "Mountain", "City")
- Override `__str__()` to include bike type.

---

#### ✅ `Customer`
- Attributes:
  - `customer_id`
  - `name`
  - `rented_vehicles`: list of vehicles
- Methods:
  - `rent_vehicle(vehicle)`
  - `return_vehicle(vehicle)`
  - `display_rentals()`

---

#### ✅ `RentalService`
- Attributes:
  - `vehicles`: list of all vehicles
  - `customers`: list of all customers
- Methods:
  - `add_vehicle(vehicle)`
  - `add_customer(customer)`
  - `find_vehicle_by_id(vehicle_id)`
  - `find_customer_by_id(customer_id)`
  - `rent_vehicle(customer_id, vehicle_id)`
  - `return_vehicle(customer_id, vehicle_id)`
  - `display_all_vehicles()`
  - `display_available_vehicles()`

---

### 🌟 Bonus (Optional)
- Try to prevent renting a vehicle that's already rented.
- Let customers rent multiple vehicles.

---
