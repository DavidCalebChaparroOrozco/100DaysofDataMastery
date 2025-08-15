# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.feature_selection import mutual_info_regression

# 1. Data Cleaning Utilities
# Convert column names to CamelCas
def clean_column_names(data):
    def to_camel_case(name):
        parts = name.replace("-", " ").replace("_", " ").split()
        return "".join([p.capitalize() if not p.isupper() else p for p in parts])
    
    data.columns = [to_camel_case(col) for col in data.columns]
    return data

# Clean missing values with smart imputatio
def handle_missing_values(data):
    # Fill postal codes with city-specific mode
    data['PostalCode'] = data.groupby('City')['PostalCode'].transform(
        lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 0)
    )
    
    # Fill remaining categoricals with 'Unknown'
    categoricals = data.select_dtypes(include=['object']).columns
    data[categoricals] = data[categoricals].fillna('Unknown')
    
    return data.dropna()

# 2. Date Feature Utilities
# Generate temporal features from datetime column
def create_date_features(data, date_cols):
    for col, prefix in date_cols.items():
        if col in data.columns:
            data[col] = pd.to_datetime(data[col], format='%d/%m/%Y')
            data[f'{prefix}Year'] = data[col].dt.year
            data[f'{prefix}MonthSin'] = np.sin(2 * np.pi * data[col].dt.month/12)
            data[f'{prefix}MonthCos'] = np.cos(2 * np.pi * data[col].dt.month/12)
            data[f'{prefix}Weekday'] = data[col].dt.weekday
    return data

# Calculate duration between two date
def calculate_time_delta(data, start_col, end_col, new_col):
    data[new_col] = (data[end_col] - data[start_col]).dt.days
    return data

# 3. Encoding Utilities
# One-hot encode categorical feature
def one_hot_encode(data, column, prefix=None):
    prefix = prefix or column
    dummies = pd.get_dummies(data[column], prefix=prefix)
    return pd.concat([data, dummies], axis=1)

# Target encoding for high-cardinality feature
def target_encode(data, column, target='Sales'):
    mean = data[target].mean()
    encodings = data.groupby(column)[target].mean().to_dict()
    data[f'TargetEnc_{column}'] = data[column].map(encodings).fillna(mean)
    return data

# 4. Transformation Utilities
# Apply log1p transformatio
def log_transform(data, column):
    data[f'Log_{column}'] = np.log1p(data[column])
    return data

# Scale using median and IQ
def robust_scale(data, column):
    q1, q3 = data[column].quantile([0.25, 0.75])
    iqr = q3 - q1
    data[f'Scaled_{column}'] = (data[column] - data[column].median()) / iqr
    return data

# 5. Feature Creation Utilities
# Create interaction featur
def create_interaction(data, col1, col2, new_col):
    data[new_col] = data[col1] / (data[col2] + 1)  # +1 to avoid division by zero
    return data

# Create aggregated feature
def create_aggregates(data, group_col, agg_cols):
    agg_funcs = {
        'mean': np.mean,
        'count': 'count',
        'sum': np.sum,
        'max': np.max,
        'min': np.min
    }
    
    aggregates = data.groupby(group_col)[agg_cols].agg(agg_funcs)
    aggregates.columns = [f'{group_col}_{"_".join(col)}' for col in aggregates.columns]
    
    return data.merge(aggregates, on=group_col, how='left')

# 6. Analysis Utilities
# Get top correlated features with targe
def get_feature_correlations(data, target_col, n=10):
    corr_matrix = data.select_dtypes(include=np.number).corr()
    return corr_matrix[target_col].sort_values(ascending=False)[1:n+1]

# Get top features by mutual informatio
def get_mutual_info(data, target_col, n=10):
    X = data.select_dtypes(include=np.number).drop(columns=[target_col]).fillna(0)
    y = data[target_col]
    mi = mutual_info_regression(X, y)
    return pd.Series(mi, index=X.columns).sort_values(ascending=False).head(n)

# 7. Main Pipeline
# Complete feature engineering pipelin
def run_feature_pipeline(data, target_col='Sales'):
    # 1. Clean data
    data = clean_column_names(data)
    data = handle_missing_values(data)
    
    # 2. Create date features
    data = create_date_features(data, {'OrderDate': 'Order', 'ShipDate': 'Ship'})
    data = calculate_time_delta(data, 'OrderDate', 'ShipDate', 'ShippingDuration')
    
    # 3. Encode categoricals
    for col in ['ShipMode', 'Segment', 'City']:
        if col in data.columns:
            if data[col].nunique() < 5:
                data = one_hot_encode(data, col)
            else:
                data = target_encode(data, col, target_col)
    
    # 4. Transform numericals
    if target_col in data.columns:
        data = log_transform(data, target_col)
        data = robust_scale(data, target_col)
    
    # 5. Create new features
    if all(col in data.columns for col in [target_col, 'ShippingDuration']):
        data = create_interaction(data, target_col, 'ShippingDuration', 'SalesPerDay')
    
    if 'CustomerID' in data.columns:
        data = create_aggregates(data, 'CustomerID', [target_col, 'ShippingDuration'])
    
    return data
