import logging

from django import forms

logger = logging.getLogger( __file__ )
from bs4 import BeautifulSoup as BS

from zforms.fields.zcheck_box import zCheckBox
from zforms.test.testcases import zFormTestCase


class zCheckBoxCase( zFormTestCase ):


    def setUp(self):
        super(zCheckBoxCase, self).setUp()

        class TestForm( forms.Form ):
            #  fields are dynamicaly added in each test
            pass

        self.form = TestForm()

    def tearDown(self):
        super(zCheckBoxCase, self).tearDown()
        self.form = None


    #
    #  RENDERING TESTS ( DEFAULT )
    #  
    def test_default_django_field_args( self ):
        logger.debug( "\n" )
        self.form.fields[ 'name' ] = zCheckBox( **{
                'required' : True ,
                'label' : 'stupid is' ,
                'initial' : True,
            } )
        rendering = self.form.as_p()
        logger.debug( "[ RENDERED FORM ]: %s\n" % rendering )
        soup = BS( rendering )
        input_tag = soup.input
        logger.debug( "[ INPUT TAG ATTRS ]: %s\n" % input_tag.attrs )
        label_tag = soup.label
        logger.debug( "[ LABEL TAG ATTRS ]: %s\n" % label_tag.attrs )

        #  assert lots
        self.assertIsNotNone( input_tag.attrs.get( 'required', None ) )
        self.assertEqual( label_tag.get_text(), 'stupid is:' )
        self.assertEqual( input_tag.attrs.get( 'checked', None ), 'checked' )
        logger.debug( "\n==================================================\n" )


    #
    #  RENDERING TESTS ( HTML ATTRIBUTE OVERRIDES )
    #  
    def test_attribute_override( self ):
        logger.debug( "\n" )
        self.form.fields[ 'name' ] = zCheckBox( **{
                'id' : 'tinker_bot' ,
                'class' : 'real cool',
                'disabled' : True ,
                'readonly' : True ,
            } )
        rendering = self.form.as_p()
        logger.debug( "[ RENDERED FORM ]: %s" % rendering )
        soup = BS( rendering )
        tag = soup.input
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
            name = zCheckBox( **{ 
                'required' : True
            } )
        valid_form = TestForm( { 'name' : True } )
        invalid_form1 = TestForm( { 'name' : '' } )
        invalid_form2 = TestForm( { 'name' : None } )

        #  assert lots
        self.assertEqual( valid_form.is_valid(), True )
        self.assertEqual( invalid_form1.is_valid(), False )
        self.assertEqual( invalid_form2.is_valid(), False )
        logger.debug( "\n==================================================\n" )


    def test_is_correct_type( self ):
        logger.debug( "\n" )
        class TestForm( forms.Form ):
            name = zCheckBox()
        valid_form = TestForm( { 'name' : True } )
        valid_form.is_valid()
        cleaned_value = valid_form.cleaned_data[ 'name' ]
        self.assertEqual( isinstance( cleaned_value, bool ), True )
        logger.debug( "\n==================================================\n" )

