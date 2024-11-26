# Public repository created for interview
# How to run this program
There are three test files - testPet.py, testStore.py, testUser.py.
Each of these files can be run separately as 'python filename.py' to test separately.
Also, the main regression file 'regFile.py' can be executed as 'python regFile.py' to run all the tests.

SAMPLE TEST RESULTS:
NOTE: testInvalidUserLogin is failing because of a bug in the swagger 
/robertcbatest$ python3 regFile.py 
TestPetDetails:2024-11-26 16:45:11,361:INFO-Pet creation successful
.TestPetDetails:2024-11-26 16:45:12,955:INFO-Pet details fetch successful
.TestPetDetails:2024-11-26 16:45:13,879:INFO-Pet fetch with wrong ID test Successful
.TestPetDetails:2024-11-26 16:45:14,790:INFO-Pet deletion successful
.TestStoreDetails:2024-11-26 16:45:15,701:INFO-Store order creation successful
.TestStoreDetails:2024-11-26 16:45:16,612:INFO-Get store order successful
.TestStoreDetails:2024-11-26 16:45:17,525:INFO-Get store inventory successful
.TestStoreDetails:2024-11-26 16:45:18,435:INFO-Store order deletion successful
.TestUserDetails:2024-11-26 16:45:19,349:INFO-User creation successful
.TestUserDetails:2024-11-26 16:45:20,260:INFO-Get user details successful
.TestUserDetails:2024-11-26 16:45:22,084:INFO-Update user details successful
.TestUserDetails:2024-11-26 16:45:22,996:INFO-user login successful
.TestUserDetails:2024-11-26 16:45:23,906:INFO-user logout successful
.TestUserDetails:2024-11-26 16:45:24,816:ERROR-Invalid user login worked
FTestUserDetails:2024-11-26 16:45:25,725:INFO-User deletion successful
.TestUserDetails:2024-11-26 16:45:26,635:INFO-Invalid username error
.
======================================================================
FAIL: test_testInvalidUserLogin (__main__.TestPet)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "regFile.py", line 52, in test_testInvalidUserLogin
    self.assertEqual(self.userInstance.testInvalidUserLogin(), True)
AssertionError: False != True

----------------------------------------------------------------------
Ran 16 tests in 16.856s

FAILED (failures=1)

