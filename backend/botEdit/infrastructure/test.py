from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.append(str(Path(__file__).parent.parent.parent.parent))  # noqa
from backend.QnA.infrastructure import load_settings    # noqa

# Tải các biến môi trường từ file .env
load_dotenv('.env')

# Tải cấu hình
settings = load_settings()

# Kiểm tra các giá trị đã được tải
print(settings.openai_api_key)
print(settings.llm_openai.openai_llm_model)
print(settings.embed_openai.openai_embed_model)
print(settings.tracing.trace)
print(settings.tracing.public_key)
print(settings.tracing.secret_key)
print(settings.tracing.user_id)
print(settings.tracing.host)
