import os

# 1. 파일 경로 설정
input_path = "07_log_analysis_script/sample_dco_log.txt"
output_path = "07_log_analysis_script/incident_summary.md"

def analyze_dco_logs():
    # 분석을 위한 변수 초기화
    total_lines = 0
    severity_counts = {}
    event_counts = {}
    high_priority_logs = []
    major_event_summary = []

    # 요약해야 할 주요 이벤트 키워드
    major_keywords = ["CRC_ERROR", "LINK_DOWN", "TICKET_ESCALATED"]

    # 파일이 없는 경우를 대비한 예외 처리
    if not os.path.exists(input_path):
        print(f"오류: {input_path} 파일을 찾을 수 없습니다.")
        return

    # 2. 파일 읽기 및 분석
    with open(input_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line: continue  # 빈 줄은 건너뜁니다.
            
            total_lines += 1
            
            # 로그 형식이 '|'로 구분되어 있으므로 이를 나눕니다.
            # 형식: YYYY-MM-DD HH:MM:SS | DEVICE | SEVERITY | EVENT | MESSAGE
            parts = [p.strip() for p in line.split("|")]
            
            if len(parts) < 5: continue # 형식이 맞지 않는 줄은 건너뜁니다.
            
            timestamp, device, severity, event, message = parts

            # 심각도(Severity)별 개수 카운트
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
            
            # 이벤트(Event)별 개수 카운트
            event_counts[event] = event_counts.get(event, 0) + 1

            # WARNING 또는 CRITICAL 로그 수집
            if severity in ["WARNING", "CRITICAL"]:
                high_priority_logs.append(line)

            # 주요 키워드가 포함된 이벤트 요약 수집
            if any(keyword in event for keyword in major_keywords):
                major_event_summary.append(f"- [{severity}] {device}: {event} ({message})")

    # 3. 분석 결과 마크다운 형식으로 작성
    report_content = []
    report_content.append("# 📋 DCO 로그 분석 요약 보고서\n")
    report_content.append(f"## 1. 전체 분석 결과")
    report_content.append(f"- **총 로그 줄 수:** {total_lines}개\n")

    report_content.append("## 2. 심각도별 통계")
    for sev, count in severity_counts.items():
        report_content.append(f"- {sev}: {count}건")
    report_content.append("")

    report_content.append("## 3. 이벤트 유형별 통계")
    for evt, count in event_counts.items():
        report_content.append(f"- {evt}: {count}건")
    report_content.append("")

    report_content.append("## 4. 주요 장애 관리 대상 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)")
    if major_event_summary:
        report_content.extend(major_event_summary)
    else:
        report_content.append("- 특이 사항 없음")
    report_content.append("")

    report_content.append("## 5. 고위험 로그 목록 (WARNING/CRITICAL)")
    if high_priority_logs:
        for log in high_priority_logs:
            report_content.append(f"- `{log}`")
    else:
        report_content.append("- 해당 사항 없음")

    # 4. 파일 저장
    # 폴더가 없다면 생성합니다.
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_content))

    print(f"분석이 완료되었습니다. 결과 파일: {output_path}")

if __name__ == "__main__":
    analyze_dco_logs()