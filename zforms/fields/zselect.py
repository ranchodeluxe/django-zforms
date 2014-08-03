#
#  django imports
#
from django import forms
from django.forms import ChoiceField
from django.core import validators
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_text, force_str, force_text

#
#  system imports
#
import logging
import json
logger = logging.getLogger( __file__ )

#
#  app imports
#
from mixins.HTMLAttributeOverrides import HTMLAttributeOverrides


class zSelect( HTMLAttributeOverrides, ChoiceField ):

    def __init__(self, *args, **kwargs):

        '''
            default validators on ChoiceField:
            ================================
            handles check to make sure value is in self.choices in validate() function
    
            default instance-level attributes on Field: 
            ===========================================
            self.required
            self.widget
            self.label
            self.initial
            self.help_text
            self.error_messages
            self.show_hidden_initial # to make it render as HiddenInput without overriding widget
            self.validators
            self.localize

        '''
        args, kwargs = self._set_overrides( *args, **kwargs )
        super( zSelect, self ).__init__( *args, **kwargs )


    def to_python( self, value ):
        parent_value = super( zSelect, self).to_python( value )
        return parent_value

    def validate(self, value):
        super( zSelect, self ).validate( value )

    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        #
        #  extra validation logic here
        #
        return value




