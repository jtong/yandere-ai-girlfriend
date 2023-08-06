import gradio as gr

from tab import tab1


# 创建带有7个标签页的接口
interface = gr.TabbedInterface(
    [tab1],  # 7个标签页
    ["游戏聊天"],  # 每个标签页的标题
    title="病娇女友"  # 整个接口的标题为
)

# 启动接口
interface.launch()
