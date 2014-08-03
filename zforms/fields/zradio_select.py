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
YES_NO_CHOICES = ( 
    ( False, 'No' ),
    ( True, 'Yes' ),
)
BOOL_CHOICES = ( 
    ( True, 'True' ),
    ( False, 'False' ),
)
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class zRadioSelect( HTMLAttributeOverrides, ChoiceField ):

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
        super( zRadioSelect, self ).__init__( *args, **kwargs )
        self.widget = forms.RadioSelect( renderer=HorizontalRadioRenderer )
        self.choices = BOOL_CHOICES
        extra_attrs = self.widget_attrs( self.widget )
        if extra_attrs:
            self.widget.attrs.update( extra_attrs )

    def to_python( self, value ):
        parent_value = super( zRadioSelect, self ).to_python( value )
        return parent_value

    def validate(self, value):
        super( zRadioSelect, self ).validate( value )

    def clean( self, value ):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)

        #
        #  extra validation logic here
        #
        return True if value == 'True' else False




