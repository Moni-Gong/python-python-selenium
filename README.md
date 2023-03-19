# python-python-selenium
轻量的自动化框架，python+selenium+unittest+HtmlTestRunner

路径说明：config：配置文件以及数据、logs：日志存放、reports：报告生成地址、screenshots：截图存放、src：源码

src下：base：底层通用功能，click、send_keys等函数。pages：单独页面功能的封装，由底层通用功能+数据配置组成。test_case：用例初始化与用例存放。test_run：批量执行用例




使用方法：运行  src/test_run/testrunner.py

前置条件1：注册并登录这个网址http://txapi.cn/console

前置条件2：打开http://txapi.cn/console，页面中查找自己的token码


前置条件3：config/查询目标.csv  到这个文件下替换自己的token码

前置条件4：src\test_case\test_base.py  代码里，替换自己的谷歌浏览器，具体教程：https://blog.csdn.net/qq_45587822/article/details/104410906

前置条件5：安装selenium库、安装html-testRunner库

