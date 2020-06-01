import datetime
from django.test import TestCase

# TODO Write Unit Test
# TODO Write Integration Test
# TODO Demonstrate Test Fixture
# Test Fixtures: The preparation/ setup for the test to execute
# Tear Down or cleanup: Removing the side effects of the test execution.
# Both of these are handled by django test library, it creates the temporary
# database in case the test is related to models,
# and destroys it , when test is completed.

# Create your tests here.
from django.utils import timezone

from dashboard.models import Address, DeviceModels, Thing, SubscribersList


class ThingModeTest(TestCase):
    # this test, tests if the function 'is_purchased_recently'
    # it buys a product now, and expects that is_purchased_recently should return true
    def test_allow_future_purchase_date(self):
        purchased_now = timezone.now()
        future_purchased_product = Thing(purchase_date=purchased_now)

        self.assertIs(future_purchased_product.is_purchased_recently(), True)

    # this test inserts a subscriber, and tests whether 'only' one email is present
    def test_add_to_subscribersList(self):
        test_name = "test name"
        test_email = "someone@test.com"
        sub = SubscribersList(name=test_name, email=test_email)
        sub.save()
        result = SubscribersList.objects.all().filter(email=test_email).count() == 1

        self.assertTrue(result, True)

    # this test inserts a subscriber, and tests whether 'only' one email is present
    def test_unsubscribe(self):
        test_name = "test name"
        test_email = "someone@test.com"
        # add a subscriber
        SubscribersList(name=test_name, email=test_email).save()

        # remove a subscriber
        SubscribersList.objects.get(name=test_name).delete()

        # Test whether the subscriber count for this email is 0
        result = SubscribersList.objects.all().filter(email=test_email).count() == 0

        self.assertTrue(result, True)
