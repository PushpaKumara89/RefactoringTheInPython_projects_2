import time

from tabulate import tabulate
from db import db_connection
from model import Page

db = db_connection.get_db_connection()


def get_all_pages():
    sql = 'SELECT * from page'
    return selection(sql)


def add_page(page: Page):
    cur = db.cursor()
    sql = 'INSERT INTO page VALUE(%s, %s, %s, %s, %s, %s, %s)'
    tem_page = (None, page.url, page.page_name, page.cover_image, page.user_saved, page.activate, page.activated_Time)
    print(page)
    cur.execute(sql, tem_page)
    db.commit()
    cur.close()
    print("Adding Success....")
    return True


def update_page(page: Page):
    cur = db.cursor()
    sql = "UPDATE page SET url=%s, page_name=%s, " \
          "cover_image=%s, user_saved=%s, activate=%s, activated_Time=%s WHERE id=%s"
    print(sql)
    tem_page = (page.url, page.page_name, page.cover_image, page.user_saved, page.activate,
                page.activated_Time, page.id)
    print(page)
    cur.execute(sql, tem_page)
    db.commit()
    cur.close()
    print("Adding Success....")
    return True


def get_pages_by_txt(txt):
    sql = f"SELECT * from page WHERE page_name LIKE '%{txt}%'"
    return selection(sql)


def get_all_pages_by_is_activated(status: bool):
    sql = f"SELECT * from page WHERE activate = {status}"
    return selection(sql)


def selection(sql: str):
    cur = db.cursor()
    cur.execute(sql)
    rst = cur.fetchall()
    print("\n"+tabulate(rst, headers=["ID", "URL", "PAGE NAME", "COVER IMG", "ACTIVATE", "Activated_Time"])+"\n")
    ar = []
    for i in rst:
        ar.append(Page(id=i[0], url=i[1], page_name=i[2], cover_image=i[3], user_saved=i[4], activate=i[5],
                       activated_Time=i[6]))
    cur.close()
    time.sleep(1)
    return ar
