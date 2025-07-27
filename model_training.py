df['label'] = df['label'].map({'male': 0, 'female': 1})

# Check for null values
print(df.isnull().sum())

# Feature and target
X = df.drop('label', axis=1)
y = df['label']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)







