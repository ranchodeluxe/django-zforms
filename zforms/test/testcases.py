from django.test import SimpleTestCase
from django.test.client import Client
from django.test.client import RequestFactory


class zFormTestCase( SimpleTestCase ):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        cls.factory = RequestFactory()

    @classmethod
    def tearDownClass(cls):
        # TODO: for some reason Django is running DB cleanup on non-transactional DB tests
        # 1) why is it doing this?
        # 2) why is the cursor.wrapped ( which is for transactions ) needed?
        #
        # Traceback (most recent call last):
        #   File "/usr/local/src/django-zforms/venv/local/lib/python2.7/site-packages/django/test/testcases.py", line 186, in tearDownClass
        #     connection.cursor = connection.cursor.wrapped
        # AttributeError: 'function' object has no attribute 'wrapped'
        pass