import random
import string
from django.db import models

# Create your models here.


class UrlRedirect(models.Model):
    original_url = models.CharField(max_length=500)  # arbitrarily chosen
    shortened_url = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    INITIAL_LENGTH = 3
    """
    The first attempt to make a short url will try to make one 3 characters long. We increase the length by one every
    time that fails.
    """

    def set_url(self, url):
        if url[:4] != "http":
            url = "http://" + url
        self.original_url = url

    def is_valid(self):
        """
        Is the original url a valid url
        """
        return True

    def make_shortened_url(self):
        length = self.INITIAL_LENGTH
        short_url = self._make_random_string(length)
        while self._short_url_already_exists(short_url):
            length += 1
            short_url = self._make_random_string(length)
        self.shortened_url = short_url

    def _make_random_string(self, length):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))

    def _short_url_already_exists(self, short_url):
        existing_entries = UrlRedirect.objects.filter(shortened_url=short_url)
        if existing_entries.count():
            return True
        return False



