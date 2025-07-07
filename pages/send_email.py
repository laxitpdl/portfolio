import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "poudellakshit0@gmail.com"
password = "jeopmqeeijvdbigw"

receiver = "poudellakshit0@gmail.com"
context = ssl.create_default_context()

message = """\ Subject: Hi!
How was your experence? """
with smtplib.SMTP_SSL(host, port, context=context) as  server:
    server.login(username, password)
    server.sendmail(username, receiver, message )


