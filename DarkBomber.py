import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.RED}###############################################
#          WHATSAPP ULTIMATE BAN TOOL         #
#            MODE : TURBO BOMBING             #
###############################################
"""

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./sessions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def send_payload(driver, phone, message, file_path=None, count=1):
    url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"
    driver.get(url)
    wait = WebDriverWait(driver, 60)

    try:
        print(f"{Fore.YELLOW}[*] Initialisation de la cible : {phone}....)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
        
        for i in range(count):
            print(f"{Fore.CYAN}[{i+1}/{count}] Envoi du payload...")
            
            if file_path and os.path.exists(file_path):
                attach_btn = driver.find_element(By.XPATH, '//div[@title="Joindre"]')
                attach_btn.click()
                time.sleep(0.5)
                media_input = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                media_input.send_keys(os.path.abspath(file_path))
                time.sleep(1.5)
                send_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
                send_btn.click()
            else:
                msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                msg_box.send_keys(message)
                driver.find_element(By.XPATH, '//span[@data-icon="send"]').click()

            time.sleep(random.uniform(1.2, 2.5)) 

        print(f"{Fore.GREEN}[SUCCESS] Attaque terminée sur {phone}")

    except Exception as e:
        print(f"{Fore.RED}[ERREUR] Interruption : {e}")

def main():
    print(BANNER)
    target = input(f"{Fore.WHITE}Numéro de la cible (ex: 33612345678) : ")
    msg = input("Message à envoyer : ")
    file = input("Chemin du média (laisser vide si aucun) : ")
    
    try:
        nbr = int(input(f"{Fore.RED}Nombre d'envois (Bombing) : "))
    except:
        nbr = 1

    driver = setup_driver()
    send_payload(driver, target, msg, file if file else None, nbr)
    
    print(f"\n{Fore.MAGENTA}[!] Opération terminée.")
    driver.quit()

if __name__ == "__main__":
    main()
