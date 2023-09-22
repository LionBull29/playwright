from playwright.sync_api import expect


def test_buying_item_from_shopping_cart(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("a").filter(has_text="1").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("Имя_Тест")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("Фамилия_Тест")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("314")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    page.get_by_role("img", name="Pony Express").click()
    page.locator("[data-test=\"back-to-products\"]").click()