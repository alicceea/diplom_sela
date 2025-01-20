from time import sleep

import allure
from selene import Browser, have, query, be

from utils.util import Configure

products_list = '//div[@id="products_list"]'
card = products_list + '/ul/li[{number}]'
favorite_button = card + '//button[contains(@class, "product-card__favorite")]'

cart_table = '//div[@class="cart-table"]'
cart_button = card + '//button[contains(@class, "product-card__title__add-to-cart-button")]'
first_size_button = card + '//ul[@class="product-card__size-list"]/li[1]'


class MainPage:

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step("Пользователь открывает главную страницу")
    def open_page(self):
        self.browser.open('/')
        sleep(Configure.sleep_wait_medium)

    @allure.step("Пользователь выбирает предложенный город")
    def choose_recommended_city_modal(self):
        try:
            self.browser.element('//*[@class="js-choice-city-close-popup city-isset"]').click()
            sleep(Configure.sleep_wait_short)
        except Exception as e:
            print(e)

    @allure.step("Пользователь закрывает модальное окно")
    def close_nag_modal(self):
        try:
            self.browser.element('//*[@id="popmechanic-snippet"]//*[@data-popmechanic-close]').click()
        except Exception as e:
            print(e)


class BabiesPage:
    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step("Пользователь открывает вкладку 'Малыши'")
    def click_tab_baby(self):
        self.browser.element('//*[@data-tab="baby"]').click()
        sleep(Configure.sleep_wait_short)

    @allure.step("Пользователь нажимает на кнопку 'Смотреть всё'")
    def open_babies_clothes_page(self):
        self.browser.element('//*[@id="menu_tab-baby"]//a[text() = "Смотреть всё"]').click()
        sleep(Configure.sleep_wait_medium)

    @allure.step("Проверка заголовка на странице Малыши")
    def assert_babies_title(self):
        self.browser.element('//h1[@data-title="Малыши"]').should(have.exact_text("ОДЕЖДА ДЛЯ МАЛЫШЕЙ"))

    @allure.step("Проверка товаров на странице Малыши")
    def assert_exist_list(self):
        self.browser.element(products_list).should(be.existing)


class FavoritePage:

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step("Пользователь нажимает на кнопку 'Избранное'")
    def open_favorites(self):
        self.browser.element('#header_user_menu_favorite_link').click()
        sleep(Configure.sleep_wait_medium)

    def add_clothes_to_favorites(self, number):
        with allure.step("Пользователь добавляет товар в избранное"):
            self.browser.element(favorite_button.format(number=number)).click()
            sleep(Configure.sleep_wait_short)
            return self.browser.element(favorite_button.format(number=number)).get(query.attribute("data-product_id"))

    @allure.step("Проверка заголовка на странице Избранное")
    def assert_title(self):
        self.browser.element('//h1[@data-title="Избранное"]').should(have.exact_text("ИЗБРАННОЕ"))

    def assert_clothes_in_favorites(self, favorite_id):
        with allure.step(f"Проверка id {favorite_id} товара в избранном"):
            self.browser.element(products_list + f'//button[@data-product_id="{favorite_id}"]').should(be.existing)

    @allure.step("Проверка отсутствия товаров в избранном")
    def assert_empty_list(self):
        self.browser.element(products_list).should(be.not_.existing)


class CartPage:

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step("Пользователь нажимает на кнопку 'Корзина'")
    def open_cart(self):
        self.browser.element('#header_user_menu_cart_link').click()
        sleep(Configure.sleep_wait_medium)

    def add_clothes_to_cart(self, number):
        with allure.step("Пользователь добавляет товар в корзину"):
            self.browser.element(cart_button.format(number=number)).click()
            sleep(Configure.sleep_wait_short)
            return self.browser.element(favorite_button.format(number=number)).get(query.attribute("data-product_id"))

    def chose_size(self, number):
        with allure.step("Пользователь выбирает размер товара для добавления в корзину"):
            self.browser.element(first_size_button.format(number=number)).click()
            sleep(Configure.sleep_wait_short)

    @allure.step("Проверка заголовка на странице Корзина")
    def assert_title(self):
        self.browser.element('//h1[@class="cart-title"]/span').should(have.text("КОРЗИНА"))

    def assert_clothes_in_cart(self, card_id):
        pass
        with allure.step(f"Проверка id {card_id} товара в корзине"):
            self.browser.element(cart_table + f'/div[2]//button[@data-product_id="{card_id}"]').should(be.existing)

    @allure.step("Проверка отсутствия товаров в корзине")
    def assert_empty_list(self):
        self.browser.element(cart_table).should(be.not_.existing)
