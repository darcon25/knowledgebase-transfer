#!/usr/bin/env python3
"""AI 伺服器 PCB／CCL 供應鏈追蹤名單。

環節順序即產業鏈上下游順序，build_pages.py 用它推導上下游關係。
代號與名稱皆已比對證交所／櫃買中心 API 驗證（2026-08-28）。
"""

# 環節由上游到下游排列，順序有意義
SEGMENTS = [
    ("銅箔", "銅箔是 PCB 的導電層原料，銅價與報價轉嫁是全鏈最上游的訊號"),
    ("玻纖布", "玻纖布與玻纖紗是基板的補強材，供給吃緊時會卡住整條鏈"),
    ("樹脂", "樹脂決定基板的高頻高速特性，是 AI 伺服器規格升級的關鍵材料"),
    ("CCL", "銅箔基板，把銅箔、玻纖布、樹脂壓合成板材，PCB 廠的直接上游"),
    ("PCB", "印刷電路板廠，AI 伺服器主板與加速卡的主要受惠者"),
    ("軟板HDI", "軟性電路板與高密度連接板，手機與伺服器內部連接"),
    ("載板", "IC 載板（ABF／BT），連接晶片與主板，供給長期吃緊"),
    ("鑽針耗材", "PCB 鑽孔耗材，出貨量是 PCB 廠稼動率的領先指標"),
    ("封測", "封裝測試，先進封裝（CoWoS、Cu-Cu）需求的直接受惠者"),
    ("電源散熱", "伺服器電源與散熱，功耗上升的受惠者"),
    ("終端需求", "晶片與伺服器品牌／代工，整條鏈的需求源頭"),
]

# code: (名稱, 環節)
COMPANIES = {
    "8358": ("金居", "銅箔"),
    "1303": ("南亞", "銅箔"),
    "1815": ("富喬", "玻纖布"),
    "1802": ("台玻", "玻纖布"),
    "1446": ("宏和", "玻纖布"),
    "5340": ("建榮", "玻纖布"),
    "5475": ("德宏", "玻纖布"),
    "1717": ("長興", "樹脂"),
    "6274": ("台燿", "CCL"),
    "2383": ("台光電", "CCL"),
    "6213": ("聯茂", "CCL"),
    "6672": ("騰輝電子-KY", "CCL"),
    "2368": ("金像電", "PCB"),
    "2313": ("華通", "PCB"),
    "2316": ("楠梓電", "PCB"),
    "5469": ("瀚宇博", "PCB"),
    "6141": ("柏承", "PCB"),
    "8213": ("志超", "PCB"),
    "4958": ("臻鼎-KY", "軟板HDI"),
    "6269": ("台郡", "軟板HDI"),
    "6153": ("嘉聯益", "軟板HDI"),
    "8039": ("台虹", "軟板HDI"),
    "3037": ("欣興", "載板"),
    "8046": ("南電", "載板"),
    "3189": ("景碩", "載板"),
    "8021": ("尖點", "鑽針耗材"),
    "3711": ("日月光投控", "封測"),
    "6510": ("精測", "封測"),
    "2308": ("台達電", "電源散熱"),
    "3324": ("雙鴻", "電源散熱"),
    "3017": ("奇鋐", "電源散熱"),
    "3665": ("貿聯-KY", "電源散熱"),
    "2330": ("台積電", "終端需求"),
    "2382": ("廣達", "終端需求"),
    "3231": ("緯創", "終端需求"),
    "2317": ("鴻海", "終端需求"),
}

# 有持倉但不在這條鏈上，只建簡頁不做鏈分析
OFF_CHAIN = {
    "2885": "元大金",
    "2481": "強茂",
    "0050": "元大台灣50",
    "009816": "凱基台灣TOP50",
    "009819": "中信數據及電力",
}

SEGMENT_ORDER = [name for name, _ in SEGMENTS]
SEGMENT_DESC = dict(SEGMENTS)


def segment_of(code: str) -> str:
    return COMPANIES.get(code, (None, None))[1]


def peers(code: str) -> list:
    """同環節的其他公司代號。"""
    seg = segment_of(code)
    return [c for c, (_, s) in COMPANIES.items() if s == seg and c != code]


def neighbours(code: str) -> tuple:
    """(上游環節, 下游環節)，用於推導傳導路徑。"""
    seg = segment_of(code)
    if seg is None:
        return (None, None)
    i = SEGMENT_ORDER.index(seg)
    up = SEGMENT_ORDER[i - 1] if i > 0 else None
    down = SEGMENT_ORDER[i + 1] if i < len(SEGMENT_ORDER) - 1 else None
    return (up, down)


def companies_in(segment: str) -> list:
    return [c for c, (_, s) in COMPANIES.items() if s == segment]


def name_of(code: str) -> str:
    if code in COMPANIES:
        return COMPANIES[code][0]
    return OFF_CHAIN.get(code, code)


if __name__ == "__main__":
    print(f"追蹤 {len(COMPANIES)} 家（鏈上）+ {len(OFF_CHAIN)} 家（鏈外持倉）")
    for seg in SEGMENT_ORDER:
        members = [f"{c} {COMPANIES[c][0]}" for c in companies_in(seg)]
        print(f"  {seg:6} {len(members):2} 家｜{'、'.join(members)}")
