#requirements for colab
# install chromium, its driver, and selenium
!apt update
!apt install chromium-chromedriver
!pip install selenium
!pip install pandas
# set options to be headless, ..
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import re
import matplotlib.pyplot as plt

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# open it, go to a website, and get results
wd = webdriver.Chrome(options=options)
wd.get("https://www.ebay.com/b/Nintendo-Switch-Consoles/139971/bn_7116325214")


#divs = wd.find_element(By.TAG_NAME, 'div')
wd.implicitly_wait(5)

page_count = 0
rating_list=[]
title_list=[]
price_list=[]

while page_count < 3:
    product_elements = wd.find_elements(By.CLASS_NAME, "s-item")

    for product in product_elements:
          # Initialize rating_element here
        try:
            rating_element = product.find_element(By.CLASS_NAME, "b-rating__rating-count")
        except NoSuchElementException:
            rating_element = None

        if rating_element:
            rating_text = rating_element.text
            rating_match = re.search(r'\d+', rating_text)# go zema samo brojot

            if rating_match:
                rating = int(rating_match.group())

                title = product.find_element(By.CLASS_NAME, "s-item__title").text
                price = product.find_element(By.CLASS_NAME, "s-item__price").text

                rating_list.append(rating)
                title_list.append(title)
                price_list.append(price)

    next_button = wd.find_element(By.CLASS_NAME, "pagination__next")
    next_button.click()
    page_count += 1
    #try:
      #  next_button = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pagination__next")))
    #    next_button.click()
   # except TimeoutException:
     #   break
data = {
    "Title": title_list,
    "Price": price_list,
    "Rating": rating_list
}
df = pd.DataFrame(data)

print(df)

plt.figure(figsize=(8, 6))
plt.hist(df["Rating"], bins=10, color='green')
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Rating Histogram")
plt.show()