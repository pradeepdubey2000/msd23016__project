# 🛡️ Cybersecurity App - Vulnerability Prediction & CVE Analysis 🔍

## 📖 Overview

Welcome to the **Cybersecurity App**, an innovative web application designed to assist with the prediction, analysis, and risk assessment of cybersecurity vulnerabilities. This app includes several modules to predict vulnerabilities, analyze CVE (Common Vulnerabilities and Exposures) data, and help you explore potential threats to your systems.

With the help of machine learning models, natural language processing, and interactive visualizations, the app offers valuable insights into vulnerabilities, affected products, and fixes.

---

## 🚀 Key Features

### 1. **Vulnerability Prediction** 🤖
- Predict cybersecurity vulnerabilities from detailed descriptions.
- Use machine learning to evaluate potential security threats based on known patterns.

### 2. **CVE Exploration & Analysis** 📊
- Interactive visualizations for exploring Common Vulnerabilities and Exposures (CVEs).
- Dive deep into various relationships between numerical and categorical variables within CVE data.
- Time-based analysis and trends on CVE records.

### 3. **CVE Solution Finder** 🛠️
- Get detailed information on CVE IDs like `CVE-2022-22947`, including:
    - Vulnerability description
    - Impact
    - Fix recommendations
    - Affected products
    - Severity rating

### 4. **CVE Similarity Search** 🔎
- Find the most similar CVE records based on a description provided.
- Utilizes embeddings and cosine similarity for an efficient search.

---

## 📋 Requirements

- **Python 3.6+**
- **Streamlit** – For building the interactive web interface.
- **Other Libraries** – Various machine learning libraries such as **XGBoost**, **CatBoost**, and **Sentence Transformers**.

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-repo/cybersecurity-app.git
cd cybersecurity-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run home.py
```

---

## 📝 How It Works

### **Vulnerability Prediction & CVE Analysis**

- **Vulnerability Prediction**: Input a detailed description of a vulnerability and get predictions for security metrics like Impact Score, Base Score, and Access Complexity.
  
- **CVE Analysis**: View CVE records with advanced filtering, date range selection, and interactive visualizations of numerical vs categorical data, trends over time, and correlations.

- **CVE Solution Finder**: Input a CVE ID, and the app queries the **Groq API** to retrieve detailed information about the vulnerability, including impact, fixes, affected products, and severity. It also extracts the relevant information using **regex**.

- **CVE Similarity Search**: Enter a vulnerability description, and the app uses machine learning models to search for the most similar CVEs in the database, ranking them by similarity.

---

## 💡 How to Use

1. **Vulnerability Prediction**: 
   - Enter a detailed description of a vulnerability.
   - Click the "Predict Metrics" button to get security metrics predictions.

2. **CVE Exploration**: 
   - Select the date range and variables for analysis.
   - View interactive plots and graphs showing trends, distributions, and correlations.

3. **CVE Solution Finder**: 
   - Enter the CVE ID (e.g., `CVE-2022-22947`).
   - Click **"Get Solution"** to retrieve detailed information, including impact, fix, and severity.

4. **CVE Similarity Search**: 
   - Enter a CVE description.
   - Click **"Find Similar CVEs"** to get a list of the top similar CVEs based on the input description.

---

## 🛠️ Development & Contribution

- **Created by**: Pradeep Dubey
- **Supervised by**: Sandeep Sir

### How to Contribute
- Fork the repository and submit a pull request with your changes.
- Ensure your changes follow the **PEP 8** style guidelines.
- Add tests for new features and functionality.

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute this code with attribution.

---

## 🏆 Acknowledgements

A special thanks to:
- **Groq API** for providing valuable CVE data.
- **Streamlit** for the easy-to-use UI framework.
- **Machine Learning Libraries** like **XGBoost** and **CatBoost** for making accurate vulnerability predictions.

---

🌐 **Stay Safe & Keep Your Systems Secure!**
