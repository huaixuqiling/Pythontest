import streamlit as st
import os
from openai import OpenAI
from click import prompt
from openai.types.conversations import message

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",

    layout="wide",

    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")

st.logo("♉")

#系统提示词
system_prompt="你是一个AI助手，名字叫小龙"

#初始化聊天信息
if "message" not in st.session_state:
    st.session_state.message=[]
#展示聊天信息
for message in st.session_state.message:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"]=="user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

#输入框
prompt = st.chat_input("请输入您想要问的问题：")
if prompt: #字符串会自动转化布尔值，看是否为空
    st.chat_message("user").write(prompt)
    print("调用大模型,提示词：",prompt)
    st.session_state.message.append({"role":"user","content":prompt})

    #调用大模型进行对话
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.message
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    #非刘氏输出解析方式
    # print(f"大模型返回的结果：{response.choices[0].message.content}")
    # st.chat_message("assistant").write(response.choices[0].message.content)
    #流式输出
    response_message=st.empty()
    full_response=""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content =chunk.choices[0].delta.content
            full_response+= content
            response_message.chat_message("assistant").write(full_response)

    st.session_state.message.append({"role": "assistant", "content": full_response})