import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter

# --- 1. DATA LOADING & CLEANING ---
try:
    df = pd.read_csv("Online Sales Data.csv")
except FileNotFoundError:
    print("Error: CSV not found. Please ensure the file is in the same folder.")
    exit()

# A. Fix Dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# B. DATA CLEANING
df['Product Name'] = df['Product Name'].str.replace('Apple MacBook Pro 16-inch', 'MacBook Pro 16-inch')

# C. Drop duplicates
df = df.drop_duplicates()

# D. Extract Month for analysis
df['Month'] = df['Date'].dt.to_period('M')

print("Data Loaded & Cleaned.")

# --- HELPER FUNCTION FOR FORMATTING ---
def currency_fmt(x, pos):
    """Turns 1000 into $1k, 500 into $500 for cleaner charts"""
    if x >= 1000:
        return f'${x*1e-3:.0f}k'
    return f'${x:.0f}'

formatter = FuncFormatter(currency_fmt)

# --- 2. VISUALIZATIONS ---
sns.set_theme(style="whitegrid")

# FIGURE 1: HISTOGRAMS
fig, axes = plt.subplots(1, 3, figsize=(15, 7), num="Distributions & Revenue Analysis")

# Plot 1: Units Sold
df['Units Sold'].hist(ax=axes[0], bins=10, color='skyblue', edgecolor='black')
axes[0].set_title('Distribution of Units Sold')
axes[0].set_xlabel('Units Sold')
axes[0].text(0.5, -0.25, "Note: Most orders are for 1-2 items", 
             transform=axes[0].transAxes, ha='center', fontsize=11, style='italic', color='#333333')

# Plot 2: Unit Price
df['Unit Price'].hist(ax=axes[1], bins=20, color='lightgreen', edgecolor='black')
axes[1].set_title('Distribution of Unit Price')
axes[1].set_xlabel('Unit Price ($)')
axes[1].xaxis.set_major_formatter(formatter)
axes[1].text(0.5, -0.25, "Note: Most items are low-priced", 
             transform=axes[1].transAxes, ha='center', fontsize=11, style='italic', color='#333333')

# Plot 3: Total Revenue
df['Total Revenue'].hist(ax=axes[2], bins=20, color='salmon', edgecolor='black')
axes[2].set_title('Distribution of Total Revenue')
axes[2].set_xlabel('Total Revenue ($)')
axes[2].xaxis.set_major_formatter(formatter)
axes[2].text(0.5, -0.25, "Note: Most revenue comes from small sales", 
             transform=axes[2].transAxes, ha='center', fontsize=11, style='italic', color='#333333')

plt.tight_layout()
plt.subplots_adjust(bottom=0.25)


# FIGURE 2: TOP 5 PRODUCTS
top_products = df.groupby('Product Name')['Total Revenue'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 6), num="Top Selling Products") 
ax = sns.barplot(x=top_products.values, y=top_products.index, palette='magma')
plt.title('Top 5 Best-Selling Products')
plt.xlabel('Total Revenue')
ax.xaxis.set_major_formatter(formatter)
plt.subplots_adjust(left=0.3) 


# FIGURE 3: REGION PIE CHART
regional_sales = df.groupby('Region')['Total Revenue'].sum()

plt.figure(figsize=(8, 8), num="Regional Market Share") 
plt.pie(regional_sales, labels=regional_sales.index, autopct='%1.1f%%', 
        colors=sns.color_palette('pastel'), startangle=140)
plt.title('Share of Revenue by Region')


# FIGURE 4: CORRELATION HEATMAP
numeric_df = df.select_dtypes(include=[np.number])

plt.figure(figsize=(6, 5), num="Statistical Correlation")
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix: Darker Red = Stronger Relationship')


# --- 3. STATISTICAL CALCULATIONS (IQR Method) ---
Q1 = df['Total Revenue'].quantile(0.25)
Q3 = df['Total Revenue'].quantile(0.75)
IQR = Q3 - Q1
outliers_count = len(df[(df['Total Revenue'] < (Q1 - 1.5 * IQR)) | (df['Total Revenue'] > (Q3 + 1.5 * IQR))])

# --- 4. EXECUTIVE SUMMARY ---
print("\n" + "="*40)
print("KPIs & KEY INSIGHTS")
print("="*40)
print(f"Total Revenue:      ${df['Total Revenue'].sum():,.2f}")
print(f"Top Product:        {top_products.index[0]}")
print(f"Top Region:         {regional_sales.idxmax()}")
print(f"Price-Rev Link:     {numeric_df.corr().loc['Unit Price', 'Total Revenue']:.2f} (Very Strong)")
print(f"Outliers Detected:  {outliers_count} (Calculated via IQR)")
print("="*40 + "\n")

# --- 5. SHOW ALL PLOTS ---
print("Generating Report Charts...")
plt.show()