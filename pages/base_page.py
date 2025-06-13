from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Ждёт появления элемента в DOM
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    # Ждёт, пока элемент станет кликабельным
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    # Ждёт, пока элемент станет видимым
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    # Кликает по элементу, ожидая его готовности
    def click(self, locator):   
        element = self.wait_for_clickable(locator)
        element.click()

    # Заполняет поле
    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    # Получает текст элемента, после его видимости
    def get_element_text(self, locator):
        answer = self.wait_for_visibility(locator)
        return answer.text
    
    # Проверяет наличие элемента в DOM
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
    
    # Проверяет видимость элемента
    def is_element_visible(self, locator):
        try:
            self.wait_for_visibility(locator)
            return True
        except:
            return False
        
    # Прокручивает страницу до элемента
    def scroll_into_view(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    # Переключается на другое окно по его handle
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    # Возвращает текущий URL
    def get_current_url(self):
        return self.driver.current_url
    
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    def wait_for_new_window(self, current_window):
        self.wait.until(lambda d: len(d.window_handles) > 1)
    
    # Выполняет произвольский JavaScript
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    # Ожидает по условию, заданному функцией
    def wait_for_condition(self, condition_function):
        return self.wait.until(condition_function)