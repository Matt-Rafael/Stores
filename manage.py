from selenium import webdriver
import time
import json

def get_host_account():
    file = open("config.json", encoding="utf-8")
    account = json.load(file)
    file.close()
    return account["host_name"], account["host_pwd"], account["groups"], account["version"]

def execute_task():
    browser = webdriver.Chrome(r"C:\Users\wcshi\Desktop\Dev\auto\chromedriver.exe")
    browser.get("https://www.linkedin.com/")
    # 定义判断元素是否存在的方法
    def element_exist(css_selector):
        try:
            browser.find_element_by_css_selector(css_selector)
            return True
        except:
            return False
    #从配置文件中加载信息
    host_name, host_pwd, groups, version = get_host_account()
    #打开网页，如果未登录的话，就先登录
    if element_exist("#login-email"):
        login_email = browser.find_element_by_id("login-email")
        login_pwd = browser.find_element_by_id("login-password")
        login_submit = browser.find_element_by_id("login-submit")
        login_email.send_keys(host_name)
        login_pwd.send_keys(host_pwd)
        login_submit.submit()
    #登录成功后的处理
    ele_version = browser.find_element_by_id("ele_version")
    ele_group = browser.find_element_by_id("ele_group")
    ele_export = browser.find_element_by_id("ele_export")
    ele_version.send_keys(version)
    for group in groups:
        ele_group.send_keys(group)
        ele_export.click()
        time.sleep(3) #导出各组的数据





if __name__ == "__main__":
    execute_task()