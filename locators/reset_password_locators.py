from selenium.webdriver.common.by import By

show_hide_password_button_locator = [By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_password input_size_default']"]

active_password_field_locator = [By.CSS_SELECTOR, "input[name='Введите новый пароль'][type='text']"]