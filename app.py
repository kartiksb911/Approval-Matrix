from flask import Flask, render_template, request, jsonify
from src.pipeline.predict_pipeline import PredictPipeline, CustomData 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        person_age = float(request.form['person_age'])
        person_income = float(request.form['person_income'])
        person_emp_exp = int(request.form['person_emp_exp'])
        loan_amnt = float(request.form['loan_amnt'])
        loan_int_rate = float(request.form['loan_int_rate'])
        loan_percent_income = float(request.form['loan_percent_income'])
        cb_person_cred_hist_length = float(request.form['cb_person_cred_hist_length'])
        credit_score = int(request.form['credit_score'])
        person_gender = request.form['person_gender']
        person_education = request.form['person_education']
        person_home_ownership = request.form['person_home_ownership']
        loan_intent = request.form['loan_intent']
        previous_loan_defaults_on_file = request.form['previous_loan_defaults_on_file']

        custom_data = CustomData(
            person_age=person_age,
            person_income=person_income,
            person_emp_exp=person_emp_exp,
            loan_amnt=loan_amnt,
            loan_int_rate=loan_int_rate,
            loan_percent_income=loan_percent_income,
            cb_person_cred_hist_length=cb_person_cred_hist_length,
            credit_score=credit_score,
            person_gender=person_gender,
            person_education=person_education,
            person_home_ownership=person_home_ownership,
            loan_intent=loan_intent,
            previous_loan_defaults_on_file=previous_loan_defaults_on_file
        )

        predict_pipeline = PredictPipeline()
        data_df = custom_data.get_data_as_dataFrame()
        prediction = predict_pipeline.predict(data_df)

        loan_status = "Approved" if prediction[0] == 1 else "Rejected"

        return render_template('index.html', prediction_text=f"Loan Status: {loan_status}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
