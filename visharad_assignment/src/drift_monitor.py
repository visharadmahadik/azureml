import pandas as pd
import argparse
from sklearn.metrics import mean_squared_error

parser = argparse.ArgumentParser()
parser.add_argument('--old_data', type=str)
parser.add_argument('--new_data', type=str)
parser.add_argument('--report_output', type=str)
args = parser.parse_args()

old_df = pd.read_csv(args.old_data)
new_df = pd.read_csv(args.new_data)

mse = mean_squared_error(old_df.mean(), new_df.mean())

with open(f"{args.report_output}/drift_report.txt", "w") as f:
    f.write(f"MSE Drift: {mse}")
