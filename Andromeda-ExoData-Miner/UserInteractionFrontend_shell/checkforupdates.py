from datetime import *
import smtplib
import os
from email.mime.text import MIMEText

def sendEmail():
    '''
    Sends an email to Hanno Rein.
    :return: None
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('team15andromeda@gmail.com', 'andromeda15')
    server.sendmail('team15andromeda@gmail.com', 'hanno.rein@utoronto.ca', "new oec update")
    server.close()
# read the date of last update
try:
    file_lastupdate = open('lastupdate.txt', 'r')
    old_date = file_lastupdate.readline()
    # compare to today; if unequal, then there was a change
    if date.today() != old_date and not os.path.isfile('emailedalready.txt'):
        sendEmail()
        # create a file "emailedalready" to show that we already emailed Hanno regarding this update
        file_write_emailedalready = open('emailedalready.txt', 'w')
        file_write_emailedalready.close()
    file_lastupdate.close()
except FileNotFoundError:
    pass




