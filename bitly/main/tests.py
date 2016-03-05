from django.db import IntegrityError
from django.test import TestCase
from models import UrlRedirect


class UrlRedirectTestCase(TestCase):
    """
    Some basic tests for most of the models functions.
    """

    def test_is_valid(self):
        model = UrlRedirect()
        model.original_url = "https://www.google.com.au/webhp?hl=en#hl=en&q=this+is+how+you+google"

        self.assertTrue(model.is_valid())

    def test_is_not_valid(self):
        """
        Does invalid pass when original_url is not a fully valid url.
        """
        model = UrlRedirect()
        model.original_url = "123"
        self.assertFalse(model.is_valid())

        model.original_url = "www.google.com.au/webhp?hl=en#hl=en&q=this+is+how+you+google"
        self.assertFalse(model.is_valid())

    def test_set_url_no_protocol(self):
        """
        Test that set url works when the protocol portion (eg http://) is not included
        """
        model = UrlRedirect()
        model.set_url('cjbrassington.com')
        self.assertEqual(model.original_url, 'http://cjbrassington.com')

    def test_set_url_incorrect_protocol_not_valid(self):
        """
        Test that the resulting url will not be valid if we pass in a non http or https protocol
        """
        model = UrlRedirect()
        model.set_url('ftp://cjbrassington.com')
        self.assertEqual(model.original_url, 'http://ftp://cjbrassington.com')
        self.assertFalse(model.is_valid())

    def test_set_complete_url(self):
        model = UrlRedirect()
        model.set_url('https://www.google.com.au/webhp?hl=en#hl=en&q=this+is+how+you+google')
        self.assertEqual(model.original_url, 'https://www.google.com.au/webhp?hl=en#hl=en&q=this+is+how+you+google')

    def test_short_url_exists(self):
        model_1 = UrlRedirect()
        model_1.shortened_url = "abc"
        model_1.save()

        model_2 = UrlRedirect()
        self.assertTrue(model_2._short_url_already_exists("abc"))
        self.assertFalse(model_2._short_url_already_exists("abc123"))

    def test_cannot_save_duplicate_short_url(self):
        model_1 = UrlRedirect()
        model_1.shortened_url = "abc"
        model_1.save()

        model_2 = UrlRedirect()
        model_2.shortened_url = "abc"
        try:
            model_2.save()
            self.fail("Should have caught the duplicate")
        except IntegrityError:
            pass

