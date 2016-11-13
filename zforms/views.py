#
#  django imports
#
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import FormView

#
#  sys imports
#
import logging
logger = logging.getLogger( __file__ )


#
#  app imports
#
from forms import DynTestForm

@method_decorator(csrf_exempt, name='dispatch')
class zFormView( FormView ):

    http_method_names = [ 'get', ]
    template_name = 'forms.html'
    form_class = DynTestForm
    http_method_names = [ 'get', 'post', ]


    def get( self, request, *args, **kwargs ):

        #
        #  context data
        #
        data = {
            'page_name': 'Forms',
            'form' : self.form_class(),
            'link' : reverse( 'forms-view' )
        }
        #data.update( request )
    
        return render_to_response( self.template_name, data )


    def post( self, request, *args, **kwargs ):

        logger.debug( "[ POST ]: %s" % request.POST )
        form = DynTestForm( request.POST )
        
        #
        #  context data
        #
        data = {
            'page_name': 'Forms',
            'form' : form,
            'link' : reverse( 'forms-view' )
        }
        #$data.update( request )
    
        if form.is_valid():
            data.update( { 'message' : 'success' } )
            return render_to_response( self.template_name, data )
        else:
            data.update( { 'message' : 'failure' } )
            return render_to_response( self.template_name, data )


