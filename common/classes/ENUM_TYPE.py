import inspect

class ENUM_TYPE( object ):
    """
    an abstract class to sublcass for easy ENUM creation
    ------------------------------------------------------

    #
    #  now we just define enums with a subclass
    #
    class DEVICE_TYPE( ENUM_TYPE ):
        ANDROID = 'Android'
        IOS = 'IPhone'


    #
    #  use it like this in a model
    #  where in the admin the key and value equate to
    #  <option value="key">value</option>
    #
    type = models.CharField(
                    verbose_name='Type',
                    max_length=30,
                    choices=DEVICE_TYPE.as_enum(),
                    default=DEVICE_TYPE.key( 'Android' )
    )


    #
    #  comparisons:
    #  we'll want to be able to grab keys or values quickly
    #  for comparisons. Use the methods ENUM.get_key( value ) to get
    #  a key for a given value and ENUM.get_value( key ) to get a value
    #  for a given key. NOTE: the latter form has a simple alias
    #  using the standard dot-accessor ENUM.<key> to grab the static
    #  attribute key and retrieve the value
    #
    ENUM.< key > ~ ENUM.get_value( < key > )
    """

    @classmethod
    def as_enum( self ):
        dict_values = {}

        for k,v in inspect.getmembers( self ):
            if not k.startswith( '__' ) and \
               not k.startswith( '_' ) and \
               not inspect.ismethod( v ) and \
               not inspect.isfunction( v ):
                dict_values[ k ] = getattr( self, k )

        return tuple( dict_values.items() )


    @classmethod
    def get_key( self, my_value ):
        ''' Used in if statements!!! '''
        
        if not my_value:
            return None
        
        # find the appropriate key for this value!
        for key, value in self.as_enum():
            if value.lower() == my_value.lower():
                return key

        return None

    @classmethod
    def get_value( self, my_key ):
        ''' Used in if statements!!! '''
        
        if not my_key:
            return None
        
        # find the appropriate key for this value!
        for key, value in self.as_enum():
            if key.lower() == my_key.lower():
                return value

        return None

    @classmethod
    def as_dict( self ):
        ''' Used above '''
        dict_values = {}
        
        # Iterate over all items associated with this class
        for e in dir( self ):
            # Skip any that aren't all upper or 'DEFAULT
            if e.isupper() and e != 'DEFAULT':
                # Add to dictionary
                dict_values[ e ] = getattr( self, e )
                
        return dict_values

