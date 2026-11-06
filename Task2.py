import pandas as pd
import numpy as np

# --------------------------------------------------
# TASK 2 : EXPLORATORY DATA ANALYSIS
# --------------------------------------------------

# Load cleaned dataset

data = pd.read_csv(
    "cleaned_data/sales_cleaned.csv"
)

print("\n========== EXPLORATORY DATA ANALYSIS ==========")

# --------------------------------------------------
# BASIC INFORMATION
# --------------------------------------------------

print("\nDATASET SHAPE")
print(data.shape)

print("\nCOLUMN NAMES")
print(data.columns.tolist())

# --------------------------------------------------
# DESCRIPTIVE STATISTICS
# --------------------------------------------------

print("\nDESCRIPTIVE STATISTICS")
print(data.describe())

# --------------------------------------------------
# CUSTOMER AGE ANALYSIS
# --------------------------------------------------

if "Age" in data.columns:

    print("\nAGE STATISTICS")

    print("Minimum Age:",
          data["Age"].min())

    print("Maximum Age:",
          data["Age"].max())

    print("Average Age:",
          round(data["Age"].mean(), 2))

# --------------------------------------------------
# SALES ANALYSIS
# --------------------------------------------------

if "Sales" in data.columns:

    print("\nSALES STATISTICS")

    print("Total Sales:",
          round(data["Sales"].sum(), 2))

    print("Average Sale:",
          round(data["Sales"].mean(), 2))

    print("Maximum Sale:",
          round(data["Sales"].max(), 2))

    print("Minimum Sale:",
          round(data["Sales"].min(), 2))

# --------------------------------------------------
# SALES BY CITY
# --------------------------------------------------

if "City" in data.columns and "Sales" in data.columns:

    city_sales = (
        data.groupby("City")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nSALES BY CITY")
    print(city_sales)

# --------------------------------------------------
# SALES BY CATEGORY
# --------------------------------------------------

if "Category" in data.columns and "Sales" in data.columns:

    category_sales = (
        data.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nSALES BY CATEGORY")
    print(category_sales)

# --------------------------------------------------
# SALES BY PRODUCT
# --------------------------------------------------

if "Product" in data.columns and "Sales" in data.columns:

    product_sales = (
        data.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTOP PRODUCTS BY SALES")
    print(product_sales.head(10))

# --------------------------------------------------
# PAYMENT METHOD
# --------------------------------------------------

if "PaymentMethod" in data.columns:

    print("\nPAYMENT METHOD USAGE")
    print(data["PaymentMethod"].value_counts())

# --------------------------------------------------
# MONTHLY SALES
# --------------------------------------------------

if "Month" in data.columns and "Sales" in data.columns:

    monthly_sales = (
        data.groupby("Month")["Sales"]
        .sum()
        .sort_index()
    )

    print("\nMONTHLY SALES")
    print(monthly_sales)

# --------------------------------------------------
# OUTLIER DETECTION USING IQR
# --------------------------------------------------

if "Sales" in data.columns:

    Q1 = data["Sales"].quantile(0.25)
    Q3 = data["Sales"].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = data[
        (data["Sales"] < lower_limit) |
        (data["Sales"] > upper_limit)
    ]

    print("\nSALES OUTLIERS")
    print(outliers)

    print("\nNUMBER OF SALES OUTLIERS")
    print(len(outliers))

# --------------------------------------------------
# BUSINESS FINDINGS
# --------------------------------------------------

print("\n========== KEY FINDINGS ==========")

if "Sales" in data.columns:

    print(
        "1. Total sales:",
        round(data["Sales"].sum(), 2)
    )

if "City" in data.columns and "Sales" in data.columns:

    best_city = (
        data.groupby("City")["Sales"]
        .sum()
        .idxmax()
    )

    print(
        "2. Highest sales city:",
        best_city
    )

if "Category" in data.columns and "Sales" in data.columns:

    best_category = (
        data.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    print(
        "3. Best performing category:",
        best_category
    )

if "Product" in data.columns and "Sales" in data.columns:

    best_product = (
        data.groupby("Product")["Sales"]
        .sum()
        .idxmax()
    )

    print(
        "4. Best performing product:",
        best_product
    )