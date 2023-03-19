from src.base.common import BasePage
from src.base.Logger import Logger

logger = Logger(logger='query').getlog()


class query(BasePage):
    # 定位器
    # 疑问，继承后定义属性不饿能用init？
    filename = '查询目标.csv'

    token_xpath = '//*[@id="0"]/div[2]/div/textarea'
    xitong_xpath = '//*[@id="1"]/div[2]/div/textarea'
    hero_xpath = '//*[@id="2"]/div[2]/div/textarea'
    click_query_xpath = '//*[@id="app"]/div/section/main/div[1]/div[2]/div/div[1]/div[4]/button'
    info_sheng_xpath = '//*[@id="app"]/div/section/main/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/span/div[2]/span[3]/div[8]/span[2]/span[2]'
    info_score_xpath = '//*[@id="app"]/div/section/main/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/span/div[1]/span[1]'


    def token_input(self):
        data = self.get_scv(self.filename, 1)
        print(data)
        self.wait(self.token_xpath, 10, 0.2)
        self.clear(self.token_xpath)
        self.send_keys1(self.token_xpath, data[0])
        print(data)

    def xitong_input(self):
        data = self.get_scv(self.filename, 1)
        self.clear(self.xitong_xpath)
        self.send_keys1(self.xitong_xpath, data[1])
        print(data)

    def hero_input(self):
        data = self.get_scv(self.filename, 1)
        self.clear(self.hero_xpath)
        self.send_keys1(self.hero_xpath, data[2])
        self.sleep(1.5)
        print(data)

    def click_query(self):
        self.click(self.click_query_xpath)

    def get_sheng_value(self):
        sheng = self.get_value(self.info_sheng_xpath)
        print(sheng)
        logger.info(sheng)
        return sheng

    def get_score_value(self):
        score = self.get_value(self.info_score_xpath)
        print(score)
        logger.info(score)
        return score

    def info_score_webwait(self):
        self.wait(self.info_score_xpath, 10, 0.2)

