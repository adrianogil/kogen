import sys
from pathlib import Path
# Ensure src/python is on the path so ``kogen`` can be imported
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src/python'))
