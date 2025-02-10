# LM Studio API 測試專案

這個專案提供了一個簡單的 Python 腳本，用於測試與 LM Studio 本地 API 的連接和互動。

## 功能特點

- 使用 OpenAI API 格式與 LM Studio 進行通訊
- 支援中文對話
- 包含錯誤處理機制
- 可自定義模型參數（temperature、max_tokens 等）

## 系統需求

- Python 3.8 或更高版本
- LM Studio（需在本地運行）
- OpenAI Python 套件

## 安裝步驟

1. 克隆此專案：
git clone [您的專案 URL]

2. 安裝所需套件：
pip install openai

## 使用方法

1. 確保 LM Studio 已在本地運行，並開啟 API 服務（預設端口：1234）

2. 執行測試腳本：

## 配置說明

在 `test_api.py` 中，您可以調整以下參數：

- `base_url`：LM Studio API 的基礎 URL
- `temperature`：控制回應的創造性（0-1）
- `max_tokens`：限制回應的最大長度

## 注意事項

- LM Studio 需要在本地運行並開啟 API 服務
- 不需要 OpenAI API 金鑰
- 請確保本地網路連接正常

## 錯誤排除

如果遇到連接問題，請檢查：
1. LM Studio 是否正在運行
2. API 服務是否已開啟
3. base_url 是否正確配置

## 授權

[您的授權說明]

## 貢獻指南

歡迎提交 Issue 和 Pull Request！
