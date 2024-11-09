from src.logger import logging
from src.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("the logging has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("custom error")
        raise CustomException (e,sys)    
