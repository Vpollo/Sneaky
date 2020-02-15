import re
import imaplib
import email
import getpass
import datetime
import json
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
    time = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    file1 = open(f"{time}.txt","w") 
    title = list()
    for num in numbers[0].split():
        typ, data=mail.uid('fetch',  num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        body = get_first_text_block(msg)
        file1.write(body)
        title.append(msg['SUBJECT'])
        # print(msg['SUBJECT'])
    file1.close()
    return (f"{time}.txt", title)

def parse():
    txt, subjectRes = getEmail()
    textfile = open(txt, 'r')
    filetext = textfile.read()
    textfile.close()
    location = re.compile(r'[A-Z][a-z]+\s[RH]\w+\s[A-Z]?\d+')
    date = re.compile(r'(\d\d?/\d\d?)')
    time = re.compile(r'\d:\d\d\w?\w?-\d:\d\d\w\w')
    locationRes = re.findall(location, filetext)
    timeRes = re.findall(time, filetext)
    dateRes = re.findall(date, filetext)
    res = dict()
    for i in range(len(subjectRes)):
        res[subjectRes[i]] = {'Location': 0, 'Date': 0, 'Time': 0}
        res[subjectRes[i]]['Location'] = locationRes[i]
        res[subjectRes[i]]['Date'] = dateRes[i]
        res[subjectRes[i]]['Time'] = timeRes[i]
    # print (res)
    return res

def processData():
    resultDict = parse()
    resultJSON = json.dumps(resultDict)
    # print (resultJSON)
    return resultJSON

processData()