from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_spreecommerce_product_extraction():

  driver = webdriver.Chrome()
  driver.get("https://demo.spreecommerce.org/")
  driver.maximize_window()

  wait = WebDriverWait(driver, 20)

  fashion_menu = driver.find_element(By.XPATH, '//*[@id="block-6468"]/a/span')
  actions = ActionChains(driver)
  actions.move_to_element(fashion_menu).perform()

  wait = WebDriverWait(driver, 20)

  men_section = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="block-6468"]/div/div/div/div[2]/h6')))

  wait = WebDriverWait(driver, 20)

  tshirt_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block-6468"]/div/div/div/div[2]/div[1]/a/span')))
  tshirt_link.click()

  WebDriverWait(driver, 40).until(EC.title_contains("T-Shirts"))
  assert "t-shirts" in driver.title.lower()

  wait.until(EC.presence_of_element_located((By.ID, "products_list")))

  products = driver.find_elements(By.CLASS_NAME, 'product-card-inner')

  extracted_data = []

  for product in products:

      try:
          name = product.find_element(By.CLASS_NAME, 'product-card-title').text
      except:
          name = "name not found"

      try:
          price = product.find_element(By.CLASS_NAME, 'product-card-price').text
      except:
          price = "Price not available"

      extracted_data.append({"name": name, "price": price})

  print("Extracted Products:\n")

  for item in extracted_data:
      print(f"Name: {item['name']}\nPrice: {item['price']}\n")


  time.sleep(10)

  expected_products = [
      "Ripped T-Shirt",
      "Pink Polo Shirt",
      "Red Polo Shirt",
      "Blue Polo Shirt",
      "Spree T-Shirt"
  ]

  extracted_names = [item['name'] for item in extracted_data]
  for expected in expected_products:
      if expected in extracted_names:
          print(f"✔️ Product found: {expected}")
      else:
          print(f"❌ Product missing: {expected}")

  driver.quit()











