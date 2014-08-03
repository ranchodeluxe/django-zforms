from django import forms
import logging
logger = logging.getLogger( __name__ )
from zforms import fields as zfields

class DynFieldMixin( object ):

    def _module_dependencies_exist( self ):
        try:
            self.fields
            forms
            forms.Form
            zfields
        except NameError:
            logger.error( "NameError" )
            return False
        except AttributeError:
            logger.error( "AttributeError" )
            return False
        return True

    def _construct_field( self, field_key_name, field_params, index=None ):
        import copy
        field_params_copy = copy.deepcopy( field_params )
        field_type = field_params_copy.get( 'type', None )
        if not field_type:
            logger.error( "[ FIELD TYPE ERROR ]: there is no 'type' attribute in the field params dict" )
            return 
        del field_params_copy[ 'type' ]
        
        # instantiate and add it to self.fields
        if index:
            field_key_name += '_%s' % str( index )
        self.fields[ field_key_name ] = getattr( zfields, field_type )( **field_params_copy )

    def _build_dynamic_fields( self, field_dict, use_index=False, index=1 ):
        if not self._module_dependencies_exist():
            logger.error( "[ IMPORT ERROR ]: %s depends on some imports that don't seem to exist" % self.__class__.__name__ )
            return
            
        for key, value in field_dict.items():
            if isinstance( value, list ):
                # start new indexing for new nested list
                if index > 1: index = 1 
                for hash_map in value:
                    nested_key, nested_value =  ( hash_map.keys()[0], hash_map.values()[0] )
                    # combine first key with nested key
                    nested_key = key + '_' + nested_key
                    index = self._build_dynamic_fields( { nested_key : nested_value }, use_index=True, index=index )
                continue
            if use_index:
                self._construct_field( key, value, index=index )
            else:
                self._construct_field( key, value )
            index += 1
        return index 




