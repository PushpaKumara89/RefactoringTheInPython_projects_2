import datetime
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def get_ime():
    s = str(datetime.datetime.now())
    s1 = ''
    for i in s:
        if i == ':' or i == '.' or i == ' ':
            i = '-'
        s1 += i
    return s1


def get_screen_shot(all_post, driver: WebDriver):
    array = []
    for i in range(5):
        s = get_ime()
        all_post[i].location_once_scrolled_into_view
        driver.execute_script('window.scrollBy(0,-150)')
        time.sleep(0.1)
        all_post[i].screenshot(s + "post.png")
        time.sleep(1.2)
        array.append(s + "post.png")
    return array


def get_cover_img(driver):
    s = get_ime()
    driver.save_screenshot(s + 'cover.png')
    time.sleep(0.1)
    return s + 'cover.png'
