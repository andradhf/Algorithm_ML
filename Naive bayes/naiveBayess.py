import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv('asian_cup.csv')

# Preprocessing: Handle missing values
df = df.dropna()

# Keep only the necessary columns
df = df[['Home_Team', 'Away_Team', 'Home_Score', 'Away_Score', 'Winning_Team', 'Losing_Team']]

# Initialize LabelEncoder
le = LabelEncoder()

# Combine all teams to ensure all labels are included in the encoder
all_teams = pd.concat([df['Home_Team'], df['Away_Team'], df['Winning_Team'], df['Losing_Team']]).unique()
le.fit(all_teams)

# Encoding categorical features
df['Home_Team'] = le.transform(df['Home_Team'])
df['Away_Team'] = le.transform(df['Away_Team'])
df['Winning_Team'] = le.transform(df['Winning_Team'])
df['Losing_Team'] = le.transform(df['Losing_Team'])

# Define features and target
features = ['Home_Team', 'Away_Team', 'Home_Score', 'Away_Score']
X = df[features]
y = df['Winning_Team']

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training Naive Bayes Model
model = GaussianNB()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)

# Encode the teams for prediction
indonesia_encoded = le.transform(['Indonesia'])[0]
australia_encoded = le.transform(['Australia'])[0]

# Prepare the input data for prediction
match_data = pd.DataFrame({
    'Home_Team': [indonesia_encoded],
    'Away_Team': [australia_encoded],
    'Home_Score': [0],  # Assuming we don't have the score yet
    'Away_Score': [0]   # Assuming we don't have the score yet
})

# Making prediction for the match Indonesia vs Australia
predicted_winner_encoded = model.predict(match_data)[0]
predicted_winner = le.inverse_transform([predicted_winner_encoded])[0]

print(f'Predicted Winner for Indonesia vs Australia: {predicted_winner}')
