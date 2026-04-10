# 🚀 AI Career Intelligence: Global Job Market Analysis

## 📌 Overview

This project analyzes a global dataset of **90,000+ AI jobs** to uncover insights into salary trends, career growth, job stability, and work culture across countries, industries, and roles.

The goal is to answer key questions:

* What drives AI salaries?
* How do AI careers grow over time?
* Which roles are stable vs risky?
* Does higher salary lead to better job satisfaction?

---

## ⚙️ Data Pipeline

This project includes an automated data pipeline for consistent and reproducible analysis.

### 🔄 Pipeline Flow

1. Load raw dataset from `data/raw/`
2. Clean and preprocess data using Python scripts
3. Save cleaned dataset to `data/processed/`
4. Use processed data for analysis and visualization

### ▶️ Run the pipeline

```bash
python run_pipeline.py
```

---

## 🛠️ Tools & Technologies

* **Python** (Pandas, NumPy)
* Data Cleaning & Feature Engineering

---

## 📊 Key Analysis Areas

### 1. Job Market Overview

* Distribution of AI jobs across countries, industries, and roles
* Identification of dominant hiring regions

### 2. Salary Intelligence

* Salary comparison across countries and experience levels
* Real salary calculation (adjusted for cost of living)
* Key drivers of AI compensation

### 3. Career Growth

* Salary progression across experience levels
* Promotion trends and career development patterns

### 4. Job Stability & Risk

* Layoff and automation risk analysis
* Trade-off between salary and job stability

### 5. Work Culture

* Relationship between salary, satisfaction, and work-life balance
* Impact of working hours on employee satisfaction

---

## 🔍 Key Insights

* AI salaries grow **2–3× from entry to senior levels**, making experience the strongest driver of compensation
* Significant variation exists across countries, but **real salary provides a more accurate comparison**
* Salary shows **weak correlation with employee satisfaction**, highlighting the importance of work-life balance
* Some roles offer **higher growth but increased risk**, showing a trade-off between stability and compensation

---

## 📁 Project Structure

```
AI_Job_Intelligence/
│
├── data/
│   ├── raw/              # Original dataset
│   └── processed/        # Cleaned dataset (pipeline output)
│
├── notebooks/            # Jupyter notebooks (analysis)
├── scripts/              # Data cleaning scripts
├── run_pipeline.py       # Pipeline runner
└── README.md
```

## 👤 Author

**Ayush**

---
