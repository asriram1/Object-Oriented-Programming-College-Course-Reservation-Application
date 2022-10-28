from mediator import *

def student_workflow():
    """Presenting student specific functionality to an authenticated user"""

    student = StudentMediator()
    create = input("Would you like to login or create a new account (Enter login / create)? ")
    #Allow a maximum of 3 login attempts
    count = 3
    if create == "login":
        #If user chooses to login
        while count !=0:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            result = student.login(username, password)
            if result == True:
                print("Logged in successfully!")
                while True:
                    action = input("""What would you like to do next? You can enter any of the following:
                    change_username <new_username>
                    change_password <new_password>
                    add_course <course_id> <course_name> (e.g. try 1122 OOP)
                    drop_course <course_name>
                    view_registered_courses
                    view_all_courses 
                    view_restrictions <course_name> (e.g. try OOP)
                    view_course_schedule <course_name> (e.g. try OOP)
                    view_room_assignment <course_name> (e.g. try Networks)
                    view_building_timings <building_name> (e.g. try JCL)
                    logout
                    """)
                    user_action = action.split(" ")[0]
                    if user_action == 'change_username':
                        argument = action.split(" ")[1]
                        student.change_username(argument)
                        print("Username changed successfully!")
                    elif user_action == 'change_password':
                        argument = action.split(" ")[1]
                        student.change_password(argument)
                        print("Password changed successfully!")
                    elif user_action == 'add_course':
                        course_id = action.split(" ")[1]
                        course_name = action.split(" ")[2]
                        student.add_course(course_id, course_name)
                        print("Added course successfully!")
                    elif user_action == 'drop_course':
                        course_name = action.split(" ")[1]
                        student.drop_course(course_name)
                        print("Dropped course successfully!")
                    elif user_action == 'view_registered_courses':
                        student.view_registered_courses()
                    elif user_action == 'view_all_courses':
                        student.view_all_courses()
                    elif user_action == 'view_restrictions':
                        course_name = action.split(" ")[1]
                        student.view_restrictions(course_name)
                    elif user_action == 'view_course_schedule':
                        course_name = action.split(" ")[1]
                        student.view_course_schedule(course_name)
                    elif user_action == 'view_room_assignment':
                        course_name = action.split(" ")[1]
                        student.view_room_assignment(course_name)
                    elif user_action == 'view_building_timings':
                        building_name = action.split(" ")[1]
                        student.view_building_timings(building_name)
                    elif user_action == 'logout':
                        student.logout()
                        print("Logged out successfully!")
                        return
                    else:
                        print("Enter a valid command")
            else:
                count -=1
                print("Incorrect login")
                print("You have",count,"login attempts left")
    elif create == "create":
        #If user chooses to create new account
        name = input("Enter your first name: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        student.create_student(name, username, password)
        print("Created student account successfully!")
        while True:
            action = input("""What would you like to do next? You can enter any of the following:
            change_username <new_username>
            change_password <new_password>
            add_course <course_id> <course_name> (e.g. try 1122 OOP)
            drop_course <course_name>
            view_registered_courses
            view_all_courses 
            view_restrictions <course_name> (e.g. try OOP)
            view_course_schedule <course_name> (e.g. try OOP)
            view_room_assignment <course_name> (e.g. try Networks)
            view_building_timings <building_name> (e.g. try JCL)
            logout
            """)
            user_action = action.split(" ")[0]
            if user_action == 'change_username':
                argument = action.split(" ")[1]
                student.change_username(argument)
                print("Username changed successfully!")
            elif user_action == 'change_password':
                argument = action.split(" ")[1]
                student.change_password(argument)
                print("Password changed successfully!")
            elif user_action == 'add_course':
                course_id = action.split(" ")[1]
                course_name = action.split(" ")[2]
                student.add_course(course_id, course_name)
                print("Added course successfully!")
            elif user_action == 'drop_course':
                course_name = action.split(" ")[1]
                student.drop_course(course_name)
                print("Dropped course successfully!")
            elif user_action == 'view_registered_courses':
                student.view_registered_courses()
            elif user_action == 'view_all_courses':
                student.view_all_courses()
            elif user_action == 'view_restrictions':
                course_name = action.split(" ")[1]
                student.view_restrictions(course_name)
            elif user_action == 'view_course_schedule':
                course_name = action.split(" ")[1]
                student.view_course_schedule(course_name)
            elif user_action == 'view_room_assignment':
                course_name = action.split(" ")[1]
                student.view_room_assignment(course_name)
            elif user_action == 'view_building_timings':
                building_name = action.split(" ")[1]
                student.view_building_timings(building_name)
            elif user_action == 'logout':
                student.logout()
                print("Logged out successfully!")
                return
            else:
                print("Enter a valid command")
            

def instructor_workflow():
    """Presenting instructor specific functionality to an authenticated user"""
    instructor = InstructorMediator()
    create = input("Would you like to login or create a new account (Enter login / create)? ")
    #Allow maximum of 3 login attempts
    count = 3
    if create == "login":
        #If user chooses to login
        while count !=0:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            result = instructor.login(username, password)
            if result == True:
                print("Logged in successfully!")
                while True:
                    action = input("""What would you like to do next? You can enter any of the following:
                    change_username <new_username>
                    change_password <new_password>
                    modify_course <course_name> <modified_features> (e.g. try OOP No_Pass/Fail)(Important: Keep all arguments to one word each)
                    view_class_rosters <course_name>
                    view_payroll
                    view_building_timings <building_name> (e.g. try JCL)
                    logout
                    """)
                    user_action = action.split(" ")[0]
                    if user_action == 'change_username':
                        argument = action.split(" ")[1]
                        instructor.change_username(argument)
                        print("Username changed successfully!")
                    elif user_action == 'change_password':
                        argument = action.split(" ")[1]
                        instructor.change_password(argument)
                        print("Password changed successfully!")
                    elif user_action == 'modify_course':
                        course_name = action.split(" ")[1]
                        features = action.split(" ")[2]
                        instructor.modify_course(course_name, features)
                        print("Modified course successfully!")
                    elif user_action == 'view_class_rosters':
                        course_name = action.split(" ")[1]
                        instructor.view_class_rosters(course_name)
                    elif user_action == 'view_payroll':
                        instructor.view_payroll()
                    elif user_action == 'view_building_timings':
                        building_name = action.split(" ")[1]
                        instructor.view_building_timings(building_name)
                    elif user_action == 'logout':
                        instructor.logout()
                        print("Logged out successfully!")
                        return
                    else:
                        print("Enter a valid command")
            else:
                count -=1
                print("Incorrect login")
                print("You have",count,"login attempts left")
    elif create == "create":
        #If user chooses to create new account
        name = input("Enter your first name: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        instructor.create_instructor(name, username, password)
        print("Created instructor account successfully!")
        while True:
            action = input("""What would you like to do next? You can enter any of the following:
            change_username <new_username>
            change_password <new_password>
            modify_course <course_name> <modified_features> (e.g. try OOP No_Pass/Fail)(Important: Keep all arguments to one word each)
            view_class_rosters <course_name>
            view_payroll
            view_building_timings <building_name> (e.g. try JCL)
            logout
            """)
            user_action = action.split(" ")[0]
            if user_action == 'change_username':
                argument = action.split(" ")[1]
                instructor.change_username(argument)
                print("Username changed successfully!")
            elif user_action == 'change_password':
                argument = action.split(" ")[1]
                instructor.change_password(argument)
                print("Password changed successfully!")
            elif user_action == 'modify_course':
                course_name = action.split(" ")[1]
                features = action.split(" ")[2]
                instructor.modify_course(course_name, features)
                print("Modified course successfully!")
            elif user_action == 'view_class_rosters':
                course_name = action.split(" ")[1]
                instructor.view_class_rosters(course_name)
            elif user_action == 'view_payroll':
                instructor.view_payroll()
            elif user_action == 'view_building_timings':
                building_name = action.split(" ")[1]
                instructor.view_building_timings(building_name)
            elif user_action == 'logout':
                instructor.logout()
                print("Logged out successfully!")
                return
            else:
                print("Enter a valid command")
            

def admin_workflow():
    """Presenting administrator specific functionality to an authenticated user"""
    admin = AdministratorMediator()
    create = input("Would you like to login or create a new account (Enter login / create)? ")
    #Allow a maximum of 3 login attempts
    count = 3
    if create == "login":
        #If the user chooses to login
        while count !=0:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            result = admin.login(username, password)
            if result == True:
                print("Logged in successfully!")
                while True:
                    action = input("""What would you like to do next? You can enter any of the following:
                    change_username <new_username>
                    change_password <new_password>
                    add_new_course <course_id> <course_name> <instructor_name> <room> <restrictions> <schedule> <section> <course_features> <registration>
                    (Important: Keep each field to one word or use underscores. Registration can be Open or Closed)  
                    (E.g add_new_course 10000 Security Shelley JCL_200 None T_5:30-7:30 A1 Instructor_Approval Open)
                    delete_course <course_name>
                    close_registration <course_name>
                    change_course_schedule <course_name> <section> <new_schedule>
                    add_instructor_payroll <instructor_name> <payroll> (e.g. try Mark 20)
                    update_instructor_payroll <instructor_name> <updated payroll> (e.g. try OOP)
                    delete_instructor_payroll <instructor_name> (e.g. try Networks)
                    add_building_timing <building> <timings>
                    update_building_timing <building> <new_timings>
                    delete_building <building_name> (e.g. try JCL)
                    logout
                    """)
                    user_action = action.split(" ")[0]
                    if user_action == 'change_username':
                        argument = action.split(" ")[1]
                        admin.change_username(argument)
                        print("Username changed successfully!")
                    elif user_action == 'change_password':
                        argument = action.split(" ")[1]
                        admin.change_password(argument)
                        print("Password changed successfully!")
                    elif user_action == 'add_new_course':
                        course_id = action.split(" ")[1]
                        course_name = action.split(" ")[2]
                        instructor_name = action.split(" ")[3]
                        room = action.split(" ")[4]
                        restrictions = action.split(" ")[5]
                        schedule = action.split(" ")[6]
                        section = action.split(" ")[7]
                        course_features = action.split(" ")[8]
                        registration = action.split(" ")[9]
                        admin.add_new_course(course_id,course_name,instructor_name,room,restrictions,schedule,section,course_features,registration)
                        print("Added new course successfully!")
                    elif user_action == 'delete_course':
                        course_name = action.split(" ")[1]
                        admin.delete_course(course_name)
                        print("Deleted course successfully!")
                    elif user_action == 'close_registration':
                        course_name = action.split(" ")[1]
                        admin.close_registration(course_name)
                        print("Course registration closed successfully!")
                    elif user_action == 'change_course_schedule':
                        course_name = action.split(" ")[1]
                        section = action.split(" ")[2]
                        new_schedule = action.split(" ")[3]
                        admin.change_course_schedule(course_name, section, new_schedule)
                        print("Course schedule changed successfully!")
                    elif user_action == 'add_instructor_payroll':
                        instructor_name = action.split(" ")[1]
                        payroll = action.split(" ")[2]
                        admin.add_instructor_payroll(instructor_name,payroll)
                    elif user_action == 'update_instructor_payroll':
                        instructor_name = action.split(" ")[1]
                        new_payroll = action.split(" ")[2]
                        admin.update_instructor_payroll(instructor_name,new_payroll)
                    elif user_action == 'delete_instructor_payroll':
                        instructor_name = action.split(" ")[1]
                        admin.delete_instructor_payroll(instructor_name)
                    elif user_action == 'add_building_timing':
                        building_name = action.split(" ")[1]
                        timings = action.split(" ")[2]
                        admin.add_building_timing(building_name, timings)
                    elif user_action == 'update_building_timing':
                        building_name = action.split(" ")[1]
                        new_timings = action.split(" ")[2]
                        admin.update_building_timing(building_name, new_timings)
                    elif user_action == 'delete_building':
                        building_name = action.split(" ")[1]
                        admin.delete_building(building_name)
                    elif user_action == 'logout':
                        admin.logout()
                        print("Logged out successfully!")
                        return
                    else:
                        print("Enter a valid command")
            else:
                count -=1
                print("Incorrect login")
                print("You have",count,"login attempts left")

    elif create == "create":
        #If the user chooses to create a new account
        name = input("Enter your first name: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        admin.create_admin(name, username, password)
        print("Created student account successfully!")
        while True:
            action = input("""What would you like to do next? You can enter any of the following:
            change_username <new_username>
            change_password <new_password>
            add_new_course <course_id> <course_name> <instructor_name> <room> <restrictions> <schedule> <section> <course_features> <registration>
            (Important: Keep each field to one word or use underscores. Registration can be Open or Closed)  
            (E.g add_new_course 10000 Security Shelley JCL_200 None T_5:30-7:30 A1 Instructor_Approval Open)
            delete_course <course_name>
            close_registration <course_name>
            change_course_schedule <course_name> <section> <new_schedule>
            add_instructor_payroll <instructor_name> <payroll> (e.g. try Mark 20)
            update_instructor_payroll <instructor_name> <updated payroll> (e.g. try OOP)
            delete_instructor_payroll <instructor_name> (e.g. try Networks)
            add_building_timing <building> <timings>
            update_building_timing <building> <new_timings>
            delete_building <building_name> (e.g. try JCL)
            logout
            """)
            user_action = action.split(" ")[0]
            if user_action == 'change_username':
                argument = action.split(" ")[1]
                admin.change_username(argument)
                print("Username changed successfully!")
            elif user_action == 'change_password':
                argument = action.split(" ")[1]
                admin.change_password(argument)
                print("Password changed successfully!")
            elif user_action == 'add_new_course':
                course_id = action.split(" ")[1]
                course_name = action.split(" ")[2]
                instructor_name = action.split(" ")[3]
                room = action.split(" ")[4]
                restrictions = action.split(" ")[5]
                schedule = action.split(" ")[6]
                section = action.split(" ")[7]
                course_features = action.split(" ")[8]
                registration = action.split(" ")[9]
                admin.add_new_course(course_id,course_name,instructor_name,room,restrictions,schedule,section,course_features,registration)
                print("Added new course successfully!")
            elif user_action == 'delete_course':
                course_name = action.split(" ")[1]
                admin.delete_course(course_name)
                print("Deleted course successfully!")
            elif user_action == 'close_registration':
                course_name = action.split(" ")[1]
                admin.close_registration(course_name)
                print("Course registration closed successfully!")
            elif user_action == 'change_course_schedule':
                course_name = action.split(" ")[1]
                section = action.split(" ")[2]
                new_schedule = action.split(" ")[3]
                admin.change_course_schedule(course_name, section, new_schedule)
                print("Course schedule changed successfully!")
            elif user_action == 'add_instructor_payroll':
                instructor_name = action.split(" ")[1]
                payroll = action.split(" ")[2]
                admin.add_instructor_payroll(instructor_name,payroll)
            elif user_action == 'update_instructor_payroll':
                instructor_name = action.split(" ")[1]
                new_payroll = action.split(" ")[2]
                admin.update_instructor_payroll(instructor_name,new_payroll)
            elif user_action == 'delete_instructor_payroll':
                instructor_name = action.split(" ")[1]
                admin.delete_instructor_payroll(instructor_name)
            elif user_action == 'add_building_timing':
                building_name = action.split(" ")[1]
                timings = action.split(" ")[2]
                admin.add_building_timing(building_name, timings)
            elif user_action == 'update_building_timing':
                building_name = action.split(" ")[1]
                new_timings = action.split(" ")[2]
                admin.update_building_timing(building_name, new_timings)
            elif user_action == 'delete_building':
                building_name = action.split(" ")[1]
                admin.delete_building(building_name)
            elif user_action == 'logout':
                admin.logout()
                print("Logged out successfully!")
                return
            else:
                print("Enter a valid command")

def main():
    """CLI for Course Registration Application"""

    #Keep looping until user quits
    while True:
        x = input("Are you a student/instructor/administrator (reply with S/I/A)? ")
        if x == "S":
            student_workflow()
        elif x == "I":
            instructor_workflow()
        elif x == "A":
            admin_workflow()
                

if __name__ == '__main__':
    main()

