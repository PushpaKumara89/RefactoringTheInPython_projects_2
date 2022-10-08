import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import selenium_activities
from model import Page, Page_field_type, Post
from service.post_service import add_post
from service.fb_page_service import update_page


def screen_add_post(page: Page):
    options = Options()
    options.headless = True
    driver: WebDriver = webdriver.Chrome(options=options)
    driver.set_window_size(750, 4000)
    driver.get(page.__getattribute__(Page_field_type.url.value))
    time.sleep(2)
    for i in range(9):
        driver.execute_script('window.scrollBy(0,900)')
        print('=')
        time.sleep(1)

    post_type1 = driver.find_elements(by=By.XPATH, value="//div[@class='g4tp4svg om3e55n1']")
    post_type2 = driver.find_elements(by=By.XPATH, value="//div[@class='_5pcr userContentWrapper']")
    post_by = driver.title
    time_date = str(datetime.datetime.now())

    see_mores = driver.find_elements(by=By.XPATH, value="//*[text()='See more']")
    print(see_mores.__len__())
    for see_more in see_mores:
        driver.execute_script("arguments[0].click()", see_more)

    print(post_by)
    img_array = []
    if post_type1.__len__() != 0:
        img_array = selenium_activities.get_screen_shot(post_type1, driver)
        post_type1[0].screenshot("hhhh\\dfdffgd.png")
        print('type1')
    elif post_type2.__len__() != 0:
        print(post_type2.__len__())
        img_array = selenium_activities.get_screen_shot(post_type2, driver)
        post_type2[0].screenshot("hhhh\\dfdffgd.png")
        print('type2')

    temp_post = Post(id=None,
                     page_id=page.__getattribute__(Page_field_type.id.value),
                     scraping_time=time_date,
                     post_by=post_by,
                     screen_shot=img_array
                     )
    print(temp_post)
    add_post(temp_post)
    driver.quit()
    return temp_post


def activate_page(page: Page):
    options = Options()
    options.headless = True
    driver: WebDriver = webdriver.Chrome(options=options)
    driver.set_window_size(750, 550)
    driver.get(page.__getattribute__(Page_field_type.url.value))
    time.sleep(2)
    title = driver.title
    page.__setattr__(Page_field_type.page_name.value, title)
    cover_img = selenium_activities.get_cover_img(driver)
    page.__setattr__(Page_field_type.cover_image.value, cover_img)
    page.__setattr__(Page_field_type.activate.value, True)
    t_time = str(datetime.datetime.now())
    page.__setattr__(Page_field_type.activated_Time.value, t_time)
    b = update_page(page)
    driver.quit()
    if b:
        return True
    else:
        return False
