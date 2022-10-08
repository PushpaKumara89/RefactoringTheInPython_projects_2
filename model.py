from enum import Enum, unique
from typing import Any


@unique
class Page_field_type(Enum):
    id = 'id'
    url = 'url'
    page_name = 'page_name'
    cover_image = 'cover_image'
    user_saved = 'user_saved'
    activate = 'activate'
    activated_Time = 'activated_Time'


class Page:
    def __init__(self, id: int, url: str, page_name: str, cover_image: str, user_saved: str, activate: bool,
                 activated_Time: str):
        self.id = id
        self.url = url
        self.page_name = page_name
        self.cover_image = cover_image
        self.user_saved = user_saved
        self.activate = activate
        self.activated_Time = activated_Time

    def __str__(self) -> str:
        return "{id :" + str(self.id) + \
               ",\nurl: " + self.url + \
               ",\npage_name: " + self.page_name + \
               ",\ncover_image: " + self.cover_image + \
               ',\nuser_saved: ' + self.user_saved + \
               ',\nactivate: ' + str(self.activate) + \
               ',\nactivated_Time: ' + self.activated_Time+' }'

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)


@unique
class Post_field_type(Enum):
    id = 'id'
    page_id = 'page_id'
    scraping_time = 'scraping_time'
    post_by = 'post_by'
    screen_shot = 'screen_shot'


class Post:
    def __init__(self, id: int, page_id: int, scraping_time: str, post_by: str, screen_shot: []):
        self.id = id
        self.page_id = page_id
        self.scraping_time = scraping_time
        self.post_by = post_by
        self.screen_shot = screen_shot

    def __str__(self) -> str:
        return "{id : " + str(self.id) + \
               ",\npage_id : " + str(self.page_id) + \
               ",\nscraping_time : " + str(self.scraping_time) + \
               ",\npost_by : " + self.post_by+' }'

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)
