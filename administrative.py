import pymongo
from pymongo import MongoClient
from abc import ABC, abstractmethod 



class Administrative(ABC):
    """Generic class to add/update/delete any information linked to key, value pairs"""
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://dbUser:pass@cluster0.uylgr.mongodb.net/administrative?retryWrites=true&w=majority")
        self.db = self.cluster['administrative']
        self.key = "general_key"
        self.value = "general_value"
        self.collection = self.db[self.value]
    def add(self, key, value):
        """Adding data to MongoDB"""
        self.post = {self.key: key, self.value: value}
        self.collection.insert_one(self.post)

    def update(self, key, new_value):
        """Modifying values for specific keys"""
        self.collection.update_one({self.key: key}, {"$set":{self.value:new_value}})

    def delete(self, key):
        """Deleting specific documents from DB"""
        self.collection.delete_one({self.key: key})

class AdministrativePayroll(Administrative):
    """Administrator payroll functionality inherited from administrative class"""
    def __init__(self):
        """Inherit cluser and db information from parent class"""
        super().__init__()
        self.key = "instructor_name"
        self.value = "payroll"
        self.collection = self.db['payroll']

    def add_instructor_payroll(self, instructor_name, payroll):
        """Adding an instructor's payroll information"""
        super().add(instructor_name, payroll)

    def update_instructor_payroll(self, instructor_name, new_payroll):
        """Modifying an instructor's payroll information"""
        super().update(instructor_name, new_payroll)

    def delete_instructor_payroll(self, instructor_name):
        """Deleting an instructor's payroll information"""
        super().delete(instructor_name)

class AdministrativeBuildingTimings(Administrative):
    """Administrator building timing functionality inherited from administrative class"""
    def __init__(self):
        """Inherit cluser and db information from parent class"""
        super().__init__()
        self.key = "building_name"
        self.value = "timings"
        self.collection = self.db['building']
    
    def add_building_timing(self, building, timings):
        """Adding a building's timing information"""
        super().add(building, timings)

        
    def update_building_timing(self, building, new_timings):
        """Modifying a building's timing information"""
        super().update(building, new_timings)


    def delete_building(self, building):
        """Deleting a building's timing information"""
        super().delete(building)



class View(ABC):
    """For viewing of data related to payrolls & building timing"""
    def __init__(self, general_name):
        """Initialize cluster and databased on MongoDB"""
        self.cluster = MongoClient("mongodb+srv://dbUser:pass@cluster0.uylgr.mongodb.net/administrative?retryWrites=true&w=majority")
        self.db = self.cluster['administrative']
        self.key = "general_key"
        self.value = "general_value"
        self.collection = self.db[self.value]
        self.key_name = general_name
    def view(self):
        """View data for specific collections"""
        results = self.collection.find({self.key: self.key_name})
        for result in results:
            print(self.value +": ", result[self.value])

class ViewInstructorPayroll(View):
    """Viewing payroll data for instructors"""
    def __init__(self, instructor_name):
        """Initialize variables to view data specific to instructor"""
        super().__init__(instructor_name)
        self.key = "instructor_name"
        self.value = "payroll"
        self.collection = self.db['payroll']
        self.key_name = instructor_name
    def view_payroll(self):
        """View data for payroll collection"""
        super().view()

class ViewBuildingTimings(View):
    """Viewing building timing data for instructors & students"""
    def __init__(self, building_name):
        """Initialize variables to view data specific to building"""
        super().__init__(building_name)
        self.key = "building_name"
        self.value = "timings"
        self.collection = self.db['building']
        self.key_name = building_name
    def view_timings(self):
        """View data for building collection"""
        super().view()