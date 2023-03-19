from selenium import webdriver
import time
import os


def get_windows_img():
    """
    把file_path保存到我们项目根目录的一个文件夹.\Screenshots下
    """
    d = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/screenshots/'
    rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screen_name = d + rq + '.png'
    try:
        driver.get_screenshot_as_file(screen_name)
        print(1)
    except NameError as e:
        get_windows_img()


driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
get_windows_img()
driver.close()
