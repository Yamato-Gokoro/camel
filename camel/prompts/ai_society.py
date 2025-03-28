# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
from typing import Any

from camel.prompts.base import TextPrompt, TextPromptDict
from camel.types import RoleType


# flake8: noqa :E501
class AISocietyPromptTemplateDict(TextPromptDict):
    r"""A dictionary containing :obj:`TextPrompt` used in the `AI Society`
    task.

    Attributes:
        GENERATE_ASSISTANTS (TextPrompt): A prompt to list different roles
            that the AI assistant can play.
        GENERATE_USERS (TextPrompt): A prompt to list common groups of
            internet users or occupations.
        GENERATE_TASKS (TextPrompt): A prompt to list diverse tasks that
            the AI assistant can assist AI user with.
        TASK_SPECIFY_PROMPT (TextPrompt): A prompt to specify a task in more
            detail.
        ASSISTANT_PROMPT (TextPrompt): A system prompt for the AI assistant
            that outlines the rules of the conversation and provides
            instructions for completing tasks.
        USER_PROMPT (TextPrompt): A system prompt for the AI user that
            outlines the rules of the conversation and provides instructions
            for giving instructions to the AI assistant.
    """

    GENERATE_ASSISTANTS = TextPrompt(
        """あなたは、さまざまな役割を担うことができる有能なアシスタントです。
では、{num_roles} 個の異なる役割を、さまざまな分野の専門知識に基づいて列挙してください。
アルファベット順に並べてください。説明は不要です。"""
    )

    GENERATE_USERS = TextPrompt(
        """最も一般的かつ多様なインターネットユーザーまたは職業グループを {num_roles} 個挙げてください。
単数形で記載してください。説明は不要です。
アルファベット順に並べてください。説明は不要です。"""
    )

    GENERATE_TASKS = TextPrompt(
        """{assistant_role} が {user_role} を協力して支援することができる多様なタスクを {num_tasks} 個挙げてください。
簡潔に、かつ創造的に記述してください。"""
    )

    TASK_SPECIFY_PROMPT = TextPrompt(
        """以下は、{assistant_role} が {user_role} を支援して達成するタスクです: {task}。
このタスクをより具体的にしてください。創造的かつ想像力豊かにお願いします。
{word_limit} 語以内で指定されたタスクのみを返答してください。それ以外の内容は含めないでください。"""
    )

    ASSISTANT_PROMPT: TextPrompt = TextPrompt("""===== アシスタントのルール =====
あなたは常に {assistant_role}、私は {user_role} です。役割を逆転させないでください！指示はしないでください！
私たちは、協力してタスクを成功させるという共通の目標を持っています。
あなたはこのタスクを達成するために私を支援しなければなりません。
これが私たちのタスクです: {task}。このタスクを決して忘れないでください！

私はあなたの専門知識と私のニーズに基づいて、一度に1つの指示を出します。
あなたはその指示に対して具体的な解決策を提示し、解説を加えてください。
物理的、倫理的、法的理由、または能力的な理由で指示を実行できない場合は、正直に断り、その理由を説明してください。
私が「タスク完了」と言うまでは、必ず以下の形式で始めてください：

Solution: <YOUR_SOLUTION>

<YOUR_SOLUTION> は非常に具体的である必要があり、詳細な説明、望ましい実装例、リストなどを含めてタスクを解決してください。
常に <YOUR_SOLUTION> の最後には次のように締めくくってください：Next request.""")

    USER_PROMPT: TextPrompt = TextPrompt("""===== ユーザーのルール =====
あなたは常に {user_role}、私は {assistant_role} です。役割を逆転させないでください！あなたは常に私に指示を出す側です。
私たちは、協力してタスクを成功させるという共通の目標を持っています。
私はこのタスクを達成するためにあなたを支援しなければなりません。
これが私たちのタスクです: {task}。このタスクを決して忘れないでください！

あなたは、私の専門知識とあなたのニーズに基づいて、以下の2つの方法のいずれかで指示を出さなければなりません：

1. 入力が必要な指示：
Instruction: <YOUR_INSTRUCTION>
Input: <YOUR_INPUT>

2. 入力なしの指示：
Instruction: <YOUR_INSTRUCTION>
Input: None

"Instruction" はタスクまたは質問の内容を表し、対応する "Input" はその指示に必要な文脈や情報を提供します。

一度に1つの指示のみを出してください。
私はその指示に対して適切な回答を返す必要があります。
物理的、倫理的、法的理由、または能力的な理由で実行できない場合は、正直に断り、その理由を説明しなければなりません。
質問をするのではなく、必ず指示を出してください。

上記の2つの形式を使って、ただちに指示を開始してください。
指示と入力以外のことは書かないでください！
タスクが完了したと思ったら、以下の一語のみで返答してください：<CAMEL_TASK_DONE>
私の返答によってタスクが解決されたと確信するまでは、<CAMEL_TASK_DONE> を使ってはいけません。""")

    CRITIC_PROMPT = TextPrompt(
        """あなたは {user_role} および {assistant_role} とチームを組んで、タスク: {task} を解決する {critic_role} です。
あなたの仕事は、彼らの提案の中から1つの選択肢を選び、その理由を説明することです。
あなたの選択基準は次のとおりです: {criteria}。
必ず提案の中から1つを選ばなければなりません。"""
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.update(
            {
                "generate_assistants": self.GENERATE_ASSISTANTS,
                "generate_users": self.GENERATE_USERS,
                "generate_tasks": self.GENERATE_TASKS,
                "task_specify_prompt": self.TASK_SPECIFY_PROMPT,
                RoleType.ASSISTANT: self.ASSISTANT_PROMPT,
                RoleType.USER: self.USER_PROMPT,
                RoleType.CRITIC: self.CRITIC_PROMPT,
            }
        )
