from test_base import Test_base
from src.pages.query_page import query

# 打开网页发现没有cookie数据，这也是要解决的，后来发现在创建webdriver时可以解决


class chaxun(Test_base):
    def test_2query(self):
        q = query(self.driver)
        q.open('http://txapi.cn/online_test')
        q.token_input()  # token码输入
        q.xitong_input()  # 系统输入
        q.hero_input()  # 英雄名称输入
        q.click_query()  # 点击查询

        # q.open('http://txapi.cn/online_test')
        q.info_score_webwait()  # 等待省战力分数的出现
        print('查询成功')

        q.get_sheng_value()  # 获取省份的值
        q.get_score_value()  # 获取战力的值
        q.get_windows_img()
        print('获取成功')




