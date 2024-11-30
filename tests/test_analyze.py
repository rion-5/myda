import sys
from pathlib import Path

# Add project root to PYTHONPATH
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.append(project_root)

import pytest
from src.analysis.analyze import perform_analysis
from src.data.preprocessing import clean_data
from src.data.make_dataset import collect_data

def test_perform_analysis():
    raw_data = collect_data()
    processed_data = clean_data(raw_data)
    analysis_results = perform_analysis(processed_data)
    assert 'accuracy' in analysis_results, "Analysis results should contain 'accuracy'"
    assert 'evaluation_metrics' in analysis_results, "Analysis results should contain 'evaluation_metrics'"
    assert 'roc_auc' in analysis_results['evaluation_metrics'], "Evaluation metrics should contain 'roc_auc'"