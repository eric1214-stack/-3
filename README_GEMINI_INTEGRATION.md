# 食品效期管理系統 - Gemini API 整合版

## 概述

本專案已成功將原有的辨識功能替換為 Google Gemini API，提供更準確的食品辨識能力。系統可以自動辨識食品圖片中的品名、到期日期、條碼和類別資訊。

## 主要功能

### 🔍 智能食品辨識
- **品名辨識**：自動識別食品名稱
- **日期辨識**：識別生產日期或到期日期，自動轉換為標準格式 (YYYY-MM-DD)
- **條碼辨識**：提取商品條碼資訊（如果存在）
- **類別分類**：自動分類食品類型（飲料、罐頭、零食、乳製品等）

### 📝 可編輯表單
- 辨識結果自動填入表單
- 使用者可手動修改任何欄位
- 支援多種食品類別和單位選擇
- 完整的食品資訊管理

### 📊 數據管理
- 食品庫存統計
- 到期日提醒
- 分類統計圖表
- 完整的 CRUD 操作

## 技術架構

### 後端技術
- **Flask**：Web 框架
- **SQLAlchemy**：資料庫 ORM
- **Google Generative AI**：Gemini API 整合
- **Pillow**：圖片處理
- **Flask-CORS**：跨域請求支援

### 前端技術
- **HTML5/CSS3/JavaScript**：基礎前端技術
- **Bootstrap 5**：UI 框架
- **Chart.js**：圖表展示
- **Bootstrap Icons**：圖標庫

## 安裝與設定

### 1. 環境需求
```bash
Python 3.8+
pip (Python 套件管理器)
```

### 2. 安裝依賴
```bash
cd food_expiry_system_cursor_optimized
pip install -r requirements.txt
```

如果沒有 requirements.txt，請手動安裝：
```bash
pip install flask flask-sqlalchemy flask-cors google-generativeai pillow
```

### 3. 設定 Gemini API 金鑰

#### 方法一：環境變數（推薦）
```bash
export GEMINI_API_KEY="您的_Gemini_API_金鑰"
```

#### 方法二：修改配置檔案
編輯 `src/main.py` 第 34 行：
```python
app.config['GEMINI_API_KEY'] = "您的_Gemini_API_金鑰"
```

### 4. 啟動應用
```bash
cd food_expiry_system_cursor_optimized
PYTHONPATH=/home/ubuntu/food_expiry_system_cursor_optimized python src/main.py
```

應用將在 `http://localhost:5001` 啟動。

## 使用指南

### 1. 上傳圖片
- 點擊上傳區域或拖放圖片
- 支援 JPG、PNG、WEBP 格式
- 檔案大小限制：10MB

### 2. 食品辨識
- 上傳圖片後點擊「識別食品」按鈕
- 系統會使用 Gemini API 分析圖片
- 辨識結果自動填入表單

### 3. 編輯與保存
- 檢查辨識結果的準確性
- 手動修改任何不正確的資訊
- 點擊「新增/更新食品」保存到資料庫

### 4. 管理食品
- 查看所有食品清單
- 監控即將到期的食品
- 使用分類篩選功能
- 查看統計圖表

## API 金鑰取得

1. 前往 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 登入您的 Google 帳戶
3. 創建新的 API 金鑰
4. 複製金鑰並設定到系統中

## 辨識提示詞

系統使用以下提示詞進行辨識：

```
請從這張圖片中辨識出食品的品名、可能的生產或到期日期（格式為YYYY-MM-DD，如果有多個日期請提供最接近當前的日期）、條碼（如果存在，請提供數字）、以及食品的類別（例如：飲料、罐頭、零食、乳製品、肉類、蔬菜、水果、烘焙、調味料、冷凍食品、其他）。請以JSON格式返回結果，如果無法辨識則對應欄位留空。
```

## 錯誤處理

### 常見問題

1. **API 金鑰錯誤**
   - 檢查金鑰是否正確設定
   - 確認金鑰有效且未過期

2. **辨識失敗**
   - 確保圖片清晰可見
   - 檢查網路連線
   - 重新上傳圖片

3. **模組找不到錯誤**
   - 確保設定 PYTHONPATH
   - 檢查所有依賴是否已安裝

### 日誌查看
系統會在控制台輸出詳細的日誌資訊，包括：
- 辨識過程
- 錯誤訊息
- API 回應

## 檔案結構

```
food_expiry_system_cursor_optimized/
├── src/
│   ├── main.py                          # 主應用程式
│   ├── models/
│   │   ├── food_item.py                 # 食品資料模型
│   │   └── recognition/
│   │       ├── gemini_recognition.py    # Gemini API 整合
│   │       └── food_recognition.py      # 辨識系統主邏輯
│   ├── routes/
│   │   └── upload.py                    # 上傳和辨識路由
│   ├── static/
│   │   ├── css/style.css               # 樣式表
│   │   ├── js/main.js                  # 前端 JavaScript
│   │   └── uploads/                    # 上傳檔案目錄
│   └── templates/
│       └── index.html                  # 主頁面模板
├── instance/
│   └── food_expiry.db                  # SQLite 資料庫
└── README_GEMINI_INTEGRATION.md        # 本說明文檔
```

## 安全注意事項

1. **API 金鑰保護**
   - 不要將 API 金鑰提交到版本控制系統
   - 使用環境變數或安全的配置管理

2. **檔案上傳安全**
   - 系統已限制檔案類型和大小
   - 定期清理上傳目錄

3. **生產環境部署**
   - 使用 WSGI 伺服器（如 Gunicorn）
   - 設定適當的防火牆規則
   - 使用 HTTPS 加密傳輸

## 版本資訊

- **版本**：Gemini Integration v1.0
- **最後更新**：2025-09-03
- **相容性**：Python 3.8+, Flask 2.0+

## 支援與回饋

如有任何問題或建議，請：
1. 檢查本文檔的常見問題部分
2. 查看系統日誌獲取詳細錯誤資訊
3. 確認 API 金鑰和網路連線正常

## 授權

本專案基於原始 food_expiry_system_cursor_optimized 專案進行修改，新增的 Gemini API 整合功能遵循相同的授權條款。

