import os 
import math 
import random
import smtplib

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random()* 10)]
    
    otp = OTP + "is your OTP"
    msg = otp 
    
    
    s= smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    
    s.login("Your gmail account","Your app password")
    emailid = input("Enter your email")
    s.sendmail("&&&&&&&&&",emailid,msg)
    
    a = input("Enter your OTP >>:")
    if a == OTP:
        print("Verified")
    else:
        print("Please check your OTP again)
              