from django import forms
from django.conf.urls import patterns, url, include

import uuid
import re
import logging
from dateutil import parser
from datetime import datetime
logger = logging.getLogger( __file__ )
from bs4 import BeautifulSoup as BS

from zforms.fields.subclassed_fields import *
from zforms.test.testcases import zFormTestCase

class zTextInputSubclassCase( zFormTestCase ):


    def setUp(self):
        super(zTextInputSubclassCase, self).setUp()

        class TestForm( forms.Form ):
            #  fields are dynamicaly added in each test
            #  of form is recreated w/ bound data
            pass

        self.form = TestForm()

    def tearDown(self):
        super(zTextInputSubclassCase, self).tearDown()
        self.form = None


    #
    #  RENDERING TESTS ( DEFAULT )
    #  
    def test_eval_hidden_input( self ):
        logger.debug( "\n========================\n" )
        self.form.fields[ 'name' ] = sTextInput( **{
                'widget' : eval('getattr( forms, "HiddenInput" )()') ,

            } )
        rendering = self.form.as_p()
        logger.debug( "[ RENDERED FORM ]: %s\n" % rendering )
        soup = BS( rendering )
        tag = soup.input
        logger.debug( "[ TAG ATTRS ]: %s\n" % tag.attrs )
        self.assertEqual( tag[ 'type' ], 'hidden' )
        logger.debug( "\n==================================================\n" )


    def test_default_django_field_args( self ):
        logger.debug( "\n" )
        self.form.fields[ 'name' ] = sTextInput( **{
                'required' : True ,
                'label' : 'stupid is' ,
                'initial' : 'stupid does' ,
            } )
        rendering = self.form.as_p()
        logger.debug( "[ RENDERED FORM ]: %s\n" % rendering )
        soup = BS( rendering )
        input_tag = soup.input
        logger.debug( "[ INPUT TAG ATTRS ]: %s\n" % input_tag.attrs )
        label_tag = soup.label
        logger.debug( "[ LABEL TAG ATTRS ]: %s\n" % label_tag.attrs )

        #  assert lots
        self.assertEqual( input_tag.attrs.get( 'required', None ), 'required' )
        self.assertEqual( label_tag.get_text(), 'stupid is:' )
        self.assertEqual( input_tag[ 'value' ], 'stupid does' )
        logger.debug( "\n==================================================\n" )


    #
    #  RENDERING TESTS ( HTML ATTRIBUTE OVERRIDES )
    #  
    def test_attribute_override( self ):
        logger.debug( "\n" )
        self.form.fields[ 'name' ] = sTextInput( **{
                'pattern' : '[0-9]' ,
                'id' : 'tinker_bot' ,
                'class' : 'real cool',
                'disabled' : True ,
                'readonly' : True ,
                'placeholder' : 'a_placeholder',
            } )
        rendering = self.form.as_p()
        logger.debug( "[ RENDERED FORM ]: %s" % rendering )
        soup = BS( rendering )
        tag = soup.input
        logger.debug( "[ TAG ATTRS ]: %s" % tag.attrs )

        #  assert lots
        self.assertEqual( tag.get( 'data-pattern', None ), '[0-9]' )
        self.assertEqual( tag.get( 'id', None ), 'tinker_bot' )
        self.assertEqual( tag.get( 'class', None ), [ 'real',  'cool' ] )
        self.assertEqual( tag.get( 'disabled', None ), 'disabled' )
        self.assertEqual( tag.get( 'readonly', None ), 'readonly' )
        self.assertEqual( tag.get( 'placeholder', None ), 'a_placeholder' )
        logger.debug( "\n==================================================\n" )

    #
    #  VALIDITY TESTS BOUND DATA
    #  
    def test_pattern_digits( self ):
        logger.debug( "\n" )
        
        class TestForm( forms.Form ):
            name = sTextInput( **{ 'pattern' : '[0-9]'  } )
        valid_form = TestForm( { 'name' : '123' } )
        invalid_form = TestForm( { 'name' : 'trickster' } )

        #  assert lots
        self.assertEqual( valid_form.is_valid(), True )
        self.assertEqual( invalid_form.is_valid(), False )
        logger.debug( "\n==================================================\n" )

    def test_pattern_dates( self ):
        logger.debug( "\n" )
        class TestForm( forms.Form ):
            date = sTextInput( **{ 'pattern' : '\d{1,2}/\d{1,2}/\d{4}', 'is_date' : True  } )
        valid_form = TestForm( { 'date' : '10/23/2014' } )
        valid_form2 = TestForm( { 'date' : '1/2/2014' } )
        invalid_form = TestForm( { 'date' : '10/23' } )

        #  assert lots
        self.assertEqual( valid_form.is_valid(), True )
        logger.debug( "[ VALID FORM API ]: %s" % valid_form.__dict__ )
        cleaned_date = valid_form.cleaned_data[ 'date' ]
        logger.debug( "[ CLEANED DATE ]: %s" % cleaned_date )
        parsed_date = parser.parse( cleaned_date )
        self.assertEqual( isinstance( parsed_date, datetime ), True )

        # invalid
        self.assertEqual( invalid_form.is_valid(), False )
    
        # valid 2
        self.assertEqual( valid_form2.is_valid(), True )
        logger.debug( "[ INVALID FORM API ]: %s" % valid_form2.__dict__ )
        cleaned_date = valid_form2.cleaned_data[ 'date' ]
        logger.debug( "[ CLEANED DATE ]: %s" % cleaned_date )
        parsed_date = parser.parse( cleaned_date )
        self.assertEqual( isinstance( parsed_date, datetime ), True )
        logger.debug( "\n==================================================\n" )

    def test_pattern_phone( self ):
        logger.debug( "\n" )
        class TestForm( forms.Form ):
            phone = sTextInput( **{ 
                 'pattern' : '\d{3}-\d{3}-\d{4}' ,
                 'pattern_error_message' : 'phone number must match format 000-000-0000' 
            } )
        valid_form = TestForm( { 'phone' : '502-234-2345' } )
        invalid_form = TestForm( { 'phone' : '10/23' } )

        #  assert lots
        self.assertEqual( valid_form.is_valid(), True )
        self.assertEqual( invalid_form.is_valid(), False )
        logger.debug( "\n==================================================\n" )

    def test_is_required( self ):
        logger.debug( "\n" )
        class TestForm( forms.Form ):
            name = sTextInput( **{ 
                'required' : True
            } )
        valid_form = TestForm( { 'name' : 'yep' } )
        invalid_form1 = TestForm( { 'name' : '' } )
        invalid_form2 = TestForm( { 'name' : None } )

        #  assert lots
        self.assertEqual( valid_form.is_valid(), True )
        self.assertEqual( invalid_form1.is_valid(), False )
        self.assertEqual( invalid_form2.is_valid(), False )
        logger.debug( "\n==================================================\n" )

    def test_min_length( self ):
        logger.debug( "\n" )
        class TestForm( forms.Form ):
            name = sTextInput( **{ 
                'min_length' : 10 ,
            } )
        valid_form = TestForm( { 'name' : '1234567891011' } )
        invalid_form = TestForm( { 'name' : '123456789' } )

        #  assert lots
        self.assertEqual( valid_form.is_valid(), True )
        self.assertEqual( invalid_form.is_valid(), False )
        logger.debug( "\n==================================================\n" )

    def test_max_length( self ):
        logger.debug( "\n" )
        class TestForm( forms.Form ):
            name = sTextInput( **{ 
                'max_length' : 10 ,
            } )
        valid_form = TestForm( { 'name' : '123456789' } )
        invalid_form = TestForm( { 'name' : '1234567891011' } )

        #  assert lots
        self.assertEqual( valid_form.is_valid(), True )
        self.assertEqual( invalid_form.is_valid(), False )
        logger.debug( "\n==================================================\n" )


