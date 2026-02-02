# 📊 Online Sales Data Analysis (Python)

## 📌 Executive Summary
Analyzed a dataset of **~$80,000 in sales transactions** using Python to uncover key revenue drivers and regional trends. The analysis focused on data cleaning (handling duplicate product entries), statistical correlation, and visualization to inform inventory and marketing strategies.

**Key Findings:**
* **Top Product:** The *MacBook Pro 16-inch* is the #1 revenue driver, significantly outperforming lower-cost high-volume items.
* **Regional Strategy:** *North America* dominates market share, suggesting ad spend should be focused there.
* **Pricing Insight:** A strong positive correlation (**0.93**) between Unit Price and Revenue confirms that high-ticket items drive growth more than volume.

---

## 🛠 Technologies Used
* **Python:** Main analysis
* **Pandas:** Data cleaning (merged duplicate "MacBook" records) & aggregation
* **Matplotlib / Seaborn:** Visualization
* **NumPy:** Statistical calculation (IQR for outlier detection)

---

## 📈 Visualizations & Insights

### 1. Top 5 Best-Selling Products
*Identified the highest-value products to prioritize inventory stocking.*
![Top Products](top_products.png)

### 2. Regional Market Share
*Analyzed sales distribution to target marketing efforts.*
![Regional Share](region_share.png)

### 3. Correlation Matrix (Price vs. Revenue)
*Discovered a 0.93 correlation, validating a "Premium Pricing" strategy.*
![Correlation](correlation_matrix.png)

---

## ⚙️ How to Run
1. Clone the repository
2. Install dependencies: `pip install pandas matplotlib seaborn`
3. Run the script: `python sales_analysis.py`
