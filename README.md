AsciiSkype
==========
Words words text text


API
===

use get.py from another program, it abstracts this!!

### /

initiate call, should return "asciipe 0" if theres an asciipe server, with version 0

### /get/frame/

returns an ascii frame, with \n as linebreaks

### /get/user/

returns the user name


Using GET.py
------------

get.py -ip IP:HOST request

where request is init to see if the remote is asciipe

or request is any of the following

### frame

gets the ascii text of the next frame

### user

gets the user profile (right now just a username)

### sound

gets a url to a sound stream
