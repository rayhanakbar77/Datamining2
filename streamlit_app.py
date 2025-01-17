import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import os
import zipfile
import io  # Add this import statement
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

dataset_dir = 'dataset'
target_file = '/workspaces/Datamining2/student-study-performance.zip'

# Debugging information
st.write(f"Current working directory: {os.getcwd()}")
st.write(f"Files in the directory: {os.listdir(os.path.dirname(os.path.abspath(target_file)))}")

# Check if the file exists
if os.path.exists(target_file):
    with zipfile.ZipFile(target_file, 'r') as extracting:
        extracting.extractall(dataset_dir)
else:
    st.error(f"File not found: {target_file}")
    st.stop()

df = pd.read_csv(f'{dataset_dir}/study_performance.csv')

# Display the dataframe
st.write(df.head())

# Display dataframe info
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

# Display dataframe shape
st.write(f"Dataframe shape: {df.shape}")

df.describe()
df.isnull().sum()
df.duplicated().sum()

df = df.rename(columns={
    df.columns[1]: 'group',
    df.columns[2]: 'parent_education_Level',
    df.columns[4]: 'test_preparation'
})

df['total_score'] = df['math_score'] + df['reading_score'] + df['writing_score']
df['mean_score'] = round(df['total_score'] / 3, 1)

# Display the updated dataframe
st.write(df.head())

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
object_cols = df.select_dtypes(exclude=['int64', 'float64']).columns

# Plot histograms for numeric columns
f, ax = plt.subplots(len(numeric_cols), 1, figsize=(15, 15))
ax = ax.flatten()

for index, cols in enumerate(numeric_cols):
    sns.histplot(data=df, x=cols, ax=ax[index], kde=True)
    ax[index].set_title(cols)

plt.tight_layout()
st.pyplot(f)

# Plot boxplots for numeric columns
f, ax = plt.subplots(len(numeric_cols), 1, figsize=(15, 15))
ax = ax.flatten()

for index, cols in enumerate(numeric_cols):
    sns.boxplot(data=df, x=cols, ax=ax[index])
    ax[index].set_title(cols)

plt.tight_layout()
st.pyplot(f)

# Plot countplots for object columns
f, ax = plt.subplots(len(object_cols), 1, figsize=(15, 20))
ax = ax.flatten()

for index, cols in enumerate(object_cols):
    sns.countplot(data=df, x=cols, ax=ax[index])
    ax[index].set_title(cols)

plt.tight_layout()
st.pyplot(f)

# Plot boxplots for numeric columns by group
f, ax = plt.subplots(len(numeric_cols), 1, figsize=(15, 30))
ax = ax.flatten()

for index, cols in enumerate(numeric_cols):
    sns.boxplot(data=df, x='group', y=cols, ax=ax[index])
    ax[index].set_title(cols)

plt.tight_layout()
st.pyplot(f)

# Plot boxplots for numeric columns by gender
f, ax = plt.subplots(len(numeric_cols), 1, figsize=(15, 30))
ax = ax.flatten()

for index, cols in enumerate(numeric_cols):
    sns.boxplot(data=df, x='gender', y=cols, ax=ax[index])
    ax[index].set_title(cols)

plt.tight_layout()
st.pyplot(f)

# Plot heatmap for numeric columns correlation
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='Reds')
st.pyplot()

def Data_transform(df):
    df = df.drop(['parent_education_Level'], axis=1)
    df['gender'] = df['gender'].map({'male': 1, 'female': 0})
    df['group'] = df['group'].map({'group A': 1, 'group B': 2, 'group C': 3, 'group D': 4, 'group E': 5})
    df['lunch'] = df['lunch'].map({'standard': 1, 'free/reduced': 0})
    df['test_preparation'] = df['test_preparation'].map({'none': 0, 'completed': 1})
    return df

df = Data_transform(df)

X = df.drop(columns=['math_score'], axis=1)
y = df['math_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

LR = LinearRegression()
LR.fit(X_train, y_train)
pred_lr = LR.predict(X_test)

st.write(f'MAE : {mean_absolute_error(y_test, pred_lr)}')
st.write(f'MSE : {mean_squared_error(y_test, pred_lr)}')
st.write(f'r2_score : {r2_score(y_test, pred_lr)}')

plt.scatter(y_test, pred_lr)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
st.pyplot()
