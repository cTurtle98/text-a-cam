'''

text-a-cam project

https://github.com/cTurtle98/text-a-cam

this is the code that checks gmail for new messages to this program

will return the address in the from field when it gets an email

'''

import json

def recieve_email():



def translate('sms_email'):

  f = open('sms-to-mms.json')
  translatiion_dict = json.load(f)
  f.close()

  emailparts = sms_email.split('@', 2)

  print (emailparts)

  #if emailparts[2] in translatiion_dict:
   # return translatiion_dict[emailparts[2]]