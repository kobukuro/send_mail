import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

import os
import base64
import setting.setting as setting

def send_email_by_smtp(smtp_ip,smtp_port,
                       email_from, password,
                       to, cc, bcc, subject,
                       content_type, content, images_in_content,
                       attached_files):
    # region check type of parameters
    assert type(to) == list
    assert type(cc) == list
    assert type(bcc) == list
    assert type(images_in_content) == list
    assert type(attached_files) == list
    # endregion
    msg = MIMEMultipart('related')
    msg['From'] = email_from
    msg['To'] = COMMASPACE.join(to)
    msg['Cc'] = COMMASPACE.join(cc)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(content, content_type))
    if content_type == setting.SMTP_CONTENT_TYPE_HTML:
        if len(images_in_content) > 0:
            for image_in_content in images_in_content:
                msg.attach(image_in_content)
    else:
        raise Exception('content_type input must be html')
    for attached_file in attached_files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(attached_file, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment',
                        filename=os.path.basename(attached_file))
        msg.attach(part)
    server = smtplib.SMTP(smtp_ip+':'+str(smtp_port))
    server.ehlo_or_helo_if_needed()  # 在Server上執行此行要comment掉
    server.starttls()  # 在Server上執行此行要comment掉
    server.ehlo_or_helo_if_needed()
    server.login(email_from, password)  # 在Server上執行此行要comment掉

    server.sendmail(email_from, to + cc + bcc, msg.as_string())
    server.quit()