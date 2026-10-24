import joblib
import re

# Load the trained ML model and TF-IDF vectorizer
model = joblib.load("job_scam_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")


def identify_warning_signs(job_text):
    """Find potential warning indicators in a job description."""

    text = job_text.lower()
    warnings = []

    warning_patterns = {
        "Possible upfront payment request": [
            r"registration fee",
            r"processing fee",
            r"upfront payment",
            r"security deposit",
            r"pay.{0,30}(fee|deposit)"
        ],
        "Unrealistic job guarantee claim": [
            r"guaranteed job",
            r"100% job guarantee",
            r"no interview required"
        ],
        "Request for sensitive information": [
            r"send.{0,30}(password|otp)",
            r"share.{0,30}(bank password|otp)"
        ]
    }

    for category, patterns in warning_patterns.items():
        if any(re.search(pattern, text) for pattern in patterns):
            warnings.append(category)

    return warnings


def assess_job(job_text):
    """Predict a job label and show supporting information."""

    if not job_text.strip():
        print("Error: Please enter a job description.")
        return

    # Transform the input using the saved vectorizer
    job_vector = tfidf.transform([job_text])

    # Predict the class
    prediction = int(model.predict(job_vector)[0])

    # Calculate the model's estimated class probability
    probabilities = model.predict_proba(job_vector)[0]
    class_index = list(model.classes_).index(prediction)
    probability = probabilities[class_index]

    # Identify possible warning signs
    warnings = identify_warning_signs(job_text)

    print("\n" + "=" * 48)
    print("       AI-BASED JOB SCAM RISK DETECTOR")
    print("=" * 48)

    if prediction == 1:
        print("ML Prediction : Potentially Suspicious")
    else:
        print("ML Prediction : Lower-Risk Classification")

    print(f"Model probability estimate: {probability:.2%}")

    print("\nPotential Warning Indicators:")

    if warnings:
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("- No listed warning patterns detected.")

    print("\nSafety Recommendations:")
    print("1. Verify the vacancy on the official company website.")
    print("2. Check the recruiter's identity and email address.")
    print("3. Be cautious about requests for recruitment fees.")
    print("4. Never share passwords or OTPs with recruiters.")
    print("5. Verify the job independently before proceeding.")

    print("\nImportant Disclaimer:")
    print("This tool provides an automated risk assessment.")
    print("Warning indicators are not proof of fraud.")
    print("Model probabilities are not guaranteed real-world")
    print("probabilities. Always verify the employer independently.")

    print("=" * 48)


if __name__ == "__main__":
    print("Welcome to Job Scam Risk Detector!")

    description = input(
        "\nPaste the job description you want to check:\n"
    )

    assess_job(description)
