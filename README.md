# 🛍 Customer Segmentation Analytics using RFM Analysis, K-Means Clustering, SQL Server & Power BI

An end-to-end **Customer Segmentation Analytics** project that uses **Python, Machine Learning, SQL Server, and Power BI** to identify customer groups based on purchasing behavior. The project applies **RFM (Recency, Frequency, Monetary) Analysis** and **K-Means Clustering** to generate actionable business insights for customer retention and targeted marketing.

---

# 📌 Project Overview

This project demonstrates a complete customer analytics workflow:

- Data Cleaning using Python
- Feature Engineering
- RFM Analysis
- Customer Segmentation using K-Means Clustering
- SQL Server Integration
- Interactive Power BI Dashboards
- Business Recommendations

---

# 🏗 Project Architecture

```
                    Customer Transaction Dataset
                                │
                                ▼
                    Python Data Cleaning (Pandas)
                                │
                                ▼
                     Feature Engineering
                                │
                                ▼
                          RFM Analysis
                                │
                                ▼
                    StandardScaler & K-Means
                                │
                                ▼
                    Customer Segmentation
                                │
                                ▼
                       SQL Server Database
                                │
                                ▼
                     Business Analytics View
                                │
                                ▼
                     Power BI Interactive Dashboard
```

---

# 📊 RFM Analysis

The project evaluates customers using three key metrics:

### Recency (R)

Days since the customer's last purchase.

### Frequency (F)

Number of purchases made by the customer.

### Monetary (M)

Total amount spent by the customer.

These metrics are used to identify valuable customer segments.

---

# 🤖 Machine Learning

## Algorithm Used

- K-Means Clustering

## Feature Scaling

- StandardScaler

## Optimal Cluster Selection

- Elbow Method

The model automatically groups customers into meaningful business segments.

---

# 👥 Customer Segments

The clustering model identifies the following customer groups:

🏆 Champions

- Highest spending customers
- Purchase very frequently
- Most recent buyers

⭐ High Value Customers

- High revenue contribution
- Regular purchasers
- Strong customer value

❤️ Loyal Customers

- Consistent purchasing behavior
- Medium spending customers
- Long-term customer base

❌ Lost Customers

- Low purchase frequency
- Low spending
- Long time since last purchase

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Processing |
| Pandas | Data Cleaning |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning |
| SQL Server | Database |
| SQLAlchemy | Database Connection |
| PyODBC | SQL Connectivity |
| Power BI | Dashboard |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```
customer-segmentation-rfm-kmeans-powerbi/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── python/
│   ├── data_cleaning.py
│   ├── rfm_analysis.py
│   ├── elbow_method.py
│   ├── clustering.py
│   ├── cluster_summary.py
│   ├── assign_segments.py
│   └── load_to_sql.py
│
├── sql/
│   ├── create_database.sql
│   ├── create_table.sql
│   ├── create_view.sql
│   └── business_queries.sql
│
├── powerbi/
│   └── Customer_Segmentation_Analytics.pbix
│
├── screenshots/
│   ├── executive_dashboard.png
│   ├── customer_segmentation.png
│   ├── marketing_insights.png
│   ├── elbow_method.png
│   └── sql_schema.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Workflow

```
Raw Customer Data

↓

Python Data Cleaning

↓

Feature Engineering

↓

RFM Analysis

↓

Data Scaling

↓

Elbow Method

↓

K-Means Clustering

↓

Business Segmentation

↓

SQL Server

↓

Power BI Dashboard
```

---

# 📈 Power BI Dashboard

## 📊 Executive Dashboard

Features

- Total Customers
- Total Revenue
- Average Customer Value
- Number of Segments
- Revenue by Segment
- Customer Distribution
- Customer Details

---

## 👥 Customer Segmentation Dashboard

Features

- Customer Distribution
- Revenue by Segment
- Average Customer Value
- Recency vs Monetary Scatter Plot
- Interactive Filters

---

## 📈 Marketing Insights Dashboard

Features

- Revenue Contribution by Segment
- Average Recency
- Average Frequency
- Marketing Recommendations
- Customer Analytics

---

# 📷 Dashboard Screenshots

## Executive Dashboard

```
c:\Users\aadvi\OneDrive\Pictures\Screenshots\executive_dashboard.png
```

---

## Customer Segmentation Dashboard

```
c:\Users\aadvi\OneDrive\Pictures\Screenshots\customer_segmentation.png
```

---

## Marketing Insights

```
c:\Users\aadvi\OneDrive\Pictures\Screenshots\marketing_insights.png
```

---

## Elbow Method

```
screenshots/elbow_method.png
```

---

# 📈 Business Insights

This project helps businesses:

- Identify VIP customers
- Detect customers at risk of churn
- Build loyalty campaigns
- Improve customer retention
- Increase customer lifetime value
- Optimize marketing strategies
- Prioritize high-value customers

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Aadvik7462/customer-segmentation-rfm-kmeans-powerbi.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Data Cleaning

```bash
python python/data_cleaning.py
```

---

## Run RFM Analysis

```bash
python python/rfm_analysis.py
```

---

## Run Elbow Method

```bash
python python/elbow_method.py
```

---

## Train K-Means Model

```bash
python python/clustering.py
```

---

## Generate Customer Segments

```bash
python python/assign_segments.py
```

---

## Load Data into SQL Server

```bash
python python/load_to_sql.py
```

---

## Open Power BI

Open

```
Customer_Segmentation_Analytics.pbix
```

---

# 📚 Skills Demonstrated

- Data Cleaning
- Feature Engineering
- RFM Analysis
- Customer Analytics
- Machine Learning
- K-Means Clustering
- SQL Server
- ETL Pipeline
- Power BI Dashboard Development
- Business Intelligence
- Data Visualization

---

# 🔮 Future Enhancements

- Azure SQL Database
- Azure Data Factory
- Azure Machine Learning
- Automated Model Retraining
- Customer Churn Prediction Integration
- Power BI Service Deployment

---

# 👨‍💻 Author

**Aadvik Singh**

Aspiring Data Analyst | Business Intelligence Analyst | Data Engineer

**GitHub:** https://github.com/Aadvik7462
