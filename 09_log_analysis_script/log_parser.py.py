# -*- coding: utf-8 -*-
"""
AWS DCO (Data Center Operations) 인턴십 대비 교육용 로그 분석 스크립트
작성 목적: Python 기초 문법(파일 입출력, 문자열 파싱, 딕셔너리 집계)을 활용하여
          인프라 장비 로그를 정적 분석하고 보고서(Markdown) 파일로 저장하기.
"""

import os

# 입력 파일명과 출력 보고서 파일명을 정의합니다.
INPUT_FILE = "sample_dco_log.txt"
OUTPUT_FILE = "incident_summary.md"

def analyze_logs():
    print(f"[{INPUT_FILE}] 로그 파일 분석 작업을 시작합니다...")
    
    # 0. 입력 파일 존재 여부 검사 (파일이 없으면 오류가 나므로 사전에 방지합니다)
    if not os.path.exists(INPUT_FILE):
        print(f"오류: '{INPUT_FILE}' 파일이 현재 경로에 존재하지 않습니다.")
        print("로그 파일을 먼저 생성하거나 경로를 확인해 주세요.")
        return

    # 분석에 필요한 변수들을 초기화합니다.
    total_lines = 0               # 전체 로그 라인 수
    severity_counts = {}          # 심각도별(INFO, WARNING 등) 발생 빈도를 저장할 딕셔너리
    event_counts = {}             # 이벤트별(Normal heartbeat, Fan Alert 등) 빈도를 저장할 딕셔너리
    warning_or_critical_logs = [] # WARNING, ERROR, CRITICAL 수준의 중요한 로그들을 수집할 리스트
    major_events = []             # CRC_ERROR, LINK_DOWN, TICKET_ESCALATED 관련 주요 이벤트 정보 저장 리스트

    # 1. 파일 열기 (with 문을 사용하면 파일 처리가 끝난 후 자동으로 닫힙니다)
    # 인코딩은 한글 및 다국어 지원을 위해 'utf-8'을 지정합니다.
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip() # 문자열 앞뒤의 줄바꿈(\\n)이나 공백 제거
            
            # 빈 줄은 분석에서 제외하고 다음 줄로 넘어갑니다.
            if not line:
                continue
                
            total_lines += 1
            
            # 로그의 형식: YYYY-MM-DD HH:MM:SS | DEVICE | SEVERITY | EVENT | MESSAGE
            # 파이프(|) 기호를 기준으로 쪼갭니다.
            parts = [part.strip() for part in line.split("|")]
            
            # 정상적인 로그 행은 총 5개의 필드로 구성되어야 합니다.
            if len(parts) != 5:
                # 형식이 맞지 않는 비정상적인 라인은 건너뜁니다.
                continue
                
            # 각 필드를 변수에 나누어 담습니다. (Unpacking)
            timestamp, device, severity, event, message = parts
            
            # 2. 심각도(Severity) 집계
            # 딕셔너리의 get() 메소드를 사용하여 기본값 0을 세팅하고 1을 더합니다.
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
            
            # 3. 이벤트(Event)별 집계
            event_counts[event] = event_counts.get(event, 0) + 1
            
            # 4. WARNING, ERROR, CRITICAL 로그 목록 별도 수집
            # 대소문자 구분을 없애고 안전하게 비교하기 위해 대문자로 변환해 확인합니다.
            sev_upper = severity.upper()
            if sev_upper in ["WARNING", "ERROR", "CRITICAL"]:
                warning_or_critical_logs.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })
                
            # 5. 핵심 이벤트 검출 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)
            # 로그에 들어있는 텍스트를 대문자로 변환하여 키워드가 포함되어 있는지 검사합니다.
            event_upper = event.upper()
            message_upper = message.upper()
            
            # A. CRC Error 체크 ("CRC" 키워드가 이벤트 이름이나 메시지에 들어있는가)
            is_crc = ("CRC" in event_upper) or ("CRC" in message_upper)
            
            # B. Link Down 체크 ("LINK DOWN" 이라는 단어나 "DOWN" 이라는 단어가 포함되었는가)
            # 단, Normal heartbeat의 DOWN 등 억울한 매칭을 피하기 위해 구체적으로 매칭합니다.
            is_link_down = ("LINK DOWN" in event_upper) or ("LINK DOWN" in message_upper) or (event_upper == "LINK DOWN") or ("CHANGED TO DOWN" in message_upper)
            
            # C. Ticket Escalated 체크 ("ESCALATED" 또는 "TICKET ESCALATED" 단어 포함 여부)
            is_ticket_escalated = ("ESCALATED" in event_upper) or ("ESCALATED" in message_upper) or ("TICKET ESCALATED" in event_upper)
            
            if is_crc or is_link_down or is_ticket_escalated:
                # 어떤 분류에 해당하는지 라벨을 달아줍니다.
                if is_crc:
                    category = "CRC_ERROR"
                elif is_link_down:
                    category = "LINK_DOWN"
                else:
                    category = "TICKET_ESCALATED"
                    
                major_events.append({
                    "category": category,
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })

    # 6. 결과를 'incident_summary.md' 보고서 파일로 생성하여 저장합니다.
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# 📋 AWS DCO 교육용 로그 분석 결과 보고서\n\n")
        out.write("이 보고서는 파이썬 표준 라이브러리만을 활용한 분석 스크립트(`dco_analyzer.py`)를 통해 가상의 DCO 실습 로그를 정밀 스캔한 결과물입니다.\n\n")
        
        # 1) 전체 분석 메트릭 요약
        out.write("## 1. 전반적인 분석 요약\n")
        out.write(f"- 📈 **전체 분석된 로그 건수:** {total_lines} 건\n")
        out.write(f"- ⚠️ **경고 및 장애급 로그 수 (WARNING/ERROR/CRITICAL):** {len(warning_or_critical_logs)} 건\n")
        out.write(f"- 🔍 **주요 관심 장애 이벤트 수 (CRC/LINK_DOWN/ESCALATION):** {len(major_events)} 건\n\n")
        
        # 2) 심각도별 통계 테이블
        out.write("## 2. 심각도(Severity)별 분포\n")
        out.write("장비 및 서비스 상태의 위험도를 보여주는 분포입니다.\n\n")
        out.write("| 심각도 등급 (Severity) | 로그 발생 개수 |\n")
        out.write("| :--- | :--- |\n")
        # 보기 좋게 심각도 이름을 정렬하여 출력합니다.
        for sev in sorted(severity_counts.keys()):
            count = severity_counts[sev]
            out.write(f"| {sev} | {count} 건 |\n")
        out.write("\n")
        
        # 3) 이벤트별 순위 테이블
        out.write("## 3. 이벤트 분류별 발생 빈도\n")
        out.write("어떤 형태의 이벤트가 가장 많이 기록되었는지 분석합니다.\n\n")
        out.write("| 이벤트 유형 (Event) | 발생 횟수 |\n")
        out.write("| :--- | :--- |\n")
        # 발생 횟수(count)가 높은 순서대로 내림차순 정렬하여 상위 목록을 기록합니다.
        sorted_events = sorted(event_counts.items(), key=lambda x: x[1], reverse=True)
        for evt, count in sorted_events:
            out.write(f"| {evt} | {count} 회 |\n")
        out.write("\n")
        
        # 4) WARNING 또는 CRITICAL 로그 상세 리스트
        out.write("## 4. 경고(WARNING) 및 장애(ERROR/CRITICAL) 상세 목록\n")
        out.write("현장 엔지니어가 즉시 원인을 점검하고 조치해야 하는 우선 등급 로그입니다.\n\n")
        if warning_or_critical_logs:
            out.write("| 발생 시간 | 대상 장비 | 심각도 | 이벤트 종류 | 상세 로그 메시지 |\n")
            out.write("| :--- | :--- | :--- | :--- | :--- |\n")
            for log in warning_or_critical_logs:
                # 굵은 글씨로 경고 레벨을 강조합니다.
                out.write(f"| {log['timestamp']} | {log['device']} | **{log['severity']}** | {log['event']} | {log['message']} |\n")
        else:
            out.write("🎉 *검출된 WARNING, ERROR, CRITICAL 로그가 없으며, 모든 인프라 장비가 지극히 정상입니다.*\n")
        out.write("\n")
        
        # 5) 주요 인시던트 집중 요약 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)
        out.write("## 5. 핵심 분석 이벤트 요약 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)\n")
        out.write("네트워크 안정성 및 장애 에스컬레이션 프로세스 상태를 파악하기 위한 전용 세션입니다.\n\n")
        if major_events:
            out.write("| 장애 분류 (Category) | 발생 시각 | 영향 장비 | 구체적 이벤트 | 조치 상황 및 티켓 상세 |\n")
            out.write("| :--- | :--- | :--- | :--- | :--- |\n")
            for ev in major_events:
                # 카테고리는 인라인 코드로 강조해 줍니다.
                out.write(f"| `{ev['category']}` | {ev['timestamp']} | {ev['device']} | {ev['event']} | {ev['message']} |\n")
        else:
            out.write("💡 *CRC 에러, 링크 다운, 혹은 서비스 티켓 상신 이벤트가 존재하지 않습니다.*\n")
            
        out.write("\n---\n")
        out.write("*이 문서는 교육 실무 실습 프로그램의 일환으로 자동 작성되었습니다. 실제 시스템의 물리적 고장 혹은 상용 클라우드 장애가 아님을 밝힙니다.*\n")

    print("\n[완료] 분석 보고서 파일이 성공적으로 생성되었습니다!")
    print(f"-> 생성된 파일명: '{OUTPUT_FILE}'")

if __name__ == "__main__":
    analyze_logs()
