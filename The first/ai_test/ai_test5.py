import streamlit as st
import os
from openai import OpenAI
import datetime
import json
from click import prompt
from openai.types.conversations import message

def save_session():
    if st.session_state.current_session:
        session_data={
            "ainame":st.session_state.ainame,
            "ainature":st.session_state.ainature,
            "message":st.session_state.message,
            "current_session":st.session_state.current_session
        }
        if not os.path.exists("session"):
            os.mkdir("session")
        with open(f"session/{st.session_state.current_session}.json","w",encoding="utf-8") as f:
            json.dump(session_data,f,ensure_ascii=False,indent=4)

def generate_session_name():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

def load_session():
    session_list=[]
    if os.path.exists("session"):
        file_list=os.listdir("session")
        for file in file_list:
            if file.endswith(".json"):
                session_list.append(file[:-5])
    return session_list

def load_sessi(session_name):
    try:
        if os.path.exists(f"session/{session_name}.json"):
            with open(f"session/{session_name}.json","r",encoding="utf-8") as f:
                session_data= json.load(f)
                st.session_state.message=session_data["message"]
                st.session_state.ainame=session_data["ainame"]
                st.session_state.ainature=session_data["ainature"]
                st.session_state.current_session=session_name
    except Exception as e:
        st.error(f"加载绘画失败: {e}")

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
system_prompt="你是一个AI助手，名字叫%s,性格%s"

#初始化聊天信息
if "message" not in st.session_state:
    st.session_state.message=[]
if "ainame" not in st.session_state:
    st.session_state.ainame="启灵"
if "ainature" not in st.session_state:
    st.session_state.ainature="温柔的台湾姑娘"
if "current_session" not in st.session_state:
    time=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    st.session_state.current_session=time
st.text(f"会话名称：{st.session_state.current_session}")
#展示聊天信息
for message in st.session_state.message:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"]=="user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

#左侧侧边栏
# st.sidebar.subheader("伴侣的信息")
# ainame=st.sidebar.text_input("伴侣的名字")
with st.sidebar:
    st.subheader("AI控制面板")
    if st.button("新建会话",width="stretch",icon="♎"):
            #1.保存当前会话信息
            save_session()
            #2.创建新的会话信息
            if st.session_state.message:
                st.session_state.message=[]
                st.session_state.current_session=generate_session_name()
                save_session()
                st.rerun()

    st.subheader("历史会话")
    session_list=load_session()
    for session in session_list:
        # if st.button(session,width="stretch",icon="🚀"):
        #     st.session_state.current_session=session
        #     st.rerun()
        s1,s2=st.columns([3,1])
        with s1:
            if st.button(session,width="stretch",icon="🚀",key=f"load_{session}",type="primary" if session==st.session_state.current_session else "secondary"):
                load_sessi(session)
                st.rerun()
        with s2:
            if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):
                pass

    st.subheader("伴侣的信息")
    ainame=st.text_input("伴侣的名字",placeholder=("请输入伴侣的昵称"),value="启灵")
    if ainame:
        st.session_state.ainame=ainame
    ainature = st.text_area("伴侣的性格",placeholder=("请输入伴侣的性格"),value="温柔的台湾姑娘")
    if ainature:
        st.session_state.ainature=ainature

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
            {"role": "system", "content": system_prompt%(st.session_state.ainame,st.session_state.ainature)},
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

    save_session()
