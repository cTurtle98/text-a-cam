'''

text-a-cam project
https://github.com/cTurtle98/text-a-cam

reply_with_image

this function takes an email address as input
it will send an html message to that email containing an image from the pi camera
'''

DEBUG = True

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from picamera import PiCamera
from time import sleep

camera = PiCamera()

IMAGEPATH = "/home/pi/image.jpg"

def reply_with_image(address):

  if DEBUG:
    print("Sending email to " + address)

  if DEBUG:
    print("creating email...")

  msg = MIMEMultipart("related")
  msg['Subject'] = ''
  msg['From'] = 'cTurtle98 camera <cam@cTurtle98.com>'
  msg['To'] = address
  msg.preamble = 'This is a multi-part message in MIME format.'

  msgAlternative = MIMEMultipart('alternative')
  msg.attach(msgAlternative)

  msgAlternative.attach(MIMEText("""\
<html>
    <body>
        <img src="cid:the_image">
    </body>
</html>
""", 'html'))

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

  f = open(IMAGEPATH, 'rb')
  msg.attach(MIMEImage(f.read()).add_header('Content-ID', '<the_image>'))
  f.close()

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