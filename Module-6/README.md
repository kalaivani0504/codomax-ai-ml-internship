# AI-Based Job Scam Risk Detector

### Final AI & Machine Learning Project | Codomax Digital Solutions Internship

## 1.Project Overview

The **AI-Based Job Scam Risk Detector** is a Python-based machine learning application designed to analyse job-posting text and identify potentially suspicious job listings.

The project uses Natural Language Processing (NLP) techniques to process job descriptions and a trained Logistic Regression model to classify job postings. It also includes rule-based warning checks to identify predefined suspicious patterns and provide basic safety recommendations.

The main goal is to help job seekers become more aware of potential risks when evaluating job advertisements.

**Note:** This project is an educational prototype. Its predictions are not a guarantee that a job posting is genuine or fraudulent.

## 2.Problem Statement

Online job platforms make it easier for job seekers to discover employment opportunities. However, fraudulent job advertisements may mislead applicants through fake offers, requests for upfront payments, misleading promises, and other suspicious practices.

Manually checking every job posting can be difficult and time-consuming.

This project aims to address this problem by analysing job-posting text using machine learning and predefined warning rules. It provides an initial risk assessment to help users identify job advertisements that may require further verification.

## 3.Project Objectives

The main objectives of this project are:

- To develop a machine learning application for analysing job-posting text.
- To apply Natural Language Processing techniques to text classification.
- To convert text into numerical features using TF-IDF.
- To train and evaluate a Logistic Regression classification model.
- To identify predefined warning indicators using rule-based checks.
- To provide basic safety recommendations for job seekers.
- To understand the practical implementation of a machine learning workflow.
- To document and publish the project using GitHub.

## 4.Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development and data processing |
| Pandas | Dataset handling and exploration |
| Scikit-learn | Machine learning and model evaluation |
| TF-IDF Vectorizer | Converts text into numerical features |
| Logistic Regression | Classifies job-posting text |
| Joblib | Saves and loads trained model components |
| Regular Expressions (Regex) | Identifies predefined warning patterns |
| Google Colab | Model development and experimentation |
| GitHub | Source code management and documentation |
| ChatGPT | Coding assistance, research, and learning support |

**AI tool integration:** ChatGPT was used as a development assistant. An external generative AI API is not integrated into the application.

## 5.How It Works

The application follows these main steps:

1. **User Input:** The user enters a job description or job-posting text.
2. **Text Processing:** The text is prepared for feature extraction.
3. **Feature Extraction:** The TF-IDF vectorizer converts the text into numerical features.
4. **Machine Learning Prediction:** The trained Logistic Regression model predicts a class based on the extracted features.
5. **Warning Detection:** Rule-based checks look for predefined suspicious patterns, such as requests for registration fees or upfront payments.
6. **Safety Recommendations:** The application displays basic precautions relevant to the detected warning indicators.
7. **Result Display:** The application shows the model's classification and the available warning information.

### Workflow

```text
Job Description
       |
       v
Text Processing
       |
       v
TF-IDF Feature Extraction
       |
       v
Trained Logistic Regression Model
       |
       v
Classification Result
       |
       v
Rule-Based Warning Checks
       |
       v
Safety Recommendations
```

The machine learning model and rule-based warning checks are separate components. A warning indicator does not independently prove that a job is fraudulent.

## 6.Model Results

The model was evaluated using a held-out test dataset.

| Evaluation Metric | Result |
|---|---:|
| Model Accuracy | 96.88% |
| Recall for the Fraudulent Class | 81% |

### Understanding the Results

**Accuracy — 96.88%**

The model correctly classified approximately 96.88% of the examples in the test dataset.

**Fraudulent-Class Recall — 81%**

The model identified approximately 81% of the fraudulent examples in the test dataset.

These results represent performance on the dataset used during evaluation. They do not guarantee the same performance on new or real-world job advertisements.

The model may produce false positives, where genuine jobs are flagged as suspicious, and false negatives, where fraudulent jobs are classified as lower-risk.

The probability estimate displayed by the application is a model output, not a verified real-world probability that a job is fraudulent.

## 7.Installation

### Prerequisites

Before running the application, ensure that you have:

- Python installed on your computer.
- Basic knowledge of running Python programs.
- The required Python libraries.
- The trained model and TF-IDF vectorizer files.

### Step 1: Clone the Repository

If the project is stored in its own GitHub repository, run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual repository URL.

Alternatively, download the project files and open the project folder on your computer.

### Step 2: Open the Project Folder

```bash
cd Module-6
```

Run this command only if your terminal is in the parent directory containing `Module-6`.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Check the Required Files

Ensure that `app.py`, `job_scam_model.pkl`, and `tfidf_vectorizer.pkl` are available at the paths expected by the application.

If the model files are stored in another folder, update the paths in the code accordingly.

## 8.How to Run the Application

Once the dependencies and required model files are available, open a terminal in the project directory.

Run:

```bash
python app.py
```

Follow the prompts displayed in the terminal.

Enter a job description when requested. The application will process the text and display the classification result, predefined warning indicators, and relevant safety recommendations.

### Example Input

```text
Job Title: Data Entry Executive

Job Description:
Work from home opportunity.
Applicants must pay a registration fee before joining.
```

### Expected Behaviour

The application processes the supplied text and displays the model's prediction and any warning indicators detected by its rules.

**Important:** The example above is illustrative. The actual prediction and warning output depend on the trained model, the application's implementation, and the text entered.

## 9.Screenshots

Screenshots of the application can be added here to demonstrate its functionality.

### Screenshot 1: Application Input and Prediction

Add a screenshot showing the application running and displaying a prediction.

Suggested file path:

Module-6/app_output-1.png.png

### Screenshot 2: Warning Indicators and Safety Recommendations

Add a screenshot showing the warning indicators and safety recommendations displayed by the application.

Suggested file path:

`Module-6/screenshots/app-output-2.png`

![Application Output 2](screenshots/app-output-2.png)

**Note:** Replace these placeholders with actual screenshots captured from your application. Ensure the image filenames and paths match the files uploaded to GitHub.

## 10.Limitations

The project has the following limitations:

- Predictions depend on the dataset and patterns learned during training.
- The model may not recognize new or previously unseen scam techniques.
- Genuine job advertisements may be classified as suspicious.
- Fraudulent job advertisements may be classified as lower-risk.
- Rule-based warnings detect only the predefined patterns included in the code.
- The application does not independently verify employers or job advertisements against external databases.
- The model's probability estimate is not necessarily a calibrated real-world risk probability.
- The project has not been established as a reliable replacement for independent verification.
- The application is an educational prototype and should not be used as the sole basis for employment decisions.

Users should independently verify employers, check official company websites, and avoid sending money or sharing sensitive information with unverified recruiters.

## 11.Future Improvements

The project could be improved through the following enhancements:

- Develop a user-friendly web interface using Streamlit or Flask.
- Evaluate the model on additional and more recent job-posting datasets.
- Improve text preprocessing and model evaluation.
- Add automated tests and better error handling.
- Provide clearer explanations of the text patterns associated with a prediction.
- Integrate a trusted external verification service, where available.
- Improve model monitoring and evaluate performance on unseen data.
- Deploy the application after appropriate security and reliability testing.

## 12.Learning Outcomes

Through this project, I gained practical experience in:

- Python application development.
- Natural Language Processing fundamentals.
- Text preprocessing and TF-IDF feature extraction.
- Training a Logistic Regression classifier.
- Splitting data into training and testing sets.
- Evaluating machine learning model performance.
- Saving and loading trained models using Joblib.
- Implementing rule-based warning checks.
- Providing basic safety recommendations.
- Documenting and maintaining a project on GitHub.
- Using AI tools to support coding, research, and learning.

## Project Information

**Project Title:** AI-Based Job Scam Risk Detector

**Internship:** AI & Machine Learning Internship

**Organization:** Codomax Digital Solutions

**Project Type:** Machine Learning / Text Classification

**Programming Language:** Python

**Repository:** Add your final GitHub repository link here.


⭐ Thank you for visiting my project!

Feedback and suggestions for improvement are welcome.
