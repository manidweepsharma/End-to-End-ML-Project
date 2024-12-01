import os

import sys
import numpy as np
import pandas as pd
import dill

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