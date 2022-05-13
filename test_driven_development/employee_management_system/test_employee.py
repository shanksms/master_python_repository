import unittest

from test_driven_development.employee_management_system.employee import Employee

NAME: str = 'Shashank'
EMPLOYEE_ID: int = 12345

class TestEmployeeComputePayout(unittest.TestCase):
    def setUp(self) -> None:
        """set up test fixtures"""
        self.shashank = Employee(name=NAME, employee_id=EMPLOYEE_ID)

    def test_employee_payout_returns_a_float(self):
        self.assertIsInstance(self.shashank.compute_payout(), float)
