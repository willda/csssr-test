import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'http://blog.csssr.ru/qa-engineer/'

class VacancyPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(URL)

    def test_link_href(self):
        wait = WebDriverWait(self.driver, 1)
        
        find_errors_block = self.driver.find_element(
            By.XPATH, '//div[@class="graphs-errors"]/a'
        )
        find_errors_block.click()
        
        link_to_test = wait.until(EC.presence_of_element_located((
            By.XPATH, '//label[@for="soft"]/a'
        )))
        assert link_to_test.get_attribute('href') == 'http://monosnap.com'

    def tearDown(self):
        self.driver.close()


if name == "__main__":
    unittest.main()
