from common.classes.ENUM_TYPE import ENUM_TYPE
class FIELD_TYPES( ENUM_TYPE ):
    #
    #
    #  map Django Field Types to zCrowd Widgets
    #
    # 
    CharField = 'zTextInput'
    TextAreaField = 'zTextArea' # no Django type, CharField with Textarea widget, fake it
    BooleanField = 'zCheckBox'
    ChoiceField = 'zSelect'
    RadioSelectField = 'zRadioSelect' # no Django type, ChoiceField with RadioSelect widget, fake it
    SelectMultipleField = 'zSelectMultiple' # no Django type, ChoiceField with widget, fake it
    DateField = 'zDateInput'
    DateTimeField = 'zDateTimeInput'

class WIDGET_TYPES( ENUM_TYPE ):
    #
    #
    #  map zCrowd Widgets to Django Widgets
    #  these should match answer_data config 'type' metadata
    #
    # 
    zTextInput = 'TextInput'
    zTextArea = 'Textarea'
    zCheckBox  = 'Checkbox'
    zRadioSelect = 'RadioSelect'
    zSelect = 'Select'
    zSelectMultiple = 'SelectMultiple'
    zDateInput = 'DateInput'
    zDateTimeInput = 'DateTimeInput'
    
from ztext_input import zTextInput
from ztext_area import zTextArea
from zcheck_box import zCheckBox
from zselect import zSelect
from zradio_select import zRadioSelect

