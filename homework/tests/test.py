import unittest
from employee import Employee
from unittest.mock import patch


class MockResponseTrue:
    status_code = 200
    elapsed = 100
    text = "response.ok = True"
    ok = True

    def __init__(self, *args, **kwargs):
        pass


class MockResponseFalse:
    status_code = 404
    elapsed = 100
    text = "response.ok = False"
    ok = False

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emplTest = Employee('Jon', 'Sina', 120)

    def test_first(self):
        self.assertEqual(self.emplTest.first, 'Jon')

    def test_last(self):
        self.assertEqual(self.emplTest.last, 'Sina')

    def test_pay(self):
        self.assertEqual(self.emplTest.pay, 120)

    def test_fullname(self):
        self.assertEqual(self.emplTest.fullname, 'Jon Sina')

    def test_email(self):
        self.assertEqual(self.emplTest.email, 'Jon.Sina@email.com')

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mocker):
        mocker.side_effect = MockResponseTrue
        self.assertEqual(self.emplTest.monthly_schedule('september'), "response.ok = True")
        mocker.side_effect = MockResponseFalse
        self.assertEqual(self.emplTest.monthly_schedule('september'), "Bad Response!")
