example_input1 = {
    'case_number' : { 
        'type' : 'zTextInput',
        'max_length': 25, 
        'min_length' : 1, 
        'pattern' : '[0-9A-Za-z ]', 
        'pattern_error_message' : 'field can only be alpha and numeric characters',
        'placeholder' : 'Enter the case number', 
        'disabled' : False, 
        'readonly' : False, 
        'required' : True ,
        'initial' : '1323BDFD'
    } ,
    'case_number_exists' : {
        'type' : 'zCheckBox',
        'disabled' : False, 
        'readonly' : False, 
        'initial' : True 
    } ,
    'case_number_match' : {
        'type' : 'zRadioSelect',
        'disabled' : False, 
        'readonly' : False, 
        'initial' : False
    } ,
    'defendant' : [
        {   'name' : {
                'type' : 'zTextInput' ,
                'pattern' : '[a-zA-Z ]', 
                'pattern_error_message' : 'field can only be alpha characters',
                'disabled' : False, 
                'readonly' : False, 
                'initial' : 'Tom Jones',
            }
        } ,

        {   'order' : {
                'type' : 'zTextInput' ,
                'pattern' : '[a-zA-Z ]', 
                'pattern_error_message' : 'field can only be alpha characters',
                'disabled' : False, 
                'readonly' : False, 
                'initial' : 'Bob Ross'
            }
        } ,
    ] ,
    'grade' : {
        'type' : 'zSelect' ,
        'disabled' : False, 
        'readonly' : False, 
        'required' : True ,
        'choices'  : (
            ('A', 'A - Perfect!! No editing needed (Approved)'), 
            ('C', 'C - Good Enough. Some editing needed (Approved)'), 
            ('B', 'B - Nicely Done! Little editing needed (Approved)'), 
            ('D', 'D - Lots of editing needed (Approved, But NO BONUS)'), 
            ('G', '0 - Cheating (Rejection)'), 
            ('F', 'F - Unusable (Rejection)'), 
            ('', '--- Select Grade ---')
        ) ,
    }
}

