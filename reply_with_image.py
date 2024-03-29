'''

text-a-cam project
https://github.com/cTurtle98/text-a-cam

reply_with_image

this function takes an email address as input
it will send an html message to that email containing an image from the pi camera
'''

DEBUG = False

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from picamera import PiCamera
from time import sleep

camera = PiCamera()

IMAGEPATH = "/home/pi/image.jpg"

def reply_with_image(address):

  if DEBUG:
    print("Sending email to " + address)

  if DEBUG:
    print("creating email...")

  msg = MIMEMultipart()
  msg['Subject'] = ''
  msg['From'] = 'cTurtle98 camera <cam@cTurtle98.com>'
  msg['To'] = address
  msg.preamble = 'text-a-cam reply message'

  if DEBUG:
    print("taking picture...")

  if DEBUG:
    print("starting camera")

  camera.start_preview()

  if DEBUG:
    print("waiting for exposure")

  sleep(2)

  if DEBUG:
    print("taking picture")
  
  camera.capture(IMAGEPATH)
  camera.stop_preview()

  if DEBUG:
    print("adding picture to email...")

  f = open(IMAGEPATH, 'rb')
  msgImage = MIMEImage(f.read())
  msgImage.add_header('Content-ID', '<0>')
  msg.attach(msgImage)
  f.close()

  if DEBUG:
    print("retreiving email password from file...")

  f = open("emailpassword.txt")
  emailpassword = f.read()
  f.close()

  if DEBUG:
    print("sending email...")
    #print(msg)


  smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  smtp.ehlo()
  smtp.login('ciaran.david.farley@gmail.com', emailpassword)
  smtp.sendmail('cam@cturtle98.com', address, msg.as_string())
  smtp.quit()

  if DEBUG:
    print("done")