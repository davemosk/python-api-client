Python API Client
=================

See http://www.meetup.com/meetup_api/clients/ as a reference.

Sample use:

from meetup import meetup_api_client as mac
from meetup import *

#
# in script to get set up authentication ...
#

  try:
    yredir = [URL to your site which will accept the redirect and get the oauth code]
    mucli = mac.MeetupOAuth(MEETUP_OAUTH_CONSUMER_KEY, MEETUP_OAUTH_CONSUMER_SECRET)
    meetup_session = mucli.new_session()
    meetup_session.fetch_request_token(yredir)
    request.session['meetup_session'] = {}
    request.session['meetup_session']['request_key'] = meetup_session.request_token.key
    request.session['meetup_session']['request_secret'] = meetup_session.request_token.secret
    yauthurl = meetup_session.get_authorize_url()
  except:    
    return render_to_response('meetup/error.html',{'message': "meetup authentication setup failed", 'additional_info': sys.exc_info()})
  return redirect(yauthurl)

#
# in script that gets redirected to -
#

   try: 
     mucli = mac.MeetupOAuth(MEETUP_OAUTH_CONSUMER_KEY, MEETUP_OAUTH_CONSUMER_SECRET)
     request_key =  request.session['meetup_session']['request_key']
     request_secret = request.session['meetup_session']['request_secret']
     meetup_session = mucli.new_session(request_key=request_key, request_secret=request_secret)
     memberid = meetup_session.fetch_access_token(verifier)
     request.session['meetup_session']['access_key'] = meetup_session.access_token.key
     request.session['meetup_session']['access_secret'] = meetup_session.access_token.secret   
  except:
    render_to_response('meetup/error.html',{'message': "meetup authentication failed", 'additional_info': sys.exc_info()})
  try:
    f = mucli.get_members(member_id=memberid, sess=meetup_session)
     
  except:
    render_to_response('meetup/error.html',{'message': "get_members meetup authentication failed", 'additional_info': sys.exc_info()})

  g = mucli.get_groups(member_id=memberid,sess=meetup_session)
  groupname = g.results[0].name
  events = g.results[0].get_events(mucli,status="past,upcoming",sess=meetup_session)

  members = mucli.get_members(group_id=groupid, sess=meetup_session)
  mpurl = members.results[3].photo_url

 

... and so on ...



This branch owes a lot to the following which it has unashamedly stolen bits from:


The orignial:
https://github.com/meetup/python-api-client

Dwight Gunning
https://github.com/dwightgunning/meetup-api

Jofusa
https://github.com/jofusa/python-api-clients

The functionality added is mainly to use version 2 of the API, as well as handle bad unicode coming back from Meetup without dying.