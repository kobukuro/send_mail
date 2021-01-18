import functions.email.send_email as send_email
import setting.setting as setting
from email.mime.image import MIMEImage

if __name__ == '__main__':
    # region 寄信
    mail_content = """<p style="font-size:16px">
                        test
                      </p>
                   """
    # 添加image到content html
    image_names = ['image1', 'image2']
    image_paths = ['images\\image1.png', 'images\\image2.png']
    image_objs = [{'image_name':'image1',
                    'image_path':'images\\image1.png'},
                  {'image_name': 'image2',
                   'image_path': 'images\\image2.png'}
                  ]
    msgImage_list = []
    for image_obj in image_objs:
        mail_content += '<img src="cid:' + image_obj['image_name'] + '"><br>'
        # region 加入圖片至msgImage_list
        fp = open(image_obj['image_path'], 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<' + image_obj['image_name'] + '>')
        msgImage_list.append(msgImage)
        # endregion
    send_email.send_email_by_smtp(smtp_ip=setting.SMTP_IP,
                                  smtp_port=setting.SMTP_PORT,
                                  email_from=setting.EMAIL_FROM,
                                  password=setting.EMAIL_PASSWORD,
                                  to=[],
                                  cc=[],
                                  bcc=[],
                                  subject='test',
                                  content_type=setting.SMTP_CONTENT_TYPE_HTML,
                                  content=mail_content,
                                  images_in_content=msgImage_list,
                                  attached_files=[])
    # endregion