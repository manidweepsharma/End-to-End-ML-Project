import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int
    ):
        self.gender = gender
        self.__dict__['race/ethnicity'] = race_ethnicity
        self.__dict__['parental level of education'] = parental_level_of_education
        self.lunch = lunch
        self.__dict__['test preparation course'] = test_preparation_course
        self.__dict__['reading score'] = reading_score
        self.__dict__['writing score'] = writing_score



    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.__dict__['race/ethnicity']],
                "parental level of education": [self.__dict__['parental level of education']],
                "lunch": [self.lunch],
                "test preparation course": [self.__dict__['test preparation course']],
                "reading score": [self.__dict__['reading score']],
                "writing score": [self.__dict__['writing score']],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)