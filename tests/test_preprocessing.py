import sys
from pathlib import Path

# Add project root to PYTHONPATH
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.append(project_root)

import pytest
from src.data.preprocessing import clean_data
from src.data.make_dataset import collect_data

def test_clean_data():
    raw_data = collect_data()
    processed_data = clean_data(raw_data)
    assert not processed_data.empty, "Processed data should not be empty"
    assert 'employ_status' in processed_data.columns, "Processed data should have 'employ_status' column"