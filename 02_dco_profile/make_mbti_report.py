# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

base = Path(r"D:\AWS-DCO-GenAI-Portfolio\02_dco_profile")
out = base / "dco_mbti_collaboration_report.png"
outputs = Path(r"C:\Users\user_26\Documents\Codex\2026-07-07\it-data-center-operations-dco-it\outputs")
outputs.mkdir(parents=True, exist_ok=True)
out_copy = outputs / "dco_mbti_collaboration_report.png"

font_regular = r"C:\Windows\Fonts\malgun.ttf"
font_bold = r"C:\Windows\Fonts\malgunbd.ttf"

def f(size, bold=False):
    return ImageFont.truetype(font_bold if bold else font_regular, size)

W, H = 1600, 2200
img = Image.new("RGB", (W, H), "#F5F7FA")
d = ImageDraw.Draw(img)

COLORS = {
    "navy": "#17243A",
    "teal": "#0F766E",
    "mint": "#DFF6EF",
    "blue": "#E8F0FF",
    "cream": "#FFF6E7",
    "white": "#FFFFFF",
    "text": "#111827",
    "muted": "#4B5563",
    "line": "#D8DEE8",
    "warning": "#2F3A4A",
}

def rr(x1, y1, x2, y2, fill, outline=None, width=2, r=28):
    d.rounded_rectangle((x1, y1, x2, y2), radius=r, fill=fill, outline=outline, width=width)

def text_size(text, font):
    box = d.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]

def wrap_by_px(text, font, max_width):
    lines = []
    for para in text.split("\n"):
        if para == "":
            lines.append("")
            continue
        current = ""
        for ch in para:
            trial = current + ch
            if text_size(trial, font)[0] <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)
    return lines

def draw_text(text, x, y, font, fill, max_width=None, line_gap=10):
    if max_width is None:
        d.text((x, y), text, font=font, fill=fill)
        return y + font.size + line_gap
    for line in wrap_by_px(text, font, max_width):
        d.text((x, y), line, font=font, fill=fill)
        y += font.size + line_gap
    return y

# Header
rr(70, 60, W-70, 335, COLORS["navy"], r=36)
d.text((120, 105), "DCO 협업 MBTI 리포트", font=f(58, True), fill="white")
d.text((120, 185), "ISTJ형 | 절차 기반 기록형 협업자", font=f(42, True), fill="#B8F3E6")
d.text((120, 250), "지금까지의 대화 기반 요약: 기록, 절차, 확인을 중심으로 협업하는 유형", font=f(28), fill="#D7DEE8")

# Summary card
rr(90, 385, W-90, 625, COLORS["white"], COLORS["line"], r=30)
d.text((130, 430), "1. 성향 요약", font=f(34, True), fill=COLORS["teal"])
summary = "문제를 바로 단정하기보다 먼저 사실을 정리하고, 정해진 절차에 따라 차분히 확인하는 편입니다. DCO 직무에서는 Ticket, SOP, Escalation, Incident Report처럼 기록과 전달이 중요한 협업 흐름에 잘 맞는 유형입니다."
draw_text(summary, 130, 490, f(29), COLORS["text"], max_width=W-260, line_gap=12)

# Strength cards
card_y = 675
card_w = 445
card_h = 300
gap = 40
cards = [
    ("강점 1", "꼼꼼한 기록", "작업 요청, 확인 내용, 조치 결과를 빠뜨리지 않고 남기려는 습관이 있습니다. Ticket 작성과 Incident Report 초안 작성에 강점으로 연결됩니다.", COLORS["mint"]),
    ("강점 2", "절차 준수", "임의로 판단하기보다 SOP와 체크리스트를 먼저 확인하는 방식이 안정적입니다. 반복 작업과 현장 운영에서 실수를 줄이는 데 도움이 됩니다.", COLORS["blue"]),
    ("강점 3", "확인과 질문", "모르는 상황을 혼자 넘기지 않고 필요한 경우 질문하거나 Escalation하려는 태도가 있습니다. 장애 대응에서 문제를 키우지 않는 협업 습관입니다.", COLORS["cream"]),
]
for i, (kicker, title, body, color) in enumerate(cards):
    x = 90 + i * (card_w + gap)
    rr(x, card_y, x+card_w, card_y+card_h, color, COLORS["line"], r=26)
    d.text((x+35, card_y+32), kicker, font=f(25, True), fill=COLORS["teal"])
    d.text((x+35, card_y+78), title, font=f(34, True), fill=COLORS["text"])
    draw_text(body, x+35, card_y+138, f(25), COLORS["muted"], max_width=card_w-70, line_gap=10)

# Workflow
rr(90, 1030, W-90, 1400, COLORS["white"], COLORS["line"], r=30)
d.text((130, 1075), "2. DCO 협업 흐름에서의 연결", font=f(34, True), fill=COLORS["text"])
flow = [
    ("Ticket", "문제 상황이나 작업 요청을 기록하고 공유하는 출발점"),
    ("SOP", "Ticket을 처리할 때 따라야 하는 표준 절차"),
    ("Escalation", "혼자 판단하기 어렵거나 권한이 필요한 상황을 상위 담당자에게 전달"),
    ("Incident Report", "발생 상황, 조치, 결과를 정리해 이후 학습과 재발 방지에 활용"),
]
y = 1145
for name, desc in flow:
    rr(130, y-8, 370, y+50, "#EAF7F4", r=18)
    d.text((155, y), name, font=f(28, True), fill=COLORS["teal"])
    d.text((410, y), desc, font=f(27), fill=COLORS["text"])
    y += 72

# Improvement and plan
rr(90, 1450, W-90, 1770, "#FFFDF7", "#E6DCC8", r=30)
d.text((130, 1495), "3. 보완할 점", font=f(34, True), fill=COLORS["text"])
improve = "아직 DCO 기술 용어와 장비 구조가 익숙하지 않을 수 있으므로, 처음 보는 상황에서 이해 속도가 느릴 수 있습니다. 따라서 기본 용어를 예시와 함께 정리하고, 교육용 장애 상황을 바탕으로 보고서 작성 연습을 반복하는 것이 좋습니다."
draw_text(improve, 130, 1555, f(27), COLORS["muted"], max_width=W-260, line_gap=12)

d.text((130, 1680), "학습 계획: 용어집 정리 → Ticket 초안 작성 → AI 답변 검토", font=f(29, True), fill=COLORS["teal"])

# Self evaluation
rr(90, 1820, W-90, 2000, COLORS["white"], COLORS["line"], r=30)
d.text((130, 1860), "4. 한 줄 자기 평가", font=f(34, True), fill=COLORS["text"])
self_eval = "저는 빠른 단정보다 정확한 확인, 개인 판단보다 절차 준수, 말로만 넘기기보다 기록으로 남기는 협업 태도를 키워가겠습니다."
draw_text(self_eval, 130, 1920, f(29), COLORS["muted"], max_width=W-260, line_gap=12)

# Footer warning
rr(90, 2045, W-90, 2140, COLORS["warning"], r=24)
warning = "보안 권고: 데이터센터 내부의 실물 부품 일련번호나 비공개 장비 명칭은 생성형 AI 프롬프트에 절대 기재하지 않습니다."
draw_text(warning, 125, 2072, f(25, True), "#FFFFFF", max_width=W-250, line_gap=8)

img.save(out)
img.save(out_copy)
print(str(out))
print(str(out_copy))
