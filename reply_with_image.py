'''

text-a-cam project
https://github.com/cTurtle98/text-a-cam

reply_with_image

this function takes an email address as input
it will send an html message to that email containing an image from the pi camera
'''

from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes

from picamera import PiCamera
from time import sleep

import smtplib

camera = PiCamera()

def reply_with_image(address):

  msg = EmailMessage()

  msg['Subject'] = ''
  msg['From'] = 'cTurtle98 camera <cam@cTurtle98.com>'
  msg['To'] = address

  msg.set_content('There should be an image here')

  image_cid = make_msgid(domain='cturtle98.com')

  msg.add_alternative("""\
<html>
    <body>
        <img src="cid:{image_cid}">
    </body>
</html>
""".format(image_cid=image_cid[1:-1]), subtype='html')

  camera.start_preview()
  sleep(2)
  camera.capture('/dev/shm/image.jpg')
  camera.stop_preview()

  with open('/dev/shm/image.jpg', 'rb') as img:

    # know the Content-Type of the image
    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

    # attach it
    msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)

  f = open("emailpassword.txt")
  emailpassword = f.read()
  f.close()

  smtp = smtplib.SMTP()
  smtp.connect('smtp.gmail.com')
  smtp.login('cam@cturtle98.com', emailpassword)
  smtp.sendmail(cam@cturtle98.com, address, msg.as_string())
  smtp.quit()