import pandas as pd
import numpy as np
def clean_data(df):
	df = df.rename(columns = {
		'salary_usd' : 'salary',
		'bonus_usd' : 'bonus'})
	df = df.drop(columns = ['id','salary_percentile'],axis = 1)
	df = df.drop_duplicates()
	df = df.dropna()
	return df