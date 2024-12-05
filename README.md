# Loan Approval Prediction System
## Introduction:-
This end-to-end project aims to develop a `Loan Approval Prediction System` that utilizes machine learning models to predict whether a loan application will be approved or rejected. The system is powered by the `XGBoost Classifier`, a powerful machine learning model, which predicts the loan status based on various factors such as personal details, loan information, and financial history.

## Features
* Data Preprocessing:This project includes data collection , data analyis,`log Transformation`,`feature scaling` and `one hot encoding` for categorical data.
* Model Selection:Various regression models are evaluated,including `Logistic regression`,`Random Forest`,`Decision Tree`,`XGBoost Classifier` to determine the best performing algorithm for approval prediction.
* Performance Metrics:use `ROC_AUC`,`Accuracy`,`Confusion Matrix`to ensure reliable prediction.
* Web Application: A user friendly web app built with `Flask` allow user to input car details and recieve instantaneous price prediction.
* Deployed: Deployed the app to `Render` for easy access and hosting.
## Technology Used
* machine learning model-->`XGBoost Classifier`
* web framework-->`Flask` and `html`
* Version Control-->`Git` and `Github`
* code editors-->`jupyter lab `and `Vscode`
* python library-->`numpy`,`Pandas`,`Matplotlib`,`seaborn`,`sklearn`
## Usage
#### Clone the Repository

To clone this repository, run the following command:

```
git clone https://github.com/kartiksb911/Approval-Matrix.git
```
#### Create a new environment for the project and activate it.
```
 conda create -p venv python=3.10 -y
 conda activate venv/
```
#### Install all necessary requirements
``` 
pip install -r requirements.txt
```
#### Train the Model
Run the following code to start the data ingestion process and train the model:

``` 
python -m src.components.data_ingestion
```
* After running this code, the model will be trained.

## Final Report
* `Accuracy` of the best_model(`XGBoost Classifier`) is `92%`
* `ROC_AUC` is `97%`
## Web App
![Image Alt](https://github.com/kartiksb911/Approval-Matrix/blob/48d95e6c0c327a80eb01738b4b22fe160faddad4/static/Screenshot%20(106).png)
## Deployment
![Image Alt](https://github.com/kartiksb911/Approval-Matrix/blob/48d95e6c0c327a80eb01738b4b22fe160faddad4/static/Screenshot%20(108).png)
## EDA
![Image Alt](https://github.com/kartiksb911/Approval-Matrix/blob/48d95e6c0c327a80eb01738b4b22fe160faddad4/static/Univariate_Num%20(3).png)
![Image Alt](https://github.com/kartiksb911/Approval-Matrix/blob/48d95e6c0c327a80eb01738b4b22fe160faddad4/static/Log%20transformation%20(1).png)
![Image Alt](https://github.com/kartiksb911/Approval-Matrix/blob/48d95e6c0c327a80eb01738b4b22fe160faddad4/static/Univariate_Categorcal%20(3).png)
## 🔗 Links
[![Github](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/kartiksb911)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kartik-bhardwaj-07b7282b7/)


