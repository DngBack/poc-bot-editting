from __future__ import annotations

import os
import sys
from pathlib import Path

import openai

sys.path.append(str(Path(__file__).parent))  # noqa
from common import AppSettings  # noqa
from common import load_settings  # noqa
from dotenv import load_dotenv  # noqa
from embedding.openai.modules import setup_embeding  # noqa
from llms.openai.modules import setup_openai  # noqa
from tracing.langfuse.trace import setup_tracing  # noqa


__all__ = [
    'AppSettings',
    'load_settings',
    'setup_embeding',
    'setup_openai',
    'setup_tracing',
]


def initialize(env_path: str):
    '''
    Load env
    Arg:
        env_path: Path of env
    Return:
        None
    '''
    load_dotenv(env_path)
    settings = load_settings()

    os.environ['OPENAI_API_KEY'] = settings.openai_api_key
    openai.api_key = os.environ['OPENAI_API_KEY']

    setup_openai(settings)
    setup_embeding(settings)
    setup_tracing(settings)

    return settings.sd_api_key
