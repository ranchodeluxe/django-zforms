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

class zTextArea( HTMLAttributeOverrides, CharField ):

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
        self.rows_cols_defaults = { 'cols' : 100, 'rows' : 20 }
        #
        #  we handle cols/rows here for convenience
        #  because Textrarea takes cols/rows as extra kwarg
        #
        cols = kwargs.get( 'cols', False )
        rows = kwargs.get( 'rows', False )
        if cols:
            self.rows_cols_defaults.update( { 'cols' : cols } )
            del kwargs[ 'cols' ]
        if rows:
            self.rows_cols_defaults.update( { 'rows' : rows } )
            del kwargs[ 'rows' ]
        args, kwargs = self._set_overrides( *args, **kwargs )
        self.widget = forms.Textarea( attrs=self.rows_cols_defaults )
        super( zTextArea, self ).__init__( *args, **kwargs )
        self._add_pattern_validator()


    def to_python( self, value ):
        parent_value = super( zTextArea, self).to_python( value )
        return parent_value


    def validate(self, value):
        super( zTextArea, self ).validate( value )


    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        #
        #  extra validation logic here
        #
        return value




