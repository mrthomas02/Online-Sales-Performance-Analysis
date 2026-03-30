# 📊 Online Sales Data Analysis

## 📌 Executive Summary
Analyzed a dataset of **~$80,000 in sales transactions** to uncover key revenue drivers and regional trends. This project demonstrates an end-to-end data pipeline, from raw data cleaning and statistical correlation in Python to a final, interactive business intelligence dashboard. 

**Key Findings:**
* **Top Product:** The *MacBook Pro 16-inch* is the #1 revenue driver, significantly outperforming lower-cost high-volume items.
* **Regional Strategy:** *North America* dominates market share, suggesting ad spend should be focused there.
* **Pricing Insight:** A strong positive correlation (**0.93**) between Unit Price and Revenue confirms that high-ticket items drive growth more than volume.

---

## 📈 Interactive Power BI Dashboard
*(Screenshot of the final dashboard)*
![Power BI Visual Screenshot](./dashboard_screenshot.png) 

> **Note:** To view the interactive data model, you can download the `.pbix` file below and open it in Power BI Desktop.

### 📁 Dashboard Deliverables
* [`power_bi_visual.pbix`](./power_bi_visual.pbix): The interactive Power BI source file.
* [`power_bi_visual.pdf`](./power_bi_visual.pdf): A static, high-resolution export of the dashboard.

---

## 🛠 Technologies Used
* **Power BI:** Interactive data modeling and executive visualization
* **Python:** Main analysis and data transformation
* **Pandas:** Data cleaning (merged duplicate "MacBook" records) & aggregation
* **Matplotlib / Seaborn:** Programmatic visualization
* **NumPy:** Statistical calculation (IQR for outlier detection)

---

## 💻 Python Visualizations & Insights

### 1. Revenue & Price Distribution
*Analyzed the spread of unit prices and order quantities. Most transactions are low-value volume orders, but revenue is driven by high-ticket outliers.*
![Distribution Analysis](images/Distributions_&_Revenue_Analysis.png)

### 2. Top 5 Best-Selling Products
*Identified the **MacBook Pro 16-inch** as the primary revenue driver, significantly outperforming high-volume/low-margin items.*
![Top Products](images/Top_Selling_Products.png)

### 3. Regional Market Share
*North America dominates the sales distribution, suggesting that marketing ad spend should be prioritized in this region.*
![Regional Share](images/Regional_Market_Share.png)

### 4. Correlation Matrix (Price vs. Revenue)
*Discovered a **0.93 correlation** between Unit Price and Total Revenue. This validates a "Premium Pricing" strategy: selling fewer expensive items generates more revenue than selling many cheap items.*
![Correlation Matrix](images/Statistical_Correlation.png)

---

## ⚙️ How to Run the Python Environment
1. Clone the repository
2. Install dependencies: `pip install pandas matplotlib seaborn`
3. Run the script: `python sales_analysis.py`
