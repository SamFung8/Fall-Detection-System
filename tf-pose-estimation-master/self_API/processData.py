from twilio.rest import Client

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import self_API.db as dbAPI 

from PIL import Image 
import imageio
from PIL import Image, ImageSequence

def send_email_message(webcam_id):
    fromaddr = "fyptest2021@gmail.com"
    toaddr = dbAPI.dbGetCareTakerEmailByElderlyId(dbAPI.dbGetElderIdByWebcamId(webcam_id))
       
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr 
      
    # storing the receivers email address  
    msg['To'] = toaddr 
      
    # storing the subject  
    msg['Subject'] = "Fall Detection Message"
      
    # string to store the body of the mail 
    body = "The people is fall!!! \n http://10.106.128.13:9000/video_feed"
      
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
      
    # open the file to be sent  
    filename = "fall.gif"
    attachment = open("C:/xampp/htdocs/web/gif_data/test.gif", "rb") 
      
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
      
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
      
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    s.login(fromaddr, "!abc12345678") 
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
      
    # terminating the session 
    s.quit()
    
	
def img2gif(gifImg, gifName):
    imageio.mimsave('C:/xampp/htdocs/web/gif_data/' + gifName, gifImg, duration=0.3)

    # Output (max) size
    size = 500, 500

    # Open source
    im = Image.open('C:/xampp/htdocs/web/gif_data/' + gifName)

    # Get sequence iterator
    frames = ImageSequence.Iterator(im)

    # Wrap on-the-fly thumbnail generator
    def thumbnails(frames):
        for frame in frames:
            thumbnail = frame.copy()
            thumbnail.thumbnail(size, Image.ANTIALIAS)
            yield thumbnail

    frames = thumbnails(frames)

    # Save output
    om = next(frames) # Handle first frame separately
    om.info = im.info # Copy sequence info
    om.save('C:/xampp/htdocs/web/gif_data/' + 'test.gif', save_all=True, append_images=list(frames), loop = 0)    
	
def send_whatsapp():
	account_sid = 'ACc66aa4c1775de41625fff63d501f1c71'
	auth_token = '67439d7bb74a68815a81d1b39bcdc762'

	# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
	client = Client(account_sid, auth_token)

	# this is the Twilio sandbox testing number
	from_whatsapp_number='whatsapp:+14155238886'
	# replace this number with your own WhatsApp Messaging number
	to_whatsapp_number='whatsapp:+85269998398'

	client.messages.create(body='Plase view your app! Your elderly was fall! ', from_=from_whatsapp_number, to=to_whatsapp_number)
    
    
