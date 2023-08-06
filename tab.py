import gradio as gr

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tab_actions import start_action, send, chat_bot


with gr.Blocks() as tab1:

    with gr.Row():
        with gr.Column(scale=1):
            temperature = gr.Slider(0, 2, value=0.75, step=0.01, label="Temperature", info="Choose between 0 and 2")
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
                chat_bot, [temperature, chatbot], [chatbot, status]
            )

            restart.click(lambda: None, None, chatbot, queue=False)
            start.click(start_action,
                        [chat_box, chatbot],
                        [chat_box, chatbot], queue=False).then(
                chat_bot, [temperature, chatbot], [chatbot, status]
            )
