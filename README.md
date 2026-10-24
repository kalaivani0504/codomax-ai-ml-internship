# Codomax AI & ML Internship 

## About This Repository

Welcome to my **AI & Machine Learning Internship Projects Repository**!

This repository documents my learning journey during the Codomax Digital Solutions AI & ML Internship. It includes Python programming exercises, a Python mini-project, data analysis and visualization, machine learning fundamentals, and an improved machine-learning-based mini-project.

Throughout this internship, I have been developing my programming skills, exploring machine learning concepts, working with datasets, and applying my knowledge to practical projects.

## Internship Objectives

- Understand the fundamentals of Artificial Intelligence and Machine Learning.
- Learn Python programming and problem-solving.
- Analyse datasets using Python libraries.
- Create visualizations to understand data.
- Train, evaluate, and test a machine learning model.
- Explore how AI tools can support coding, research, and productivity.
- Build practical projects and maintain project documentation using GitHub.

## Modules Overview

### Module 01: Introduction to AI & Python
**Duration:** Day 1 – Day 4

**Topics Covered:**
- Introduction to Artificial Intelligence (AI).
- Introduction to Machine Learning (ML).
- Difference between AI, ML, and Deep Learning.
- Real-world applications of AI.
- Python variables and data types.
- Operators and conditional statements.
- Loops, lists, and functions.
- Beginner-friendly Python programming exercises.

**Learning Outcome:** Developed a foundation in AI concepts and Python programming.

### Module 02: Python Mini Project
**Duration:** Day 5 – Day 8

**Project:** Student Grade Calculator

**Topics Covered:**
- Applying Python programming concepts.
- Accepting and processing user input.
- Performing calculations using Python.
- Using conditional statements to determine grades.
- Organizing project code.
- Uploading project files to GitHub.

**Learning Outcome:** Applied fundamental Python concepts to build a simple, practical application.

### Module 03: Data Analysis & Visualization
**Duration:** Day 9 – Day 12

**Technologies:** Python, Pandas, NumPy, Matplotlib

**Topics Covered:**
- Loading and exploring a sample dataset.
- Understanding rows, columns, and data types.
- Performing basic data cleaning.
- Analysing data using Pandas and NumPy.
- Calculating summary statistics.
- Creating bar charts, line charts, and pie charts using Matplotlib.

**Learning Outcome:** Gained practical experience in data exploration, basic analysis, and visualization.

### Module 04: Machine Learning Fundamentals
**Duration:** Day 13 – Day 16

**Technologies:** Python, Pandas, Scikit-learn

**Topics Covered:**
- Understanding the machine learning workflow.
- Preparing data for model training.
- Splitting data into training and testing sets.
- Training a machine learning model.
- Making predictions and evaluating model performance.
- Understanding classification results and evaluation metrics.

**Learning Outcome:** Learned how to prepare data, train a machine learning model, and evaluate its predictions.

### Module 05: AI Tools & Mini Project
**Duration:** Day 17 – Day 20

**Project:** AI-Based Job Scam Risk Detector

**Objective:** Improve a previous machine learning project by applying AI-assisted development practices and adding useful features.

**Topics Covered:**
- Exploring ChatGPT for coding assistance, research, and productivity.
- Improving an existing machine learning project.
- Integrating a trained model into a Python application.
- Saving and loading trained machine learning components.
- Adding rule-based warning indicators.
- Providing safety recommendations for suspicious job postings.
- Documenting the project and sharing the learning journey.

**Learning Outcome:** Applied machine learning concepts in a practical application and learned how AI tools can support software development.

> Note: ChatGPT was used as a development assistant. An external generative AI API is not integrated into the application.

## Featured Project: AI-Based Job Scam Risk Detector

### Project Overview

The AI-Based Job Scam Risk Detector is a Python application designed to analyse job-posting text and classify it as potentially suspicious or lower-risk based on a trained machine learning model.

The project uses Natural Language Processing (NLP) techniques to convert job-posting text into numerical features. A Logistic Regression classifier then uses these features to make a prediction.

The application also checks for predefined warning indicators, such as requests for registration fees or upfront payments, and displays safety recommendations.

**Important:** This tool is intended for preliminary risk assessment. Its predictions cannot guarantee that a job posting is fraudulent or genuine.

### Key Features

- Analyse job-posting text entered by the user.
- Predict potential job scam risk using a trained machine learning model.
- Convert text into numerical features using TF-IDF.
- Use a Logistic Regression classifier for prediction.
- Display a model-generated class probability estimate.
- Identify predefined warning indicators using rule-based checks.
- Provide basic safety recommendations.
- Load saved model components for local execution.

### Machine Learning Workflow

1. **Dataset:** Used a job-postings dataset containing genuine and fraudulent job-posting labels.
2. **Data Preparation:** Prepared the text data and target labels.
3. **Feature Extraction:** Used TF-IDF to convert text into numerical features.
4. **Data Splitting:** Split the dataset into training and testing sets.
5. **Model Training:** Trained a Logistic Regression classifier.
6. **Model Evaluation:** Evaluated the model using classification metrics.
7. **Model Saving:** Saved the trained classifier and TF-IDF vectorizer.
8. **Application Development:** Built a Python application that loads the saved components and analyses user-provided job text.

### Model Evaluation

The model achieved the following results on the held-out test dataset:

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 96.88% |
| Recall for the fraudulent class | 81% |

**Understanding these results:**
- **Accuracy (96.88%):** The model correctly classified approximately 96.88% of the test examples.
- **Fraudulent-class recall (81%):** The model identified approximately 81% of the fraudulent examples in the test set.

These results reflect performance on the dataset used for evaluation. Real-world performance may differ, and the model may still produce false positives or false negatives.

### Technologies Used

- **Python** — Application development and data processing.
- **Pandas** — Dataset handling and exploration.
- **Scikit-learn** — Machine learning, TF-IDF, and model evaluation.
- **TF-IDF Vectorizer** — Text feature extraction.
- **Logistic Regression** — Text classification.
- **Joblib** — Saving and loading trained model components.
- **Regular Expressions (Regex)** — Rule-based warning detection.
- **GitHub** — Version control and project documentation.
- **Google Colab** — Model development and experimentation.
- **ChatGPT** — Development assistance and learning support.

## Repository Structure

```text
codomax-ai-ml-internship/
│
├── Module-1/
│   ├── learning-notes.md
│   └── python-programs/
│
├── Module-2/
│   ├── student_grade_calculator.py
│   └── README.md
│
├── Module-3/
│   ├── data-analysis.ipynb
│   └── README.md
│
├── Module-4/
│   ├── machine-learning-model.ipynb
│   └── README.md
│
├── Module-5/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   └── learning-notes.md
│
└── README.md
```

*This is a suggested structure. Keep only the files and folders that actually exist in your repository, and change the filenames to match your project.*

## How to Run the Job Scam Risk Detector

### Prerequisites

- Python installed on your computer.
- Required Python libraries.
- The trained model and TF-IDF vectorizer files.

### Step 1: Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 2: Check the Required Files

Make sure the following files are available in the same folder as `app.py`:

```text
app.py
job_scam_model.pkl
tfidf_vectorizer.pkl
requirements.txt
```

### Step 3: Run the Application

```bash
python app.py
```

### Step 4: Enter Job-Posting Text

Enter a job description when prompted. The application will analyse the text and display its classification, warning indicators, and safety recommendations.

**Note:** This is a local command-line application, not a publicly hosted web application.

## Limitations

- Predictions depend on the dataset and patterns learned during training.
- The model may not recognize new or previously unseen scam techniques.
- A genuine job posting may be flagged as suspicious.
- A fraudulent job posting may be classified as lower-risk.
- Rule-based warnings only detect the predefined patterns included in the code.
- The displayed class probability is a model estimate, not a guaranteed real-world scam probability.
- The application does not independently verify employers or job postings against external databases.
- The project is an educational prototype and should not be used as the sole basis for employment decisions.

## Future Improvements

- Develop a user-friendly web interface using Streamlit or Flask.
- Evaluate the model on additional and more recent job-posting data.
- Improve text preprocessing and model evaluation.
- Add explainable indicators showing which text patterns influenced a prediction.
- Integrate a trusted external verification service, if available.
- Add automated testing and improve error handling.
- Deploy the application after security and reliability testing.

## Key Learnings

Through these internship modules, I gained experience in:

- Python programming fundamentals.
- Problem-solving through a Python mini-project.
- Data analysis and visualization.
- Machine learning workflows and model evaluation.
- Text classification using NLP and TF-IDF.
- Saving and loading machine learning models.
- Developing a practical Python application.
- Using AI tools to support learning and development.
- Writing project documentation and maintaining a GitHub repository.

## About Me

I am a Computer Science graduate and aspiring IT professional interested in Python programming, Artificial Intelligence, Machine Learning, and practical software development.

This repository represents my learning journey, hands-on practice, and continuous efforts to improve my technical skills through project-based learning.

## Acknowledgement

I would like to thank **Codomax Digital Solutions** for providing the opportunity to explore AI and Machine Learning concepts through internship-based learning activities.

---

⭐ Thank you for visiting my repository!

**If you find this project interesting, feel free to explore the code and share your feedback.**
