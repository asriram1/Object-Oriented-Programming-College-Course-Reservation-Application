import unittest
from administrative import *
import random

class Testing(unittest.TestCase):

    def test_instructor_payroll_add(self):
        """Test if payroll information is added to MongoDB"""
        self.cluster = MongoClient("mongodb+srv://dbUser:pass@cluster0.uylgr.mongodb.net/administrative?retryWrites=true&w=majority")
        self.db = self.cluster['administrative']
        self.collection = self.db['payroll']
        self.payroll = AdministrativePayroll()
        self.instructor_name = "random" + str(random.randint(1,1000000))
        self.amount = random.randint(1,1000000)
        self.payroll.add_instructor_payroll(self.instructor_name,self.amount )
        results = self.collection.find({"instructor_name": self.instructor_name})
        for result in results:
            self.answer = result['payroll']
        self.collection.delete_one({"instructor_name": self.instructor_name})
        self.assertEqual(self.amount,self.answer)

    def test_update_instructor_payroll(self):
        """Test if payroll information is updated on MongoDB"""
        self.cluster = MongoClient("mongodb+srv://dbUser:pass@cluster0.uylgr.mongodb.net/administrative?retryWrites=true&w=majority")
        self.db = self.cluster['administrative']
        self.collection = self.db['payroll']
        self.payroll = AdministrativePayroll()
        self.instructor_name = "random" + str(random.randint(1,1000000))
        self.amount = random.randint(1,1000000)
        self.payroll.add_instructor_payroll(self.instructor_name,self.amount )
        self.new_amount = random.randint(1,1000000)
        self.payroll.update_instructor_payroll(self.instructor_name,self.new_amount)
        results = self.collection.find({"instructor_name": self.instructor_name})
        for result in results:
            self.answer = result['payroll']

        self.collection.delete_one({"instructor_name": self.instructor_name})
        self.assertEqual(self.new_amount,self.answer)

    def test_delete_instructor_payroll(self):
        """Test if payroll information is deleted from MongoDB"""
        self.cluster = MongoClient("mongodb+srv://dbUser:pass@cluster0.uylgr.mongodb.net/administrative?retryWrites=true&w=majority")
        self.db = self.cluster['administrative']
        self.collection = self.db['payroll']
        self.payroll = AdministrativePayroll()
        self.instructor_name = "random" + str(random.randint(1,1000000))
        self.amount = random.randint(1,1000000)
        self.payroll.add_instructor_payroll(self.instructor_name,self.amount )
        self.new_amount = random.randint(1,1000000)
        self.payroll.delete_instructor_payroll(self.instructor_name)
        results = self.collection.find({"instructor_name": self.instructor_name})
        self.count = 0
        for result in results:
            self.count +=1
        self.assertEqual(self.count,0)


    def test_building_timing_add(self):
        """Test if building information is added to MongoDB"""
        self.cluster = MongoClient("mongodb+srv://dbUser:pass@cluster0.uylgr.mongodb.net/administrative?retryWrites=true&w=majority")
        self.db = self.cluster['administrative']
        self.collection = self.db['building']
        self.building = AdministrativeBuildingTimings()
        self.building_name = "random" + str(random.randint(1,1000000))
        self.timings = random.randint(1,1000000)
        self.building.add_building_timing(self.building_name,self.timings )
        results = self.collection.find({"building_name": self.building_name})
        for result in results:
            self.answer = result['timings']
        self.collection.delete_one({"building_name": self.building_name})
        self.assertEqual(self.timings,self.answer)

    def test_update_building_timing(self):
        """Test if building information is updated on MongoDB"""
        self.cluster = MongoClient("mongodb+srv://dbUser:pass@cluster0.uylgr.mongodb.net/administrative?retryWrites=true&w=majority")
        self.db = self.cluster['administrative']
        self.collection = self.db['building']
        self.building = AdministrativeBuildingTimings()
        self.building_name = "random" + str(random.randint(1,1000000))
        self.timings = random.randint(1,1000000)
        self.building.add_building_timing(self.building_name,self.timings )
        self.new_timings = random.randint(1,1000000)
        self.building.update_building_timing(self.building_name,self.new_timings)
        results = self.collection.find({"building_name": self.building_name})
        for result in results:
            self.answer = result['timings']
        self.collection.delete_one({"building_name": self.building_name})
        self.assertEqual(self.new_timings,self.answer)
  
    def test_delete_building(self):
        """Test if building information is deleted from MongoDB"""
        self.cluster = MongoClient("mongodb+srv://dbUser:pass@cluster0.uylgr.mongodb.net/administrative?retryWrites=true&w=majority")
        self.db = self.cluster['administrative']
        self.collection = self.db['building']
        self.building = AdministrativeBuildingTimings()
        self.building_name = "random" + str(random.randint(1,1000000))
        self.timings = random.randint(1,1000000)
        self.building.add_building_timing(self.building_name,self.timings )
        self.building.delete_building(self.building_name)
        results = self.collection.find({"building_name": self.building_name})
        self.count = 0
        for result in results:
            self.count +=1
        self.assertEqual(self.count,0)

    

if __name__ == '__main__':
    unittest.main()


