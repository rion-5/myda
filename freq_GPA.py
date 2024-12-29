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




result2 = cut(employ_data['GPA'], bins=[0,2,2.5,3,3.5,4,4.5], labels=['0-2','2-2.5','2.5-3','3-3.5','3.5-4','4-4.5'])

freq_GPA = pd.DataFrame(result2.value_counts()).reset_index()
print(freq_GPA)
freq_GPA = freq_GPA.rename(columns={'count':'frequency'}).sort_values(by='GPA')
freq_GPA['relative_frequency'] = freq_GPA['frequency'].apply(lambda x: x/freq_GPA['frequency'].sum())

print(freq_GPA)


import matplotlib.pyplot as plt


fig2, ax2 = plt.subplots()
ax2.hist(employ_data['GPA'], bins=10, edgecolor='black', color='#2c3e50')

# x축, y축 라벨 설정
ax2.set_xlabel('GPA')
ax2.set_ylabel('Frequency')

# 그래프 제목 설정
ax2.set_title('GPA 분포')

# # x축 눈금 설정 (범주형 데이터이므로 범위를 표시)
# ax2.set_xticks(range(6))
# ax2.set_xticklabels(employ_data['GPA'])

# 그래프 출력
fig2.show()
plt.show()