Django-zForms
=================

There are some people out there who still render HTML form fields with Django/Python. While using forms for server-side validation makes sense ( and only in some cases ), using them as renderers is only be useful in the simplest of situations or else it gets ugly fast.

Goal(s)
-------------

* Write some wrappers around forms.Form and forms.fields to create easier-to-use instantiation options

* Create a one-to-one mapping of HTML types to Django widget types and abstract out the 'Field' concept. As a programmer I want to say, 'I need a TextInput'. I do not want to say, 'I need a CharField with a TextInput override'. The fact that CharField has code reuse for Textarea(s), TextInput(s) and CheckBox(s) should be abstracted away from the end user but still provide all possible override options.

* Give every field input the ability to override HTML attributes such as class, id, pattern, required on field input instantiation so we don't have to deal with it post field instantiation ( creates ugly code )

* Create the most common input types with sane defaults and endpoints for quick override configuratin on the Field ( clean, validate, to_python )





