# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from connect import create_driver

class FirstTest:

     addr = 'http://artek.org'

     # insert_query_text - Процедура заходит на артек, находит элемент query и записывает в него текст - lol
     def insert_query_text(self):
         # Подключение
        driver = create_driver (host='idp7.dev.idpowers.com', port=32825)
        driver.get(self.addr)
        print "Тестируемый сайт:"
        print self.addr
        print "Тест страницы:"
        title = driver.title
         # Для манипуляции строками с кириллицей, перед строкой u
        if(title == u'МДЦ «Артек»'):
           print u'Главная страница ' + title
        else:
           print driver.title
        FormAutorxPath = '/ html / body / div[1] / div[2] / header / div[1] / div[3] / div[2] / a'
        log = 'r-sasha@children.ru'
        pas = '66666666'
        logxPath = '/html/body/div[1]/div[2]/form/div[1]/input'
        passxPath = '/html/body/div[1]/div[2]/form/div[3]/input'
        form = driver.find_element_by_xpath(FormAutorxPath)
        form.click ()
        login = driver.find_element_by_xpath(logxPath)
        password = driver.find_element_by_xpath(passxPath)
        login.send_keys(log)
        password.send_keys(pas)
        enter = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/button')
        enter.click()
        enterToArtek = '/ html / body / div[1] / div[2] / div[3] / form[1] / button'
        enterToArtekButton = driver.find_element_by_xpath(enterToArtek)
        enterToArtekButton.click()
        menuPath = '/html/body/div[1]/div/div[2]/div/div[2]'
        menu = driver.find_element_by_xpath(menuPath)
        menu.click()
        camp = '/html/body/div[1]/div/div[2]/div/div[3]/div[2]/a'
        campButtn = driver.find_element_by_xpath(camp)
        time.sleep (7)
        campButtn.click()
        inputPath = '/html/body/div[2]/div[2]/div/main/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div[1]'
        input = driver.find_element_by_xpath (inputPath)
        input.send_keys('lol kek')
        pathButtnEnter = '/html/body/div[2]/div[2]/div/main/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/button'
        BtnEnterCamp = driver.find_element_by_xpath (pathButtnEnter)
        BtnEnterCamp.click()
        time.sleep(300)
        # elem.clear()
        driver.quit()
     def __init__(self):
       self.insert_query_text()

       class TestEvent:

           addr = 'http://artek.org'

           # insert_query_text - Процедура заходит на артек, находит элемент query и записывает в него текст - lol
           def insert_query_text(self):
               # Подключение
               driver = create_driver (host='idp7.dev.idpowers.com', port=32825)
               driver.get (self.addr)
               print "Тестируемый сайт:"
               print self.addr
               print "Тест страницы:"
               title = driver.title
               # Для манипуляции строками с кириллицей, перед строкой u
               if (title == u'МДЦ «Артек»'):
                   print u'Главная страница ' + title
               else:
                   print driver.title
               FormAutorxPath = '/ html / body / div[1] / div[2] / header / div[1] / div[3] / div[2] / a'
               log = 'r-sasha@children.ru'
               pas = '66666666'
               logxPath = '/html/body/div[1]/div[2]/form/div[1]/input'
               passxPath = '/html/body/div[1]/div[2]/form/div[3]/input'
               form = driver.find_element_by_xpath (FormAutorxPath)
               form.click ()
               login = driver.find_element_by_xpath (logxPath)
               password = driver.find_element_by_xpath (passxPath)
               login.send_keys (log)
               password.send_keys (pas)
               enter = driver.find_element_by_xpath ('/html/body/div[1]/div[2]/form/button')
               enter.click ()
               enterToArtek = '/ html / body / div[1] / div[2] / div[3] / form[1] / button'
               enterToArtekButton = driver.find_element_by_xpath (enterToArtek)
               enterToArtekButton.click ()
               menuPath = '/html/body/div[1]/div/div[2]/div/div[2]'
               menu = driver.find_element_by_xpath (menuPath)
               menu.click ()
               camp = '/html/body/div[1]/div/div[2]/div/div[3]/div[2]/a'
               campButtn = driver.find_element_by_xpath (camp)
               time.sleep (7)
               campButtn.click ()
               inputPath = '/html/body/div[2]/div[2]/div/main/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div[1]'
               input = driver.find_element_by_xpath (inputPath)
               input.send_keys ('lol kek')
               pathButtnEnter = '/html/body/div[2]/div[2]/div/main/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/button'
               BtnEnterCamp = driver.find_element_by_xpath (pathButtnEnter)
               BtnEnterCamp.click ()
               time.sleep (300)
               # elem.clear()
               driver.quit ()

           def __init__(self):
               self.insert_query_text ()

