import allure
from allure_commons.types import Severity
from selene import browser

from pages.pages import MainPage, FavoritePage, BabiesPage, CartPage

main_page = MainPage(browser)
babies_page = BabiesPage(browser)
favorite_page = FavoritePage(browser)
cart_page = CartPage(browser)


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь открывает вкладку 'Малыши' все товары")
def test_open_babies_clothes():
    main_page.open_page()
    main_page.choose_recommended_city_modal()

    babies_page.click_tab_baby()
    babies_page.open_babies_clothes_page()

    babies_page.assert_babies_title()
    babies_page.assert_exist_list()


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь открывает вкладку страницу 'Избранное'")
def test_open_favorites():
    main_page.open_page()
    main_page.choose_recommended_city_modal()
    favorite_page.open_favorites()

    favorite_page.assert_title()
    favorite_page.assert_empty_list()


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь добавляет 3 первых товара в избранное")
def test_add_any_clothes_to_favorites():
    favorites_ids = []
    main_page.open_page()
    main_page.choose_recommended_city_modal()

    babies_page.click_tab_baby()
    babies_page.open_babies_clothes_page()

    babies_page.assert_babies_title()

    for i in range(1, 4):
        favorites_ids.append(
            favorite_page.add_clothes_to_favorites(i)
        )

    favorite_page.open_favorites()
    favorite_page.assert_title()

    for favorite_id in favorites_ids:
        favorite_page.assert_clothes_in_favorites(favorite_id)


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь открывает вкладку страницу 'Корзина'")
def test_open_cart():
    main_page.open_page()
    main_page.choose_recommended_city_modal()
    cart_page.open_cart()

    cart_page.assert_title()
    cart_page.assert_empty_list()


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь добавляет 3 первых товара в корзину")
def test_add_any_clothes_to_cart():
    cart_ids = []
    main_page.open_page()
    main_page.choose_recommended_city_modal()

    babies_page.click_tab_baby()
    babies_page.open_babies_clothes_page()

    babies_page.assert_babies_title()

    for i in range(1, 4):
        cart_ids.append(
            cart_page.add_clothes_to_cart(i)
        )
        cart_page.chose_size(i)

    cart_page.open_cart()
    cart_page.assert_title()

    for card_id in cart_ids:
        cart_page.assert_clothes_in_cart(card_id)
