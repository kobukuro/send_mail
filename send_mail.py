import functions.email.send_email as send_email
import setting.setting as setting
from email.mime.image import MIMEImage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date, datetime, timedelta

if __name__ == '__main__':
    # # region 寄信
    # mail_content = """<p style="font-size:16px">
    #                     test
    #                   </p>
    #                """
    # # 添加image到content html
    # image_names = ['image1', 'image2']
    # image_paths = ['images\\image1.png', 'images\\image2.png']
    # image_objs = [{'image_name':'image1',
    #                 'image_path':'images\\image1.png'},
    #               {'image_name': 'image2',
    #                'image_path': 'images\\image2.png'}
    #               ]
    # msgImage_list = []
    # for image_obj in image_objs:
    #     mail_content += '<img src="cid:' + image_obj['image_name'] + '"><br>'
    #     # region 加入圖片至msgImage_list
    #     fp = open(image_obj['image_path'], 'rb')
    #     msgImage = MIMEImage(fp.read())
    #     fp.close()
    #     msgImage.add_header('Content-ID', '<' + image_obj['image_name'] + '>')
    #     msgImage_list.append(msgImage)
    #     # endregion
    # send_email.send_email_by_smtp(smtp_ip=setting.SMTP_IP,
    #                               smtp_port=setting.SMTP_PORT,
    #                               email_from=setting.EMAIL_FROM,
    #                               password=setting.EMAIL_PASSWORD,
    #                               to=[],
    #                               cc=[],
    #                               bcc=[],
    #                               subject='test',
    #                               content_type=setting.SMTP_CONTENT_TYPE_HTML,
    #                               content=mail_content,
    #                               images_in_content=msgImage_list,
    #                               attached_files=[])
    # # endregion

    target_url = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article'
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.set_window_position(0, 0)
    driver.get(target_url)
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div.page-wrapper.document-page > div.titlebar-container > h1')))
    driver.set_window_size(1920, 1080)
    # scroll_height = driver.execute_script(
    #     'return document.querySelector("body > div.content-container.fr-quick-border-layout.ui-state-enabled > div.fr-quick-adaptive-layout.ui-state-enabled").scrollHeight')
    # driver.set_window_size(1920, scroll_height)
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    image_name_with_ext = '{0}_{1}.png'.format('test', now)
    image_path = image_name_with_ext
    driver.save_screenshot(image_path)
    driver.quit()