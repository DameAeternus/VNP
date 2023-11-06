import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://mobelix.com.mk/mk/mobilni-telefoni"
response = requests.get(url)

# Initialize lists to store the extracted data
phone_brands_list = []
phone_types_list = []
phone_prices_list = []

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the phone information
    phone_brands = soup.find_all("h5", class_="mb-0")
    phone_types = soup.find_all("h3", class_="h5 font-weight-normal")
    phone_prices = soup.find_all("p", class_="h5 price")
    for price in phone_prices:
      price_text = price.get_text()
      if price_text.endswith("ден"):
            price_text = price_text[:-3]  # Remove the last 3 characters


    # Use zip to combine the lists and iterate through them
    for brand, phone_type, price in zip(phone_brands, phone_types, phone_prices):
        phone_brands_list.append(brand.get_text())
        phone_types_list.append(phone_type.get_text())
        phone_prices_list.append(price.get_text())

else:
    print("Failed to retrieve the webpage.")
print("Phone Brands List:", phone_brands_list)
print("Phone Types List:", phone_types_list)
print("Phone Prices List:", phone_prices_list)


# Calculate statistical elements for the "Phone Price" column
mean_price = df["Phone Price"].mean()
median_price = df["Phone Price"].median()
std_deviation = df["Phone Price"].std()
min_price = df["Phone Price"].min()
max_price = df["Phone Price"].max()

# Create a DataFrame from the lists and name the columns
data = {
    "Phone Brand": phone_brands_list,
    "Phone Type": phone_types_list,
    "Phone Price": phone_prices_list
}

df = pd.DataFrame(data)
# Clean the "Phone Price" column by removing non-numeric characters
df["Phone Price"] = df["Phone Price"].str.replace(r'[^\d.]', '', regex=True)

# Split the string and take the first number (assuming it's the main price)
df["Phone Price"] = df["Phone Price"].str.split('.').str[0]

# Convert the "Phone Price" column to float
df["Phone Price"] = df["Phone Price"].astype(float)



# Print the calculated statistical elements
print("Mean Price:", mean_price)
print("Median Price:", median_price)
print("Standard Deviation:", std_deviation)
print("Minimum Price:", min_price)
print("Maximum Price:", max_price)

# Create a histogram for the price values
plt.figure(figsize=(10, 5))
plt.hist(df["Phone Price"], bins=20, edgecolor='k', alpha=0.7)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Create a bar chart for price ranges (e.g., bins of prices)
# You can customize the number of bins and labels as needed
price_bins = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000]
price_labels = ["0-10000", "10000-20000", "20000-30000", "30000-40000", "40000-50000", "50000-60000", "60000-70000", "70000-80000", "80000-90000", "90000-100000", "100000-110000", "110000-120000"]
df["Price Range"] = pd.cut(df["Phone Price"], bins=price_bins, labels=price_labels)

# Count the occurrences of each price range
price_range_counts = df["Price Range"].value_counts().sort_index()

# Create a bar chart for price ranges
plt.figure(figsize=(10, 5))
plt.bar(price_range_counts.index, price_range_counts.values)
plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()