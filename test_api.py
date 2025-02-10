from openai import OpenAI

client = OpenAI(
    base_url="http://192.168.30.177:1234/v1/",  # 添加 /v1 路徑
    api_key="not-needed"  # LM Studio 不需要 API key
)

try:
    response = client.chat.completions.create(
        model="local-model",
        messages=[{"role": "user", "content": "你好"}],
        temperature=0.7,  # 添加溫度參數
        max_tokens=1000   # 添加最大令牌數
    )

    # 添加調試信息
    print("完整回應：", response)

    if response and response.choices:
        print("回應內容：", response.choices[0].message.content)
    else:
        print("API 未返回有效回應")

except Exception as e:
    print(f"發生錯誤：{str(e)}")
