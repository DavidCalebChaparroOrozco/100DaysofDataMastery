# Import necessary libraries
import pandas as pd
import numpy as np

def load_titanic_dataset():
    import seaborn as sns
    return sns.load_dataset('titanic')

def overview(data):
    print("=".center(50, "="))
    print(f"\nTitanic Dataset Overview")
    print(f"Shape: {data.shape}")
    print("=".center(50, "="))

    print("Information about the features:")
    print(data.info())
    print("=".center(50, "="))

    print("Basic statistics check:")
    print(data.describe())
    print("=".center(50, "="))

    print("\nChecking the number of unique values:")
    unique_counts = {col: data[col].nunique() for col in data.columns}
    unique_data = pd.DataFrame(unique_counts, index=["Unique Count"]).T
    print(unique_data)

    print("\nCheck for missing values:")
    print(data.isnull().sum())
    print("=".center(50, "="))

def remove_duplicates(data):
    print("\nSTEP 1: Checking for Duplicates")
    print("Number of duplicate rows before:", data.duplicated().sum())
    data = data.drop_duplicates()
    print("Number of duplicate rows after:", data.duplicated().sum())
    print("=".center(50, "="))
    return data

def handle_missing_values(data):
    print("\nSTEP 2: Handling Missing Values")

    # Fill missing 'age' by median in pclass + who group
    print("\nAge missing values before:", data['age'].isnull().sum())
    data['age'] = data.groupby(['pclass', 'who'])['age'].transform(
        lambda x: x.fillna(x.median()))
    print("Age missing values after:", data['age'].isnull().sum())

    # Drop 'deck' due to high missing rate
    print("\nDropping 'deck' column due to excessive missing values (77%)")
    if 'deck' in data.columns:
        data.drop('deck', axis=1, inplace=True)

    # Fill missing 'embarked' and 'embark_town' with mode
    print("\nEmbarked missing values before:", data['embarked'].isnull().sum())
    mode_port = data['embarked'].mode()[0]
    data['embarked'] = data['embarked'].fillna(mode_port)
    data['embark_town'] = data['embark_town'].fillna(mode_port)
    print("Embarked missing values after:", data['embarked'].isnull().sum())
    print("=".center(50, "="))
    return data

def fix_formatting(data):
    print("\nSTEP 3: Standardizing Formats")
    data['embark_town'] = data['embark_town'].str.title()
    data['who'] = data['who'].str.lower()
    print("\nStandardized 'embark_town' and 'who' columns:")
    print("Unique embark_town:", data['embark_town'].unique())
    print("Unique who:", data['who'].unique())
    print("=".center(50, "="))
    return data

def correct_data_types(data):
    print("\nSTEP 4: CORRECTING DATA TYPES")
    data['pclass'] = data['pclass'].astype('object')
    # Optional:
    # data['survived'] = data['survived'].astype(bool)
    print("Data types after conversion:")
    print(data.dtypes)
    print("=".center(50, "="))
    return data

def check_outliers(data):
    print("\nSTEP 5: Checking for Outliers")
    print("Age range:", data['age'].min(), "to", data['age'].max())
    print("Fare range:", data['fare'].min(), "to", data['fare'].max())
    print("""
NOTE ABOUT FARES:
- $0 fares might represent crew (but Titanic dataset is passengers only)
- $512 is extremely high but plausible for luxury suites
- We'll keep all fares as they represent real pricing tiers
""")
    print("=".center(50, "="))
    return data

def drop_irrelevant_columns(data, columns_to_drop=None):
    print("\nSTEP 6: Removing Irrelevant Columns")
    if columns_to_drop:
        data = data.drop(columns=columns_to_drop, axis=1)
        print(f"Dropped columns: {columns_to_drop}")
    else:
        print("No irrelevant columns specified to drop.")
    print("=".center(50, "="))
    return data

def final_report(data):
    print("\nFinal Data Quality REPORT")
    print("Missing values:")
    print(data.isnull().sum())
    print("\nData types:")
    print(data.dtypes)
    print("\nDataset shape:", data.shape)
    print("=".center(50, "="))
    return data

def save_clean_data(data, path='outputs/titanic_cleaned.csv'):
    data.to_csv(path, index=False)
    print(f"\nCleaned dataset saved to {path}")