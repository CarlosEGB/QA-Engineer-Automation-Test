from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, '#main-search-form h2')
    signin_button = (By.XPATH, "//div[@id='root']//child::span[@class='J-sA-label']//ancestor::div[@role='button']")
    search_button = (By.XPATH, "//button[contains(@class,'animation-search')]")

    name_tag_input = (By.CSS_SELECTOR, "input[aria-label='Origen']")
    name_dropdown_column_input = (By.CSS_SELECTOR, "input[aria-label='Destino']")
    search_tag_input = (By.XPATH, "//div[@id='main-search-form']//child::span[text()='Solo ida']")
    cancel_button = (By.CSS_SELECTOR, "div.c_neb-item-close")
    create_column_disabled_button = (By.XPATH, "//div[contains(@class,'-nav-button')]//child::div")


def option_menu_right(option):
    return By.XPATH, f"//div[contains(@class,'menu-item-title') and text()='{option}']"