import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "asadafzal353@gmail.com"
    password = "dfsqptbjrwdeqbct"

    receiver = "asadafzal680@gmail.com"
    context = ssl.create_default_context()
   

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    content = """\
    Subject: Hi!
    This is a dummy email!
    Hope that you would not be annoyed by it!!!
    """
    send_email(message=content)

