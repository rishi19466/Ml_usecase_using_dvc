import argparse
import os
from pkgutil import get_data
import numpy as np
import pandas as pd
from src.utils.all_utils import read_yaml, create_directory

def get_data(config_path):
    config = read_yaml(config_path)
    data_path = config['data_source']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file_path = config['artifacts']['raw_local_file']
    # raw_local_file_path = os.path.join(raw_local_dir,raw_local_file)
    #
    df = pd.read_csv(data_path, sep=';')
    # print(data.head())
    # data.to_csv(raw_local_file_path, sep =",", index = False)

# save dataset in the local directory
# Create path for directorty
    artifacts_dir = config["artifacts"]['artifacts_dir']
    raw_local_dir = config["artifacts"]['raw_local_dir']
    raw_local_file = config["artifacts"]['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)

    create_directory(dirs= [raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    
    df.to_csv(raw_local_file_path, sep=",", index=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)