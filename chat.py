from httplib2 import Http
from json import dumps

def main(msg):
    url = '<hangouts url>'
    bot_message = {
        'text' : msg}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )


while(True):

    msg = raw_input("Enter msg:")
    main(msg)