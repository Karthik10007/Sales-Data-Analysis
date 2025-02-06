import pandas as pd

def sales_summary(data):
    """Display a basic sales summary."""
    print("\nBasic Sales Summary:")
    print(data.describe())

def total_sales_by_category(data):
    """Calculate total sales for each product category."""
    if 'Category' in data.columns and 'Sales' in data.columns:
        category_sales = data.groupby('Category')['Sales'].sum()
        print("\nTotal Sales by Category:")
        print(category_sales)
        return category_sales
    else:
        print("Error: Missing 'Category' or 'Sales' column in the data.")

def top_selling_products(data, top_n=5):
    """Find top N best-selling products."""
    if 'Product' in data.columns and 'Sales' in data.columns:
        top_products = data.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(top_n)
        print(f"\nTop {top_n} Selling Products:")
        print(top_products)
        return top_products
    else:
        print("Error: Missing 'Product' or 'Sales' column in the data.")
