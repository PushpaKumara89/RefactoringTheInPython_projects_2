import threading
import time
from service import fb_page_service
from scrapping_data import activate_page, screen_add_post


def activate_call():
    while True:
        not_activated_pages = fb_page_service.get_all_pages_by_is_activated(status=False)
        for single_page in not_activated_pages:
            print("Activating..... " + single_page.url)
            activate_page(single_page)
            time.sleep(2)
        time.sleep(60*10)


def post_collect():
    activated_pages = fb_page_service.get_all_pages_by_is_activated(status=True)
    for page in activated_pages:
        print("activate " + page.url)
        screen_add_post(page)
        time.sleep(3)


while True:
    activate_page_t = threading.Thread(target=activate_call)
    activate_page_t.start()
    time.sleep(2)
    post_collect_t = threading.Thread(target=post_collect)
    post_collect_t.start()
    time.sleep(60 * 60)
