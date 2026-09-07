import json
import anthropic

class Agent:
    BASE_SYSTEM_PROMPT = (
        "You are an autonomous agent that can take multiply tool-calling steps when helpful."
        "The user only sees your response when you stop using tools, not your tool usage or reasoning steps."
        "When you provide your answer without calling tools, make it complete and standalone. \n"
        "Additional instructions:\n"
    )

    def __init__(
        self,
        name,
        system_prompt="You are a helpful assistant.",
        model="claude-sonnet-4-6",
        tools=None,
        tool_schemas=None,
        max_turns=10
    ):
        self.client = anthropic.Anthropic()
        self.name = name
        self.model = model
        self.system_prompt = self.BASE_SYSTEM_PROMPT + system_prompt
        self.max_turns = max_turns

        self.tools = {} if tools is None else dict(tools)
        self.tool_schemas = [] if tool_schemas is None else list(tool_schemas
        )

    def _extract_text(self, content):
        return "".join(
            block.text for block in content:
            if getattr(block, "type", None) =="text"
        )

    def _build_request_args(self, messages):
        request_args = {
            "model": self.model,
            "system": self.system_prompt,
            "messages": messages,
            "max_tokens": 8000,
        }

        if self.tool_schemas:
            request_args["tools"] = self.tool_schemas

            return request_args