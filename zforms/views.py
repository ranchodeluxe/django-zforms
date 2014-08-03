#
#  django imports
#
from django.views.generic import View, TemplateView, FormView
from django.forms.models import model_to_dict
from django.contrib.sites.models import Site
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.conf import settings


#
#  sys imports
#
import json
import logging
logger = logging.getLogger( __file__ )


#
#  app imports
#
from common.functions.log_traceback import LogTraceback
from forms import DynTestForm

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
        data.update( csrf(request) )
    
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
        data.update( csrf(request) )
    
        if form.is_valid():
            data.update( { 'message' : 'success' } )
            return render_to_response( self.template_name, data )
        else:
            data.update( { 'message' : 'failure' } )
            return render_to_response( self.template_name, data )


