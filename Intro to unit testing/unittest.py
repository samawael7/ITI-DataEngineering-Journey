# unittest
# Run unittest/pytest
# check all files in the root directory
# run specific files start with test_

# Naming Convention/Rule + Strict Rules to use unittest: 
# Test file must start/begin with test_
# Test Classes must inherit from unittest.
# Test Methods start/begin with test_

import unittest
import main
# The AAA Testing Model
# Arrange: Prepare data and environment (Test Cases + Edge Cases)
# Scenario => Test Cases
# Normal Value
# Zero Values (1st Edge Case)
# Negative Values (2nd Edge Case)
# Large Values (3rd Edge Case)

# Test Case       => Inputs                   => Expected Result
# Case 1          => add(1,2)                 => 3
# Case 2          => add(0,0)                 => 0
# Case 3          => add(1,-5)                => -4
# Case 4          => add(1000000,5000000)     => 6000000


# Test Suit: Group of related test cases
class TestSomething(unittest.TestCase):
    # unittest.TestCase: Base Class provide testing functionality
    def test_add_1(self): # Test Case
        # Act: Execute the original/source function => Actual Result
        actual_result = main.add(1,2) # Arguments => Arranged Data
        expected_result = 3

        # Assert: Verify the result is correct => Actual Result = Expected Result
        self.assertEqual(actual_result, expected_result)
    
    def test_add_2(self): # Test Case
        actual_result = main.add(0,0)
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_divide(self): # Test Case
        actual_result = main.divide(10, 2)
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

# Run unittest Tests
# run one file:
# Terminal: python -m unittest test_main.py

# Run all Test files:
# Terminal: python -m unittest discover


# Status Code:
# . (The dot) => Passed
# F           => Failed

# The Output in case of Passed:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK


# The Output in case of Failure:
# .F
# ======================================================================
# FAIL: test_add_2 (test_main.TestSomething.test_add_2)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "E:\desktop-projects\zagazig-de46r2-testing\test_main.py", line 39, in test_add_2
#     self.assertEqual(actual_result, expected_result)
#     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError: 0 != 4

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (failures=1)