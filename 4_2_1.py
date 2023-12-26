import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, from_email, from_password, to_email):
  '''
  Функция отправляет письмо на указанную почту.
  subject(str): тема письма;
  message(str): текст письма;
  from_email(str): адрес отправителя;
  from_password(str): пароль отправителя;
  to_email(str): адрес получателя.
  
  '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    print(from_email, from_password)

    server.login(from_email, from_password)

    msg.attach(MIMEText(message, 'plain'))
    server.send_message(msg)

    server.quit()
    print('Email sent successfully!')

s = 'Тестовое сообщение'
mess = 'Это тестовое сообщение! Все получилось!'
from_1 = 'the.nat.cool@gmail.com'
from_2 = '****************' # пароль изменен в целях безопасности
to_em = 'krinj404@yandex.ru'


send_email(s, mess, from_1, from_2, to_em)
