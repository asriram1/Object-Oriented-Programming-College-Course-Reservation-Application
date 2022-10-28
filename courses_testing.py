import unittest
from courses import *
import random

class Testing(unittest.TestCase):
        
    def test_add_course(self):
        """Testing registering for course by student"""
        self.courses_table = CourseListTable()
        self.courses_table.create_table()
        self.student_name = "random"+str(random.randint(1,1000000))
        self.student = StudentRegistrations(self.student_name)
        self.student.add_course(1122, "OOP")
        command = """
           SELECT * FROM registrations WHERE student_name = %s;
        """
        val = (self.student_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        self.assertIs(1,len(results_list))

    def test_drop_course(self):
        self.courses_table = CourseListTable()
        self.courses_table.create_table()
        self.student_name = "random"+str(random.randint(1,1000000))
        self.student = StudentRegistrations(self.student_name)
        self.student.add_course(1122, "OOP")
        self.student.drop_course("OOP")
        command = """
           SELECT * FROM registrations WHERE student_name = %s;
        """
        val = (self.student_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        self.assertIs(0,len(results_list))

    def test_add_new_course(self):
        """Testing adding new course to the database by admin"""
        self.courses_table = CourseListTable()
        self.courses_table.create_table()
        self.admin = CourseAdministration("admin1")
        self.course_id =  random.randint(1,100000)
        self.course_name ="test"
        self.instructor_name = "test"
        self.room = "test"
        self.restrictions = "test"
        self.schedule = "test"
        self.section = "test"
        self.course_features = "test"
        self.registration = "test"
        self.admin.add_new_course(self.course_id, self.course_name, self.instructor_name, self.room, self.restrictions, self.schedule, self.section, self.course_features, self.registration)
        command = """
           SELECT * FROM courses_table WHERE course_id = %s;
        """
        val = (self.course_id,)
        results_list = self.courses_table.execute_select_command(command, val)
        self.assertIs(1,len(results_list))

    def test_delete_course(self):
        """Testing deleting course from the database by admin"""
        self.courses_table = CourseListTable()
        self.courses_table.create_table()
        self.admin = CourseAdministration("admin1")
        self.course_id =  random.randint(1,10000)
        self.course_name ="test"+str(random.randint(1,1000000))
        self.instructor_name = "test"
        self.room = "test"
        self.restrictions = "test"
        self.schedule = "test"
        self.section = "test"
        self.course_features = "test"
        self.registration = "test"
        self.admin.add_new_course(self.course_id, self.course_name, self.instructor_name, self.room, self.restrictions, self.schedule, self.section, self.course_features, self.registration)
        self.admin.delete_course(self.course_name)
        command = """
           SELECT * FROM courses_table WHERE course_name = %s;
        """
        val = (self.course_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        self.assertIs(0,len(results_list))

    def test_close_registration(self):
        self.courses_table = CourseListTable()
        self.courses_table.create_table()
        self.admin = CourseAdministration("admin1")
        self.course_id =  random.randint(1,10000)
        self.course_name ="test"+str(random.randint(1,1000000))
        self.instructor_name = "test"
        self.room = "test"
        self.restrictions = "test"
        self.schedule = "test"
        self.section = "test"
        self.course_features = "test"
        self.registration = "Open"
        self.admin.add_new_course(self.course_id, self.course_name, self.instructor_name, self.room, self.restrictions, self.schedule, self.section, self.course_features, self.registration)
        self.admin.close_registration(self.course_name)
        command = """
           SELECT registration FROM courses_table WHERE course_name = %s;
        """
        val = (self.course_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        self.assertEqual("Closed",results_list[0][0])

    def test_change_course_schedule(self):
        """Testing enforcing course schedule changes by admin"""
        self.courses_table = CourseListTable()
        self.courses_table.create_table()
        self.admin = CourseAdministration("admin1")
        self.course_id =  random.randint(1,10000)
        self.course_name ="test"+str(random.randint(1,1000000))
        self.instructor_name = "test"
        self.room = "test"
        self.restrictions = "test"
        self.schedule = "test"
        self.section = "test"
        self.course_features = "test"
        self.registration = "Open"
        self.admin.add_new_course(self.course_id, self.course_name, self.instructor_name, self.room, self.restrictions, self.schedule, self.section, self.course_features, self.registration)
        self.new_schedule= "schedule"+str(random.randint(1,1000000))
        self.admin.change_course_schedule(self.course_name, self.section, self.new_schedule)
        command = """
           SELECT schedule FROM courses_table WHERE course_name = %s;
        """
        val = (self.course_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        self.assertEqual(self.new_schedule,results_list[0][0])

    def test_change_course_features(self):
        """Testing course feature changes by an instructor"""

        #Ensuring that instructor teaches the course which they will modify
        self.courses_table = CourseListTable()
        self.courses_table.create_table()
        self.instructor = InstructorCourseModify("instructor_1")
        self.admin = CourseAdministration("admin1")
        self.course_id =  random.randint(1,10000)
        self.course_name ="test"+str(random.randint(1,1000000))
        self.instructor_name = "instructor_1"
        self.room = "test"
        self.restrictions = "test"
        self.schedule = "test"
        self.section = "test"
        self.course_features = "test"
        self.registration = "Open"
        self.admin.add_new_course(self.course_id, self.course_name, self.instructor_name, self.room, self.restrictions, self.schedule, self.section, self.course_features, self.registration)
        self.new_course_features = "features"+str(random.randint(1,1000000))
        self.instructor.modify_course_features(self.course_name, self.new_course_features)
        command = """
           SELECT course_features FROM courses_table WHERE course_name = %s;
        """
        val = (self.course_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        self.assertEqual(self.new_course_features,results_list[0][0])



if __name__ == '__main__':
    unittest.main()
