from pickle import TRUE
from bot.scraper import Bot
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from bot.constants import BASE_URL_s



with Bot(Service = Service,
    ChromeDriverManager = ChromeDriverManager,
    driverWait = WebDriverWait,
    EC = EC,
    By = By, Options= Options,
    NoSuchElementException=NoSuchElementException,
    StaleElementReferenceException=StaleElementReferenceException
    ) as bot:
    bot.load_video(url='https://www.youtube.com/watch?v=CtnX1EJHbC0')