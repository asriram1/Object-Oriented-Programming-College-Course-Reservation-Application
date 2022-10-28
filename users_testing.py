import unittest
from users import *

class Testing(unittest.TestCase):

    def test_database_creation(self):
        """Testing if users database creation is successful"""
        db = Database('Database','Users.db')
        db.create_connection()
        self.assertIsInstance(db, Database)

    def test_user_creation(self):
        """Testing if a new generic user is created successfully"""
        user = User("user2", "user_name2", "user_password2")
        UserDeletion.delete_user("user_name2","user_password2")
        self.assertIsInstance(user, User)

    def test_student_creation(self):
        """Testing if a new student is created successfully"""
        student = Student("name", "user_id", "random_password")
        UserDeletion.delete_user("user_id","random_password")
        self.assertIsInstance(student, Student)
    
    def test_instructor_creation(self):
        """Testing if a new instructor is created successfully"""
        instructor = Instructor("Instructor2", "instructor2", "intstructor_password2")
        UserDeletion.delete_user("instructor2","intstructor_password2")
        self.assertIsInstance(instructor, Instructor)

    def test_user_deletion(self):
        """Testing if a user gets deleted successfully"""
        student = Student("Student_4", "joey", "my_pass")
        return_value = UserDeletion.delete_user("joey", "my_pass")
        self.assertTrue(return_value)

    def test_user_login(self):
        """Testing if user login successful"""
        return_value = UserAuthentication.login("user_id","random_password")
        self.assertTrue(return_value)

    def test_user_logout(self):
        """Testing if user login successful"""
        return_value = UserAuthentication.logout("user_id","random_password")
        self.assertTrue(return_value)

    def test_password_change(self):
        """Testing if password change successful"""
        return_value = UserModification.change_password("user_id","new_password","random_password")
        self.assertTrue(return_value)

    def test_username_change(self):
        """Testing if username change successful"""
        return_value = UserModification.change_username("user_id","new_password","new_user_id")
        self.assertTrue(return_value)
    


if __name__ == '__main__':
    unittest.main()
