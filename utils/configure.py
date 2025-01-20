import os

from dotenv import load_dotenv

load_dotenv()


class Configure:
    base_url = "https://www.sela.ru"
    sleep_wait_unbelievable = 300
    sleep_wait_medium = 1
    sleep_wait_short = 0.3
    is_local = os.getenv('is_local')
    selenoid_login = os.getenv('selenoid_login')
    selenoid_pass = os.getenv('selenoid_pass')
    selenoid_uri = os.getenv('selenoid_uri')
    selenoid_path = f'https://{selenoid_login}:{selenoid_pass}{selenoid_uri}'
