import smtplib
 
# list of email_id to send the mail
li = ["ssganvir08@gmail.com", "sayalimane8698@gmail.com"]
 
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("gayatrisjadhav07@gmail.com", "qwhkdpwuprgwuoxu")
    message = "nalayk....bawlat"
    s.sendmail("gayatrisjadhav07@gmail.com", dest, message)
    s.quit()
