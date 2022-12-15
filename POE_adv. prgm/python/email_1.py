from smtplib import*
import smtplib,ssl
obj=smtplib.SMTP_SSL("smtp.gmail.com",465)
obj.login("gayatrisjadhav07@gmail.com","adrexcywftlmzeuc")
obj.sendmail("gayatrisjadhav07@gmail.com","sayalimane8698@gmail.com","Hiii nalayk tuz ky zalay sgla amche vande ahet")
obj.quit()
