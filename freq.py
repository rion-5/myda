from src.data.make_dataset import collect_data
import pandas as pd

employ_data = pd.DataFrame(collect_data())

column_mapping = {
  "성별":"Gender",
  "외국인학생":"Foreign_Student",
  "평점평균":"GPA",
  "토익점수":"TOEIC_Score",
  "취업구분":"Employment_Status",
  "입학전형명":"Admission_Type",
  "인턴십현장실습인정학점":"Internship_Credit",
  "교환유학생여부":"Exchange_Student"
}
employ_data.rename(columns=column_mapping, inplace = True)

qual=['Gender','Foreign_Student','Employment_Status','Admission_Type','Exchange_Student']

for col in qual:
   employ_data[col] = employ_data[col].astype('category')

employ_data.info()

from pandas import cut

result1 = cut(employ_data['TOEIC_Score'], bins=[0,600,700,800,900,1000],labels=['0-600','601-700','701-800','801-900','901-1000'])
freq_TOEIC_Score = pd.DataFrame(result1.value_counts()).reset_index()
freq_TOEIC_Score = freq_TOEIC_Score.rename(columns={'count':'frequency'}).sort_values(by='TOEIC_Score')

freq_TOEIC_Score['relative_frequency'] = freq_TOEIC_Score['frequency'].apply(lambda x: x/freq_TOEIC_Score['frequency'].sum())

print(freq_TOEIC_Score)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8,5))
ax.set_title('TOEIC Score')
bars = ax.bar(freq_TOEIC_Score['TOEIC_Score'],freq_TOEIC_Score['frequency'])
for bar in bars:
   height = bar.get_height()
   ax.text(bar.get_x() + bar.get_width()/2, height, f'{int(height)}', ha='center',va='bottom')

fig.tight_layout()
plt.show()



