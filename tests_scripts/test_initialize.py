from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))  # noqa
from backend.botEdit.infrastructure import initialize  # noqa

api_sd_key = initialize('.env')
print(api_sd_key)
