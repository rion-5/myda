import sys
from pathlib import Path

# Add project root to PYTHONPATH
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.append(project_root)

import pytest
from src.data.make_dataset import collect_data

def test_collect_data():
    data = collect_data()
    assert data is not None, "Data should not be None"
    assert isinstance(data, list), "Data should be a list"
    assert len(data) > 0, "Data should not be empty"