import os

import sys
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score 
#from sklearn.modelselection import GridSearchCV
from src.exception import CustomException

def save_object(file_path, object):
    '''
    This function saves an object to a pickle file.
    Parameters:
    file_path: The path where the object needs to be saved.
    object: The object to be saved.
    '''
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(object, file_obj)
            print(f'Object saved successfully at: {file_path}')

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models):#,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            #para=param[list(models.keys())[i]]

            #gs = GridSearchCV(model,para,cv=3)
            #gs.fit(X_train,y_train)

            #model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)