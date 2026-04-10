import pandas as pd
import numpy as np
from scripts.data_cleaning import clean_data

print('Loading Data...')
df = pd.read_csv('data/raw/global_ai_jobs.csv')
print('Cleaning Data...')
df = clean_data(df)
print('Saving Cleaned Data...')
df.to_csv("data/processed/cleaned_jobs.csv", index=False)
