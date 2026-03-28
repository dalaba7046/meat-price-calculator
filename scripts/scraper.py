import sys
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import requests
from bs4 import BeautifulSoup
import json
import os
import re
from datetime import datetime

def safe_float(value):
    try:
        return float(value.replace(',', ''))
    except (TypeError, ValueError, AttributeError):
        return None

def extract_first_number(text):
    if not text: return None
    m = re.search(r"(\d+(?:\.\d+)?)", text.replace(',', ''))
    return safe_float(m.group(1)) if m else None

def get_pig_price_kg():
    """抓取毛豬批發價 (來源: PPG 畜產行情網)"""
    url = "https://ppg.naif.org.tw"
    headers = {'User-Agent': 'Mozilla/5.0...'}
    try:
        r = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        # 尋找表格中最新的日期列
        rows = soup.select("table tr")
        for row in rows:
            tds = row.find_all('td')
            if len(tds) >= 5 and re.match(r"\d{2}/\d{2}", tds[0].get_text(strip=True)):
                return extract_first_number(tds[-1].get_text(strip=True))
    except Exception as e:
        print(f"豬肉爬取失敗: {e}")
    return 79.2 # 預設值

def get_beef_price_kg():
    """抓取國產牛批發價 (來源: 中央畜產會首頁)"""
    url = "https://www.naif.org.tw"
    try:
        r = requests.get(url, timeout=15)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        # 定位「閹公牛」
        target_td = soup.find('td', string=re.compile(r'閹公牛'))
        if target_td:
            price_td = target_td.find_next_sibling('td')
            return extract_first_number(price_td.get_text(strip=True))
    except Exception as e:
        print(f"牛肉爬取失敗: {e}")
    return 189.0 # 預設值

def main():
    pork_kg = get_pig_price_kg()
    beef_kg = get_beef_price_kg()
    
    # 建立多來源 JSON 結構
    data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "wholesale": {
            "pig": round(pork_kg, 2),
            "beef": round(beef_kg, 2),
            "unit": "NTD/kg"
        },
        "reference_retail": {
            "pork_normal": 150,     # 一般豬肉零售
            "beef_imported": 400,   # 一般進口牛
            "beef_local": 600,      # 國產溫體牛
            "beef_premium": 1000    # 高檔肋眼/沙朗
        },
        "metadata": {
            "pork_source": "https://ppg.naif.org.tw",
            "beef_source": "https://www.naif.org.tw"
        }
    }

    # 寫入專案 data 目錄
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_path = os.path.join(repo_root, 'data', 'prices.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ 多來源架構已就緒！(寫入 {output_path})")

if __name__ == "__main__":
    main()
