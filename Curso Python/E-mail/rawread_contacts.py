from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Função para ler os contatos do arquivo de texto
# e retornar a lista de nomes e emails
def get_contacts(filename):
    names=[]
    emails=[]
    with open(filename,mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names,emails

def read_template(filename):
    with open(filename,mode='r', encoding='utf-8') as template_file:
        template_file_content=template_file.read()
    return Template(template_file_content)

# Configurando SMTPserver
s=smtplib.SMTP(host='smtp.gmail.com',port=587)
s.starttls()
MY_ADDRESS='gpoianibarcellos@gmail.com'
MY_PASS='dunGeon@01'
s.login(MY_ADDRESS,MY_PASS)

names, emails= get_contacts('mycontacts.txt')
message_template=read_template('message.txt')

for name, email in zip(names,emails):
    msg=MIMEMultipart() # criando a msg
    message=message_template.substitute(PERSON_NAME=name.title())
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']='Isto é um teste do Poiani!'

    msg.attach(MIMEText(message,'plain'))

    s.send_message(msg)

    del msg