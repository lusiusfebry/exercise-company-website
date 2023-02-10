import smtplib
import os
def send_email(user_email,topic,message):
    my_email = "febrypythontest@gmail.com"
    password = os.getenv("password_email")

    to_email = f"{my_email}"

    msg = f"Subject: New email from {user_email}\n\nFrom : {user_email}\nTopic: {topic}\n{message}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=to_email,msg=msg)

