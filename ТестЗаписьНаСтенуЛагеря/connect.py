#!/usr/bin/python
# coding: utf-8
from selenium import webdriver                            
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# общая функция подключения возвращает УРЛ для подключения и Браузер
def create_driver(host='idp7.dev.idpowers.com', port=4444):
    executor_url = 'http://{host}:{port}/wd/hub'.format(
        host=host, port=port)
    return webdriver.Remote(
        command_executor=executor_url, 
        desired_capabilities=DesiredCapabilities.CHROME
    )

