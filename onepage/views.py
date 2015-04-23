# Create your views here.
from django.core.context_processors import csrf
from django.http import HttpResponse
import json

def alert_mail(destinataire, name, mail, message):
    # Import smtplib for the actual sending function
    import smtplib
    # Import the email modules we'll need
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.MIMEBase import MIMEBase
    from email import Encoders

    # Open a plain text file for reading. For this example, assume that
    # the text file contains only ASCII characters.
    #fp = open(textfile, 'rb')
    # Create a text/plain message
    #msg = MIMEText("Attention!!! test")
    html = """\
             <html>
               <head></head>
               <body>
                  Emetteur:<b> %s </b><br>
                  Email : <b> %s </b><br>
                  Message:<b> %s </b>
               </body>
             </html>
             """ % (str(name), str(mail), str(message))

    msg = MIMEMultipart('alternative')
    content = MIMEText(html, 'html')
    msg.attach(content)
 
    #fp.close()
    #me = "alerte.raspberry.esigetel@gmail.com"
    me = "mywebsitepsav@gmail.com"
    you = "angebouabre@gmail.com" 
    msg['Subject'] = '*** MESSAGE DU WEBSITE ***'
    msg['From'] = "MYWEBSITE"
    msg['To'] = you
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo
    s.login(me,"")
    s.sendmail(me, [you], msg.as_string())
    s.quit()


def sendMail(request):
    if request.is_ajax():
        data = request.GET 
        name = data["name"]
        mail = data["mail"]
        message = data["mess"]
        alert_mail("angebouabre@gmail.com", name, mail, message)
    status = json.dumps({'status':'ok'})
    return HttpResponse(status, content_type='application/json')
