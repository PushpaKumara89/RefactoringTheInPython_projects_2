import time

from tabulate import tabulate
from db import db_connection
from model import Post

db = db_connection.get_db_connection()


def get_all_posts():
    cur = db.cursor()
    sql = 'SELECT scraping_time, post_by from post'
    cur.execute(sql)
    rst = cur.fetchall()
    print("\n"+tabulate(rst, headers=["SCRAPPING TIME", "PAGE NAME"])+"\n")
    cur.close()
    time.sleep(1)
    return rst


def get_post_by_txt(txt):
    pass


def add_post(post: Post):
    cur = db.cursor()
    sql = 'INSERT INTO post VALUE(%s, %s, %s, %s)'
    temp_post = (None, post.page_id, post.scraping_time, post.post_by)
    print(temp_post)
    cur.execute(sql, temp_post)
    add_screen_shot(post.screen_shot, cur.lastrowid)
    db.commit()
    cur.close()
    print("Adding Success....")


def add_screen_shot(screen_shots: [], id: int):
    cur = db.cursor()
    sql = 'INSERT INTO post_imgs VALUE(%s, %s, %s)'
    for x in screen_shots:
        temp_image = (None, id, x)
        cur.execute(sql, temp_image)

