
# 🛒 SpreeCommerce Product Extraction (Selenium Test)

## 📖 Overview

This automation script uses Selenium WebDriver to navigate the [SpreeCommerce demo site](https://demo.spreecommerce.org/), hover over the "Fashion" menu, navigate to the "T-Shirts" section under "Men", and extract product names and prices from the page.

It prints the extracted product details and verifies whether certain expected products are listed on the site.

---

## 🚀 Features

* Opens the SpreeCommerce demo site using Chrome WebDriver.
* Hovers over the "Fashion" category to reveal submenus.
* Navigates to the Men's T-Shirts section.
* Extracts product names and prices displayed on the page.
* Verifies the presence of expected T-Shirt products.
* Logs results in a readable format to the console.
* Waits for dynamic content using explicit waits.
* Handles missing elements gracefully with try-except blocks.

---

## 🛠️ Technologies Used

* Python
* Selenium WebDriver
* ChromeDriver
* XPath & CSS Selectors
* ActionChains for mouse hover actions

---

## 🔧 Prerequisites

Ensure the following are installed before running the script:

* Python 3.7+
* Google Chrome (latest recommended)
* ChromeDriver (compatible with your Chrome version)
* Required Python packages:

  ```bash
  pip install selenium
  ```

---

## 📁 Project Structure

```
spreecommerce_product_extraction/
├── spree_product_test.py          # Main test script
├── README.md                      # Project documentation (this file)
```

---

## ▶️ How to Run

1. Clone or download this repository.
2. Open your terminal and navigate to the project directory.
3. Run the test:

   ```bash
   python spree_product_test.py
   ```
4. Check the console output to view extracted products and validation results.

---

## ✅ Sample Output

```
Extracted Products:

Name: Ripped T-Shirt
Price: $19.99

Name: Red Polo Shirt
Price: $25.00

...

✔️ Product found: Ripped T-Shirt
✔️ Product found: Pink Polo Shirt
❌ Product missing: Spree T-Shirt
```

---

## 📌 Note

* This test is dependent on the live demo site of SpreeCommerce which may update or change content. If products are renamed or removed, the validation will reflect those changes.
* Ensure that your ChromeDriver version matches the installed version of Chrome.

