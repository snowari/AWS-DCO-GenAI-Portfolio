# 📋 AWS DCO 교육용 로그 분석 결과 보고서

이 보고서는 파이썬 표준 라이브러리만을 활용한 분석 스크립트(`dco_analyzer.py`)를 통해 가상의 DCO 실습 로그를 정밀 스캔한 결과물입니다.

## 1. 전반적인 분석 요약
- 📈 **전체 분석된 로그 건수:** 140 건
- ⚠️ **경고 및 장애급 로그 수 (WARNING/ERROR/CRITICAL):** 5 건
- 🔍 **주요 관심 장애 이벤트 수 (CRC/LINK_DOWN/ESCALATION):** 6 건

## 2. 심각도(Severity)별 분포
장비 및 서비스 상태의 위험도를 보여주는 분포입니다.

| 심각도 등급 (Severity) | 로그 발생 개수 |
| :--- | :--- |
| ERROR | 2 건 |
| INFO | 135 건 |
| WARNING | 3 건 |

## 3. 이벤트 분류별 발생 빈도
어떤 형태의 이벤트가 가장 많이 기록되었는지 분석합니다.

| 이벤트 유형 (Event) | 발생 횟수 |
| :--- | :--- |
| Normal heartbeat | 125 회 |
| Ticket opened | 3 회 |
| Ticket escalated | 3 회 |
| Maintenance completed | 3 회 |
| Fan Alert | 1 회 |
| Temperature warning | 1 회 |
| SSD failure warning | 1 회 |
| CRC error 증가 | 1 회 |
| Link Down | 1 회 |
| Link Up | 1 회 |

## 4. 경고(WARNING) 및 장애(ERROR/CRITICAL) 상세 목록
현장 엔지니어가 즉시 원인을 점검하고 조치해야 하는 우선 등급 로그입니다.

| 발생 시간 | 대상 장비 | 심각도 | 이벤트 종류 | 상세 로그 메시지 |
| :--- | :--- | :--- | :--- | :--- |
| 2026-07-03 01:05:00 | DEMO_CORE_SW_02 | **WARNING** | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2 |
| 2026-07-03 02:05:00 | EDU_SRV_R04_N12 | **WARNING** | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12 |
| 2026-07-03 02:10:00 | EDU_SRV_R04_N12 | **ERROR** | SSD failure warning | Drive Slot 3 SSD wearout indicator FAILING (SMART wear 96%). IP: 192.0.2.12 |
| 2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | **WARNING** | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |
| 2026-07-03 03:06:00 | SAMPLE_TOR_SW_01 | **ERROR** | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost. |

## 5. 핵심 분석 이벤트 요약 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)
네트워크 안정성 및 장애 에스컬레이션 프로세스 상태를 파악하기 위한 전용 세션입니다.

| 장애 분류 (Category) | 발생 시각 | 영향 장비 | 구체적 이벤트 | 조치 상황 및 티켓 상세 |
| :--- | :--- | :--- | :--- | :--- |
| `TICKET_ESCALATED` | 2026-07-03 01:10:00 | DEMO_CORE_SW_02 | Ticket escalated | Ticket EDU-TKT-2026-0001 escalated to Local Infrastructure Team. |
| `TICKET_ESCALATED` | 2026-07-03 02:15:00 | EDU_SRV_R04_N12 | Ticket escalated | Ticket EDU-TKT-2026-0002 escalated to DCO Hardware Support. |
| `CRC_ERROR` | 2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |
| `LINK_DOWN` | 2026-07-03 03:06:00 | SAMPLE_TOR_SW_01 | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost. |
| `TICKET_ESCALATED` | 2026-07-03 03:12:00 | SAMPLE_TOR_SW_01 | Ticket escalated | Ticket EDU-TKT-2026-0003 escalated to Onsite Cabling Team. |
| `CRC_ERROR` | 2026-07-03 03:30:00 | SAMPLE_TOR_SW_01 | Normal heartbeat | System status is healthy. Interface Gi0/1 running with 0 CRC errors. IP: 192.0.2.1 |

---
*이 문서는 교육 실무 실습 프로그램의 일환으로 자동 작성되었습니다. 실제 시스템의 물리적 고장 혹은 상용 클라우드 장애가 아님을 밝힙니다.*
