import argparse
from pkgutil import get_data
import numpy as np
import pandas as pd
fro src.utils.all_utils import read_yaml

def get_data(config_path):
    config = read_yaml(conig_path)
    print(config)




if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default='onfig/config.yaml')
    parsed_args = args.parse_args()
    get_data(config_path = parsed_args.config)