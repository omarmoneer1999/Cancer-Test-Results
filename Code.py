# load dataset
import pandas as pd
import numpy as np
df = pd.read_csv('cancer_test_data.csv')
df.head()
df.info()

# number of patients
df['patient_id'].count()

# number of patients with cancer
df[df['has_cancer'] == True].count()

# number of patients without cancer
df[df['has_cancer'] == False].count()

# proportion of patients with cancer
(df['has_cancer'] == True).mean()

# proportion of patients without cancer
(df['has_cancer'] == False).mean()

# proportion of patients with cancer who test positive
(((df['has_cancer'] == True) & (df['test_result']== 'Positive') ).mean())*10
###    or (df.query('has_cancer')['test_result'] == 'Positive').mean()

# proportion of patients with cancer who test negative
(((df['has_cancer'] == True) & (df['test_result']== 'Negative') ).mean())*10
###    or (df.query('has_cancer')['test_result'] == 'Negative').mean()

# proportion of patients without cancer who test positive
((df['has_cancer'] == False) & (df['test_result']== 'Positive') ).mean()
### or   (df.query('has_cancer == False')['test_result'] == 'Positive').mean()

# proportion of patients without cancer who test negative
((df['has_cancer'] == False) & (df['test_result']== 'Negative') ).mean()
### or  (df.query('has_cancer == False')['test_result'] == 'Negative').mean()
