# Veloria Tech ML Intern Assignment

## Overview

This repository contains my submission for the AI/ML Engineering Internship assignment from Veloria Tech Private Limited.

The assignment consists of:

* Task 1: Web Scraping Cricket Match Data
* Task 2: Machine Learning Match Winner Prediction
* Task 3 (Bonus): Not Attempted

---

## Project Structure

```text
veloria-tech-ml-intern-assignment/
│
├── scraper.py
├── match_data.csv
├── model.py
├── README.md
└── x_g_b_model.pkl
```

---

# Task 1 – Web Scraping

## Objective

Collect cricket match information from a publicly available cricket statistics website and store it in CSV format.

## Data Collected

The scraper extracts:

* Match Date
* Team Names
* Venue
* Match Result
* Top Scorer
* Top Score

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas

## How to Run

Install dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

Run:

```bash
python scraper.py
```

Output:

```text
match_data.csv
```

---

# Task 2 – Machine Learning Prediction Model

## Objective

Build a machine learning model that predicts the winning team based on historical cricket match data.

## Dataset

The dataset contains match information such as:

* Team 1
* Team 2
* Toss Winner
* Toss Decision
* Venue
* City
* Match Winner

## Data Preprocessing

The following preprocessing steps were performed:

1. Selected relevant columns.
2. Handled missing values using the most frequent value.
3. Removed duplicate records.
4. Balanced the dataset using oversampling.
5. Cleaned text fields by:

   * Converting to lowercase
   * Removing spaces
   * Removing punctuation
6. Encoded categorical variables using One-Hot Encoding.
7. Encoded target labels using Label Encoding.

## Models Evaluated

The following machine learning algorithms were tested:

* Logistic Regression
* Random Forest Classifier
* XGBoost Classifier
* Bagging Classifier
* Support Vector Machine (SVM)
* Decision Tree Classifier

## Final Model

After comparing model performance, XGBoost was selected as the final model and saved as:

```text
x_g_b_model.pkl
```

## Evaluation Metrics

The models were evaluated using:

* Accuracy Score
* F1 Score
* Precision Score
* Recall Score
* Confusion Matrix
* Classification Report


## How to Run

Install dependencies:

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
```

Run:

```bash
python model.py
```

The script will:

1. Load and preprocess the dataset.
2. Train multiple models.
3. Display evaluation metrics.
4. Save the best-performing model.

---

# Challenges Faced

* Handling missing values in match data.
* Managing categorical cricket team information.
* Balancing class distribution among winning teams.
* Comparing multiple machine learning algorithms fairly.
* Feature encoding for machine learning models.

---

# Results

The model was evaluated using:

* Accuracy Score
* F1 Score
* Precision Score
* Recall Score
* Confusion Matrix

XGBoost achieved the best overall performance among the tested algorithms.

<img width="1168" height="775" alt="Screenshot 2026-06-06 111122" src="https://github.com/user-attachments/assets/248e0c80-0d70-4b3d-887e-5f4cf043130f" />


---

# Libraries Used

```text
pandas
numpy
requests
beautifulsoup4
scikit-learn
xgboost
matplotlib
seaborn
pickle
```

---

# Submission Notes

* Task 1 Completed
* Task 2 Completed
* Task 3 (Semantic Search / RAG) Not Attempted

This project was completed as part of the Veloria Tech AI/ML Engineering Internship assignment.
