import html
import re
from base64 import b64encode
from pathlib import Path

import requests
import streamlit as st


API_URL = "http://127.0.0.1:8001/allocate"
APP_DIR = Path(__file__).resolve().parent
LOGO_PATH = APP_DIR / "assets" / "investai-growth.svg"
LOGO_DATA_URI = "data:image/svg+xml;base64," + b64encode(LOGO_PATH.read_bytes()).decode("ascii")


st.set_page_config(
    page_title="InvestAI",
    page_icon=str(APP_DIR / "assets" / "investai-growth.svg"),
    layout="wide",
    initial_sidebar_state="expanded",
)


def title_case(value: str) -> str:
    return value.strip().title() if value else ""


def esc(value) -> str:
    return html.escape(str(value), quote=True)


def clean_result_markdown(text: str) -> str:
    return re.sub(
        r"(?m)^\s*[-*_]{3,}\s*$",
        '<div class="thin-separator"></div>',
        text,
    )


def card(icon: str, label: str, value: str, tone: str = "blue") -> str:
    return (
        f'<div class="profile-card {tone}">'
        f'<div class="profile-icon">{icon}</div>'
        "<div>"
        f'<div class="profile-label">{esc(label)}</div>'
        f'<div class="profile-value">{esc(value)}</div>'
        "</div>"
        "</div>"
    )


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900&display=swap');

    :root {
        --muted: #9fb0cc;
        --text: #f7f9ff;
    }

    html, body, [class*="css"] {
        font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .stApp {
        color: var(--text);
        background:
            radial-gradient(circle at 18% 8%, rgba(105, 72, 255, .25), transparent 23%),
            radial-gradient(circle at 74% 3%, rgba(20, 42, 120, .45), transparent 28%),
            radial-gradient(circle at 92% 24%, rgba(4, 211, 220, .16), transparent 24%),
            linear-gradient(135deg, #081024 0%, #050915 54%, #06131c 100%);
    }

    .stApp:before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background-image:
            linear-gradient(rgba(255,255,255,.025) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,.025) 1px, transparent 1px);
        background-size: 32px 32px;
        mask-image: linear-gradient(90deg, transparent 0%, #000 18%, #000 88%, transparent 100%);
    }

    header[data-testid="stHeader"] {
        background: rgba(5, 9, 21, .72);
        border-bottom: 1px solid rgba(91, 126, 186, .18);
        backdrop-filter: blur(14px);
    }

    [data-testid="stSidebarCollapsedControl"] button,
    button[kind="headerNoPadding"] {
        color: #dcecff !important;
    }

    .main .block-container {
        max-width: 1420px;
        padding: .25rem 2.3rem 1.6rem !important;
    }

    div[data-testid="stAppViewBlockContainer"] {
        padding-top: 0 !important;
    }

    section[data-testid="stSidebar"] {
        width: 332px !important;
        background:
            radial-gradient(circle at 15% 10%, rgba(30, 193, 255, .11), transparent 27%),
            linear-gradient(180deg, rgba(10, 21, 43, .98), rgba(6, 12, 27, .99));
        border-right: 1px solid rgba(89, 119, 175, .28);
        box-shadow: 18px 0 60px rgba(0, 0, 0, .35);
    }

    section[data-testid="stSidebar"] > div {
        padding: .85rem 1.25rem 1.1rem;
    }

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    .stMarkdown p {
        color: var(--muted) !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: var(--text) !important;
    }

    .brand-row {
        display: flex;
        align-items: center;
        gap: 13px;
        margin: 2px 0 22px;
    }

    .brand-mark {
        width: 72px;
        height: 72px;
        display: grid;
        place-items: center;
    }

    .brand-logo-image {
        width: 72px;
        height: 72px;
        display: block;
        filter: drop-shadow(0 0 18px rgba(75, 96, 255, .38));
    }

    .growth-logo {
        position: relative;
        width: 46px;
        height: 44px;
    }

    .growth-logo .bar {
        position: absolute;
        bottom: 8px;
        width: 8px;
        border-radius: 3px 3px 1px 1px;
        background: linear-gradient(180deg, #39d9ff, #7b55ff);
        box-shadow: 0 0 9px rgba(52, 210, 255, .42);
    }

    .growth-logo .bar.one {
        left: 5px;
        height: 13px;
    }

    .growth-logo .bar.two {
        left: 18px;
        height: 22px;
    }

    .growth-logo .bar.three {
        left: 31px;
        height: 31px;
    }

    .growth-logo .axis {
        content: "";
        position: absolute;
        left: 3px;
        right: 3px;
        bottom: 6px;
        height: 3px;
        border-radius: 999px;
        background: rgba(139, 110, 255, .9);
    }

    .growth-logo .arrow {
        position: absolute;
        left: 6px;
        top: 15px;
        width: 34px;
        height: 22px;
        border-left: 4px solid #39d9ff;
        border-top: 4px solid #39d9ff;
        border-radius: 3px 0 0 0;
        transform: skew(-32deg) rotate(-19deg);
        transform-origin: left bottom;
        filter: drop-shadow(0 0 8px rgba(57, 217, 255, .65));
    }

    .growth-logo .arrow-head {
        position: absolute;
        right: 1px;
        top: 4px;
        width: 14px;
        height: 14px;
        border-top: 4px solid #39d9ff;
        border-right: 4px solid #39d9ff;
        transform: rotate(6deg);
        filter: drop-shadow(0 0 8px rgba(57, 217, 255, .65));
    }

    .growth-logo .dot {
        position: absolute;
        right: 3px;
        top: 1px;
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #39d9ff;
        box-shadow: 0 0 10px rgba(57, 217, 255, .75);
    }

    .brand-title {
        color: #ffffff;
        font-size: 29px;
        line-height: 1;
        font-weight: 900;
        letter-spacing: 0;
    }

    .brand-title span {
        color: #57b8ff;
    }

    .brand-subtitle {
        margin-top: 7px;
        color: #9fb0c8;
        font-size: 11px;
        font-weight: 600;
    }

    .side-hero,
    .demo-card,
    .privacy-card {
        border: 1px solid rgba(93, 113, 255, .46);
        border-radius: 13px;
        background: linear-gradient(135deg, rgba(48, 61, 140, .66), rgba(18, 31, 59, .62));
        box-shadow: inset 0 0 28px rgba(115, 92, 255, .14), 0 13px 34px rgba(0,0,0,.2);
        padding: 14px;
    }

    .side-hero {
        display: flex;
        align-items: center;
        gap: 13px;
        margin-bottom: 18px;
    }

    .side-icon,
    .small-icon {
        width: 44px;
        height: 44px;
        flex: 0 0 44px;
        display: grid;
        place-items: center;
        border-radius: 13px;
        background: linear-gradient(135deg, rgba(93, 102, 255, .75), rgba(69, 56, 160, .8));
        color: white;
        font-size: 23px;
        box-shadow: 0 0 24px rgba(98, 85, 255, .28);
    }

    .side-title {
        color: white;
        font-size: 15px;
        font-weight: 850;
    }

    .side-text {
        margin-top: 3px;
        color: #bac7dd;
        font-size: 12px;
        line-height: 1.35;
    }

    .sidebar-label {
        display: flex;
        gap: 5px;
        align-items: center;
        margin: 11px 0 8px;
        color: #b9c6dc;
        font-size: 13px;
        font-weight: 700;
    }

    div[role="radiogroup"] {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
        padding: 6px;
        border-radius: 13px;
        border: 1px solid rgba(68, 87, 132, .62);
        background: linear-gradient(135deg, rgba(20, 33, 62, .96), rgba(11, 21, 42, .96));
        box-shadow: inset 0 1px rgba(255,255,255,.05), 0 12px 24px rgba(0,0,0,.12);
    }

    div[role="radiogroup"] label {
        margin: 0 !important;
        min-height: 43px;
        justify-content: center;
        border-radius: 10px;
        color: #dce6f7 !important;
        font-size: 12px;
        font-weight: 800;
        border: 1px solid transparent;
        transition: .18s ease;
    }

    div[role="radiogroup"] label p,
    div[role="radiogroup"] label span,
    div[role="radiogroup"] label div {
        color: #dce6f7 !important;
        font-weight: 850 !important;
        white-space: nowrap;
    }

    div[role="radiogroup"] label:has(input:checked) {
        background: linear-gradient(135deg, #6b78ff, #49b8ff);
        box-shadow: 0 7px 20px rgba(74, 132, 255, .32);
        border-color: rgba(141, 200, 255, .58);
    }

    div[role="radiogroup"] label:has(input:checked) p,
    div[role="radiogroup"] label:has(input:checked) span,
    div[role="radiogroup"] label:has(input:checked) div {
        color: #ffffff !important;
    }

    div[role="radiogroup"] label > div:first-child {
        opacity: 0 !important;
        width: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .demo-card {
        margin-top: 18px;
        background: linear-gradient(145deg, rgba(20, 35, 69, .86), rgba(13, 25, 48, .88));
        border-color: rgba(75, 94, 146, .44);
    }

    .demo-head {
        display: flex;
        gap: 12px;
        align-items: flex-start;
        margin-bottom: 16px;
    }

    .demo-grid {
        border-radius: 12px;
        padding: 13px;
        background: rgba(36, 52, 90, .64);
    }

    .demo-row {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        color: #c5d1e6;
        font-size: 12px;
        line-height: 2.35;
        font-weight: 700;
    }

    .demo-row span {
        color: #d7e2f6;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .demo-row strong {
        color: #f3f7ff;
    }

    .privacy-card {
        display: flex;
        gap: 12px;
        margin-top: 21px;
        border-color: rgba(49, 107, 206, .58);
        background: linear-gradient(135deg, rgba(24, 42, 87, .78), rgba(9, 30, 60, .78));
    }

    .stNumberInput input,
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(19, 31, 58, .9) !important;
        border-color: rgba(80, 103, 158, .65) !important;
        color: white !important;
        border-radius: 12px !important;
    }

    .status-wrap {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 16px;
        margin: 0 0 4px;
    }

    .backend-pill {
        display: inline-flex;
        align-items: center;
        gap: 9px;
        padding: 10px 15px;
        border: 1px solid rgba(68, 122, 176, .38);
        border-radius: 999px;
        background: rgba(7, 22, 42, .72);
        color: #1de5ca;
        font-size: 12px;
        font-weight: 850;
    }

    .backend-pill:before {
        content: "";
        width: 11px;
        height: 11px;
        border-radius: 50%;
        background: #00d5ab;
        box-shadow: 0 0 18px #00d5ab;
    }

    .theme-dot {
        width: 39px;
        height: 39px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        border: 1px solid rgba(100, 129, 178, .3);
        background: rgba(17, 28, 52, .8);
        color: white;
        font-size: 18px;
    }

    .hero-shell {
        position: relative;
        min-height: 248px;
        overflow: hidden;
    }

    .hero-shell:before {
        content: "";
        position: absolute;
        left: -120px;
        right: -70px;
        top: 118px;
        height: 140px;
        border-top: 2px solid rgba(88, 72, 255, .34);
        border-radius: 50%;
        transform: rotate(-6deg);
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 15px;
        border: 1px solid rgba(80, 99, 255, .72);
        border-radius: 999px;
        background: linear-gradient(90deg, rgba(92, 69, 218, .48), rgba(27, 91, 156, .36));
        color: #9ec3ff;
        font-size: 12px;
        font-weight: 900;
        box-shadow: 0 0 22px rgba(74, 90, 255, .24);
    }

    .hero-title {
        margin-top: 11px;
        max-width: 660px;
        font-size: clamp(38px, 4.35vw, 62px);
        line-height: .98;
        font-weight: 950;
        letter-spacing: 0;
        color: #fbfcff;
        text-shadow: 0 2px 0 rgba(255,255,255,.12), 0 18px 44px rgba(0,0,0,.38);
    }

    .hero-title span {
        background: linear-gradient(90deg, #a690ff 0%, #7d80ff 45%, #12dde2 100%);
        -webkit-background-clip: text;
        color: transparent;
    }

    .hero-copy {
        margin-top: 16px;
        max-width: 770px;
        color: #b9ccec;
        font-size: 17px;
        line-height: 1.55;
        font-weight: 650;
    }

    .hero-art {
        position: relative;
        width: min(100%, 460px);
        height: 255px;
        min-width: 0;
        margin-left: auto;
        overflow: visible;
        isolation: isolate;
    }

    .art-glow {
        position: absolute;
        inset: 48px 24px 0;
        z-index: -2;
        border-radius: 50%;
        background: radial-gradient(ellipse, rgba(11, 227, 216, .16), rgba(88, 59, 255, .18) 34%, transparent 70%);
        filter: blur(14px);
    }

    .podium {
        position: absolute;
        right: 36px;
        bottom: 2px;
        width: 325px;
        height: 74px;
        border-radius: 50%;
        z-index: 0;
        background: radial-gradient(ellipse at 50% 36%, rgba(36, 45, 119, .93), rgba(10, 15, 48, .92) 68%);
        border-bottom: 8px solid #11d9d3;
        box-shadow: 0 18px 30px rgba(0, 0, 0, .38), 0 0 32px rgba(14, 215, 210, .3);
    }

    .podium:before,
    .podium:after {
        content: "";
        position: absolute;
        border-radius: 50%;
    }

    .podium:before {
        left: 22px;
        right: 22px;
        bottom: 13px;
        height: 48px;
        background: radial-gradient(ellipse at 50% 40%, rgba(37, 24, 112, .94), rgba(11, 14, 45, .92) 74%);
        border-bottom: 6px solid rgba(135, 68, 255, .78);
        box-shadow: 0 0 21px rgba(125, 65, 255, .35);
    }

    .podium:after {
        left: 50px;
        right: 50px;
        bottom: 34px;
        height: 28px;
        background: radial-gradient(ellipse, rgba(14, 39, 78, .95), rgba(10, 15, 44, .86) 70%);
        border-bottom: 2px solid rgba(58, 222, 235, .5);
    }

    .chart-panel {
        position: absolute;
        right: 100px;
        top: 20px;
        z-index: 2;
        width: 190px;
        height: 137px;
        overflow: hidden;
        border-radius: 12px;
        border: 1px solid rgba(116, 89, 255, .72);
        background:
            linear-gradient(rgba(120, 108, 255, .09) 1px, transparent 1px),
            linear-gradient(90deg, rgba(120, 108, 255, .09) 1px, transparent 1px),
            linear-gradient(145deg, rgba(41, 43, 114, .92), rgba(11, 18, 54, .92));
        background-size: 24px 24px, 24px 24px, auto;
        box-shadow: inset 0 1px rgba(255, 255, 255, .13), inset 0 0 30px rgba(118, 85, 255, .16), 0 0 28px rgba(52, 79, 255, .28);
    }

    .chart-bars {
        position: absolute;
        left: 38px;
        right: 22px;
        bottom: 22px;
        height: 80px;
        display: flex;
        align-items: end;
        justify-content: space-between;
    }

    .bar {
        width: 16px;
        border-radius: 5px 5px 1px 1px;
        background: linear-gradient(180deg, #bb54ff, #3076ff);
        box-shadow: 0 0 13px rgba(102, 104, 255, .48);
    }

    .b1 { height: 31px; }
    .b2 { height: 46px; }
    .b3 { height: 64px; }
    .b4 { height: 82px; }

    .trend-line {
        position: absolute;
        left: 43px;
        top: 54px;
        width: 122px;
        height: 66px;
    }

    .trend-line i {
        position: absolute;
        height: 2px;
        transform-origin: left center;
        background: linear-gradient(90deg, #7d74ff, #19e0e2);
        box-shadow: 0 0 9px rgba(24, 221, 229, .64);
    }

    .trend-line i:nth-child(1) { left: 0; top: 49px; width: 37px; transform: rotate(-29deg); }
    .trend-line i:nth-child(2) { left: 32px; top: 30px; width: 36px; transform: rotate(-23deg); }
    .trend-line i:nth-child(3) { left: 65px; top: 15px; width: 35px; transform: rotate(-28deg); }
    .trend-line i:nth-child(4) { left: 95px; top: 0; width: 28px; transform: rotate(-37deg); }

    .trend-end {
        position: absolute;
        right: 4px;
        top: -6px;
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #20e5e1;
        box-shadow: 0 0 12px #20e5e1;
    }

    .donut {
        position: absolute;
        right: 12px;
        top: 49px;
        z-index: 2;
        width: 78px;
        height: 78px;
        border-radius: 14px;
        border: 1px solid rgba(89, 100, 224, .72);
        background: linear-gradient(145deg, rgba(36, 45, 105, .9), rgba(13, 23, 60, .92));
        box-shadow: inset 0 1px rgba(255,255,255,.1), 0 0 23px rgba(75, 84, 255, .27);
    }

    .donut:after {
        content: "";
        position: absolute;
        inset: 18px;
        border-radius: 50%;
        background: conic-gradient(#10dfd7 0 32%, #7449ff 32% 63%, #36adff 63% 100%);
        box-shadow: inset 0 0 0 14px rgba(10, 19, 47, .96);
    }

    .alloc-chip {
        position: absolute;
        z-index: 3;
        min-width: 70px;
        padding: 12px;
        border-radius: 10px;
        font-weight: 900;
        line-height: 1;
        border: 1px solid;
        box-shadow: 0 0 25px currentColor;
        backdrop-filter: blur(8px);
    }

    .alloc-chip small {
        display: block;
        margin-bottom: 4px;
        font-size: 12px;
    }

    .alloc-chip strong {
        font-size: 26px;
    }

    .stocks {
        left: 15px;
        top: 82px;
        color: #77a4ff;
        background: rgba(42, 82, 197, .48);
        transform: rotate(-5deg);
    }

    .bonds {
        left: 110px;
        top: 149px;
        color: #13f0dc;
        background: rgba(0, 148, 135, .42);
    }

    .cash {
        right: 42px;
        top: 146px;
        color: #ffd16f;
        background: rgba(190, 112, 16, .45);
        transform: rotate(4deg);
    }

    .orb {
        position: absolute;
        border-radius: 50%;
        background: #13dbe5;
        box-shadow: 0 0 18px currentColor;
    }

    .orb.one { width: 9px; height: 9px; color: #4da2ff; left: 29px; top: 28px; }
    .orb.two { width: 8px; height: 8px; color: #12e0d8; right: 14px; top: 96px; }
    .orb.three { width: 7px; height: 7px; color: #754dff; right: 40px; top: 158px; }

    .pill-card,
    .feature-card {
        min-height: 58px;
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 12px 16px;
        border-radius: 13px;
        border: 1px solid rgba(57, 86, 147, .64);
        background: linear-gradient(135deg, rgba(16, 34, 70, .78), rgba(9, 20, 43, .82));
        box-shadow: inset 0 1px rgba(255,255,255,.06);
    }

    .pill-card.purple { border-color: rgba(111, 91, 255, .52); }
    .pill-card.teal { border-color: rgba(16, 205, 204, .42); }

    .pill-icon,
    .feature-icon {
        width: 36px;
        height: 36px;
        display: grid;
        place-items: center;
        font-size: 24px;
        color: white;
    }

    .pill-title,
    .feature-title {
        color: #dfe8ff;
        font-size: 13px;
        font-weight: 850;
    }

    .pill-sub,
    .feature-sub {
        margin-top: 3px;
        color: #a8b9d5;
        font-size: 12px;
        line-height: 1.35;
    }

    .profile-panel {
        margin-top: 18px;
        padding: 17px 19px 18px;
        border-radius: 17px;
        border: 1px solid rgba(64, 92, 151, .6);
        background: linear-gradient(160deg, rgba(14, 29, 62, .82), rgba(7, 15, 32, .88));
        box-shadow: 0 18px 60px rgba(0,0,0,.2);
    }

    .section-head {
        display: flex;
        gap: 14px;
        align-items: center;
        margin-bottom: 18px;
    }

    .section-icon {
        width: 40px;
        height: 40px;
        display: grid;
        place-items: center;
        border-radius: 12px;
        color: white;
        font-size: 27px;
        background: linear-gradient(135deg, #6d72ff, #35b7ff);
    }

    .section-title {
        color: white;
        font-size: 23px;
        font-weight: 900;
        letter-spacing: 0;
    }

    .section-sub {
        margin-top: 5px;
        color: #aebbd3;
        font-size: 13px;
        font-weight: 650;
    }

    .profile-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 16px;
    }

    .profile-card {
        display: flex;
        align-items: center;
        gap: 16px;
        min-height: 91px;
        padding: 15px 18px;
        border-radius: 12px;
        border: 1px solid rgba(80, 105, 170, .62);
        background: linear-gradient(135deg, rgba(30, 50, 99, .82), rgba(17, 28, 56, .86));
        min-width: 0;
    }

    .profile-card.purple {
        border-color: rgba(103, 75, 159, .76);
        background: linear-gradient(135deg, rgba(53, 37, 89, .86), rgba(25, 22, 51, .88));
    }

    .profile-card.teal {
        border-color: rgba(11, 129, 132, .76);
        background: linear-gradient(135deg, rgba(17, 74, 80, .84), rgba(12, 41, 51, .9));
    }

    .profile-card.gold {
        border-color: rgba(137, 111, 72, .74);
        background: linear-gradient(135deg, rgba(59, 51, 42, .88), rgba(34, 31, 30, .92));
    }

    .profile-icon {
        width: 66px;
        height: 66px;
        display: grid;
        place-items: center;
        flex: 0 0 66px;
        border-radius: 15px;
        background: rgba(99, 130, 235, .28);
        font-size: 32px;
        box-shadow: inset 0 1px rgba(255,255,255,.08);
    }

    .profile-label {
        color: #8fa1c0;
        font-size: 13px;
        font-weight: 800;
    }

    .profile-value {
        margin-top: 8px;
        color: #ffffff;
        font-size: clamp(18px, 1.6vw, 23px);
        font-weight: 950;
        line-height: 1.1;
        overflow-wrap: anywhere;
    }

    .stButton > button {
        width: 100%;
        height: 63px;
        border: 0 !important;
        border-radius: 999px !important;
        color: white !important;
        background: linear-gradient(90deg, #813cff 0%, #6d5cff 35%, #25a0f2 70%, #08dfcb 100%) !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        box-shadow: 0 18px 50px rgba(48, 111, 255, .34), 0 0 30px rgba(8, 223, 203, .22);
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 22px 64px rgba(48, 111, 255, .42), 0 0 38px rgba(8, 223, 203, .3);
    }

    .why-title {
        display: flex;
        align-items: center;
        gap: 11px;
        margin: 24px 0 5px;
        color: white;
        font-size: 22px;
        font-weight: 950;
    }

    .why-sub {
        color: #9fabbd;
        font-size: 13px;
        font-weight: 650;
        margin: 0 0 12px 42px;
    }

    .feature-card {
        min-height: 104px;
        padding: 13px 17px;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 16px;
    }

    .st-key-feature_ai .stButton > button,
    .st-key-feature_allocation .stButton > button,
    .st-key-feature_etf .stButton > button {
        position: relative;
        min-height: 116px;
        height: 116px;
        padding: 18px 58px 18px 92px;
        border: 1px solid !important;
        border-radius: 14px !important;
        color: #dfe8ff !important;
        text-align: left;
        white-space: pre-line;
        font-size: 14px !important;
        font-weight: 850 !important;
        line-height: 1.55 !important;
        box-shadow: inset 0 1px rgba(255,255,255,.06), 0 10px 30px rgba(0,0,0,.13) !important;
        transform: none !important;
    }

    .st-key-feature_ai .stButton > button {
        border-color: rgba(91, 58, 184, .82) !important;
        background: linear-gradient(135deg, rgba(31, 28, 88, .9), rgba(18, 22, 50, .94)) !important;
    }

    .st-key-feature_allocation .stButton > button {
        border-color: rgba(0, 135, 121, .82) !important;
        background: linear-gradient(135deg, rgba(7, 72, 68, .88), rgba(10, 38, 48, .94)) !important;
    }

    .st-key-feature_etf .stButton > button {
        border-color: rgba(141, 82, 35, .82) !important;
        background: linear-gradient(135deg, rgba(71, 43, 35, .9), rgba(36, 27, 29, .95)) !important;
    }

    .st-key-feature_ai .stButton > button:before,
    .st-key-feature_allocation .stButton > button:before,
    .st-key-feature_etf .stButton > button:before {
        position: absolute;
        left: 18px;
        top: 23px;
        width: 56px;
        height: 56px;
        display: grid;
        place-items: center;
        border-radius: 15px;
        font-size: 28px;
    }

    .st-key-feature_ai .stButton > button:before {
        content: "✦";
        background: rgba(102, 85, 255, .28);
    }

    .st-key-feature_allocation .stButton > button:before {
        content: "◔";
        background: rgba(4, 220, 196, .22);
    }

    .st-key-feature_etf .stButton > button:before {
        content: "▣";
        background: rgba(239, 136, 58, .22);
    }

    .st-key-feature_ai .stButton > button:after,
    .st-key-feature_allocation .stButton > button:after,
    .st-key-feature_etf .stButton > button:after {
        content: "›";
        position: absolute;
        right: 17px;
        top: 40px;
        width: 33px;
        height: 33px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        background: rgba(255,255,255,.1);
        color: #dce7f8;
        font-size: 25px;
        font-weight: 700;
    }

    .st-key-feature_ai .stButton > button:hover,
    .st-key-feature_allocation .stButton > button:hover,
    .st-key-feature_etf .stButton > button:hover {
        transform: translateY(-2px) !important;
        filter: brightness(1.13);
    }

    .feature-detail {
        display: grid;
        grid-template-columns: 54px 1fr;
        gap: 16px;
        margin-top: 16px;
        padding: 18px 20px;
        border: 1px solid rgba(73, 107, 172, .58);
        border-radius: 14px;
        background: linear-gradient(135deg, rgba(16, 31, 64, .92), rgba(8, 18, 38, .95));
        box-shadow: inset 0 1px rgba(255,255,255,.06);
    }

    .feature-detail-icon {
        width: 52px;
        height: 52px;
        display: grid;
        place-items: center;
        border-radius: 14px;
        background: linear-gradient(135deg, rgba(100, 88, 255, .56), rgba(34, 174, 225, .46));
        font-size: 26px;
    }

    .feature-detail-title {
        color: #ffffff;
        font-size: 17px;
        font-weight: 900;
    }

    .feature-detail-copy {
        margin-top: 5px;
        color: #b5c4dc;
        font-size: 13px;
        line-height: 1.55;
        font-weight: 650;
    }

    .feature-card.purple {
        border-color: rgba(91, 58, 184, .82);
        background: linear-gradient(135deg, rgba(31, 28, 88, .82), rgba(18, 22, 50, .88));
    }

    .feature-card.teal {
        border-color: rgba(0, 135, 121, .82);
        background: linear-gradient(135deg, rgba(7, 72, 68, .78), rgba(10, 38, 48, .88));
    }

    .feature-card.orange {
        border-color: rgba(141, 82, 35, .82);
        background: linear-gradient(135deg, rgba(71, 43, 35, .82), rgba(36, 27, 29, .9));
    }

    .feature-icon {
        width: 68px;
        height: 68px;
        flex: 0 0 68px;
        border-radius: 15px;
        background: rgba(102, 85, 255, .25);
        font-size: 34px;
    }

    .feature-card.teal .feature-icon {
        background: rgba(4, 220, 196, .22);
    }

    .feature-card.orange .feature-icon {
        background: rgba(239, 136, 58, .22);
    }

    .next-dot {
        margin-left: auto;
        width: 34px;
        height: 34px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: #d4dcee;
        background: rgba(255,255,255,.1);
        font-size: 24px;
        font-weight: 700;
    }

    .steps {
        display: grid;
        grid-template-columns: 1fr 80px 1fr 80px 1fr;
        align-items: center;
        margin-top: 14px;
        opacity: .78;
    }

    .step-item {
        display: grid;
        grid-template-columns: 51px 1fr;
        align-items: center;
        gap: 16px;
    }

    .step-num {
        width: 44px;
        height: 44px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        border: 2px solid rgba(48, 186, 220, .45);
        background: linear-gradient(135deg, rgba(91, 68, 205, .78), rgba(32, 59, 126, .8));
        color: white;
        font-size: 18px;
        font-weight: 900;
    }

    .step-line {
        border-top: 2px dotted rgba(103, 121, 161, .45);
    }

    .step-title {
        color: #c6cfde;
        font-size: 13px;
        font-weight: 900;
    }

    .step-copy {
        margin-top: 3px;
        color: #758399;
        font-size: 12px;
        line-height: 1.35;
        font-weight: 650;
    }

    .result-box {
        padding: 18px 20px;
        border-radius: 16px;
        border: 1px solid rgba(64, 92, 151, .62);
        background: linear-gradient(145deg, rgba(15, 29, 56, .9), rgba(9, 17, 35, .92));
        color: #dce7f8;
    }

    .result-box p,
    .result-box li,
    .result-box h1,
    .result-box h2,
    .result-box h3 {
        color: #dce7f8 !important;
    }

    .result-box hr {
        height: 1px !important;
        min-height: 1px !important;
        margin: 10px 0 12px !important;
        border: 0 !important;
        border-top: 1px solid rgba(116, 145, 196, .24) !important;
        background: transparent !important;
        box-shadow: none !important;
    }

    .result-box table {
        width: 100%;
        margin: 10px 0 14px;
        border-collapse: collapse;
        border-spacing: 0;
        background: transparent !important;
    }

    .result-box th,
    .result-box td {
        padding: 10px 12px;
        border: 0 !important;
        border-bottom: 1px solid rgba(116, 145, 196, .18) !important;
        color: #dce7f8 !important;
        background: transparent !important;
    }

    .result-box th {
        color: #ffffff !important;
        font-weight: 900;
    }

    .result-box thead tr,
    .result-box tbody tr {
        border: 0 !important;
        background: transparent !important;
    }

    .thin-separator {
        width: 100%;
        height: 1px;
        margin: 8px 0 10px;
        background: rgba(132, 162, 214, .28);
        border: 0;
        border-radius: 0;
        box-shadow: none;
    }

    .result-disclaimer {
        margin-top: 14px;
        padding: 12px 14px;
        border-radius: 13px;
        border: 1px solid rgba(247, 186, 80, .34);
        background: rgba(92, 61, 16, .22);
        color: #f4d28f;
        font-size: 12px;
        line-height: 1.45;
        font-weight: 650;
    }

    div[data-testid="stAlert"] {
        border-radius: 14px;
    }

    hr {
        height: 1px !important;
        min-height: 1px !important;
        margin: 8px 0 10px !important;
        border: 0 !important;
        border-top: 1px solid rgba(100, 125, 171, .18) !important;
        background: transparent !important;
        box-shadow: none !important;
    }

    .footer-note {
        margin-top: 22px;
        color: #72819a;
        font-size: 11px;
        text-align: center;
        line-height: 1.7;
    }

    @media (max-width: 900px) {
        .main .block-container {
            padding: .35rem 1rem 1.3rem !important;
        }

        .hero-art {
            display: none;
        }

        .hero-title {
            font-size: 40px;
        }

        .steps {
            grid-template-columns: 1fr;
            gap: 14px;
        }

        .step-line {
            display: none;
        }

        .profile-grid,
        .feature-grid {
            grid-template-columns: 1fr;
        }
    }

    @media (min-width: 901px) and (max-width: 1180px) {
        .profile-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }

        .feature-grid {
            grid-template-columns: 1fr;
        }

        .hero-art {
            transform: scale(.86);
            transform-origin: top right;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown(
        f"""
        <div class="brand-row">
            <div class="brand-mark">
                <img class="brand-logo-image" src="{LOGO_DATA_URI}" alt="InvestAI logo">
            </div>
            <div>
                <div class="brand-title">Invest<span>AI</span></div>
                <div class="brand-subtitle">Smart Investments, Brighter Futures</div>
            </div>
        </div>
        <div class="side-hero">
            <div class="side-icon">&#8962;</div>
            <div>
                <div class="side-title">Investment Profile</div>
                <div class="side-text">Tell us about your goals</div>
            </div>
        </div>
        <div class="sidebar-label">Choose Profile <span style="opacity:.6">&#9432;</span></div>
        """,
        unsafe_allow_html=True,
    )

    mode = st.radio(
        "Profile Mode",
        ["Example Profile", "My Profile"],
        label_visibility="collapsed",
        horizontal=True,
    )

    if mode == "Example Profile":
        age = 30
        goal = "retirement"
        horizon = 25
        risk = "medium"

        st.markdown(
            """
            <div class="demo-card">
                <div class="demo-head">
                    <div class="small-icon">&#9879;</div>
                    <div>
                        <div class="side-title">Demo Profile (Fixed)</div>
                        <div class="side-text">A pre-filled profile to quickly test the application.</div>
                    </div>
                </div>
                <div class="demo-grid">
                    <div class="demo-row"><span>&#127874; &nbsp; Age</span><strong>30</strong></div>
                    <div class="demo-row"><span>&#127919; &nbsp; Goal</span><strong>Retirement</strong></div>
                    <div class="demo-row"><span>&#8987; &nbsp; Horizon</span><strong>25 Years</strong></div>
                    <div class="demo-row"><span>&#128737; &nbsp; Risk</span><strong>Medium</strong></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """<div class="sidebar-label">Your Details</div>""",
            unsafe_allow_html=True,
        )
        age = st.number_input("Your Age", min_value=18, max_value=100, value=25, step=1)
        goal = st.selectbox(
            "Investment Goal",
            [
                "retirement",
                "buy a house",
                "wealth creation",
                "child education",
                "emergency fund",
                "other",
            ],
        )
        if goal == "other":
            goal = st.text_input("Enter your goal", placeholder="Example: Start a business")
        horizon = st.slider("Investment Horizon", min_value=1, max_value=50, value=10)
        risk = st.select_slider("Risk Tolerance", options=["low", "medium", "high"], value="medium")

    st.markdown(
        """
        <div class="privacy-card">
            <div class="small-icon">&#128737;</div>
            <div>
                <div class="side-title">Privacy</div>
                <div class="side-text">Your profile is used only to generate the investment recommendation.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <div class="status-wrap">
        <div class="backend-pill">Backend Connected</div>
        <div class="theme-dot">&#9788;</div>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_left, hero_right = st.columns([1.22, 0.78], gap="large")

with hero_left:
    st.markdown(
        """
        <div class="hero-shell">
            <div class="hero-badge">&#129302; AI-POWERED INVESTMENT PLANNER</div>
            <div class="hero-title">Build a smarter path to<br><span>your financial goals.</span></div>
            <div class="hero-copy">
                Get an AI-generated asset allocation and diversified ETF recommendations based on
                your age, investment goal, time horizon and risk tolerance.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown(
        """
        <div class="hero-art">
            <div class="art-glow"></div>
            <div class="orb one"></div>
            <div class="orb two"></div>
            <div class="orb three"></div>
            <div class="chart-panel">
                <div class="trend-line"><i></i><i></i><i></i><i></i><b class="trend-end"></b></div>
                <div class="chart-bars">
                    <div class="bar b1"></div>
                    <div class="bar b2"></div>
                    <div class="bar b3"></div>
                    <div class="bar b4"></div>
                </div>
            </div>
            <div class="donut"></div>
            <div class="alloc-chip stocks"><small>Stocks</small><strong>60%</strong></div>
            <div class="alloc-chip bonds"><small>Bonds</small><strong>30%</strong></div>
            <div class="alloc-chip cash"><small>Cash</small><strong>10%</strong></div>
            <div class="podium"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

pill1, pill2, pill3 = st.columns(3)
with pill1:
    st.markdown(
        """
        <div class="pill-card">
            <div class="pill-icon">&#128202;</div>
            <div><div class="pill-title">Personalized Analysis</div><div class="pill-sub">Powered by AI</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with pill2:
    st.markdown(
        """
        <div class="pill-card purple">
            <div class="pill-icon">&#9684;</div>
            <div><div class="pill-title">Smart Asset Allocation</div><div class="pill-sub">Stocks, Bonds &amp; Cash</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with pill3:
    st.markdown(
        """
        <div class="pill-card teal">
            <div class="pill-icon">&#127793;</div>
            <div><div class="pill-title">Diversified ETF Ideas</div><div class="pill-sub">Global Opportunities</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

profile_cards = "".join(
    [
        card("&#127874;", "Age", f"{age} Years", "blue"),
        card("&#127919;", "Investment Goal", title_case(goal), "purple"),
        card("&#8987;", "Investment Horizon", f"{horizon} Years", "teal"),
        card("&#128737;", "Risk Tolerance", title_case(risk), "gold"),
    ]
)

st.markdown(
    (
        '<div class="profile-panel">'
        '<div class="section-head">'
        '<div class="section-icon">&#128100;</div>'
        "<div>"
        '<div class="section-title">Your Investment Profile</div>'
        '<div class="section-sub">This information will be used by the AI investment agent.</div>'
        "</div>"
        "</div>"
        f'<div class="profile-grid">{profile_cards}</div>'
        "</div>"
    ),
    unsafe_allow_html=True,
)

st.write("")
generate = st.button("Generate My Investment Plan", use_container_width=True)


if generate:
    if mode == "My Profile" and not str(goal).strip():
        st.error("Please enter your investment goal.")
        st.stop()

    profile = {
        "age": age,
        "goal": goal,
        "horizon": horizon,
        "risk": risk,
    }

    try:
        with st.spinner("AI is building your investment plan..."):
            response = requests.post(API_URL, json=profile, timeout=120)

        if response.status_code == 200:
            result = response.json()
            st.success("Your investment plan is ready!")

            st.markdown(
                """
                <div class="why-title"><span>&#128202;</span><span>Suggested Asset Allocation</span></div>
                <div class="why-sub">AI-generated allocation based on your profile.</div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(clean_result_markdown(result["allocation"]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(
                """
                <div class="why-title"><span>&#128188;</span><span>ETF Recommendations</span></div>
                <div class="why-sub">Diversified ETF options aligned with the suggested allocation.</div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(clean_result_markdown(result["recommendations"]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(
                """
                <div class="result-disclaimer">
                    Educational use only. This application provides general investment information
                    and does not constitute personalized financial advice. Investments involve risk.
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.error("FastAPI returned an error.")
            st.code(response.text)

    except requests.exceptions.ConnectionError:
        st.error("FastAPI backend is not running.")
        st.code("uvicorn app:app --reload")
    except requests.exceptions.Timeout:
        st.error("The AI request took too long. Please try again.")
    except Exception as exc:
        st.error("Something went wrong.")
        st.exception(exc)

else:
    st.markdown(
        """
        <div class="why-title"><span>&#10024;</span><span>Why use InvestAI?</span></div>
        <div class="why-sub">A simple AI workflow for understanding your investment profile.</div>
        """,
        unsafe_allow_html=True,
    )

    feature_ai, feature_allocation, feature_etf = st.columns(3)
    with feature_ai:
        if st.button(
            "AI Analysis\nSee how your profile is understood",
            key="feature_ai",
            use_container_width=True,
        ):
            st.session_state.feature_detail = "ai"
    with feature_allocation:
        if st.button(
            "Smart Allocation\nSee how stocks, bonds and cash are balanced",
            key="feature_allocation",
            use_container_width=True,
        ):
            st.session_state.feature_detail = "allocation"
    with feature_etf:
        if st.button(
            "ETF Suggestions\nSee how diversified fund ideas are selected",
            key="feature_etf",
            use_container_width=True,
        ):
            st.session_state.feature_detail = "etf"

    feature_details = {
        "ai": (
            "✦",
            "AI Analysis",
            "This step reads your age, financial goal, investment horizon and risk tolerance together. "
            "It turns those details into a simple investment profile that guides the rest of the plan.",
        ),
        "allocation": (
            "◔",
            "Smart Allocation",
            "This explains how your money could be spread across growth assets such as stocks, "
            "stability-focused bonds, and cash. The mix is educational and is based on your time horizon and risk comfort.",
        ),
        "etf": (
            "▣",
            "ETF Suggestions",
            "This step maps the suggested asset mix to diversified ETF categories. ETFs are collections of investments, "
            "which can help spread exposure instead of depending on a single company or asset.",
        ),
    }

    selected_feature = st.session_state.get("feature_detail")
    if selected_feature in feature_details:
        detail_icon, detail_title, detail_copy = feature_details[selected_feature]
        st.markdown(
            f"""
            <div class="feature-detail">
                <div class="feature-detail-icon">{detail_icon}</div>
                <div>
                    <div class="feature-detail-title">{detail_title}</div>
                    <div class="feature-detail-copy">{detail_copy}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="why-title"><span>&#9889;</span><span>How It Works</span></div>
        <div class="why-sub">Get your investment plan in 3 simple steps.</div>
        <div class="steps">
            <div class="step-item">
                <div class="step-num">1</div>
                <div><div class="step-title">Enter Your Profile</div><div class="step-copy">Provide your age, goal, investment horizon and risk tolerance.</div></div>
            </div>
            <div class="step-line"></div>
            <div class="step-item">
                <div class="step-num">2</div>
                <div><div class="step-title">AI Builds Allocation</div><div class="step-copy">LangGraph processes your profile through the investment workflow.</div></div>
            </div>
            <div class="step-line"></div>
            <div class="step-item">
                <div class="step-num">3</div>
                <div><div class="step-title">Get ETF Ideas</div><div class="step-copy">The AI maps the suggested allocation to diversified ETF options.</div></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
