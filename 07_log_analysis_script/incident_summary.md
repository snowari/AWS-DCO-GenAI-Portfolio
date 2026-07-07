# 📋 DCO 로그 분석 요약 보고서

## 1. 전체 분석 결과
- **총 로그 줄 수:** 140개

## 2. 심각도별 통계
- INFO: 135건
- WARNING: 3건
- ERROR: 2건

## 3. 이벤트 유형별 통계
- Normal heartbeat: 125건
- Fan Alert: 1건
- Ticket opened: 3건
- Ticket escalated: 3건
- Maintenance completed: 3건
- Temperature warning: 1건
- SSD failure warning: 1건
- CRC error 증가: 1건
- Link Down: 1건
- Link Up: 1건

## 4. 주요 장애 관리 대상 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)
- 특이 사항 없음

## 5. 고위험 로그 목록 (WARNING/CRITICAL)
- `2026-07-03 01:05:00 | DEMO_CORE_SW_02 | WARNING | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2`
- `2026-07-03 02:05:00 | EDU_SRV_R04_N12 | WARNING | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12`
- `2026-07-03 03:05:00 | SAMPLE_TOR_SW_01 | WARNING | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1`