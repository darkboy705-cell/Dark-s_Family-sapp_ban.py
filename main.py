import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, init

init(autoreset=True)

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./sessions")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def send_bombing(driver, phone, message, file_path=None, count=1):
    driver.get(f"https://web.whatsapp.com/send?phone={phone}&text={message}")
    wait = WebDriverWait(driver, 60)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
        for i in range(count):
            if file_path and os.path.exists(file_path):
                driver.find_element(By.XPATH, '//div[@title="Joindre"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(os.path.abspath(file_path))
                wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))).click()
            else:
                driver.find_element(By.XPATH, '//span[@data-icon="send"]').click()
            print(f"{Fore.GREEN}[{i+1}/{count}] Envoyé")
            time.sleep(random.uniform(1.5, 3.0))
    except Exception as e: print(f"{Fore.RED}Erreur: {e}")

if __name__ == "__main__":
    target = input("Numéro (ex: 33612345678) : ")
    msg = input("Message : ")
    file = input("Chemin média (vide si aucun) : ")
    cnt = int(input("Nombre d'envois : "))
    dr = setup_driver()
    send_bombing(dr, target, msg, file if file else None, cnt)
    dr.quit()
