import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    """
    Class to configure data ingestion parameters.
    """
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    """
    Class to manage data ingestion and preprocessing.
    """

    def __init__(self):
        self.ingestion_config =DataIngestionConfig()

    
    def initiate_data_ingestion(self):
        """
        Method to initiate data ingestion.
        """
        logging.info("Initiating data ingestion")

        try:
            pass
            df = pd.read_csv('Notebooks\data\StudentsPerformance.csv')
            logging.info("Read the data as dataframe...")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Split Initialized...")
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingestion completed successfully...")

            return (
                #self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()




