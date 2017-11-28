from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebFroxy():    
    browser = webdriver.Chrome('c:/chromedriver/chromedriver.exe')
    wait  = WebDriverWait(browser, 5)

    def openBrowser(self, link):
        self.browser.get(link)

    def quit(self):
        self.browser.quit()

    def doClickByLinkText(self,linkText):
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, linkText))).click()

    def doClickByName(self,name):
        self.wait.until(EC.presence_of_element_located((By.NAME, name))).click()

    def doClickById(self,id):
        self.wait.until(EC.presence_of_element_located((By.ID, id))).click()

    def setValueByName(self, name, val):
        self.wait.until(EC.presence_of_element_located((By.NAME, name))).send_keys(val)

    def doVisibilityClickByCssSelector(self, seletor):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor))).click()


