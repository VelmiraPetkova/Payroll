from unittest import TestCase

from company.company import Company

class CompanyTest(TestCase):
    def setUp(self) -> None:
        self.companyTest = Company("Test1","1234567890", "Bulgaria, Sofia", 1203, "TestManager")

    def test_object_is_instance_corectly(self):
        # Asert test value in instance
        self.assertEqual("Test1", self.companyTest.name)
        self.assertEqual("1234567890", self.companyTest.company_id)
        self.assertEqual("Bulgaria, Sofia", self.companyTest.address)
        self.assertEqual(1203, self.companyTest.economic_activities)
        self.assertEqual("TestManager", self.companyTest.manager)
        self.assertEqual([], self.companyTest.contracts)

    def test_name_error(self):
        with self.assertRaises(ValueError) as ex:
            self.companyTest.name = ""
        self.assertEqual("The company name is not allowed to be empty!", str(ex.exception))

    def test_company_id_error(self):
        with self.assertRaises(ValueError) as ex:
            self.companyTest.company_id = "123456"
        self.assertEqual("Company ID should be 10 symbols long!", str(ex.exception))

