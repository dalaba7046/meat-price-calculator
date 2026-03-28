# 🥩 肉身價值計算機 (Meat-Body Value Calculator)

這是一個充滿社會惡意的工具。透過串接台灣最新豬肉與牛肉批發價格，對比使用者的月薪與體重（台斤），精確計算出你在肉類市場中的「身價分級」。

> **警語：** 計算結果可能導致職涯焦慮或食慾不振，請斟酌使用。

---

## 🚀 核心邏輯

本專案不儲存任何使用者隱私資料（薪資、體重），所有運算皆在客戶端（瀏覽器）完成。

1. **體重換算：** $KG \times 1.667 = 台斤$
2. **身價計算：** $月薪 \div 總台斤 = 單斤身價$
3. **即時對比：** 串接「中央畜產會」每日批發行情，將你的單斤身價與豬/牛肉價對比。

---

## 📊 身價分級系統 (Tier List)

| 身價倍數 (身價/肉價) | 等級稱號 | 系統回饋描述 |
|---|---|---|
| > 1.5x 牛價 | ✨ 頂級和牛 | 肉界貴族，勞動市場的稀有部位，建案廣告都在等你。 |
| 1.0x ~ 1.5x 牛價 | 🐂 溫體好牛 | 身價穩定，是社會的中流砥柱，值得被溫柔對待。 |
| 豬價 ~ 牛價之間 | 🐎 社會牛馬 | 雖然辛苦，但好歹是個撐起市場的要角。 |
| < 1.0x 豬價 | 🐕 豬狗等級 | 你的勞動力產出比豬肉還便宜，建議重新投胎或轉職。 |
| < 0.5x 豬價 | 💀 豬狗不如 | 系統已斷氣。你的身價連滷肉飯裡的碎肉都買不起。 |

---

## 📂 資料夾結構

```
meat-price-calculator/
├── .github/workflows/    # [自動化] 每日定時執行爬蟲更新肉價
├── data/                 # [數據] 存放爬蟲產出的 prices.json
├── scripts/              # [爬蟲] Python 爬蟲腳本 (scraper.py)
├── index.html            # [前端] 主頁面 (UI 與計算邏輯)
├── style.css             # [樣式] 迷因風格 CSS
└── README.md             # [說明] 本文件
```

---

## 🛠 技術棧

- **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla)
- **Backend (Data):** Python (BeautifulSoup / Requests)
- **Automation:** GitHub Actions（用於每日更新 `data/prices.json`）
- **Hosting:** GitHub Pages（零成本託管）

---

## 📡 數據來源

- **豬肉：** [中央畜產會 - 毛豬批發行情](https://ppg.naif.org.tw/)
- **牛肉：** 中央畜產會 - 肉牛交易行情

---

## 🚀 部署到 GitHub Pages

1. Fork 或 clone 此倉庫
2. 在 GitHub repo Settings → Pages，設定 Source 為 `main` branch 根目錄
3. GitHub Actions 會在每天 08:00 (台灣時間) 自動執行爬蟲並更新 `data/prices.json`
4. 可至 Actions 頁面手動觸發 **每日更新肉價** workflow 立即更新

## 🐍 手動執行爬蟲

```bash
pip install requests beautifulsoup4 lxml
python scripts/scraper.py
```
