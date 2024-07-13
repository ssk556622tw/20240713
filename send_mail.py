import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "ssk556622tw@gmail.com" #設定寄件人
receiver = ["A99228@capital.com.tw","ssk556622tw@gmail.com"]#設定收件人


for receivers in receiver:
    msg = MIMEMultipart() #設定mail物件
    msg["From"] = sender #設定寄件人
    msg["To"] = receivers   #設定收件人
    header = Header("Test Send Email","utf-8") #設定內容格式
    msg["Subject"] = header.encode() #將編碼後的header裝回物件中

    body = "this is email send from python" #寄件內容
    msg.attach(MIMEText(body)) #將寄件內容放至物件中
    # mbody = MIMEText(body)
    # msg.attach(mbody)  13行是14~15行的縮寫
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
    #With 從...連線至...(用SSL連線至Gmail)465是GMAIL的PORT口 as 伺服器
    #context=ssl_context 的意思是我不曉得context原本的格式，強制改成ssl連線
        server.login(sender,"gfpc knge rivf awjk")
        server.sendmail(sender,receivers,msg.as_string())
    print("success sned email")    