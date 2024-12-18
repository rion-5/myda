# coding: utf-8
from src.data.make_dataset import collect_data_employ
employ_data = collect_data_employ()
employ_data.info()
import pandas as pd
employ_data = pd.DataFrame(employ_data)
qual =['성별','외국인학생','입학전형명','교환유학생여부','취업구분']
for col in qual:
    employ_data[col] = employ_data[col].astype('category')
    
employ_data.describe(include=['category'])
freq_sex = pd.DataFrame(employ_data['성별']).value_counts()
freq_sex
del freq_sex
freq_sex['도수'] = pd.DataFrame(employ_data['성별']).value_counts()
freq_sex['상대도수'] = employ_data['성별'].value_counts(normalize = True)
freq_sex = pd.DataFrame(employ_data['성별']).value_counts()
freq_sex['상대도수'] = employ_data['성별'].value_counts(normalize = True)
freq_sex
from scipy.stats import spearmanr, kendalltau
employ_data.info()
corr, p = spearmanr(employ_data['평점평균'],employ_data['토익점수'])
p
print("스피어만 상관계수는 {:.3f}, p-value는 {:.3f}".format(corr,p))
corr, p = spearmanr(employ_data['외국인학생'],employ_data['입학전형명'])
print("스피어만 상관계수는 {:.3f}, p-value는 {:.3f}".format(corr,p))
freq_sex = freq_sex.rename(columns= {'성별':'도수'})
type(freq_sex)
freq_sex
del freq_sex
employ_data['성별'].value_counts()
freq_sex = pd.DataFrame(employ_data['성별'].value_counts())
type(freq_sex)
freq_sex['상대도수'] = employ_data['성별'].value_counts(normalize = True)
freq_sex
freq_sex = freq_sex.rename(columns= {'count':'도수'})
freq_sex
