import selenium
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support
import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.ui
import requests


# user_data_dir = "C:\\Users\\YourUsername\\AppData\\Local\\Google\\Chrome\\User Data"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
# chrome_options.add_experimental_option('detach', True)

# driver = webdriver.Chrome(options=chrome_options)

response = requests.get('https://www.amazon.com/HP-i5-12450H-GeForce-Backlit-Touchpad/dp/B0D845LL5R/ref=sr_1_1?dib=eyJ2IjoiMSJ9.8R84c5Ga82BHISFn-7n2R8sIPy6-h7HxawhUjrtmymrCn1V4zXQ820csrwl4OED5EAZqYqxqBZFexKv6W5U8EvebL3SL_6cA-WI2acKU79pgANsGQyJmAv-b_cRmWnnWsOKx6bpuj_g-zVxRpODo3JJ5sVkjch62z3GDtYywyLWMO_NU2z3Rv5XDCSYmKJA9WdpCeWrRNhKpGaNzmdl_u0SFIHuEbUUwtyrgUFZ5Mss.oucpkcTq_gYecTbxb4ovoTy5IWV_qGKCMgmp-eepIls&dib_tag=se&keywords=gaming+laptops&pf_rd_i=121739139011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=4828e6b1-2650-4036-b64f-998beed80961&pf_rd_r=574RH3F9EXR6WYPC0546&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1732194607&sr=8-1')

# price = driver.find_element(By.XPATH, '//*[@id="poExpander"]/div[1]/div/table/tbody/tr[2]/td[2]/span').text


# driver.quit()
print(response.text)
