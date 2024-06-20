import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from lime.lime_tabular import LimeTabularExplainer

class TransactionRiskAssessorExplainable:
    def __init__(self, transaction_data):
        self.transaction_data = transaction_data
        self.model = RandomForestClassifier(n_estimators=100)
        self.explainer = LimeTabularExplainer(self.transaction_data.values, feature_names=self.transaction_data.columns, class_names=['low_risk', 'high_risk'])

    def train_model(self):
        X = self.transaction_data.drop(['risk_level'], axis=1)
        y = self.transaction_data['risk_level']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def assess_transaction_risk(self, transaction_data):
        prediction = self.model.predict(transaction_data)
        explanation = self.explainer.explain_instance(transaction_data.values, self.model.predict_proba, num_features=5)
        return prediction, explanation

    def update_model(self, new_transaction_data):
        self.transaction_data = pd.concat([self.transaction_data, new_transaction_data])
        self.train_model()
