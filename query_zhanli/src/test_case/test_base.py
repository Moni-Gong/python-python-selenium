import unittest
from selenium import webdriver


class Test_base(unittest.TestCase):
    def setUp(self):
        data = r'C:\Users\7\AppData\Local\Google\Chrome\User Data'
        option = webdriver.ChromeOptions()
        option.add_argument(f'--user-data-dir={data}')
        self.driver = webdriver.Chrome(options=option)  # 设置Chrome浏览器，且获取本地Chrome的用户数据
        self.driver.implicitly_wait(10)  # 设置隐式等待
        self.driver.maximize_window()  # 最大化浏览器

    def TearDown(self):
        self.quit()


if __name__ == '__main__':
    unittest.main()
