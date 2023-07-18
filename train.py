"""
Training script for DMD
"""
from run import DMD_run

DMD_run(model_name='dmd', dataset_name='mosi', is_tune=False, seeds=[1111], model_save_dir="./model",
         res_save_dir="./result", log_dir="./log", mode='train', is_distill=True)
