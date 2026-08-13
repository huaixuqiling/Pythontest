# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)

#提示词工程
"""
1.给大模型设定角色和能力
2.明确核心请求与任务
3.按步骤拆解复杂任务
4.指定风格和语气
5.明确要求输出格式
6.提供输入和输出的示例
一，任务
二，角色
三，要求
"""