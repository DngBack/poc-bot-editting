from __future__ import annotations

import sys
from pathlib import Path

from common import AppSettings
from llama_index.core import Settings
from llama_index.embeddings.openai import OpenAIEmbedding
sys.path.append(str(Path(__file__).parent.parent))


def setup_embeding(
        settings: AppSettings,
):
    embed = OpenAIEmbedding(
        model=settings.embed_openai.openai_embed_model,
    )

    Settings.embed_model = embed
