from selenium.webdriver.common.by import By

main_page_title_locator = [By.XPATH, ".//h1[text()='Соберите бургер']"]

login_button_locator = [By.XPATH, ".//button[text()='Войти в аккаунт']"]

header_login_locator = [By.XPATH, ".//h2[text()='Вход']"]

restore_password_link_locator = [By.XPATH, ".//a[text()='Восстановить пароль']"]

restore_button_locator = [By.XPATH, ".//button[text()='Восстановить']"]

email_field_locator = [By.XPATH, "//input[@name='name']"]

save_button_locator = [By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']"]

show_hide_password_button_locator = [By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_password input_size_default']"]

active_password_field_locator = [By.CSS_SELECTOR, "input[name='Введите новый пароль'][type='text']"]