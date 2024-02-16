from selenium.webdriver.common.by import By

main_page_title_locator = [By.XPATH, ".//h1[text()='Соберите бургер']"]

order_button_locator = [By.XPATH, ".//button[text()='Оформить заказ']"]

login_button_locator = [By.XPATH, ".//button[text()='Войти в аккаунт']"]

personal_account_button = [By.XPATH, ".//p[text()='Личный Кабинет']"]

constructor_button_locator = [By.XPATH, ".//p[text()='Конструктор']"]

ordered_feed_locator = [By.XPATH, ".//p[text()='Лента Заказов']"]

ingredient_locator = [By.XPATH,  ".//p[text()='Флюоресцентная булка R2-D3']"]

pop_up_window_locator = [By.XPATH,  ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]

close_button_locator = [By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]

un_active_element_locator = [By.XPATH, ".//section[@class='Modal_modal__P3_V5']"]

ingredient_counter_link_locator = [By.XPATH, '//*[contains(@href,"/ingredient/")]//p[contains(@class,"counter_counter__num")]']

dragndrop_bun_target_locator = [By.XPATH, './/span[text()="Перетяните булочку сюда (верх)"]']

oder_modal_opened_link_locator = [By.XPATH, './/section[contains(@class,"Modal_modal_opened__3ISw4")]']

oder_modal_order_number_locator = [By.XPATH, './/h2[contains(@class,"Modal_modal__title_shadow")]']

ingredient_3_link_locator = [By.XPATH, '(//*[contains(@href,"/ingredient/")])[3]']

ingredient_7_link_locator = [By.XPATH, '(//*[contains(@href,"/ingredient/")])[7]']













