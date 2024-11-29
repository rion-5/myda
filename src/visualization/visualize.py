# src/visualization/visualize.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_visualizations(processed_data: pd.DataFrame):
    """
    Create visualizations for the analysis
    Args:
        processed_data: 전처리된 데이터프레임
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=processed_data, x='GPA', y='TOEIC_score', 
                    hue='employ_status', alpha=0.6)
    plt.title('GPA vs TOEIC Score by Employment Status')
    plt.savefig('reports/figures/employment_analysis.png')
    plt.close()