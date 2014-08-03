from django import forms

from zforms import fields as zfields
from test.data import example_input1 as example_input
from mixins.DynFieldMixin import DynFieldMixin


#
#
#  example of a dynamically-generated form
#  created directly from the config
#
#
class DynTestForm( DynFieldMixin, forms.Form ):

    def __init__( self, *args, **kwargs ):
        super( DynTestForm, self ).__init__( *args, **kwargs )
        self._build_dynamic_fields( example_input )















#
#
#  example of an auto-generated form
#  created from a template
#
#
class DeclarativeTestForm( forms.Form ):

    data_id = zfields.zTextInput( **{
        'pattern' : '[0-9]', 
        'pattern_error_message' : 'data_id field can only be numeric',
        'disabled' : False, 
        'readonly' : False, 
        'id' : 'data_id',
        'initial' : 102343,
        'widget' :  eval( 'getattr( forms, "HiddenInput" )()' )
    } )

    username = zfields.zTextInput( **{ 
        'max_length': 100, 
        'min_length' : 2, 
        'pattern' : '[0-9A-Za-z]', 
        'pattern_error_message' : 'Usernames can only be alpha and numeric characters',
        'placeholder' : 'Enter your cool username!', 
        'disabled' : False, 
        'required' : True ,
        'readonly' : False, 
        'id' : 'username_target',
        'initial' : 'whizjunkmob!'
    } )

    is_staff = zfields.zCheckBox( **{ 
        'disabled' : False, 
        'readonly' : False, 
        'id' : 'is_staff_chk',
        'initial' : True 
    } )

    skills = zfields.zSelect( **{
        'disabled' : False, 
        'readonly' : False, 
        'id' : 'skills',
        'initial' : 'fart',
        'choices' : (
            ( 'program', 'program' ) ,
            ( 'read' , 'read' ) , 
            ( 'write', 'write' ),
            ( 'fart', 'fart' ),
        )
    } )

    is_friendly = zfields.zRadioSelect( **{
        'disabled' : False, 
        'readonly' : False, 
        'id' : 'is_friendly',
        'initial' : False
    } )

    
    comments = zfields.zTextArea( **{
        'disabled' : False, 
        'readonly' : False, 
        'id' : 'comment_box',
        'rows' : 300, 
        'cols' : 30, 
        'initial' : 'Enter your comments here!'
    } )

