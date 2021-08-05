from selenium import webdriver
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

option = Options()
option.headless = True

url = "https://mam.jogjaprov.go.id/stream?vid=5b687cd7-34fc-4cfa-9179-5dc07ffba5f3&c=0.526167146420224"

driver = webdriver.Chrome(chrome_options=option)
driver.get(url)

