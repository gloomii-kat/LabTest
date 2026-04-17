import sys
import os

# Add the project root folder so the test file can import getbest.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import io
from getbest import getCols, findTop

def test_getCols_basic():
    # Simulated CSV file with the standard column order
    data = io.StringIO(
        "Course,Student Number,Mark,Comment\n"
        "ELEN3020,160001,72,OK\n"
    )

    num_col, mark_col = getCols(data)

    assert num_col == 1
    assert mark_col == 2

def test_findTop_basic():
    # Simulated CSV file with multiple students and distinct marks
    data = io.StringIO(
        "Course,Student Number,Mark,Comment\n"
        "ELEN3020,160001,72,OK\n"
        "ELEN3020,167381,90,Check\n"
        "ELEN3020,143211,83,-\n"
    )

    num_col, mark_col = getCols(data)
    best_idx, best = findTop(data, num_col, mark_col)

    assert best_idx == "167381"
    assert best == 90