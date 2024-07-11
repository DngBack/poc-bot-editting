from __future__ import annotations

import sys
from pathlib import Path

from common import AppSettings
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
sys.path.append(str(Path(__file__).parent.parent))


def setup_openai(
        settings: AppSettings,
):
    llm = OpenAI(
        model=settings.llm_openai.openai_llm_model,
    )

    Settings.llm = llm
