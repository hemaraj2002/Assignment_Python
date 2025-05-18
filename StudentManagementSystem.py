class Student:
    def __init__(self, student_id, name, course, avg_marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.avg_marks = avg_marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Average Marks: {self.avg_marks}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter student's ID: ")
        name = input("Enter student's name: ")
        course = input("Enter student's course: ")
        avg_marks = float(input("Enter student's average marks: "))
        student = Student(student_id, name, course, avg_marks)
        self.students[student_id] = student
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students.values():
                print(student)

    def update_student(self):
        student_id = input("Enter ID of student to update: ")
        if student_id in self.students:
            name = input("Enter new name: ")
            course = input("Enter new course: ")
            avg_marks = float(input("Enter new average marks: "))
            student = self.students[student_id]
            student.name = name
            student.course = course
            student.avg_marks = avg_marks
            print("Student updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self):
        student_id = input("Enter ID of student to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def menu(self):
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    system = StudentManagementSystem()
    system.menu()

if __name__ == "__main__":
    main()
