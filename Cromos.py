import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Login
driver.get("https://steamcommunity.com/login/home/?goto=id%2Fezhor%2Finventory%2F")
driver.implicitly_wait(60)
driver.find_element(By.ID, "inventory_link_753").click()

while(True):
    # Tags
    time.sleep(3)
    driver.find_element(By.ID, "filter_tag_show").click()
    driver.implicitly_wait(60)
    driver.find_element(By.ID, "tag_filter_753_0_misc_marketable").click()
    driver.implicitly_wait(60)
    driver.find_element(By.ID, "tag_filter_753_0_item_class_item_class_2").click()

    # Sticker
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[@class="itemHolder" and not(@style)]').click()
    time.sleep(0.5)
    stickerName = driver.find_element(By.ID, "iteminfo0_item_name").text
    print("Selling " + stickerName + "...", end = ' ')

    # Read Price
    time.sleep(1) 
    price = driver.find_element(By.ID, "iteminfo0_item_market_actions").text.split("\n")
    price = price[1]
    price = price.split(" ")
    price = price[len(price)-1]

    # Sell    
    driver.execute_script("SellCurrentSelection();")
    time.sleep(1)
    priceInput = driver.find_element(By.ID, "market_sell_buyercurrency_input")
    priceInput.clear()
    priceInput.send_keys(price)
    time.sleep(1)
    ssa = driver.find_element(By.ID, "market_sell_dialog_accept_ssa")
    if(ssa.get_attribute('checked') != "true"):
        ssa.click()
    time.sleep(0.5)
    driver.find_element(By.ID, "market_sell_dialog_accept").click()
    time.sleep(1)
    driver.find_element(By.ID, "market_sell_dialog_ok").click()
    print("Sold for " + price)
    time.sleep(1)
