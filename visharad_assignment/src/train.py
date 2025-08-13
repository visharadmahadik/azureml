import pandas as pd
import joblib
import argparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

parser = argparse.ArgumentParser()
parser.add_argument('--input_data', type=str)
parser.add_argument('--model_output', type=str)
args = parser.parse_args()

df = pd.read_csv(args.input_data)
X = df.drop('species', axis=1)
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, f"{args.model_output}/model.pkl")
from azureml.core.model import Model

# Register the model
model = Model.register(
    workspace=ws,
    model_path='outputs/model.pkl',  # Local path to the model file
    model_name='ganesh_registered_model',  # Name to register the model under
    description='My model trained with scikit-learn',
    tags={'type': 'Regression', 'framework': 'scikit-learn'}
)
