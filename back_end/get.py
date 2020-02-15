import imaplib
import email
import getpass
import datetime
# Cite From https://gist.github.com/nickoala/569a9d191d088d82a5ef5c03c0690a02
def get_first_text_block(msg):
    maintype = msg.get_content_maintype()
    if maintype == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return msg.get_payload()
def getEmail():
    username = 'foodcmu@gmail.com'
    password = 'tartanhacks2020'
    mail = imaplib.IMAP4_SSL('imap.gmail.com') # EMAIL SERVER
    mail.login(username, password)
    mail.select("inbox")
    sinceDate = (datetime.date.today() - datetime.timedelta(5)).strftime("%d-%b-%Y")
    result, numbers = mail.uid('search', None, 
            '(SENTSINCE {date} FROM "cmu.edu" BODY "food")'.format(date=sinceDate))
    result, numbers1 = mail.uid('search', None, 
            '(SENTSINCE {date} FROM "cmu.edu" BODY "pizza")'.format(date=sinceDate))
    time = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    file1 = open(f"{time}.txt","w") 
    # food
    for num in numbers[0].split():
        typ, data=mail.uid('fetch',  num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        body = get_first_text_block(msg)
        file1.write(body)
        print(msg['SUBJECT'])
    # pizza
    for num1 in numbers1[0].split():
        typ1, data1=mail.uid('fetch',  num1, '(RFC822)')
        msg1 = email.message_from_bytes(data1[0][1])
        body1 = get_first_text_block(msg1)
        file1.write(body1)
        print(msg1['SUBJECT'])
    file1.close()
getEmail()