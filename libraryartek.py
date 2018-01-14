# coding: utf-8
import json
import time

import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from connect import create_driver
from selenium.webdriver.support import expected_conditions as ec

import urllib


class element_to_be_clicked(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = EC.visibility_of_element_located(self.locator)(driver)
        try:
            element.click()
            return element
        except:
            return False


'''
Класс FirstTest
Цикл действий:
1)заходим на артек.орг
2)авторизуемся за вожатого
3) вводим в верхнюю строку поиска значение lol kek
Атрибуты класса:
1)addr = 'http://artek.org'
Содержит УРЛ тестируемого ресурса
Методы класса:
1)def insert_query_text(self)
Описание методов:
Пdef insert_query_text(self) - роцедура внутри класса,
которая реализует весь цикл действий для реализации теста
Конструкторы класса
1)def __init__(self):
Данный тест не проходил рефакторинг
'''
class FirstTest:
    addr = 'http://artek.org'

    # insert_query_text - Процедура заходит на артек, находит элемент query и записывает в него текст - lol
    def insert_query_text(self):
        # Подключение
        driver = create_driver (host='idp7.dev.idpowers.com', port=32779)
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
        FormAutorxPath = '/html/body/div[1]/div[2]/header/div[1]/div[3]/div[2]/a'
        log = 'r-sasha@children.ru'
        pas = '66666666'
        logxPath = '/html/body/div[1]/div[2]/form/div[1]/input'
        passxPath = '/html/body/div[1]/div[2]/form/div[3]/input'
        form = driver.find_element_by_xpath(FormAutorxPath)
        form.click()
        login = driver.find_element_by_xpath(logxPath)
        password = driver.find_element_by_xpath(passxPath)
        login.send_keys(log)
        password.send_keys(pas)
        enter = driver.find_element_by_xpath ('/html/body/div[1]/div[2]/form/button')
        enter.click ()
        enterToArtek = '/html/body/div[1]/div[2]/div[3]/form[1]/button'
        enterToArtekButton = driver.find_element_by_xpath(enterToArtek)
        enterToArtekButton.click()
        menuPath = '/html/body/div[1]/div/div[2]/div/div[2]'
        menu = driver.find_element_by_xpath(menuPath)
        menu.click()
        camp = '/html/body/div[1]/div/div[2]/div/div[3]/div[2]/a'
        campButtn = driver.find_element_by_xpath(camp)
        time.sleep(7)
        campButtn.click()
        inputPath = '/html/body/div[2]/div[2]/div/main/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div[1]'
        input = driver.find_element_by_xpath(inputPath)
        input.send_keys('lol kek')
        pathButtnEnter = '/html/body/div[2]/div[2]/div/main/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/button'
        BtnEnterCamp = driver.find_element_by_xpath(pathButtnEnter)
        BtnEnterCamp.click()
        time.sleep(300)
        # elem.clear()
        driver.quit()

    def __init__(self):
        self.insert_query_text()

'''
Класс TestEvent.
Атрибуты:
1)addr = 'http://artek.org'
УРЛ тестируемого ресурса
Методы:
def test(self, driver):
Параметры:
driver - подключение к ресурсу
Описание методов:
def test
Реализует процедуру по созданию мероприятия
Констркуторы:
1)def __init__(self)
'''
class TestEvent:
    addr = 'http://artek.org'

    def xpath(self, url):

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(element_to_be_clicked((By.XPATH, url)))

    def test(self, driver):
        # Подключение

        driver.get (self.addr)

        print "Тестируемый сайт:"
        print self.addr
        print "Тест страницы:"
        title = driver.title

        if (title == u'МДЦ «Артек»'):
            print u'Главная страница ' + title
        else:
            print driver.title


        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/header/div[1]/div[3]/div[2]/div[2]/a').click()
        driver.find_element_by_xpath('//*[@id="js-sign-in"]/div[1]/input').send_keys('r-sasha@artek.ru')
        driver.find_element_by_xpath('//*[@id="js-sign-in"]/div[2]/input').send_keys('66666666')
        driver.find_element_by_xpath('//*[@id="js-sign-in-submit"]').click()

        time.sleep (5)

        # Блок сохранения картинки
        print('JSON')
        driver.get('http://plus.artek.org/api/photo/14007/?format=json')
        time.sleep(5)
        image_data = driver.find_element_by_tag_name ('body').text
        print(image_data)
        image_data = json.loads (image_data)
        driver.get (image_data['original']['download'])
        filename = image_data['original']['src'].replace ('http://media.artek.org/media/', '').replace ('/', '_')
        image_path = "/tmp/{filename}".format (filename=filename)
        # Конец Блока сохранения картинки
        time.sleep(9)

        driver.get('http://plus.artek.org')

        '''
        but = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH,
                                                '/html/body/div[1]/div/div[2]/div/div[1]/a')))
        but.click()
        '''

        time.sleep(4)

        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div[1]/a').click()
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/main/form/div/div[1]/div[2]/div[1]/div/label[1]/span').click ()
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/main/form/div/div[2]/div[2]/div[1]/div/label[1]/span').click()
        driver.find_element_by_xpath(
            '//*[@id="id_location"]').send_keys (u'Артек')
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/main/form/div/div[5]/div[2]/form/div[2]/input').send_keys (u'Румянцев')
        time.sleep (5)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/main/form/div/div[5]/div[2]/form/div[3]/div/div[1]/div/div/div[3]/div').click()
        time.sleep (6)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/main/form/div/div[7]/div[2]/div[1]/div/div[1]/div[1]/input') \
            .send_keys ('13.12.2018')
        driver.find_element_by_xpath (
            '/html/body/div[2]/div[2]/div/main/form/div/div[7]/div[2]/div[1]/div/div[2]/div[1]/input') \
            .send_keys ('15.12.2018')
        driver.find_element_by_xpath(
            '//*[@id="id_title"]').send_keys (u'День открытых дверей в АРТЕКЕ!')
        driver.find_element_by_xpath(
            '//*[@id="id_description"]').send_keys (u'Данное мероприятие является тестовым')
        driver.find_element_by_xpath(
            '// *[ @ id = "id_info"]').send_keys (u'Информация по мероприятию')
        driver.find_element_by_xpath(
            '//*[@id="id_background"]').send_keys (image_path)
        time.sleep(6)
        driver.find_element_by_xpath (
            "/html/body/div[2]/div[2]/div/main/form/div/div[12]/div[2]/div[1]/div/div[1]/div[2]") \
            .click()
        time.sleep(6)
        driver.find_element_by_xpath (
            "/html/body/div[2]/div[2]/div/main/form/div/div[13]/div/div/button").click ()
        time.sleep(6)

    def __init__(self):

        self.driver = None
        driver = None
        try:
            driver = create_driver (host='idp7.dev.idpowers.com', port=32779)
            self.test (driver)
            print "Статус: \n Test success"
            driver.quit()
        except:
            driver = create_driver (host='idp7.dev.idpowers.com', port=32779)
            print "Статус:\n Test error\n Ошибка\n"
            driver.quit()





# Вспомогательный тест для расшаривания мероприятий в другие ДЦ- алгоритм действий:
# Авторизация менеджером
# Заходим в мероприятие и находим ранее созданное мероприятие 'День открытых дверей в АРТЕКЕ!'
# Ставим галочку "В другие ДЦ и сохраняем
class Test:
    addr = 'http://artek.org'

    def mainTest(self, driver):

        driver.get (self.addr)
        title = driver.title
        if (title == u'МДЦ «Артек»'):
            print u'Главная страница ' + title
        else:
            print driver.title
        time.sleep(5)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div[1]/div[3]/div[2]/div[2]/a').click()
        driver.find_element_by_xpath(
            '//*[@id="js-sign-in"]/div[1]/input').send_keys('r-sasha@artek.ru')
        driver.find_element_by_xpath(
            '//*[@id="js-sign-in"]/div[2]/input').send_keys('66666666')
        driver.find_element_by_xpath(
            '//*[@id="js-sign-in-submit"]').click()
        time.sleep(5)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div[2]').click ()

        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]').click()


        driver.find_element_by_xpath (
            '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div[7]/div/a').click ()
        time.sleep(6)
        fix = driver.find_element_by_xpath (
            '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]')
        fix.click()
        fix.click()
        fix.click()
        driver.find_element_by_xpath (
            '/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[7]/div/a').click ()
        driver.maximize_window ()
        driver.find_element_by_xpath (
            '/html/body/div[3]/div/header/div[1]/div/nav/a[9]/span').click ()
        driver.find_element_by_xpath (
            '/html/body/div[3]/div/div/div/div/div/div[1]/section/div[1]/div[1]/input') \
            .send_keys (u'День открытых дверей в АРТЕКЕ!');
        time.sleep(6)
        driver.find_element_by_xpath (
            '/html/body/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/a').click ()
        time.sleep (6)
        driver.find_element_by_xpath (
            '/html/body/div[3]/div/div/div/div/div/div[1]/div[2]/form/div[3]/div/div/div[2]/div[7]/div[2]/div/div[2]/label') \
            .click()
        driver.find_element_by_xpath (
            '/html/body/div[3]/div/div/div/div/div/div[1]/div[2]/form/div[1]/button').click ()
        time.sleep(6)

    def __init__(self):

        driver = None

        try:
            driver = create_driver(host='idp7.dev.idpowers.com', port=32779)
            self.mainTest (driver)
            print "Статус: \n Test success"
            driver.quit ()
        except:
            driver = create_driver(host='idp7.dev.idpowers.com', port=32779)
            print "Статус:\n Test error\n Ошибка\n"
            driver.quit ()



'''
Класс takeEvent.
Атрибуты:
1)addr = 'http://artek.org'
УРЛ тестируемого ресурса
Методы:
def mainDream(self, driver):
Параметры:
driver - подключение к ресурсу
Описание методов:
mainDream
Реализует процедуру по принятию мероприятия из артека в campDream
Констркуторы:
1)def __init__(self)
'''
class takeEvent ():
    addr = 'http://campdream.ru/'

    def mainDream(self, driver):
        driver.get (self.addr)

        title = driver.title
        if (title == u'МДЦ «Артек»'):
            print u'Главная страница ' + title
        else:
            print driver.title
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/header/div[1]/div[3]/div[2]/a').click()
        driver.find_element_by_xpath(
            '//*[@id="js-sign-in"]/div[1]/input').send_keys('manager@test.ru')
        driver.find_element_by_xpath(
            '//*[@id="js-sign-in"]/div[2]/input').send_keys('666666')
        driver.find_element_by_xpath(
            '//*[@id="js-sign-in-submit"]').click()
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div a').click()
        time.sleep(4)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/a[6]').click()
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/header/div[1]/div/nav/a[8]').click()
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div/div/div[1]/section/div[1]/div[2]/div[2]/label').click()


        time.sleep(4)
        driver.execute_script("$('.manager-events__button').click();")
        time.sleep(4)


    def __init__(self):

        driver = None

        try:
            driver = create_driver(host='idp7.dev.idpowers.com', port=32779)
            self.mainDream(driver)
            print "Статус: \n Test success"
            driver.quit()
        except Exception as ex:
            driver = create_driver(host='idp7.dev.idpowers.com', port=32779)
            print "Статус:\n Test error\n Ошибка: {}\n".format(str(ex))
            driver.quit()
