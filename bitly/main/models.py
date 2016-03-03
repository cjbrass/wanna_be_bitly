import random
import string
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class UrlRedirect(models.Model):
    original_url = models.CharField(max_length=500)  # arbitrarily chosen
    shortened_url = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)  # can use this later to expire entries if we so desire

    INITIAL_LENGTH = 3
    """
    The first attempt to make a short url will try to make one 3 characters long. We increase the length by one every
    time that fails.
    """

    def set_url(self, url):
        """
        If the url does not start with http, we add it in so that the Django redirect will work. If the site is https,
        then the site should handle the switch (so going to http://google.com will still get you to google, and google
        will handle switching you to https)
        """
        if url[:4] != "http":
            url = "http://" + url
        self.original_url = url

    def is_valid(self):
        """
        Is the original url a valid url? Currently using Django's validator, which I believe is just regex
        """
        val = URLValidator()
        try:
            val(self.original_url)
        except ValidationError:
            return False
        return True

    def make_shortened_url(self):
        """
        Randomly generate a short string for the new url. If that url exists, we make a slightly longer string and try
        again. Chose this method because it was simple to implement, and allows for short urls.
        """
        length = self.INITIAL_LENGTH
        short_url = self._make_random_string(length)
        while self._short_url_already_exists(short_url):
            length += 1
            short_url = self._make_random_string(length)
        self.shortened_url = short_url

    def _make_random_string(self, length):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))

    def _short_url_already_exists(self, short_url):
        """
        does the given short url already exist in the db
        """
        existing_entries = UrlRedirect.objects.filter(shortened_url=short_url)
        if existing_entries.count():
            return True
        return False
