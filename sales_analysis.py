import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Original Dataset")
print(df)


print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)


print("\nMissing Values:")
print(df.isnull().sum())


df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Price"] = df["Price"].fillna(df["Price"].mean())


total_revenue = df["Total_Sales"].sum()

best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

average_sales = df["Total_Sales"].mean()

print("\n========== SALES REPORT ==========")
print(f"Total Sales: ₹{total_revenue}")
print(f"Average Sales: ₹{average_sales:.2f}")
print(f"Best Selling Product: {best_product}")

print("\nSales by Product:")
print(df.groupby("Product")["Total_Sales"].sum())