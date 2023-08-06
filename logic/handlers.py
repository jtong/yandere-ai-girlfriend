import json
import re

from logic.llm_driver import step
from logic.prompts.state_change_cal_prompt import state_change_cal_prompt


def build_StateChange(state):
    def StateChange(action_input):
        change_json = json.loads(action_input)
        for key in change_json:
            if key in state:
                state[key] = change_json[key] + state[key]

        return json.dumps(state)
    return StateChange


def build_StateChangeCal(chat_history):

    def StateChangeCal(action_input):
        cal_prompt = state_change_cal_prompt(chat_history)

        def valid(result: str):
            return re.search(r'<observation>.*?</observation>', result, re.DOTALL) is not None

        message = step(cal_prompt)
        max = 3
        while (not valid(message)):
            message = step(cal_prompt)
            max -= 1
            if max == 0:
              raise Exception("没有完整的xml，重试超时")
        return message

    return StateChangeCal


