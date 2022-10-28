from users import *
from courses import *
from administrative import *
import time

class StudentMediator:
    """Student-specific course registration functionality"""

    def __init__(self):
        """Initialize student informtation"""
        self.username = ""
        self.password = ""
        self.login_status = 0
        self.courses = StudentCourseViewing()
    def create_student(self, name, username, password):
        """Register a new student if no account created"""
        try:
            Student(name,username,password)
        except:
            time.sleep(0)
        self.username = username
        self.password = password
        self.registrations = StudentRegistrations(name)
        UserAuthentication.login(username, password)
        self.login_status = 1

    def login(self, username, password):
        """Authenticate given student"""
        self.username = username
        self.password = password
        login_result = UserAuthentication.login(username, password)

        if login_result ==True:
            self.login_status = 1
            self.name = UserInformation.get_user_name(username,password)
            self.registrations = StudentRegistrations(self.name)
            if self.name == "User doesn't exist":
                return False
                print("Incorrect Login")
            else:
                return True
        else:
            return "Incorrect Login"

    def change_username(self,new_username):
        UserModification.change_username(self.username, self.password, new_username)
        self.username = new_username

    def change_password(self, new_password):
        UserModification.change_password(self.username, self.password, new_password)
        self.password = new_password

    def add_course(self, course_id, course_name):
        self.registrations.add_course(course_id, course_name)

    def drop_course(self, course_name):
        self.registrations.drop_course(course_name)
    
    def view_registered_courses(self):
        self.registrations.view_registered_courses()
    
    def view_all_courses(self):
        self.courses.view_all_courses()
    
    def view_restrictions(self, course_name):
        """View all restrictions for selected course"""
        self.courses.view_restrictions(course_name)

    def view_course_schedule(self, course_name):
        """View all restrictions for selected course"""
        self.courses.view_course_schedule(course_name)
    
    def view_room_assignment(self, course_name):
        self.courses.view_room_assignment(course_name)

    def logout(self):
        UserAuthentication.logout(self.username, self.password)
        self.username = ""
        self.password = ""
        self.login_status = 0

    def view_building_timings(self, building_name):
        building = ViewBuildingTimings(building_name)
        building.view_timings()


class InstructorMediator:
    """Instructor specific course functionality"""

    def __init__(self):
        self.name = ""
        self.username = ""
        self.password = ""
        self.login_status = 0

    def create_instructor(self, name, username, password):
        """Creating a new instructor account"""
        try:
            Instructor(name,username,password)
        except:
            time.sleep(0)
        self.name = name
        self.username = username
        self.password = password
        UserAuthentication.login(username, password)
        self.login_status = 1
    
    def login(self, username, password):
        """Authenticating instructor credentials"""
        self.username = username
        self.password = password
        login_result = UserAuthentication.login(username, password)
        if login_result ==True:
            self.login_status = 1
            self.name = UserInformation.get_user_name(username,password)
            if self.name == "User doesn't exist":
                return False
                print("Incorrect Login")
            else:
                return True
        else:
            return "Incorrect Login"
    
    def logout(self):
        UserAuthentication.logout(self.username, self.password)
        self.username = ""
        self.password = ""
        self.login_status = 0
    
    def change_username(self,new_username):
        UserModification.change_username(self.username, self.password, new_username)
        self.username = new_username

    def change_password(self, new_password):
        UserModification.change_password(self.username, self.password, new_password)
        self.password = new_password
    
    def modify_course(self, course_name, modified_features):
        """Modify course specific functionality if the course is taught by the instructor"""
        course_modify = InstructorCourseModify(self.name)
        course_modify.modify_course_features(course_name, modified_features)

    def view_class_rosters(self, course_name):
        """View students enrolled in any course"""
        rosters = InstructorClassRosters(self.name)
        rosters.view_class_roster(course_name)
    
    def view_payroll(self):
        """View the instructor-specific payroll"""
        payroll = ViewInstructorPayroll(self.name)
        payroll.view_payroll()

    def view_building_timings(self, building_name):
        """View building timings for any building"""
        building = ViewBuildingTimings(building_name)
        building.view_timings()

class AdministratorMediator:
    """Administrator specific course functionality"""

    def __init__(self):
        self.name = ""
        self.username = ""
        self.password = ""
        self.login_status = 0
        
    def create_admin(self, name, username, password):
        """Creating a new Admin account"""
        try:
            Administrator(name,username,password)
        except:
            time.sleep(0)
        self.name = name
        self.username = username
        self.password = password
        UserAuthentication.login(username, password)
        self.admin = CourseAdministration(self.username)
        self.admin_payroll = AdministrativePayroll()
        self.admin_building = AdministrativeBuildingTimings()
        self.login_status = 1
    
    def login(self, username, password):
        """Authenticating admin credentials"""
        self.username = username
        self.password = password
        login_result = UserAuthentication.login(username, password)
        if login_result ==True:
            self.login_status = 1
            self.name = UserInformation.get_user_name(username,password)
            if self.name == "User doesn't exist":
                return False
                print("Incorrect Login")
            else:
                self.admin = CourseAdministration(self.username)
                self.admin_payroll = AdministrativePayroll()
                self.admin_building = AdministrativeBuildingTimings()
                return True
        else:
            return "Incorrect Login"

    def change_username(self,new_username):
        UserModification.change_username(self.username, self.password, new_username)
        self.username = new_username

    def change_password(self, new_password):
        UserModification.change_password(self.username, self.password, new_password)
        self.password = new_password

    def add_new_course(self, course_id, course_name, instructor_name, room, restrictions, schedule, section, course_features, registration ):
        """Add a new course to the database"""
        self.admin.add_new_course(course_id, course_name, instructor_name, room, restrictions, schedule, section, course_features, registration )
    
    def delete_course(self, course_name):
        self.admin.delete_course(course_name)

    def close_registration(self, course_name):
        self.admin.close_registration(course_name)
    
    def change_course_schedule(self, course_name, section, new_schedule):
        self.admin.change_course_schedule(course_name, section, new_schedule)

    def add_instructor_payroll(self, instructor_name, payroll):
        """Add payroll information for any instructor"""
        self.admin_payroll.add_instructor_payroll(instructor_name, payroll)

    def update_instructor_payroll(self, instructor_name, new_payroll):
        self.admin_payroll.update_instructor_payroll(instructor_name, new_payroll)

    def delete_instructor_payroll(self, instructor_name):
        self.admin_payroll.delete_instructor_payroll(instructor_name)

    def add_building_timing(self, building, timings):
        """Add building timing information available to all users"""
        self.admin_building.add_building_timing(building, timings)
    
    def update_building_timing(self, building, new_timings):
        self.admin_building.update_building_timing(building, new_timings)

    def delete_building(self, building):
        self.admin_building.delete_building(building)
    
    def logout(self):
        UserAuthentication.logout(self.username, self.password)
        self.username = ""
        self.password = ""
        self.login_status = 0


    
 




    


    

