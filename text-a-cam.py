'''
text-a-cam project

https://github.com/cTurtle98/text-a-cam

this is the main orchestration program
'''

from reply_with_image import reply_with_image

print("what email would you like to send an email to?")

email = input()

reply_with_image(email)