How to run the application:

- You can utilize the CLI.py file to navigate all the course registration functionality through the command line.
In order to run the file use the 'python CLI.py' command.

Setting up the MySQL Database:

- I have configured MySQL on the bounded context involving the courses & registrations. You can set up MySQL locally using the username - 'root', password - 'root', & create a 
database called 'courses'. Everything else should set up automatically when the code is run.

Other Databases:

- I am using SQLite as my DBMS for the users bounded context, and the db itself can be found in the Database directory. 
- For the administration bounded context I have utilized MongoDB's Atlas.

Navigating the application:

- You can navigate the application as either a student, instructor or administrator
- Running the application as administrator first might help with adding courses, payroll, building information etc. which plays into the functionality used by students
& instructors
- In order for the commands to work, you might need to make sure that each argument is just one word (using underscores etc.). As an example if you have add_new_course <course_id> <course_name> <instructor_name> <room> <restrictions> <schedule> <section> <course_features> <registration> 
You could pass something like:
add_new_course 10000 Security Shelley JCL_200 None T_5:30-7:30 A1 Instructor_Approval Open
- For the view_payroll and view_building_timings functionality, I have also already set up some objects on the MongoDB cluster, so you could query JCL or Regenstein as building names for example

Testing:

- Tests are available for each of the bounded contexts, which can be run using the python <bounded_context_name>_testing.py command.

Other information

- Students can only add courses if they are 'Open' for registration
- Users have three attempts to login
- Instructors can only view their payroll information (connected to their name) and not any other instructor's
- Instructors can only modify course features for courses they teach
- New accounts can only be created if unique passwords and usernames are chosen




