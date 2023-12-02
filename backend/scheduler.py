class Student:
    def __init__(self, name):
        self.name = name
        self.classes = []

    def add_class(self, class_name):
        if class_name not in self.classes:
            self.classes.append(class_name)
            print(f"{self.name} added {class_name} to their schedule.")
        else:
            print(f"{self.name} is already enrolled in {class_name}.")

    def view_schedule(self):
        if not self.classes:
            print(f"{self.name} has not selected any classes yet.")
        else:
            print(f"{self.name}'s Class Schedule:")
            for class_name in self.classes:
                print(class_name)

def main():
    students = []

    while True:
        print("\nClass Selection App")
        print("1. Create Student")
        print("2. Add Class to Student's Schedule")
        print("3. View Student's Schedule")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            student = Student(name)
            students.append(student)
            print(f"Student {name} created.")
        
        elif choice == "2":
            name = input("Enter student's name: ")
            student = next((s for s in students if s.name == name), None)
            if student:
                class_name = input("Enter class name to add: ")
                student.add_class(class_name)
            else:
                print(f"Student {name} not found.")
        
        elif choice == "3":
            name = input("Enter student's name: ")
            student = next((s for s in students if s.name == name), None)
            if student:
                student.view_schedule()
            else:
                print(f"Student {name} not found.")
        
        elif choice == "4":
            print("Exiting the Class Selection App. Goodbye!")
            break

if __name__ == "__main__":
    main()
