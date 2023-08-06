import gradio as gr

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tab_actions import start_action, send, chat_bot


with gr.Blocks() as tab1:

    with gr.Row():
        with gr.Column(scale=1):
            other_prompt_input = gr.Textbox(lines=3, label="其他要求", value="")
            # status = gr.State(value="")
            status = gr.Label(value="继续对话")
            start = gr.Button(value="开始", variant="primary")
            restart = gr.Button("Clear")

        with gr.Column(scale=1):

            chatbot = gr.Chatbot(label="交流")
            chat_box = gr.Textbox(label="玩家回复")

            chat_box.submit(send,
                            [chat_box, chatbot],
                            [chat_box, chatbot], queue=False).then(
                chat_bot, [ other_prompt_input, chatbot], [chatbot, status]
            )

            restart.click(lambda: None, None, chatbot, queue=False)
            start.click(start_action,
                        [chat_box, chatbot],
                        [chat_box, chatbot], queue=False).then(
                chat_bot, [ other_prompt_input, chatbot], [chatbot, status]
            )
