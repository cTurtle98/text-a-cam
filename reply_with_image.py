'''

text-a-cam project
https://github.com/cTurtle98/text-a-cam

reply_with_image

this function takes an email address as input
it will send an html message to that email containing an image from the pi camera
'''

DEBUG = True

from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes

from picamera import PiCamera
from time import sleep

import smtplib

camera = PiCamera()

IMAGEPATH = "/home/pi/image.jpg"

def reply_with_image(address):

  if DEBUG:
    print("Sending email to " + address)

  if DEBUG:
    print("creating email...")

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

  if DEBUG:
    print("taking picture...")

  print("starting camera")
  camera.start_preview()
  print("waiting for exposure")
  sleep(2)
  print("taking picture")
  camera.capture(IMAGEPATH)
  #camera.close()
  print("closing camera")
  camera.stop_preview()

  if DEBUG:
    print("adding picture to email...")

  with open(IMAGEPATH, 'rb') as img:

    # know the Content-Type of the image
    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

    # attach it
    msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)

  if DEBUG:
    print("retreiving email password from file...")

  f = open("emailpassword.txt")
  emailpassword = f.read()
  f.close()

  if DEBUG:
    print("sending email...")

  smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  smtp.ehlo()
  smtp.login('ciaran.david.farley@gmail.com', emailpassword)

  smtp.sendmail('cam@cturtle98.com', address, msg.as_string())
  smtp.quit()

  if DEBUG:
    print("done")