from django import forms
from django.conf.urls import patterns, url, include

import uuid
import re
import logging
from dateutil import parser
from datetime import datetime
logger = logging.getLogger( __file__ )
from bs4 import BeautifulSoup as BS

from zforms.fields.subclassed_fields import sPlainTextInput
from zforms.test.testcases import zFormTestCase


class zPlainTextInputCaseSubclass( zFormTestCase ):


    def setUp(self):
        super(zPlainTextInputCaseSubclass, self).setUp()

        class TestForm( forms.Form ):
            #  fields are dynamicaly added in each test
            pass

        self.form = TestForm()

    def tearDown(self):
        super(zPlainTextInputCaseSubclass, self).tearDown()
        self.form = None


    #
    #  RENDERING TESTS ( DEFAULT )
    #  
    def test_default_rendering( self ):
        logger.debug( "\n========================\n" )
        self.form.fields[ 'name' ] = sPlainTextInput(**{ 'initial' : 'hey there' })
        rendering = self.form.as_p()
        logger.debug( "[ RENDERED FORM ]: %s\n" % rendering )
        soup = BS( rendering )
        tag = soup.span
        logger.debug( "[ SPAN RENDERING ]: %s\n" % tag )
        self.assertEqual( tag.text, 'hey there' )
        logger.debug( "\n==================================================\n" )

