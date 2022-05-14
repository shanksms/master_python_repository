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

    def test_employee_payout_no_commission_no_hours(self):
        self.assertAlmostEqual(self.shashank.compute_payout(), 1000.00)

    def test_employee_payout_no_commission(self):
        self.shashank.hours_worked = 10.0
        self.assertAlmostEqual(self.shashank.compute_payout(), 2000.00)

    def test_employee_payout_with_commission(self):
        self.shashank.hours_worked = 10.0
        self.shashank.contracts_landed = 10
        self.assertAlmostEqual(self.shashank.compute_payout(), 3000.00)

    def test_employee_payout_with_commission_disabled(self):
        self.shashank.hours_worked = 10.0
        self.shashank.contracts_landed = 10
        self.shashank.has_commission = False
        self.assertAlmostEqual(self.shashank.compute_payout(), 2000.00)


if __name__ == '__main__':
    unittest.main()