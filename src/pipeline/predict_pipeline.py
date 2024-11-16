import sys,os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import numpy as np
from sklearn.metrics import roc_auc_score

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features,true_labels=None):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            numerical_columns = ['person_age', 'person_income', 'person_emp_exp', 'loan_amnt', 
                                 'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length', 
                                 'credit_score']
            for column in numerical_columns:
                features[column] = np.log1p(features[column])  

            data_scaled=preprocessor.transform(features)
            predictions=model.predict(data_scaled)
            
            return predictions
        
        except Exception as e:
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,
                 person_age:float,
                 person_income:float,
                 person_emp_exp:int,
                 loan_amnt:float,
                 loan_int_rate:float,
                 loan_percent_income:float,
                 cb_person_cred_hist_length:float,
                 credit_score:int,
                 person_gender:str,
                 person_education:str,
                 person_home_ownership:str,
                 loan_intent:str,
                 previous_loan_defaults_on_file:str
                 ):
        self.person_age=person_age
        self.person_income=person_income
        self. person_emp_exp= person_emp_exp
        self.loan_amnt=loan_amnt
        self.loan_int_rate=loan_int_rate
        self.loan_percent_income=loan_percent_income
        self.cb_person_cred_hist_length=cb_person_cred_hist_length
        self.credit_score=credit_score
        self.person_gender=person_gender
        self.person_education=person_education
        self.person_home_ownership=person_home_ownership
        self.loan_intent=loan_intent
        self.previous_loan_defaults_on_file=previous_loan_defaults_on_file

    def get_data_as_dataFrame(self):
        try:
            custom_data_input_dict={
                "person_age":[self.person_age],
                "person_income":[self.person_income],
                "person_emp_exp":[self.person_emp_exp],
                "loan_amnt":[self.loan_amnt],
                "loan_int_rate":[self.loan_int_rate],
                "loan_percent_income":[self.loan_percent_income],
                "cb_person_cred_hist_length":[self.cb_person_cred_hist_length],
                "credit_score":[self.credit_score],
                "person_gender":[self.person_gender],
                "person_education":[self.person_education],
                "person_home_ownership":[self.person_home_ownership],
                "loan_intent":[self.loan_intent],
                "previous_loan_defaults_on_file":[self.previous_loan_defaults_on_file]
            } 

            df=pd.DataFrame(custom_data_input_dict)
            return df
        except Exception as e:
            raise CustomException(e,sys)   
                