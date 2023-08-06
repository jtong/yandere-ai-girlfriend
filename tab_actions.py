# 定义第一个标签页的输入和输出
import random

from logic.reply_once import reply_once, Response


def send(user_message, history):
    if (len(history) == 0):
        return "", history + [["我这是在哪?", "你醒啦？"], ["你是谁？", None]]
    else:
        return "", history + [[user_message, None]]


state = {
    "trust": 30,
    "like": 100,
    "hurt": 0,
}


def start_action(user_message, history):
    reset_state()
    return send(user_message, history)


def reset_state():
    state = {
        "trust": 30,
        "like": 100,
        "hurt": 90,
    }


def chat_bot(temperature, history):
    # 定义一个空字符串，用来拼接每一轮对话
    chat_history_string = ''
    # 遍历 history 列表中的每一个元素
    for item in history:
        # 取出当前元素中的问题和回答
        question, answer = item

        # 将问题和回答拼接成一个字符串，并添加到结果字符串中
        chat_history_string += f"玩家: {question}\n“女友”: {answer}\n" if answer else f"玩家: {question}\n"

    response: Response = reply_once(chat_history_string, state, temperature)

    if response is not None:
        post_history(history, response)
        status_result = ""
        # if response.strategy == "砍死玩家":
        #     status_result = "砍死玩家"
        # chatgpt_result = "这是模拟返回的ChatGPT生成的回复"
        # time.sleep(1)
        return history, response.strategy
    else:
        return chat_bot(temperature, history)


def post_history(history, parsed_response):
    history[-1][1] = parsed_response.line
