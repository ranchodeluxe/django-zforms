from django import forms
from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.test.client import RequestFactory


import json, sys, os


'''
from fields.ztext_input import zTextInput
from fields.ztext_area import zTextArea
from fields.zcheck_box import zCheckBox
from fields.zselect import zSelect
from fields.zradio_select import zRadioSelect
#from zforms.test.json_configs import *
'''


class zFormTestCase( SimpleTestCase ):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        cls.factory = RequestFactory()

        # json ease of acccess in all tests
        '''
        cls.config_1 = json.loads( config_1, indent=4 )
        cls.config_2 = json.loads( config_2, indent=4 )
        cls.config_3 = json.loads( config_3, indent=4 )
        cls.config_4 = json.loads( config_4, indent=4 )
        cls.config_5 = json.loads( config_5, indent=4 )
        cls.config_6 = json.loads( config_6, indent=4 )
        cls.config_7 = json.loads( config_7, indent=4 )
        cls.config_8 = json.loads( config_8, indent=4 )
        cls.config_9 = json.loads( config_9, indent=4 )
        cls.config_10 = json.loads( config_10, indent=4 )
        cls.config_11 = json.loads( config_11, indent=4 )
        cls.config_12 = json.loads( config_12, indent=4 )
        '''

