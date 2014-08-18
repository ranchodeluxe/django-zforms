#
#  django imports
#
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.widgets import *

#
#  sys imports
#
import re
import inspect
import logging
logger = logging.getLogger( __file__ )

#
#  app imports
#
from zforms.fields import FIELD_TYPES, WIDGET_TYPES

class HTMLAttributeOverrides( object ):
    '''
        supply all zfield widgets with common HTML attribute overrides on instantiation
    '''

    def _set_overrides( self, *args, **kwargs ):
        #
        #  widget attribute overrides have to be deleted 
        #  before calling zfield superclass constructors 
        #
        #
        self._chartype_html_attrs = []
        self._standard_html_attrs = []

        #
        #  char type HTML attributes
        #
        # PATTERN
        self.pattern = kwargs.get( 'pattern', None )
        if self.pattern is not None:
            #
            #
            #  TODO: real flexible regex detection needs some work here, it's ok for now.
            #  this attribute will be rendered as data-pattern in HTML for JavaScript
            #  to use in it's own regex testing. As is, it will cause problems 
            #  with HTML5 if it's rendered as 'pattern' attribute on validation of form. 
            #  However, it would be great if we can find a way to make it work with 'pattern'
            #  attribute validation for HTML5 by default and kill two birds with one stone
            #
            #
            prefix = '^'
            suffix = '$' if self.pattern[-1] in [ '+', '*', '}' ] else '+$'
            self.django_pattern = r'%s%s%s' % ( prefix, self.pattern, suffix )
            self.django_pattern_error_message = kwargs.get( 'pattern_error_message', 'Enter valid input that matches the expected regex pattern' )
            self._chartype_html_attrs.append( { 'data-pattern' : self.pattern } ) 
            del kwargs[ 'pattern' ]

        # PATTERN ERROR MESSAGE 
        self.pattern_error_message = kwargs.get( 'pattern_error_message', None )
        if self.pattern_error_message is not None:
            del kwargs[ 'pattern_error_message' ]
            

        # PLACEHOLDER
        self.placeholder = kwargs.get( 'placeholder', None )
        if self.placeholder is not None:
            self._chartype_html_attrs.append( { 'placeholder' : self.placeholder } ) 
            del kwargs[ 'placeholder' ]

        #
        #
        #  COMMON HTML ATTRIBUTES 
        #
        #
        # ID
        self.id = kwargs.get( 'id', None )
        if self.id is not None:
            self._standard_html_attrs.append( { 'id' : self.id } ) 
            del kwargs[ 'id' ]

        # CLASS
        self.css_class = kwargs.get( 'class', None )
        if self.css_class is not None:
            self._standard_html_attrs.append( { 'class' : self.css_class } ) 
            del kwargs[ 'class' ]

        # DISABLED
        self.disabled = kwargs.get( 'disabled', None )
        if self.disabled is not None:
            if self.disabled:
                self._standard_html_attrs.append( { 'disabled' : 'disabled' } ) 
            del kwargs[ 'disabled' ]

        # READ_ONLY
        self.readonly = kwargs.get( 'readonly', None )
        if self.readonly is not None:
            if self.readonly:
                self._standard_html_attrs.append( { 'readonly' : 'readonly' } )
            del kwargs[ 'readonly' ]

        #
        #  REQUIRED as HTML5 attribute
        #  Django handles required as check but
        #  we also want to add it as element attr
        #
        self.required_option = kwargs.get( 'required', None )
        if self.required_option is not None:
            if self.required_option: 
                self._standard_html_attrs.append( { 'required' : 'required' } ) 
            # no need to delete kwargs( 'required' ) b/c all Django fields support it


        return args, kwargs

    def widget_attrs( self, widget ):
        attrs = super( HTMLAttributeOverrides, self ).widget_attrs( widget )

        if isinstance( widget, TextInput ) or isinstance( widget, Textarea ) or isinstance( widget, HiddenInput ):
            for attr in self._chartype_html_attrs: attrs.update( attr )

        # add standard HTML attributes
        for attr in self._standard_html_attrs: attrs.update( attr )

        return attrs


    def _add_pattern_validator( self ):
        #
        #  this has be run only after superclass __init__ has run
        #
        if not hasattr( self, 'django_pattern' ) or not self.django_pattern:
            return
        self.django_pattern_regex = re.compile( self.django_pattern )
        self.django_pattern_validator = validators.RegexValidator( self.django_pattern_regex, self.django_pattern_error_message, code='Invalid!' )
        self.validators.append( self.django_pattern_validator )


    


