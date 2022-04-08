"""Holds the company class for My Prof"""

class Company():
    """
    When this object is created it creates a company object to hold
    data about the business.
    """
    def __init__(self, name, years_active, num_employees):
        self.name = name
        self.years_active = years_active
        self.num_employees = num_employees
        