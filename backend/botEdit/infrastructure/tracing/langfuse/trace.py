from __future__ import annotations

import sys
from pathlib import Path

from common import AppSettings
from langfuse.llama_index import LlamaIndexCallbackHandler
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager
sys.path.append(str(Path(__file__).parent.parent))


def setup_tracing(settings: AppSettings):
    trace = settings.tracing.trace
    if trace:
        callback_handler = LlamaIndexCallbackHandler(
            public_key=settings.tracing.public_key,
            secret_key=settings.tracing.secret_key,
            host=settings.tracing.host,
            user_id=settings.tracing.user_id,
        )
        Settings.callback_manager = CallbackManager([callback_handler])
