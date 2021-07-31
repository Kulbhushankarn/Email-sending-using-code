import smtplib
#This code is written by Kulbhushan Karn
to=input("Enter To Email-id")
sub=input("Enter subject")
Meg=input("Enter Message")

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("karnkulbhushan@gmail.com","rahulkarn")

mymessage="subject:{}\n\n{}".format(sub,Meg)
s.sendmail("karnkulbhushan@gmail.com",to,mymessage)
print("Mail Send Successfully")
