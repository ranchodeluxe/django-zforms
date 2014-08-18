#
#  django imports
#
from django import forms
from django.forms import CharField
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


class PlainTextWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        new_value = mark_safe(value) if value is not None else ''
        return '<span>' + new_value + '</span>'

class zPlainTextInput( HTMLAttributeOverrides, CharField ):

    def __init__(self, *args, **kwargs):

        '''
            default validators on CharField:
            ================================
            self.validators.append(validators.MinLengthValidator(int(min_length)))
            self.validators.append(validators.MaxLengthValidator(int(max_length)))
    
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
        self.widget = PlainTextWidget()
        super( zPlainTextInput, self ).__init__( *args, **kwargs )
        self._add_pattern_validator()

    def to_python( self, value ):
        parent_value = super( zPlainTextInput, self).to_python( value )
        return parent_value

    def validate(self, value):
        super( zPlainTextInput, self ).validate( value )

    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        #
        #  extra validation logic here
        #
        return value




