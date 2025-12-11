# 變更日誌 - Gemini API 整合版

## [1.0.0] - 2025-09-03

### 新增功能
- ✨ 整合 Google Gemini API 進行食品辨識
- 🔍 支援品名、日期、條碼、類別的智能辨識
- 📝 辨識結果自動填入可編輯表單
- 🛡️ 完整的錯誤處理和容錯機制
- 🌐 新增 CORS 支援，改善前後端通信

### 修改內容
- 🔄 完全替換原有的辨識系統
- 📦 移除對 pyzbar、opencv-python、pytesseract 的依賴
- 🎨 優化前端介面，改善使用者體驗
- ⚙️ 重構後端架構，提升程式碼可維護性

### 技術改進
- 🚀 使用 Gemini 1.5 Flash 模型，提升辨識準確度
- 📅 支援多種日期格式自動轉換
- 🔧 改善配置管理，支援環境變數
- 📊 保持原有的數據管理和統計功能

### 檔案變更

#### 新增檔案
- `src/models/recognition/gemini_recognition.py` - Gemini API 整合模組
- `config.py` - 配置管理檔案
- `README_GEMINI_INTEGRATION.md` - 詳細使用說明
- `CHANGELOG.md` - 本變更日誌

#### 修改檔案
- `src/main.py` - 新增 CORS 支援和 Gemini API 配置
- `src/models/recognition/food_recognition.py` - 重構辨識系統邏輯
- `src/static/css/style.css` - 優化樣式設計
- `src/static/js/main.js` - 移除不必要的程式碼
- `requirements.txt` - 更新依賴清單

#### 移除功能
- ❌ 移除基於 OpenCV 和 Tesseract 的 OCR 辨識
- ❌ 移除條碼掃描功能（改為 AI 辨識）
- ❌ 移除複雜的圖像預處理流程

### 使用方式變更
1. **API 金鑰設定**：需要設定 Gemini API 金鑰
2. **啟動方式**：需要設定 PYTHONPATH 環境變數
3. **辨識流程**：簡化為一鍵辨識，結果自動填入表單

### 相容性
- ✅ 保持原有的資料庫結構
- ✅ 保持原有的 API 端點
- ✅ 保持原有的前端操作流程
- ✅ 向下相容現有的食品資料

### 已知問題
- ⚠️ 需要網路連線才能使用辨識功能
- ⚠️ Gemini API 有使用配額限制
- ⚠️ 辨識準確度依賴圖片品質

### 未來計劃
- 🔮 支援批量圖片辨識
- 🔮 新增辨識結果信心度顯示
- 🔮 支援更多語言的辨識
- 🔮 新增辨識歷史記錄功能

