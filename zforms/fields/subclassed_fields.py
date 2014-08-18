#
#  django imports
#
from django import forms
from django.forms.widgets import HiddenInput
from django.core import validators
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_text, force_str, force_text

#
#  system imports
#
import logging
import json
from dateutil import parser
logger = logging.getLogger( __file__ )

#
#  app imports
#
from ztext_input import zTextInput
from ztext_area import zTextArea
from zcheck_box import zCheckBox
from zselect import zSelect
from zradio_select import zRadioSelect
from zhidden_input import zHiddenInput
from zplain_text_input import zPlainTextInput

class sTextInput(  zTextInput ):

    def __init__(self, *args, **kwargs):
        self.is_date = kwargs.get( 'is_date', False )
        if self.is_date: del kwargs[ 'is_date' ]
        super( sTextInput, self ).__init__( *args, **kwargs )

    def to_python( self, value ):
        parent_value = super( sTextInput, self).to_python( value )
        return parent_value

    def validate(self, value):
        super( sTextInput, self ).validate( value )
    
        #
        #  extra validation logic here
        #  runs before validators are called
        #  must throw ValidationError
        #

    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        if self.required:
            self.run_validators(value)

        if value != '':
            self.run_validators(value)

        #
        #  extra validation logic here
        #
        if self.is_date:
            try: 
                parser.parse( value )
            except TypeError:
                raise ValidationError('the date was not parsable as a date')
 
        return value




class sTextArea(  zTextArea ):

    def __init__(self, *args, **kwargs):
        super( sTextArea, self ).__init__( *args, **kwargs )

    def to_python( self, value ):
        parent_value = super( sTextArea, self).to_python( value )
        return parent_value

    def validate(self, value):
        super( sTextArea, self ).validate( value )

        #
        #  extra validation logic here
        #  runs before validators are called
        #  must throw ValidationError
        #

    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        if self.required:
            self.run_validators(value)

        if value != '':
            self.run_validators(value)

        #
        #  extra validation logic here
        #
        return value





class sCheckBox(  zCheckBox ):

    def __init__(self, *args, **kwargs):
        super( sCheckBox, self ).__init__( *args, **kwargs )


    def to_python( self, value ):
        parent_value = super( sCheckBox, self).to_python( value )
        return parent_value

    def validate(self, value):
        super( sCheckBox, self ).validate( value )

        #
        #  extra validation logic here
        #  runs before validators are called
        #  must throw ValidationError
        #

    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        #
        #  extra validation logic here
        #
        return value




class sRadioSelect(  zRadioSelect ):

    def __init__(self, *args, **kwargs):
        super( sRadioSelect, self ).__init__( *args, **kwargs )

    def to_python( self, value ):
        parent_value = super( sRadioSelect, self ).to_python( value )
        return parent_value

    def validate(self, value):
        super( sRadioSelect, self ).validate( value )

        #
        #  extra validation logic here
        #  runs before validators are called
        #  must throw ValidationError
        #


    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        #
        #  extra validation logic here
        #
        return True if value == 'True' else False


class sSelect(  zSelect ):

    def __init__(self, *args, **kwargs):
        super( sSelect, self ).__init__( *args, **kwargs )

    def to_python( self, value ):
        parent_value = super( sSelect, self ).to_python( value )
        return parent_value

    def validate(self, value):
        super( sSelect, self ).validate( value )

        #
        #  extra validation logic here
        #  runs before validators are called
        #  must throw ValidationError
        #


    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        #
        #  extra validation logic here
        #
        return value


class sHiddenInput(  zHiddenInput ):

    def __init__(self, *args, **kwargs):
        self.is_date = kwargs.get( 'is_date', False )
        if self.is_date: del kwargs[ 'is_date' ]
        super( sHiddenInput, self ).__init__( *args, **kwargs )

    def to_python( self, value ):
        parent_value = super( sHiddenInput, self ).to_python( value )
        return parent_value

    def validate(self, value):
        super( sHiddenInput, self ).validate( value )

        #
        #  extra validation logic here
        #  runs before validators are called
        #  must throw ValidationError
        #


    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        if self.required:
            self.run_validators(value)

        if value != '':
            self.run_validators(value)

        #
        #  extra validation logic here
        #
        if self.is_date:
            try: 
                parser.parse( value )
            except TypeError:
                raise ValidationError('the date was not parsable as a date')

        #
        #  extra validation logic here
        #
        return value


class sPlainTextInput( zPlainTextInput ):

    def __init__(self, *args, **kwargs):
        super( sPlainTextInput, self ).__init__( *args, **kwargs )

    def to_python( self, value ):
        parent_value = super( sPlainTextInput, self ).to_python( value )
        return parent_value

    def validate(self, value):
        super( sPlainTextInput, self ).validate( value )

        #
        #  extra validation logic here
        #  runs before validators are called
        #  must throw ValidationError
        #


    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        #
        #  extra validation logic here
        #
        return value








