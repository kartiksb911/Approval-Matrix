import os,sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import train_test_split_data


@dataclass
class DataIngestionConfig:
        train_data_path=os.path.join("artifacts","train.csv")
        test_data_path=os.path.join("artifacts","test.csv")
        raw_data_path=os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # Load the dataset
            df = pd.read_csv("notebook/data/loan_data.csv")
            logging.info("reading the csv data")
             # Ensure that the directory for saving files exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

             # Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("splitting the data")
            # Split the data into training and testing datasets
            train_data,test_data=train_test_split_data(df,0.2)
            # Save train and test data to CSV
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            # Return paths of the train and test datasets
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )        
        except Exception as e:
            # Catch and log any exceptions that occur during data ingestion
            raise CustomException(e,sys)
        
if(__name__=="__main__"):
    # Initialize and run the data ingestion process
    obj=DataIngestion()
    obj.initiate_data_ingestion()
        