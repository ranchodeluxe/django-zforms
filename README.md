django-zforms
==============

## Background

The goal of the [django.forms.fields](https://github.com/django/django/blob/1.10.3/django/forms/fields.py) and
[django.forms.widgets](https://github.com/django/django/blob/1.10.3/django/forms/widgets.py) API is to help render
server-side forms and setup validation rules to leverage in the submission cycle.

This thought experiment was an attempt to reinterpret Django form and field instantiation that doesn't work directly with models.
Largely, it's unfinished and the interpretation has its own warts. However, the frustrations mentioned
below are still valid. These days I barely render any forms server-side. This experiment grew out of a need to
render forms on the server based on JSON configurations and without a Django model.

## API Frustrations

0. Django uses base `Field` and `Widget` classes to try and create a separation of concern for rendering and validating forms.
The `Field` is responsible for higher-level concerns such as coordinating validation, the rendering of multiple inputs and wrapping
inputs in help text. Each `Widget` is really about defining sane element attribute defaults and then rendering that element.

In practice though, this is often confusing. It forces the developer to know something about the API. For example,
here's how we create a `<textarea>` element since there is no high-level `Field` subclass:

    ```python
    In [36]: from django.forms import Form; from django.forms.fields import *; from django.forms.widgets import *

    In [37]: form = Form()

    In [38]: form.fields['comment'] = CharField(widget=Textarea)

    In [40]: form.as_p()
    Out[40]: u'<p><label for="id_comment">Comment:</label> <textarea cols="40" id="id_comment" name="comment" rows="10" required>\r\n</textarea></p>'
    ```
Something about this API feels wrong. As a programmer I want to say, "I need a Textarea element".
I do not want to say, "I need a CharField with a Textarea override". The fact that `CharField` has code reuse for `Textarea`s,
`TextInput`s and `CheckBox`s should be abstracted away from the API and yet still provide override options.

0. Then there's the issue of where to pass element attributes for rendering versus for functional use. For example, let's say
I want a `<input type="text"/>` field with some custom `data-*` attributes that my Javascript will key off of. I also want
this field to NOT be `required`, meaning it can be empty on a POST.

To render my custom-defined `data-*` attributes I would pass extra arguments to the `Widget` subclass. By default an input will
be rendered with a `required` attribute unless you tell it not to. `required` in this case
is not only a rendering consideration it's a functional one for validation. So that functional consideration is passed to the
`Field` subclass but not the `Widget`.

    ```python
    In [59]: form.fields['comment'] = CharField(required=False, widget=TextInput(attrs={"data-id": "12345", "data-type": "comment"}
        ...: ))

    In [60]: form.as_p()
    Out[60]: u'<p><label for="id_comment">Comment:</label> <input data-id="12345" data-type="comment" id="id_comment" name="comment" type="text" /></p>'
    ```

That's interesting. The `Field` subclasses also take an `initial` argument for the `value` attribute. But `value` is a just another HTML attribute
on an element, so `Widget` would override that because it handles the rendering too. Not quite.

    ```python
    In [75]: form.fields['comment'] = CharField(required=False, initial='blah', widget=TextInput(attrs={"data-id": "12345", "data-t
        ...: ype": "comment", "value": "blah2"}))

    In [76]: form.as_p()
    Out[76]: u'<p><label for="id_comment">Comment:</label> <input data-id="12345" data-type="comment" id="id_comment" name="comment" type="text" value="blah" /></p>'
    ```
So it's clear the developer has to carefully know what they can and cannot pass into `Field` versus `Widget` subclasses.

I would prefer to pass all initialization options into one constructor.

    ```python
    form.fields['comment'] = zTextInput(**{
        'initial': 'blah2',
        'required': False,
        'data_attrs': { 'id': 1234, 'type': 'comment' }
    })
    ```

## Getting Started

Mostly don't, as this is experimental. To get a sense for how the API was refactored follow these instructions
to download the repo and run the tests inside a bare-bones Django application. Grok the tests in `zforms/test/`

```bash
$ virtualenv --python=python2.7 venv
$ source venv/bin/activate
$ pip install -r requirements
$ python manage.py migrate
$ python manage.py test
```

## TODO:
0. complain about the lack of supporting HTML5 `Field` sublasses
0. complain about the lack of support for removing `<label>` elements without removing all element `id` attributes
0. complain about how the validation machinery should just reuse the HTML5 `pattern` regex attribute for most validation in the future!
0. develop a better API then the current reinterpretation