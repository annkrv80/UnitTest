import unittest
from vehicle import Vehicle, Car, Motorcycle

class TestVehicle(unittest.TestCase):  
    def setUp(self):
        self.vehicle_1 = Car('Nissan', 'Super', 2019)
        self.vehicle_2 = Motorcycle('Honda', 'XXL', 2015)

        #vehicle_1.testDrive()
        #vehicle_2.testDrive()
        #vehicle_1.park()
        #vehicle_2.park()

    def test_car_instance_is_vehicle_instance(self):   
        self.assertIsInstance(self.vehicle_1, Vehicle, 'Не наследуется от Vehicle')

    def test_motorcycle_instance_is_vehicle_instance(self):   
        self.assertIsInstance(self.vehicle_2, Vehicle, 'Не наследуется от Vehicle')
    
    def test_car_has_4_wheels(self):
        self.assertEqual(self.vehicle_1.numWheel, 4, 'Должно быть 4 колеса')

    def test_motorcycle_has_2_wheels(self):
        self.assertEqual(self.vehicle_2.numWheel, 2, 'Должно быть 2 колеса')

    def test_car_test_drive_speed(self):  
        self.vehicle_1.testDrive()  
        self.assertEqual(self.vehicle_1.speed, 60, 'Скорость должна быть равна 60')

    def test_motorcycle_test_drive_speed(self):
        self.vehicle_2.testDrive()
        self.assertEqual(self.vehicle_2.speed, 75, 'Скорость должна быть равна 75')

    def test_car_park_stops(self):
        self.vehicle_1.testDrive()
        self.vehicle_1.park()
        self.assertEqual(self.vehicle_1.speed, 0, 'Машина не остановилась')

    def test_motorcycle_park_stops(self):
        self.vehicle_2.testDrive()
        self.vehicle_2.park()
        self.assertEqual(self.vehicle_2.speed, 0, 'Мотоцикл не остановился')
        

if __name__ == '__main__':
    unittest.main()
    