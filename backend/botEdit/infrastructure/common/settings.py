from __future__ import annotations

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class OpenAI_Embed_Config(BaseModel):
    '''
    Setting Config for OpenAI API in Embed
    '''
    openai_embed_model: str


class OpenAI_Llm_Config(BaseModel):
    '''
    Setting Config for OpenAI API
    '''
    openai_llm_model: str


class TracingConfig(BaseModel):
    '''
    Setting Config for Tracing with Langfuse
    '''
    trace: bool = True
    public_key: str
    secret_key: str
    user_id: str
    host: str = 'https://us.cloud.langfuse.com'


class AppSettings(BaseSettings):
    '''
    Load env
    '''
    model_config = SettingsConfigDict(env_nested_delimiter='__')
    sd_api_key: str
    openai_api_key: str
    llm_openai: OpenAI_Llm_Config
    embed_openai: OpenAI_Embed_Config
    tracing: TracingConfig


def load_settings() -> AppSettings:
    return AppSettings()
