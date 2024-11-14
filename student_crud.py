import unittest

class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}

    # CREATE
    def create_student(self, student_id, name, age, major):
        if student_id in self.students:
            print("Student with this ID already exists.")
            return False
        else:
            self.students[student_id] = Student(student_id, name, age, major)
            print("Student created successfully.")
            return True

    # READ
    def read_student(self, student_id):
        if student_id in self.students:
            print(str(self.students[student_id]) + "\n")
            return student_id
        else:
            print("Student not found.")

    def read_all_students(self):
        if not self.students:
            print("No students registered.")
            return []
        else:
            for student in self.students.values():
                print(str(student))
            return self.students.values()

    # UPDATE
    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            print("Student updated successfully.")
            return True
        else:
            print("Student not found.")
            return False

    # DELETE
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
            return True
        else:
            print("Student not found.")
            return False
        
class Crud_Test(unittest.TestCase):
    def setUp(self):
        self.system = StudentRegistrationSystem()
    
    # Test for creating a student - Valid
    def test_create_student_valid(self):
        student_id = "1"
        name = "Minh"
        age = 20
        major = "Comp. Sci."
        result = self.system.create_student(student_id, name, age, major)
        self.assertTrue(result)
        self.assertIn(student_id, self.system.students)
        self.assertEqual(self.system.students[student_id].name, name)
        self.assertEqual(self.system.students[student_id].age, age)
        self.assertEqual(self.system.students[student_id].major, major)
        
    # Test for creating a student - Invalid
    def test_create_student_invalid(self):
        student_id = "1"
        name = "Minh"
        age = 20
        major = "Comp. Sci."
        self.system.create_student(student_id, name, age, major)
        result = self.system.create_student(student_id, name, age, major)
        self.assertFalse(result)

    # Test for reading a student - Valid
    def test_read_student_valid(self):
        student_id = "1"
        name = "Minh"
        age = 20
        major = "Comp. Sci."
        self.system.create_student(student_id, name, age, major)
        result = self.system.read_student(student_id)
        self.assertTrue(result)
        self.assertEqual(result, student_id)
        self.assertEqual(self.system.students[result].name, name)
        self.assertEqual(self.system.students[result].age, age)
        self.assertEqual(self.system.students[result].major, major)
        
    # Test for reading a student - Invalid
    def test_read_student_invalid(self):
        student_id = "1"
        result = self.system.read_student(student_id)
        self.assertFalse(result)
        
    #Test for reading all student - Valid
    def test_read_all_students_valid(self):
        student_id = "1"
        name = "Minh"
        age = 20
        major = "Comp. Sci."
        self.system.create_student(student_id, name, age, major)
        result = list(self.system.read_all_students())
        self.assertTrue(result)
        self.assertEqual(result[0].student_id, student_id)
        self.assertEqual(self.system.students[result[0].student_id].name, name)
        self.assertEqual(self.system.students[result[0].student_id].age, age)
        self.assertEqual(self.system.students[result[0].student_id].major, major)
        
        student_id_2 = "2"
        name_2 = "Vo"
        age_2 = 20
        major_2 = "Comp. Sci."
        self.system.create_student(student_id_2, name_2, age_2, major_2)
        result = list(self.system.read_all_students())
        self.assertTrue(result)
        self.assertEqual(result[0].student_id, student_id)
        self.assertEqual(self.system.students[result[0].student_id].name, name)
        self.assertEqual(self.system.students[result[0].student_id].age, age)
        self.assertEqual(self.system.students[result[0].student_id].major, major)
        self.assertEqual(result[1].student_id, student_id_2)
        self.assertEqual(self.system.students[result[1].student_id].name, name_2)
        self.assertEqual(self.system.students[result[1].student_id].age, age_2)
        self.assertEqual(self.system.students[result[1].student_id].major, major_2)
        
    #Test for reading all student - Invalid
    def test_read_all_students_invalid(self):
        result = self.system.read_all_students()
        self.assertFalse(result)
        
    #Test for updating student - Valid
    def test_update_student_valid(self):
        student_id = "1"
        name = "Minh"
        age = 20
        major = "Comp. Sci."
        self.system.create_student(student_id, name, age, major)
        name_update = "Vo"
        age_update = 21
        major_update = "Business"
        result = self.system.update_student(student_id, name_update, age_update, major_update)
        self.assertTrue(result)
        self.assertIn(student_id, self.system.students)
        self.assertEqual(self.system.students[student_id].name, name_update)
        self.assertEqual(self.system.students[student_id].age, age_update)
        self.assertEqual(self.system.students[student_id].major, major_update)

    #Test for updating student - Invalid
    def test_update_student_invalid(self):
        student_id = "1"
        name = "Minh"
        age = 20
        major = "Comp. Sci."
        result = self.system.update_student(student_id, name, age, major)
        self.assertFalse(result)
        

    #Test for deleting student - Valid
    def test_delete_student_valid(self):
        student_id = "1"
        name = "Minh"
        age = 20
        major = "Comp. Sci."
        self.system.create_student(student_id, name, age, major)
        result = self.system.delete_student(student_id)
        self.assertTrue(result)
        self.assertNotIn(student_id, self.system.students)
        
    #Test for deleting student - Invalid
    def test_delete_student_invalid(self):
        student_id = "1"
        name = "Minh"
        age = 20
        major = "Comp. Sci."
        self.system.create_student(student_id, name, age, major)
        result = self.system.delete_student("2")
        self.assertFalse(result)
        self.assertIn(student_id, self.system.students)
        self.assertEqual(self.system.students[student_id].name, name)
        self.assertEqual(self.system.students[student_id].age, age)
        self.assertEqual(self.system.students[student_id].major, major)

if __name__ == '__main__':
    unittest.main()
    