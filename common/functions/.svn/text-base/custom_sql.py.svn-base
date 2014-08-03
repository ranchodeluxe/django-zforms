import logging
logger = logging.getLogger( __file__ )

def CustomSQLQuery( sql, args ):
    from django.db import connection
    cursor = connection.cursor()

    # Data retrieval operation - no commit required
    cursor.execute( sql, args )
    rows = cursor.fetchall()
    cursor.execute( "COMMIT" )

    return rows

def CustomStoredProcedureQuery( sql, args ):
    
    from django.db import connection
    from datetime import datetime
    from time import mktime

    referer = 'ref%s' % int( mktime( datetime.now().timetuple() ) )
    new_args = ( referer, ) + args
    #logger.debug( "Referer: %s" % referer )
    
    cursor = connection.cursor()
    cursor.execute( "BEGIN" )
    cursor.execute( sql % new_args )
    cursor.execute( "FETCH ALL IN %s" % referer )
    results = cursor.fetchall()
    cursor.execute( "COMMIT" )
    
    return results