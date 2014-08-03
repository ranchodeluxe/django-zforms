from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from common.functions.log_traceback import LogTraceback

import logging
logger = logging.getLogger( __file__ )

def SendEmail( template_name, content, email_to, email_from, subject, email_bcc ):
    '''
    Send Email
     - will always send text message
     - if html version exists, it will send that also
    '''

    try:
        plaintext = get_template( '%s.txt' % template_name )
        text_content = plaintext.render( content )

        # create msg object and send email
        msg = EmailMultiAlternatives( subject, \
                                      text_content, \
                                      email_from, \
                                      [ email_to ])

        if email_bcc:
            msg.bcc = email_bcc

        try:
            html      = get_template( '%s.html' % template_name )
            html_content = html.render( content )

            msg.attach_alternative( html_content, "text/html" )

        except Exception, args:
            logger.debug( 'HTML email failure: %s, %s' % ( Exception, args ) )
            LogTraceback()

        msg.send()

        logging.info( '%s email sent from [%s] to [%s]' % \
                        ( template_name, email_from, email_to ) )

        return

    except Exception, args:
        logger.debug( 'Plaintext email failure: %s, %s' % ( Exception, args ) )
        LogTraceback()

        return
