import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.impute import SimpleImputer

# Read the CSV file
df = pd.read_csv('/content/drive/MyDrive/fake_bills.csv', sep=";")
print(df)

# Label encoding for 'margin_low' and mapping 'is_genuine' to 0 and 1
# label encoder converts categorical labels into numerical form
# True se mapira vo 1 a false vo 0
le = LabelEncoder()
df['margin_low'] = le.fit_transform(df['margin_low'])
df['is_genuine'] = df['is_genuine'].map({True: 1, False: 0})
df['margin_low'].unique()
print(df)

# Impute missing values in 'margin_low' with mean
imputer = SimpleImputer(strategy='mean')
df[['margin_low']] = imputer.fit_transform(df[['margin_low']])

# Impute missing values in the entire DataFrame with mean
imputer = imputer.fit(df)
df = imputer.transform(df)
print(df)

# Split the data into features (X) and target variable (y)
X = df.iloc[:, 1:]
y = df['is_genuine'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the KNeighborsClassifier model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Test accuracy: {accuracy:.2f}')

# Create and plot the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
conf_df = pd.DataFrame(conf_matrix, index=sorted(set(y)), columns=sorted(set(y)))

plt.figure(figsize=(8, 6))
sns.heatmap(conf_df, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title("Confusion matrix")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
