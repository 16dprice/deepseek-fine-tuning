import os
from openai import OpenAI

from openai.types.chat import ChatCompletionMessageParam
from openai.types import ChatModel

class OpenAIApiClient:
    def __init__(self):
        self._client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
    
    def chat_completion(
        self,
        messages: list[ChatCompletionMessageParam],
        temperature: float = 0.2,
        model: ChatModel = "gpt-4o-mini"
    ):
        completion = self._client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=temperature
        )
        return completion.choices[0].message.content
