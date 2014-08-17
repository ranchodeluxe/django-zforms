from django import forms
from django.conf.urls import patterns, url, include

import uuid
import re
import logging
from dateutil import parser
from datetime import datetime
logger = logging.getLogger( __file__ )
from bs4 import BeautifulSoup as BS

from zforms.fields.zselect import zSelect
from zforms.test.testcases import zFormTestCase


class zSelectCase( zFormTestCase ):


    def setUp(self):
        super(zSelectCase, self).setUp()

        class TestForm( forms.Form ):
            #  fields are dynamicaly added in each test
            pass

        self.form = TestForm()

    def tearDown(self):
        super(zSelectCase, self).tearDown()
        self.form = None


    #
    #  RENDERING TESTS ( DEFAULT )
    #  
    def test_default_django_field_args( self ):
        logger.debug( "\n" )
        self.form.fields[ 'name' ] = zSelect( **{
                'required' : True ,
                'label' : 'stupid is' ,
            } )
        rendering = self.form.as_p()
        logger.debug( "[ RENDERED FORM ]: %s\n" % rendering )
        soup = BS( rendering )
        input_tag = soup.find( 'select' )
        logger.debug( "[ INPUT TAG ATTRS ]: %s\n" % input_tag.attrs )
        label_tag = soup.label
        logger.debug( "[ LABEL TAG ATTRS ]: %s\n" % label_tag.attrs )

        #  assert lots
        self.assertEqual( input_tag.attrs.get( 'required', None ), 'required' )
        self.assertEqual( label_tag.get_text(), 'stupid is:' )
        logger.debug( "\n==================================================\n" )


    #
    #  RENDERING TESTS ( HTML ATTRIBUTE OVERRIDES )
    #  
    def test_attribute_override( self ):
        logger.debug( "\n" )
        self.form.fields[ 'name' ] = zSelect( **{
                'id' : 'tinker_bot' ,
                'class' : 'real cool',
                'disabled' : True ,
                'readonly' : True ,
            } )
        rendering = self.form.as_p()
        logger.debug( "[ RENDERED FORM ]: %s" % rendering )
        soup = BS( rendering )
        tag = soup.find( 'select' )
        logger.debug( "[ TAG ATTRS ]: %s" % tag.attrs )

        #  assert lots
        self.assertEqual( tag.get( 'id', None ), 'tinker_bot' )
        self.assertEqual( tag.get( 'class', None ), [ 'real',  'cool' ] )
        self.assertEqual( tag.get( 'disabled', None ), 'disabled' )
        self.assertEqual( tag.get( 'readonly', None ), 'readonly' )
        logger.debug( "\n==================================================\n" )

    #
    #  VALIDITY TESTS BOUND DATA
    #  
    def test_is_required( self ):
        logger.debug( "\n" )
        class TestForm( forms.Form ):
            name = zSelect( **{ 
                'required' : True ,
                'choices' : (
                    ( 'Y' , 'Yes' ) ,
                    ( 'N' , 'No'  ) ,
                ) ,
            } )
        valid_form = TestForm( { 'name' : 'Y' } )
        invalid_form1 = TestForm( { 'name' : '' } )
        invalid_form2 = TestForm( { 'name' : None } )

        #  assert lots
        self.assertEqual( valid_form.is_valid(), True )
        self.assertEqual( invalid_form1.is_valid(), False )
        self.assertEqual( invalid_form2.is_valid(), False )
        logger.debug( "\n==================================================\n" )


    def test_empty_value( self ):
        logger.debug( "\n" )
        class TestForm( forms.Form ):
            name = zSelect( **{ 
                'required' : False ,
                'choices' : (
                    ( ''  , '--Select Something--' ) ,
                    ( 'Y' , 'Yes' ) ,
                    ( 'N' , 'No'  ) ,
                ) ,
            } )
        valid_form = TestForm( { 'name' : '' } )
        logger.debug( "[ ERROR ]: %s" % valid_form._errors )
        #cleaned_value = valid_form.cleaned_data[ 'name' ]
        self.assertEqual( valid_form.is_valid() , False )
        self.assertEqual( valid_form._errors[ 'name' ][0] , 'you must select one of the options' )
        logger.debug( "\n==================================================\n" )

