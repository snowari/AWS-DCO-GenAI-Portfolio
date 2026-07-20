# 🌐 AWS DCO 인턴십 직무 이해를 위한 생성형 AI 활용 포트폴리오

> [!IMPORTANT]
> **본 저장소는 데이터 센터 운영(DCO) 직무 이해와 인프라 장애 조치 프로세스를 학습하기 위해 작성된 교육 실습용 포트폴리오입니다.**
> 수록된 모든 로그, 티켓 ID, 장비명 및 조치 시나리오는 가상의 샘플 데이터이며, 실제 AWS의 상용 인프라, 운영 절차, 혹은 특정 서비스 시스템과 무관함을 밝힙니다.

---

## 📝 프로젝트 소개

본 프로젝트는 데이터 센터 운영(DCO, Data Center Operations) 직무의 핵심 역할과 실무 흐름을 탐구하고, 생성형 AI(Generative AI) 비서와의 적극적인 협업을 통해 **인프라 상태 진단, 장애 분석 자동화, 그리고 근무 교대(Shift Handover) 워크플로우**를 완성해 나간 실무 학습형 결과물입니다.

AI를 단순한 질답용 도구가 아닌 **페어 프로그래머이자 테크니컬 라이터**로 포지셔닝하여, DCO 기초 개념 정의부터 로그 파싱 엔진 구축, 인시던트 리포트 검증, 티켓 우선순위 분류까지 주도적으로 검증하고 수정하는 "인간-AI 협업 프로세스"를 정립했습니다.

---

## 📅 차시별 학습 및 수행 내용

본 포트폴리오는 총 12차시의 단계별 시나리오를 바탕으로 점진적으로 인프라 운영 역량을 심화하도록 설계되었습니다.

| 차시 | 주요 활동 테마 | 산출물 및 실습 문서 바로가기 |
| :--- | :--- | :--- |
| **1차시** | DCO 직무 분석 및 생성형 AI 활용 지점 도출 | [DCO 직무 키워드 정의서](file:///D:/AWS-DCO-GenAI-Portfolio/01_dco_glossary/dco_job_keywords.md) |
| **2차시** | 개인 강점 연계 DCO 협업 리포트 작성 | [DCO 직무 협업 유형 리포트](file:///D:/AWS-DCO-GenAI-Portfolio/02_dco_profile/dco_collaboration_profile.md) |
| **3차시** | 데이터 센터 인프라 기초 용어 체계화 | [DCO 기초 용어 사전](file:///D:/AWS-DCO-GenAI-Portfolio/01_dco_glossary/dco_infra_terms.md) |
| **4차시** | 교육용 SOP(표준운영절차) 분석 및 체크리스트화 | [SOP 분석 및 요약본](file:///D:/AWS-DCO-GenAI-Portfolio/03_sop_analysis/dco_sop_summary_and_checklist.md) / [체크리스트](file:///D:/AWS-DCO-GenAI-Portfolio/03_sop_analysis/dco_sop_checklist.md) |
| **5차시** | 로컬 개발 환경(Python/Git/VS Code) 구성 | [개발 환경 자가진단표](file:///D:/AWS-DCO-GenAI-Portfolio/04_environment_setup/install_check.md) |
| **6차시** | AI 협업용 Antigravity CLI 환경 검증 | [agy CLI 검증서](file:///D:/AWS-DCO-GenAI-Portfolio/05_antigravity_cli/agy_cli_check.md) |
| **7차시** | `agy` 기반 인프라 점검 체크리스트 자동 작성 | [랙 점검 가이드](file:///D:/AWS-DCO-GenAI-Portfolio/06_cli_file_automation/rack_checklist.md) / [샘플 티켓](file:///D:/AWS-DCO-GenAI-Portfolio/06_cli_file_automation/sample_ticket.md) |
| **8차시** | `agy` 활용 교육용 모의 로그 분석 | [모의 로그 분석기 V1](file:///D:/AWS-DCO-GenAI-Portfolio/07_log_analysis_script/log_parser.py) |
| **9차시** | Google AI Studio 활용 분석 파서 고도화 | [로그 파서 스크립트 V2](file:///D:/AWS-DCO-GenAI-Portfolio/09_log_analysis_script/log_parser.py.py) / [대시보드 요약본](file:///D:/AWS-DCO-GenAI-Portfolio/09_log_analysis_script/incident_summary.md) |
| **10차시** | CRC Error 및 Link Down 장애 상태 진단 | [CRC 및 링크다운 분석서](file:///D:/AWS-DCO-GenAI-Portfolio/10_incident_analysis/crc_linkdown_analysis.md) |
| **11차시** | 교차 검증을 거친 Incident Report 초안 작성 | [교육용 Incident Report](file:///D:/AWS-DCO-GenAI-Portfolio/11_incident_report/dco_incident_report.md) |
| **12차시** | 티켓 영향도 평가 및 교대 인수인계 전송 | [우선순위 판단 매트릭스 CSV](file:///D:/AWS-DCO-GenAI-Portfolio/12_ticket_triage_handover/ticket_priority_matrix.csv) / [Shift Handover Memo](file:///D:/AWS-DCO-GenAI-Portfolio/12_ticket_triage_handover/shift_handover.md) |

---

## 🚀 프로젝트에서 수행한 주요 활동

- **인프라 용어 및 표준 절차(SOP) 구조화:** 랙(Rack), ToR 스위치, SLA, NIC 등 데이터 센터 핵심 하드웨어 및 운영 용어를 색인화하고 복잡한 SOP 가이드를 원클릭 점검용 마크다운 체크리스트로 단순화했습니다.
- **자동화 및 로그 파싱 파이프라인 개발:** Python 정규식을 이용해 비정형 데이터 센터 모의 로그파일을 파싱하여, 심각도(Severity) 및 이벤트 카테고리별로 자동 분류해 주는 진단 툴(`log_parser.py`)을 설계하고 실행했습니다.
- **장애 상황 단계별 원인 및 추정 분석:** 네트워크 링크 플래핑과 전송 CRC 에러 이슈를 대상으로, 실제 발생한 '사실 데이터'와 추론 영역인 '가능한 원인', 추가 규명이 필요한 '미확인 내용'을 명확히 격리 분석했습니다.
- **장애 보고서(Incident Report) 및 인수인계 체계 수립:** 현장 대응 작업 결과를 비전공자도 볼 수 있게 구조화하고, 교대 시점 발생 중인 오픈 티켓들의 서비스 영향과 이중화 상태를 분석해 티켓의 우선순위를 부여한 교대 메모(Handover Memo)를 기획했습니다.

---

## 🛠️ 사용 도구 및 활용 내용

| 도구 | 활용 목적 및 상세 내용 |
| :--- | :--- |
| **Antigravity CLI (`agy`)** | 로컬 프로젝트의 디렉토리 탐색, 마크다운 문서 자동 템플릿 생성 및 다차원 로그 정밀 스캔 자동화 적용. |
| **Google AI Studio** | 대규모 모의 로그 파싱을 위한 고성능 Python 정규 표현식 추출 로직 생성 및 대시보드 스크립트 피드백 수렴. |
| **Gemini (3.5 Flash)** | DCO 도메인 개념 학습 가이드 및 장애 분석 보고서 톤앤매너 검증, 한국어 인코딩 교정 조력자. |
| **Python** | 모의 로그 분석 파서 개발 (`log_parser.py`), `server.log` 다중 파일 분류 자동화 구현. |
| **VS Code** | Python 스크립트 작성, 테스트용 가상 디렉토리 파일 상태 동기화 및 마크다운 최종 가독성 레이아웃 설계. |
| **Git / GitHub** | 각 실습 단계별 산출물의 이력 추적 및 학습형 포트폴리오를 위한 버전 관리(BOM 인코딩 제어 이력 등). |

---

## 📊 주요 산출물 일람

```text
AWS-DCO-GenAI-Portfolio/
├── 01_dco_glossary/
│   ├── dco_infra_terms.md          # 랙, PDU, ToR 스위치 등 물리 장비 용어 사전
│   └── dco_job_keywords.md         # DCO 직무 키워드 및 개념 정리서
├── 02_dco_profile/
│   └── dco_collaboration_profile.md # DCO 직무 맞춤형 협업 리포트
├── 03_sop_analysis/
│   ├── dco_sop_summary_and_checklist.md # SOP 개요 및 위험 예방 체크리스트
│   └── dco_sop_checklist.md        # 가상 하드웨어 조치용 절차 체크리스트
├── 04_environment_setup/
│   └── install_check.md            # Python 및 로컬 환경 진단표
├── 05_antigravity_cli/
│   └── agy_cli_check.md            # agy CLI 실행 및 통합 환경 확인서
├── 06_cli_file_automation/
│   ├── rack_checklist.md           # CLI 생성용 물리 랙 실사 가이드템플릿
│   └── sample_ticket.md            # 모의 티켓 구조화 템플릿
├── 09_log_analysis_script/
│   ├── log_parser.py.py            # 로그 데이터 자동 분류 파서 스크립트
│   └── incident_summary.md         # Severity/Event별 수량 계측 통계서
├── 10_incident_analysis/
│   └── crc_linkdown_analysis.md    # 포트 CRC 및 링크 다운 시간순 심층 분석서
├── 11_incident_report/
│   └── dco_incident_report.md      # 가상 DCO 장애 분석 종합 보고서 (최종안)
└── 12_ticket_triage_handover/
    ├── ticket_priority_matrix.csv  # 윈도우/코드 범용 (UTF-8 BOM) 우선순위 표
    └── shift_handover.md           # 3줄 요약을 포함한 근무 인수인계 메모
```

---

## 💡 생성형 AI 활용 원칙

포트폴리오 설계 과정에서 AI의 무분별한 결과 채택으로 발생할 수 있는 데이터 왜곡 및 보안 사고를 방지하기 위해 다음과 같은 **협업 가이드라인**을 준수했습니다.

1. **초안으로의 한정 사용:** AI가 제공한 텍스트 및 스크립트는 정답이 아닌 '검토용 초안'으로 한정하여, 사람이 최종적으로 인코딩 및 기재 수치를 교차 확인했습니다.
2. **사실(Fact)과 가설의 완벽 격리:** 로그 상 확인되는 사실 데이터(예: CRC 154건, 팬 RPM 15%)와 유추 영역(예: 케이블 노화 가능성, 포트 이물질 오염 가능성)을 섞어 서술하지 않고 분류를 이원화했습니다.
3. **독립적 의사결정:** 서비스 영향성 평가 및 티켓 우선순위 선정 시, AI의 자체 추론에 전적으로 의존하지 않고 사용자가 직접 6대 판단 기준을 연계해 최종 결정을 내렸습니다.
4. **엄격한 데이터 가상화:** 실제 기업 내부 인프라 식별자, 개인 IP, 장비 조작 패스워드 등 민감한 비공개 보안 정보는 일절 입력 데이터로 공유하지 않고 오직 실습용 가상 식별자만 활용했습니다.

---

## 🎯 배운 점 (Key Takeaways)

- **정량적 로그 분석의 가치:** 인프라 장애 시 "연결이 되지 않는다"는 모호한 표현 대신, "Gi0/1 포트에서 5분간 154개의 CRC 에러 발생 후 다운됨"과 같은 정량적 데이터 기반의 인포메이션 추출법을 학습했습니다.
- **Severity(심각도)와 Priority(우선순위)의 분리:** 단순 장비 이상 수준(Severity)과 현재 가용성(이중화 작동 여부, 복구 상태, 영향 서버 대수)에 근거해 실무적으로 무엇을 먼저 해결할지 결정하는 업무의 우선순위(Priority) 조율 매커니즘을 터득했습니다.
- **이중화 시스템 설계의 중요성:** PDU 전압 이상이나 SSD 장애 발생 시 백업 피드(B Feed)와 스토리지 미러링(RAID) 설계가 실제 대규모 서비스 다운타임을 방어하는 핵심 장벽이 됨을 로그 흐름 분석을 통해 입증했습니다.
- **교차 검증 및 인코딩 트러블슈팅:** AI 어시스턴트 사용 시 윈도우와 코드 에디터 간 인코딩 인식차(EUC-KR vs UTF-8 BOM)와 같은 로컬 파일 입출력 문제를 파이썬 인코딩 변환 스크립트 실행을 통해 실전 트러블슈팅하며 운영 환경에서의 정밀성 중요도를 체득했습니다.

---

## ⚠️ 프로젝트 범위와 제한

본 저장소의 모든 실무 결과물은 학습형 모의 과제입니다.

- 실제 AWS DCO 현업 서비스 인프라 점검 가이드라인이 아닙니다.
- 내부 비공개 SOP(표준운영절차)나 기밀 운영 툴의 스크린샷은 수록하지 않았습니다.
- 가상 시나리오에 한해 하드웨어 문제를 분석하며, 실제 대규모 상용 망의 물리적 장비 교체 조치 절차를 대변하지 않습니다.
