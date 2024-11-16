import os
import sys
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from src.utils import  save_object
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from xgboost import XGBClassifier

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            xgb_model = XGBClassifier(learning_rate= 0.1, max_depth= 7, n_estimators= 300,scale_pos_weight=0.778056/  0.221944)
            xgb_model.fit(x_train,y_train)

            y_pred=xgb_model.predict(x_test)
            y_pred_proba=xgb_model.predict_proba(x_test)[:,1]

            accuracy = accuracy_score(y_test, y_pred)
            conf_matrix = confusion_matrix(y_test, y_pred)
            class_report = classification_report(y_test, y_pred)
            roc_auc = roc_auc_score(y_test, y_pred_proba)
                
            logging.info(f"Accuracy: {accuracy}")
            logging.info(f"ROC AUC: {roc_auc}")
            logging.info(f"Confusion Matrix:\n{conf_matrix}")
            logging.info(f"Classification Report:\n{class_report}")
            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=xgb_model)
           
        except Exception as e:
            raise CustomException(e, sys)
