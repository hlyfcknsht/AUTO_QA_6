from selenium import webdriver
from selenium.webdriver.common.by import By

proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
              '103.151.246.38:10001', '199.60.103.228:80', '199.60.103.228:80',
              '199.60.103.28:80', ]

for PROXY in proxy_list:
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=&s' % PROXY)
        chrome_options.add_argument("--headless")
        URL = 'https://2ip.ru/'

        with webdriver.Chrome() as browser:
            browser.get(URL)
            print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

            browser.set_page_load_timeout(5)

            proxy_list.remove(PROXY)
    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {PROXY}")
        continue
