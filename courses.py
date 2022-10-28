from abc import ABC, abstractmethod 
import sqlite3
from sqlite3 import Error
import random
import os
import mysql.connector


class CoursesDatabase:
    """Initializes MySQL to connect to courses database"""
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "courses"
        )

        self.mycursor = self.cnx.cursor()
    def connection(self):
        return self.cnx
    def db_cursor(self):
        return self.mycursor

class Table(ABC):
    """An abstract class to provide an interface for the StudentRegistration & CourseList tables"""

    def __init__(self):
        """Generic table creation script"""
        self.db = CoursesDatabase()
        self.cnx = self.db.connection()
        self.mycursor = self.db.db_cursor()
        self.create_table_sql = """"""
    
    def create_table(self):
        """Creating the table"""
        try:
            self.mycursor.execute(self.create_table_sql)
        except Error as e:
            print(e)

    def execute_command(self, command,val):
        """Execute any SQL command for this table"""
        try:
            self.mycursor.execute(command,val)
            self.cnx.commit()
            # self.mycursor.close()
            # self.cnx.close()
        except Error as e:
            print(e)
    
    def execute_select_command(self, command, val):
        """Execute any Select SQL command for this table"""
        try:
            self.mycursor.execute(command,val)
            self.rows = self.mycursor.fetchall()
            return self.rows
        except Error as e:
            print(e)


class StudentRegistrationTable(Table):

    def __init__(self):
        """Initialize registrations table"""
        super().__init__()
        self.create_table_sql = "CREATE TABLE IF NOT EXISTS registrations(registration_id int PRIMARY KEY, student_name VARCHAR(50) NOT NULL, course_id int NOT NULL, course_name VARCHAR(50) NOT NULL);"
    
    def create_table(self):
        """Creating the table"""
        super().create_table()


    def execute_command(self, command,val):
        """Execute any SQL command for this table"""
        super().execute_command(command,val)

    def execute_select_command(self, command, val):
        """Execute any Select SQL command for this table"""
        return super().execute_select_command(command, val)

class CourseListTable(Table):

    def __init__(self):
        """Initialize courses table"""
        super().__init__()
        self.create_table_sql = """ CREATE TABLE IF NOT EXISTS courses_table( course_id int PRIMARY KEY, course_name VARCHAR(50) NOT NULL, instructor_name VARCHAR(50) NOT NULL,
         room VARCHAR(20) NOT NULL, restrictions VARCHAR(100) NOT NULL, schedule VARCHAR(50) NOT NULL, section VARCHAR(20) NOT NULL, course_features VARCHAR(50) NOT NULL, 
         registration VARCHAR(50) NOT NULL);"""

    def create_table(self):
        """Creating the table"""
        super().create_table()

    def execute_command(self, command, val):
        """Execute any SQL command for this table"""
        super().execute_command(command,val)

    def execute_select_command(self, command, val):
        """Execute any Select SQL command for this table"""
        return super().execute_select_command(command, val)



class StudentRegistrations:
    """Implements student-specfic course functionality. Student needs to be logged in."""

    def __init__(self, student_name):
        """Initialize all relevant tables"""
        self.student_name = student_name
        self.table = StudentRegistrationTable()
        self.table.create_table()
        self.courses_table = CourseListTable()
        self.courses_table.create_table()


    def add_course(self, course_id, course_name):
        """Add the given course in the registrations table for given student""" 
        registration_id = random.randint(0,10000000)
        
        #Check if course_name & course_id exist
        command = """
           SELECT * FROM courses_table WHERE course_name = %s AND course_id = %s;
        """
        val = (course_name, course_id)
        results_list = self.courses_table.execute_select_command(command, val)  

        #Check if course is open for registration
        command = """
            SELECT registration FROM courses_table WHERE course_name = %s
        """
        val = (course_name, )
        results = self.courses_table.execute_select_command(command, val)
        registration = []
        for x in results:
            registration = x

        #If the course exists & registration is open register, otherwise print appropriate message
        if results_list and registration[0] != "Closed":
            command = """
                INSERT INTO registrations(registration_id, student_name, course_id, course_name) VALUES(%s,%s,%s,%s);
            """
            val = (registration_id, self.student_name, course_id, course_name)
            self.table.execute_command(command,val)
        elif registration[0] =="Closed":
            print("Registration for this course is closed")
        else:
            print("Enter a valid course name & id!")
    
    def drop_course(self, course_name):
        """Drop the given course for student"""
        command = """
            DELETE FROM registrations WHERE student_name = %s AND course_name = %s
        """
        val = (self.student_name, course_name)
        self.table.execute_command(command,val)

    def view_registered_courses(self):
        """View all registered courses"""
        command = """
           SELECT * FROM registrations WHERE student_name = %s;
        """
        val = (self.student_name,)
        results_list = self.table.execute_select_command(command, val)
        for x in results_list:
            print(x)
    

class StudentCourseViewing:
    """Student can view courses without being logged in"""

    def __init__(self):
        """Iniitalize relevant tables"""
        self.courses_table = CourseListTable()
        self.courses_table.create_table()

    def view_all_courses(self):
        """View all courses in the database"""

        command = """
           SELECT * FROM courses_table WHERE 1 = %s;
        """
        val = (1,)
        results_list = self.courses_table.execute_select_command(command, val)
        for x in results_list:
            print(x)

    def view_restrictions(self, course_name):
        """View all restrictions for selected course"""
    
        command = """
           SELECT restrictions FROM courses_table WHERE course_name = %s;
        """
        val = (course_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        for x in results_list:
            print(x)

    def view_course_schedule(self, course_name):
        """View schedule for selected course"""
    
        command = """
           SELECT schedule FROM courses_table WHERE course_name = %s;
        """
        val = (course_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        for x in results_list:
            print(x)
    
    def view_room_assignment(self, course_name):
        """View room assignment for selected course"""
    
        command = """
           SELECT room FROM courses_table WHERE course_name = %s;
        """
        val = (course_name,)
        results_list = self.courses_table.execute_select_command(command, val)
        for x in results_list:
            print(x)
    



class CourseAdministration:
    """Implements Administrator specfic functionality for courses"""

    def __init__(self, admin_username):
        """Iniitalize relevant tables"""
        self.admin_username = admin_username
        self.courses_table = CourseListTable()
        self.courses_table.create_table()

    def add_new_course(self, course_id, course_name, instructor_name, room, restrictions, schedule, section, course_features, registration ):
        """Add a new course to the database"""
        command  = """
        INSERT INTO courses_table(course_id, course_name, instructor_name, room, restrictions, schedule, section, course_features, registration) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        val = (course_id, course_name, instructor_name, room, restrictions, schedule, section, course_features, registration)
        self.courses_table.execute_command(command,val)

    
    def delete_course(self, course_name):
        """Delete a course from the database"""

        command = """
            DELETE FROM courses_table WHERE course_name = %s
        """
        val = (course_name,)
        self.courses_table.execute_command(command,val)

    def close_registration(self, course_name):
        """Close registration for course"""

        command = """
            UPDATE courses_table SET registration = "Closed" WHERE course_name = %s
        """
        val = (course_name,)
        self.courses_table.execute_command(command,val)

    def change_course_schedule(self, course_name, section, new_schedule):
        """Change course schedule for given section of course"""

        command = """
            UPDATE courses_table SET schedule = %s WHERE course_name = %s AND section = %s
        """
        val = (new_schedule,course_name, section)
        self.courses_table.execute_command(command,val)



class InstructorCourseModify:
    """Course feature modification functionality for instructors"""

    def __init__(self, instructor_name):
        """Iniitalize relevant tables"""
        self.instructor_name = instructor_name
        self.courses_table = CourseListTable()
        self.courses_table.create_table()

    def modify_course_features(self,course_name, new_features):
        """Modify features for course if taught by instructor"""

        #Check if instructor teaches course
        command = """
           SELECT * FROM courses_table WHERE course_name = %s AND instructor_name = %s;
        """
        val = (course_name, self.instructor_name)
        results_list = self.courses_table.execute_select_command(command, val)  
        #If the course is taught by instructor, modify course features
        if results_list:
            command = """
                UPDATE courses_table SET course_features = %s WHERE course_name = %s
            """
            val = (new_features,course_name)
            self.courses_table.execute_command(command,val)
        else:
            print("You can only update course features for your courses")
    

class InstructorClassRosters:
    """View class rosters regardless of whether class taught by instructor or not"""

    def __init__(self, instructor_name):
        """Iniitalize relevant tables"""
        self.instructor_name = instructor_name
        self.registrations_table = StudentRegistrationTable()
        self.registrations_table.create_table()

    def view_class_roster(self,course_name):
        """View all registered students for given course"""
        command = """
           SELECT student_name FROM registrations WHERE course_name = %s;
        """
        val = (course_name,)
        results_list = self.registrations_table.execute_select_command(command,val)
        for x in results_list:
            print(x)
    

