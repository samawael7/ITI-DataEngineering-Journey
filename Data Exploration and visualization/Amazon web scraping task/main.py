from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

url = "https://www.amazon.eg/s?i=electronics&rh=n%3A21832883031%2Cp_123%3A46655&language=en"
driver.get(url)

time.sleep(5)

products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

results = []

for product in products:
    try:        
        name = product.find_element(By.XPATH, './/h2//span').text
        
        try:
            price_whole = product.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
            price_fraction = product.find_element(By.XPATH, './/span[@class="a-price-fraction"]').text
            full_price = f"{price_whole}.{price_fraction} EGP"
        except:
            full_price = "No Price"

        try:
            rating_element = product.find_element(By.XPATH, './/i[contains(@class, "a-icon-star")]/span')
            rating = rating_element.get_attribute("innerHTML")
        except:
            try:
                rating = product.find_element(By.XPATH, './/span[contains(@aria-label, "stars")]').get_attribute("aria-label")
            except:
                rating = "No Rating"

        try:
            reviews = product.find_element(By.XPATH, './/span[@class="a-size-base s-underline-text"]').text
        except:
            reviews = "0"

        try:
            image_url = product.find_element(By.XPATH, './/img[@class="s-image"]').get_attribute("src")
        except:
            image_url = "No Image"

        results.append({
            "Product Name": name,
            "Price": full_price,
            "Rating": rating,
            "Reviews": reviews,
            "Image URL": image_url
        })
        
    except Exception as e:
        continue

df = pd.DataFrame(results)
print(df)

df.to_csv("amazon_mobiles.csv", index=False)

driver.quit()