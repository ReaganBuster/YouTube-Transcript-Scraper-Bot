from selenium import webdriver
import time
from bot.pdf_manager import PDFManager

class Bot(webdriver.Chrome):
    def __init__(self, Service, ChromeDriverManager, driverWait, EC, By, Options, NoSuchElementException, StaleElementReferenceException, teardown=False)-> None:    
        services = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        super(Bot, self).__init__(service=services, options=chrome_options)
        self.by = By
        self.driverWait = driverWait
        self.teardown = teardown
        self.expectedConditions = EC
        self.noSuchElement = NoSuchElementException
        self.staleElementRef = StaleElementReferenceException
        
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_video(self, url):
        print()
        self.get(url)
        self.click_more()
        self.click_btn()
        self.get_load_and_save_pdf()
        


    def click_more(self):
        while True:
            try: 
                more = self.driverWait(self, 10).until(self.expectedConditions.element_to_be_clickable((self.by.XPATH, "//*[@id='expand']")))
                more.click()
                break
            except Exception as e:
                print(str(e))
                
        time.sleep(10)
            
    def click_btn(self):
        while True:
            try:
                buttonArea = self.driverWait(self,10).until(self.expectedConditions.presence_of_element_located((self.by.XPATH, "//*[@id='primary-button']")))
                # self.execute_script("arguments[0].scrollIntoView();", buttonArea)
                showLoad = buttonArea.find_element(self.by.CSS_SELECTOR, '#primary-button > ytd-button-renderer > yt-button-shape > button > yt-touch-feedback-shape > div')
                showLoad.click()
                break
            except Exception as e:
                print(str(e))
                
        time.sleep(10)

    def get_load_and_save_pdf(self):
        try:
            title = self.find_element(self.by.CSS_SELECTOR, "#title > h1 > yt-formatted-string")
            pdf_manager = PDFManager(filename=title.text)
            pay_load_section = self.driverWait(self, 10).until(self.expectedConditions.presence_of_element_located((self.by.XPATH, "//*[@id='segments-container']")))
            load = pay_load_section.find_elements(self.by.CSS_SELECTOR, '#segments-container > ytd-transcript-segment-renderer > div > yt-formatted-string')
            for line in load:
                pdf_manager.add_text(line.text)
        except Exception as e:
            print(str(e))
