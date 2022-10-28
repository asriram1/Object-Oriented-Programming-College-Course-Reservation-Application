from abc import ABC, abstractmethod 
import sqlite3
from sqlite3 import Error
import random
import os


global_conn = None

class Database:
    """User Database storing all user related credentials"""
    def __init__(self, db_folder, db_file):
        """Initialize DB"""
        self._db_folder = db_folder
        self._db_file = db_file
        self._conn = None
        self._base_dir = os.path.dirname(os.path.abspath(__file__))
        self._path = os.path.join(self._base_dir, self._db_folder , self._db_file)
        
    def create_connection(self):
        """Connect to DB"""
        global global_conn
        conn = None
        
        if not os.path.exists(self._path):
            try:
                global_conn = sqlite3.connect(self._db_file)
                self.create_table(global_conn)
            except Error as e:
                print(e)
        else:
            global_conn = sqlite3.connect(self._path)

    def create_table(self,conn):
        """Create Users Table in DB if not already exists"""
        create_table_sql = """ CREATE TABLE IF NOT EXISTS users(
                                            id integer PRIMARY KEY,
                                            role text NOT NULL,
                                            name text NOT NULL,
                                            username text NOT NULL UNIQUE, 
                                            password text NOT NULL UNIQUE,
                                            login_status integer NOT NULL
                                        );
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)


class User(ABC):
    """Interface class for all users - including students, instructors & administrators"""
    def __init__(self, name, username, password):
        """Adding a new user to the User Database"""
        global global_conn
        db = Database('Database','Users.db')
        db.create_connection()
        self._role = "User"
        self._id = random.randint(0,10000000)
        self._name = name
        self._username = username
        self._password = password
        self._login_status = 0
        self.sql = """
            INSERT INTO Users(id, role, name, username, password, login_status)
            VALUES(?,?,?,?,?,?);
        """
        data_tuple = (self._id, self._role, self._name, self._username, self._password, self._login_status)
        cur = global_conn.cursor()
        cur.execute(self.sql, data_tuple)
        global_conn.commit()


class Student(User):
    """Student account class inherited from User base class"""
    def __init__(self, name, username, password):
        """Adding a new student to the User Database"""
        global global_conn
        db = Database('Database','Users.db')
        db.create_connection()
        self._role = "Student"
        self._id = random.randint(0,10000000)
        self._name = name
        self._username = username
        self._password = password
        self._login_status = 0
        self.sql = """
            INSERT INTO Users(id, role, name, username, password, login_status)
            VALUES(?,?,?,?,?,?);
        """
        data_tuple = (self._id, self._role, self._name, self._username, self._password, self._login_status)
        cur = global_conn.cursor()
        cur.execute(self.sql, data_tuple)
        global_conn.commit()
    

class Instructor(User):
    """Instructor account class inherited from User base class"""
    def __init__(self, name, username, password):
        """Adding a new instructor to the User Database"""
        global global_conn
        db = Database('Database','Users.db')
        db.create_connection()
        self._role = "Instructor"
        self._id = random.randint(0,10000000)
        self._name = name
        self._username = username
        self._password = password
        self._login_status = 0
        self.sql = """
            INSERT INTO Users(id, role, name, username, password, login_status)
            VALUES(?,?,?,?,?,?);
        """
        data_tuple = (self._id, self._role, self._name, self._username, self._password, self._login_status)
        cur = global_conn.cursor()
        cur.execute(self.sql, data_tuple)
        global_conn.commit()


class Administrator(User):
    """Administrator account class inherited from User base class"""
    def __init__(self, name, username, password):
        """Adding a new admin to the User Database"""
        global global_conn
        db = Database('Database','Users.db')
        db.create_connection()
        self._role = "Administrator"
        self._id = random.randint(0,10000000)
        self._name = name
        self._username = username
        self._password = password
        self._login_status = 0
        self.sql = """
            INSERT INTO Users(id, role, name, username, password, login_status)
            VALUES(?,?,?,?,?,?);
        """
        data_tuple = (self._id, self._role, self._name, self._username, self._password, self._login_status)
        cur = global_conn.cursor()
        cur.execute(self.sql, data_tuple)
        global_conn.commit()

class UserAuthentication:
    """Enable all users to login and logout"""
    def login(username, password):
        """Authenticate User Login"""
        db = Database('Database','Users.db')
        db.create_connection()
        global global_conn
        try:
            sql = """
                    UPDATE Users
                    SET login_status = 1
                    WHERE username = ? AND
                        password = ?
            """

            data_tuple = (username, password)
            cur = global_conn.cursor()
            cur.execute(sql, data_tuple)
            global_conn.commit()
            return True
        except:
            return "User doesn't exist"
    def logout(username, password):
        """Logout given user"""
        try:
            db = Database('Database','Users.db')
            db.create_connection()
            global global_conn
            sql = """
                    UPDATE Users
                    SET login_status = 0
                    WHERE username = ? AND
                        password = ?
            """

            data_tuple = (username, password)
            cur = global_conn.cursor()
            cur.execute(sql, data_tuple)
            global_conn.commit()
            return True
        except:
            return "User doesn't exist"


class UserModification:

    def change_username(old_username, password, new_username):
        """Allow a user to change their username after verifying credentials"""
        db = Database('Database','Users.db')
        db.create_connection()
        global global_conn
        try:
            sql = """
                UPDATE Users
                SET username = ?
                WHERE username = ? AND password = ?;
            """
            data_tuple = (new_username, old_username, password)
            cur = global_conn.cursor()
            cur.execute(sql, data_tuple)
            global_conn.commit()
            return True
        except:
            return "User doesn't exist"

    def change_password(username, old_password, new_password):
        """Allow a user to change their passwrod after verifying credentials"""
        db = Database('Database','Users.db')
        db.create_connection()
        global global_conn
        try:
            sql = """
                UPDATE Users
                SET password = ?
                WHERE username = ? AND password = ?;
            """
            data_tuple = (new_password, username, old_password)
            cur = global_conn.cursor()
            cur.execute(sql, data_tuple)
            global_conn.commit()
            return True
        except:
            return "User doesn't exist"


class UserDeletion:

    def delete_user(username, password):
        """Allow an admin to delete a user after verifying credentials"""
        db = Database('Database','Users.db')
        db.create_connection()
        global global_conn
        try:
            sql = """
                DELETE FROM Users
                WHERE username = ? AND password = ?;
            """
            data_tuple = (username, password)
            cur = global_conn.cursor()
            cur.execute(sql, data_tuple)
            global_conn.commit()
            return True
        except:
            return "User doesn't exist"


class UserInformation:

    def get_user_name(username, password):
        """Get a user's name using login credentials"""
        db = Database('Database','Users.db')
        db.create_connection()
        global global_conn
        try:
            sql = """
                SELECT name FROM Users
                WHERE username = ? AND password = ?;
            """
            data_tuple = (username, password)
            cur = global_conn.cursor()
            cur.execute(sql, data_tuple)
            rows = cur.fetchall()
            return rows[0][0]
        except:
            return "User doesn't exist"
    

