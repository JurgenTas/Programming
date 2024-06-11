import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, KBinsDiscretizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(123)
n = 1000
target = np.random.randint(0, 2, size=n)  # Binary target variable
categorical1 = np.random.choice(['A', 'B'], size=n)
categorical2 = np.random.choice(['X', 'Y'], size=n)
numeric1 = np.random.uniform(0, 100, size=n)
numeric2 = np.random.normal(50, 10, size=n)
numeric3 = np.random.exponential(2, size=n)
numeric4 = np.random.poisson(3, size=n)
numeric5 = np.random.lognormal(1, 0.5, size=n)

# Create the DataFrame
data = {
    'target': target,
    'categorical1': categorical1,
    'categorical2': categorical2,
    'numeric1': numeric1,
    'numeric2': numeric2,
    'numeric3': numeric3,
    'numeric4': numeric4,
    'numeric5': numeric5
}
df = pd.DataFrame(data)

# Identify categorical and numerical columns
categorical_cols = ['categorical1', 'categorical2']
numeric_cols = ['numeric1', 'numeric2', 'numeric3', 'numeric4', 'numeric5']

# Bin numerical columns
numeric_transformer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')

# One-hot encode all features
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
numeric_transformer_ohe = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_cols),
        ('num', Pipeline([('binner', numeric_transformer), ('encoder', numeric_transformer_ohe)]), numeric_cols)
    ])

# Create a pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LogisticRegression())
])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), 
                                                    df['target'], test_size=0.2, random_state=123)

# Fit the pipeline
pipeline.fit(X_train, y_train)

# Evaluate the model using ROC curve
y_pred_proba = pipeline.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Model')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()
