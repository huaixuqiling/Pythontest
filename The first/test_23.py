import streamlit as st
#大标题
st.title("streamlit 入门演示")
st.header("streamlit 一级标题")
st.subheader("streamlit 二级标题")

st.write("啊伟大伟大·")
st.write("dawdadwdadawdwad")

st.image("./resources/图片1.png",width=500)

st.video("resources/perfectMoment_9211578268485693452_8.mp4")


st.logo("./resources/图片1.png")

students_data={
    "姓名":["王琳","达瓦","王""王wad""大王的","王adw","琳"],
    "学号":["1232","1232","1232","1232","1232"]
}
st.table(students_data)

name=st.text_input("请输入姓名")
st.write(f"您输入的姓名为{name}")

password=st.text_input("请输入密码",type="password")
st.write(f"您输入的密码为{password}")

gender=st.radio("请选择您的性别",["男","女","武装直升机"],index=1)
st.write(gender)