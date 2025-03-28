## sample.pyの実行手順

  1. 依存関係をインストールする。

    ```bash
    uv venv .venv --python=3.10
    source .venv/bin/activate
    uv pip install -e . 
    uv pip install 'camel-ai[web_tools]'
    uv pip install numpy pandas unstructured pillow 
    ```

  2. `.env_dev`ファイルを作成し、下記の内容を記載する。

    ```
    # API設定
    OPENAI_BASE_URL=https://exchangers-macstudio.tailcfc41a.ts.net:8443/api/
    OPENAI_API_KEY="<LM Studioで発行したAPIキー>"

    # Langfuse設定
    LANGFUSE_PUBLIC_KEY="<Langfuseで発行した公開鍵>"
    LANGFUSE_SECRET_KEY="<Langfuseで発行した秘密鍵>"
    LANGFUSE_HOST="https://exchangers-macstudio.tailcfc41a.ts.net:8444"

    # ユーザー情報
    USER_NAME="<使用者名>"
    ```
    注釈）`USER_NAME`の例：山田太郎の場合、`t.yamada`

  3. 以下のコマンドを実行する。
    ```bash
    python sample.py
    ```

<details><summary>実行結果</summary>

```bash
$ python sample.py
2025-03-28 15:25:10,288 - dotenv.main - WARNING - python-dotenv could not parse statement starting at line 118
2025-03-28 15:25:10,288 - dotenv.main - WARNING - python-dotenv could not parse statement starting at line 119
INFO:__main__:モデルファクトリの作成
INFO:__main__:Toolの設定
INFO:__main__:Agentの設定
WARNING:root:Invalid or missing `max_tokens` in `model_config_dict`. Defaulting to 999_999_999 tokens.
INFO:__main__:リクエスト_パターン1:CAMEL-AIは何ですか？
INFO:httpx:HTTP Request: POST https://exchangers-macstudio.tailcfc41a.ts.net:8443/api/chat/completions "HTTP/1.1 200 OK"
INFO:camel.agents.chat_agent:Model gemma-3-27b-it, index 0, processed these messages: [{'role': 'user', 'content': 'CAMEL-AIは何ですか？'}]
INFO:primp:response: https://duckduckgo.com/?q=CAMEL-AI 200
INFO:primp:response: https://links.duckduckgo.com/d.js?q=CAMEL-AI&kl=wt-wt&l=wt-wt&p=&s=0&df=&vqd=4-302687636677574903818799288221522334592&bing_market=wt-WT&ex=-1 200
INFO:camel.agents.chat_agent:Model gemma-3-27b-it, index 0, processed these messages: [{'role': 'user', 'content': 'CAMEL-AIは何ですか？'}, {'role': 'assistant', 'content': '', 'tool_calls': [{'id': '715082047', 'type': 'function', 'function': {'name': 'search_duckduckgo', 'arguments': '{"query": "CAMEL-AI", "source": "text", "max_results": 5}'}}]}, {'role': 'tool', 'content': '[{\'result_id\': 1, \'title\': \'CAMEL-AI Finding the Scaling Laws of Agents\', \'description\': \'CAMEL-AI.org is the 1st LLM multi-agent framework and an open-source community dedicated to finding the scaling law of agents.\', \'url\': \'https://www.camel-ai.org/\'}, {\'result_id\': 2, \'title\': \'GitHub - camel-ai/camel: CAMEL: The first and the best multi-agent ...\', \'description\': \'🐫 CAMEL is an open-source community dedicated to finding the scaling laws of agents. We believe that studying these agents on a large scale offers valuable insights into their behaviors, capabilities, and potential risks. To facilitate research in this field, we implement and support various types of agents, tasks, prompts, models, and simulated environments. Join us (Discord or WeChat) in ...\', \'url\': \'https://github.com/camel-ai/camel\'}, {\'result_id\': 3, \'title\': "Welcome to CAMEL\'s documentation! — CAMEL 0.2.37 documentation", \'description\': "CAMEL-AI is a multi-agent framework that enables you to create and use LLM-based agents for real-world tasks. Learn how to install, setup, and use CAMEL-AI\'s key modules, agents, data generation, models, tools, and cookbooks.", \'url\': \'https://docs.camel-ai.org/\'}, {\'result_id\': 4, \'title\': \'camel-ai · PyPI\', \'description\': \'CAMEL-AI is a community-driven project that supports various types of agents, tasks, prompts, models, and simulated environments. It enables researchers to study the scaling laws of agents, generate data, automate tasks, and simulate worlds with millions of agents.\', \'url\': \'https://pypi.org/project/camel-ai/\'}, {\'result_id\': 5, \'title\': \'camel-ai.org · GitHub\', \'description\': \'CAMEL-AI.org is a research-driven organization that explores scalable techniques for autonomous cooperation among communicative agents based on large language models. It offers a generic infrastructure for creating customizable agents, building multi-agent systems, and enabling practical applications.\', \'url\': \'https://github.com/camel-ai/\'}]', 'tool_call_id': '715082047'}]
INFO:__main__:レスポンス_パターン1: CAMEL-AIは、LLM（大規模言語モデル）を用いたマルチエージェントフレームワークであり、オープンソースコミュニティです。エージェントのスケーリング則を見つけることに特化しており、様々なエージェント、タスク、プロンプト、モデル、シミュレーション環境をサポートしています。研究者がエージェントの行動や能力、潜在的なリスクを理解するためのインフラを提供し、データ生成、タスク自動化、大規模なエージェントによる世界のシミュレーションなどを可能にします。

詳細については、以下のリンクを参照してください。

*   **CAMEL-AI 公式サイト:** [https://www.camel-ai.org/](https://www.camel-ai.org/)
*   **GitHub リポジトリ:** [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel)
*   **ドキュメント:** [https://docs.camel-ai.org/](https://docs.camel-ai.org/)
*   **PyPI:** [https://pypi.org/project/camel-ai/](https://pypi.org/project/camel-ai/)
*   **GitHub 組織:** [https://github.com/camel-ai/](https://github.com/camel-ai/)
INFO:__main__:リクエスト_パターン2:CAMEL フレームワークへの Github リンクとは何ですか？
INFO:camel.agents.chat_agent:Model gemma-3-27b-it, index 0, processed these messages: [{'role': 'user', 'content': 'CAMEL-AIは何ですか？'}, {'role': 'assistant', 'content': '', 'tool_calls': [{'id': '715082047', 'type': 'function', 'function': {'name': 'search_duckduckgo', 'arguments': '{"query": "CAMEL-AI", "source": "text", "max_results": 5}'}}]}, {'role': 'tool', 'content': '[{\'result_id\': 1, \'title\': \'CAMEL-AI Finding the Scaling Laws of Agents\', \'description\': \'CAMEL-AI.org is the 1st LLM multi-agent framework and an open-source community dedicated to finding the scaling law of agents.\', \'url\': \'https://www.camel-ai.org/\'}, {\'result_id\': 2, \'title\': \'GitHub - camel-ai/camel: CAMEL: The first and the best multi-agent ...\', \'description\': \'🐫 CAMEL is an open-source community dedicated to finding the scaling laws of agents. We believe that studying these agents on a large scale offers valuable insights into their behaviors, capabilities, and potential risks. To facilitate research in this field, we implement and support various types of agents, tasks, prompts, models, and simulated environments. Join us (Discord or WeChat) in ...\', \'url\': \'https://github.com/camel-ai/camel\'}, {\'result_id\': 3, \'title\': "Welcome to CAMEL\'s documentation! — CAMEL 0.2.37 documentation", \'description\': "CAMEL-AI is a multi-agent framework that enables you to create and use LLM-based agents for real-world tasks. Learn how to install, setup, and use CAMEL-AI\'s key modules, agents, data generation, models, tools, and cookbooks.", \'url\': \'https://docs.camel-ai.org/\'}, {\'result_id\': 4, \'title\': \'camel-ai · PyPI\', \'description\': \'CAMEL-AI is a community-driven project that supports various types of agents, tasks, prompts, models, and simulated environments. It enables researchers to study the scaling laws of agents, generate data, automate tasks, and simulate worlds with millions of agents.\', \'url\': \'https://pypi.org/project/camel-ai/\'}, {\'result_id\': 5, \'title\': \'camel-ai.org · GitHub\', \'description\': \'CAMEL-AI.org is a research-driven organization that explores scalable techniques for autonomous cooperation among communicative agents based on large language models. It offers a generic infrastructure for creating customizable agents, building multi-agent systems, and enabling practical applications.\', \'url\': \'https://github.com/camel-ai/\'}]', 'tool_call_id': '715082047'}, {'role': 'assistant', 'content': 'CAMEL-AIは、LLM（大規模言語モデル）を用いたマルチエージェントフレームワークであり、オープンソースコミュニティです。エージェントのスケーリング則を見つけることに特化しており、様々なエージェント、タスク、プロンプト、モデル、シミュレーション環境をサポートしています。研究者がエージェントの行動や能力、潜在的なリスクを理解するためのインフラを提供し、データ生成、タスク自動化、大規模なエージェントによる世界のシミュレーションなどを可能にします。\n\n詳細については、以下のリンクを参照してください。\n\n*   **CAMEL-AI 公式サイト:** [https://www.camel-ai.org/](https://www.camel-ai.org/)\n*   **GitHub リポジトリ:** [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel)\n*   **ドキュメント:** [https://docs.camel-ai.org/](https://docs.camel-ai.org/)\n*   **PyPI:** [https://pypi.org/project/camel-ai/](https://pypi.org/project/camel-ai/)\n*   **GitHub 組織:** [https://github.com/camel-ai/](https://github.com/camel-ai/)'}, {'role': 'user', 'content': 'CAMEL フレームワークへの Github リンクとは何ですか？'}]
INFO:primp:response: https://duckduckgo.com/?q=CAMEL+framework+github+link 200
INFO:primp:response: https://links.duckduckgo.com/d.js?q=CAMEL+framework+github+link&kl=wt-wt&l=wt-wt&p=&s=0&df=&vqd=4-195351212789830909078587528299601487522&bing_market=wt-WT&ex=-1 200
INFO:camel.agents.chat_agent:Model gemma-3-27b-it, index 0, processed these messages: [{'role': 'user', 'content': 'CAMEL-AIは何ですか？'}, {'role': 'assistant', 'content': '', 'tool_calls': [{'id': '715082047', 'type': 'function', 'function': {'name': 'search_duckduckgo', 'arguments': '{"query": "CAMEL-AI", "source": "text", "max_results": 5}'}}]}, {'role': 'tool', 'content': '[{\'result_id\': 1, \'title\': \'CAMEL-AI Finding the Scaling Laws of Agents\', \'description\': \'CAMEL-AI.org is the 1st LLM multi-agent framework and an open-source community dedicated to finding the scaling law of agents.\', \'url\': \'https://www.camel-ai.org/\'}, {\'result_id\': 2, \'title\': \'GitHub - camel-ai/camel: CAMEL: The first and the best multi-agent ...\', \'description\': \'🐫 CAMEL is an open-source community dedicated to finding the scaling laws of agents. We believe that studying these agents on a large scale offers valuable insights into their behaviors, capabilities, and potential risks. To facilitate research in this field, we implement and support various types of agents, tasks, prompts, models, and simulated environments. Join us (Discord or WeChat) in ...\', \'url\': \'https://github.com/camel-ai/camel\'}, {\'result_id\': 3, \'title\': "Welcome to CAMEL\'s documentation! — CAMEL 0.2.37 documentation", \'description\': "CAMEL-AI is a multi-agent framework that enables you to create and use LLM-based agents for real-world tasks. Learn how to install, setup, and use CAMEL-AI\'s key modules, agents, data generation, models, tools, and cookbooks.", \'url\': \'https://docs.camel-ai.org/\'}, {\'result_id\': 4, \'title\': \'camel-ai · PyPI\', \'description\': \'CAMEL-AI is a community-driven project that supports various types of agents, tasks, prompts, models, and simulated environments. It enables researchers to study the scaling laws of agents, generate data, automate tasks, and simulate worlds with millions of agents.\', \'url\': \'https://pypi.org/project/camel-ai/\'}, {\'result_id\': 5, \'title\': \'camel-ai.org · GitHub\', \'description\': \'CAMEL-AI.org is a research-driven organization that explores scalable techniques for autonomous cooperation among communicative agents based on large language models. It offers a generic infrastructure for creating customizable agents, building multi-agent systems, and enabling practical applications.\', \'url\': \'https://github.com/camel-ai/\'}]', 'tool_call_id': '715082047'}, {'role': 'assistant', 'content': 'CAMEL-AIは、LLM（大規模言語モデル）を用いたマルチエージェントフレームワークであり、オープンソースコミュニティです。エージェントのスケーリング則を見つけることに特化しており、様々なエージェント、タスク、プロンプト、モデル、シミュレーション環境をサポートしています。研究者がエージェントの行動や能力、潜在的なリスクを理解するためのインフラを提供し、データ生成、タスク自動化、大規模なエージェントによる世界のシミュレーションなどを可能にします。\n\n詳細については、以下のリンクを参照してください。\n\n*   **CAMEL-AI 公式サイト:** [https://www.camel-ai.org/](https://www.camel-ai.org/)\n*   **GitHub リポジトリ:** [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel)\n*   **ドキュメント:** [https://docs.camel-ai.org/](https://docs.camel-ai.org/)\n*   **PyPI:** [https://pypi.org/project/camel-ai/](https://pypi.org/project/camel-ai/)\n*   **GitHub 組織:** [https://github.com/camel-ai/](https://github.com/camel-ai/)'}, {'role': 'user', 'content': 'CAMEL フレームワークへの Github リンクとは何ですか？'}, {'role': 'assistant', 'content': '', 'tool_calls': [{'id': '684341184', 'type': 'function', 'function': {'name': 'search_duckduckgo', 'arguments': '{"query": "CAMEL framework github link", "source": "text", "max_results": 1}'}}]}, {'role': 'tool', 'content': "[{'result_id': 1, 'title': 'GitHub - camel-ai/camel: CAMEL: The first and the best multi-agent ...', 'description': 'This example demonstrates how to create a ChatAgent using the CAMEL framework and perform a search query using DuckDuckGo. Install the tools package:', 'url': 'https://github.com/camel-ai/camel'}]", 'tool_call_id': '684341184'}]
INFO:__main__:レスポンス_パターン2: CAMELフレームワークのGitHubリンクは、[https://github.com/camel-ai/camel](https://github.com/camel-ai/camel) です。これは、CAMELプロジェクトのリポジトリであり、ソースコードやドキュメントなどが含まれています。
```
<details>