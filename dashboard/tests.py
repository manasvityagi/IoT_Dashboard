from django.test import TestCase

# TODO Write Unit Test
# TODO Write Integration Test
# TODO Demonstrate Test Fixture


# Create your tests here.
from dashboard.models import Address


class DashboardModelTest(TestCase):
    #
    def test_field(self):
        address  = Address()

