from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent
from camel.toolkits import SearchToolkit
import os
import logging

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env_dev')
load_dotenv(dotenv_path)

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)

logger.info("モデルファクトリの作成")

model = ModelFactory.create(
  model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
  # model_type=ModelType.GPT_4O,
  model_type="gemma-3-27b-it",
  model_config_dict={"temperature": 0.0},
  api_key=os.getenv("OPENAI_API_KEY"),
  url=os.getenv("OPENAI_BASE_URL"),
)

logger.info("Toolの設定")

# ブラウザ検索用のToolKit
search_tool = SearchToolkit().search_duckduckgo

logger.info("Agentの設定")

agent = ChatAgent(model=model, tools=[search_tool])

request_1 = "CAMEL-AIは何ですか？"
logger.info(f"リクエスト_パターン1:{request_1}")

response_1 = agent.step(request_1)
logger.info(f"レスポンス_パターン1: {response_1.msgs[0].content}")

request_2 = "CAMEL フレームワークへの Github リンクとは何ですか？"
logger.info(f"リクエスト_パターン2:{request_2}")

response_2 = agent.step(request_2)
logger.info(f"レスポンス_パターン2: {response_2.msgs[0].content}")
