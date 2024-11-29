# MYDA Project

GPA와 TOEIC 점수가 취업에 미치는 영향 분석 프로젝트

## 설치 방법
```bash
conda env create -f environment.yml
conda activate myda
```
## 실행 방법
```bash
python main.py
```
## 프로젝트 구조
```
myda/
├── src/
│   ├── data/
│   │   ├── make_dataset.py    # DB data collection
│   │   ├── preprocessing.py   # Data cleaning
│   ├── analysis/
│   │   ├── analyze.py         # Logistic regression
│   ├── visualization/
│   │   ├── visualize.py       # Plotting
│   ├── main.py                # Pipeline orchestration
├── docs/
│   ├── analysis_results.md    # Results documentation
├── tests/
│   ├── test_preprocessing.py  # Test for data cleaning
│   ├── test_analyze.py        # Test for analysis
├── data/
│   ├── raw/                   # Raw data
│   ├── processed/             # Processed data
├── reports/
│   ├── figures/               # Figures and plots
├── environment.yml            # Conda environment configuration
├── README.md                  # Project documentation
```

