# AjouLLM Agent — 프로젝트 분석 및 배포 로드맵

> **문서 목적**: 본 문서는 NousResearch/hermes-agent의 단순 fork에서 출발한 본 프로젝트를
> **아주대학교 학생을 위한 전문화된 AjouLLM 전용 AI Agent**로 발전시키기 위한
> 전략적 분석과 단계별 실행 계획을 제시한다.
>
> **작성 기준일**: 2026-05-07
> **현재 브랜치**: `main` (clean)
> **상위 5개 커밋**: 리브랜딩 / AjouLLM provider 통합 / 설치 경로 표준화

---

## 1. 프로젝트 정체성 분석 (Identity Analysis)

### 1.1 출발점 — Upstream과의 관계

| 구분 | Upstream (Hermes Agent) | AjouLLM Agent (본 프로젝트) |
|---|---|---|
| 제공자 | Nous Research | 아주대학교 학생 커뮤니티 |
| 대상 사용자 | 글로벌 일반 개발자 | 아주대학교 재학생·연구자 |
| LLM 백엔드 | OpenRouter, Anthropic, OpenAI 등 30+ provider | **AjouLLM Gateway (Mindlogic Factchat)** 우선 |
| 인증/과금 | 사용자 개별 API key | 학교 발급 API key (학생 무료/저비용 가정) |
| 설치 경로 | `~/.hermes` | `~/.ajou-hermes` (충돌 회피) |
| 브랜딩 | 일반 | Ajou Blue & Gold 전용 스킨 |
| 학습 루프 | 범용 skill 자동 생성 | 학업·연구 도메인 특화 skill 축적 |

### 1.2 정당성 (Why this project exists)

본 프로젝트가 단순한 fork를 넘어 독립 프로덕트로 존재해야 하는 **세 가지 근거**:

1. **인프라 정당성** — 아주대학교는 자체 LLM Gateway(`factchat-cloud.mindlogic.ai`)를
   운영한다. Upstream Hermes는 이 endpoint를 알지 못하며, OpenAI 호환 layer만으로는
   Mindlogic 특유의 인증·rate-limit·model catalog 노출 방식을 제대로 다룰 수 없다.
   → **provider profile을 통한 1급 시민(first-class) 통합이 필수**.
2. **사용자 정당성** — 일반 학생은 OpenAI/Anthropic 결제 수단이 없거나 부담스럽다.
   학교 LLM을 "기본값"으로 두고, 설치 후 바로 동작하는 zero-config 경험은 학생에게
   유의미한 진입 장벽 제거이다.
3. **교육적 정당성** — Closed Learning Loop가 학업 맥락(과제, 논문, 코딩 실습)에서
   축적되면, 학교 단위로 공유 가능한 "공통 skill 풀"이 만들어진다.
   이는 한 학생의 도구가 아닌 **학내 지식 자산**으로 발전 가능한 구조이다.

### 1.3 현재 진행 상황 (As-of 2026-05-07)

- [x] AjouLLM provider profile 작성 (`plugins/model-providers/ajoullm/`)
- [x] 설치 경로/브랜딩 표준화 (`.ajou-hermes`, README 한국어화)
- [x] 설치 스크립트 fork 운영자 repo로 재배선 (`shguddn8591/hermes-agent-ajou`)
- [x] Ajou Blue & Gold 스킨 추가
- [ ] AjouLLM Gateway 실제 endpoint 검증 및 model catalog 동기화
- [ ] 학생용 인증 플로우(학번/포털 연동) 미구현 — 현재는 raw API key 입력
- [ ] 한국어 문서 site (Docusaurus) — `website/` 존재하나 Ajou 콘텐츠 부재
- [ ] 학업 도메인 skill (인용 포맷, 학사 일정, LMS 연동 등) 미구현

---

## 2. 사용성 분석 (Usability Analysis)

### 2.1 사용자 페르소나

| 페르소나 | 기술 수준 | 주요 사용 시나리오 | 현재 진입 장벽 |
|---|---|---|---|
| **A. CS 전공 고학년** | 상 (CLI/git 익숙) | 코드 리뷰, PR 작성, 자동화 | 낮음 — 현재 타겟에 부합 |
| **B. 비전공 일반 학부생** | 하 (terminal 처음) | 과제 요약, 글쓰기, 일정 관리 | **매우 높음** — 설치부터 막힘 |
| **C. 대학원생/연구자** | 중상 | 논문 정리, 데이터 분석, 실험 자동화 | 중간 — Python 환경 이해 필요 |
| **D. 교직원** | 하~중 | 메일 초안, 일정 자동화 | 높음 — 데스크탑 GUI 부재 |

→ **현재 프로젝트는 A 페르소나만 만족**한다. B/D 페르소나를 잡지 못하면
"아주대 전체 학생용"이라는 슬로건은 성립하지 않는다.

### 2.2 사용성 결함(Usability Gaps) Top 7

1. **CLI 진입 장벽** — `curl | bash`는 비전공 학생에게 위협적이다.
2. **API key 수동 입력** — 학교 포털 SSO와 연결되지 않아, 키 발급 경로를 사용자가 직접 따라가야 한다.
3. **에러 메시지 영어 잔존** — `hermes doctor` 출력은 대부분 영어이다.
4. **gateway/messaging 설정 복잡도** — Telegram/Discord 연동은 토큰 발급이 선행되어야 한다.
5. **첫 실행 후 "무엇을 해야 할지" 가이드 부재** — onboarding wizard 후 빈 prompt만 떠 있다.
6. **업데이트 메커니즘 불투명** — fork 특성상 upstream 동기화 정책이 사용자에게 보이지 않는다.
7. **모바일 부재** — Termux 지원이 있으나, 일반 학생에게는 사실상 불가용.

---

## 3. 기술 부채 및 리스크 (Technical Debt & Risk)

### 3.1 Fork 관리 리스크

- **Upstream divergence**: NousResearch는 활발히 개발 중이다 (최근 커밋: `feat(models): grok-4.3 추가`).
  현재 운영 정책으로는 6개월 후 conflict가 폭증할 가능성이 높다.
- **권장**: `upstream` remote를 명시적으로 두고, 분기마다 dry-run merge를 수행하는 자동화(GitHub Action) 도입.

### 3.2 라이선스·브랜딩 리스크

- 원작자: Nous Research (MIT) → 라이선스 자체는 자유롭다.
- 그러나 README가 여전히 `hermes-agent.nousresearch.com` 문서 사이트와 Discord를 가리킨다.
  → **사용자가 문제 발생 시 잘못된 채널로 유입**되어 양쪽 커뮤니티 모두에 혼란을 야기한다.
- "아주대학교 전용(Exclusive)" 배지를 사용 중이나, 학교의 공식 승인 여부는 문서에 명시되어 있지 않다.
  → **학교 로고/명칭 사용 권한**을 공식 절차로 확보해야 배포 가능.

### 3.3 보안 리스크

- `.env.example`에 30+개 provider 키 자리표시자가 노출 — 일반 학생이 실수로 commit할 위험.
- Gateway 모듈은 Telegram/Discord webhook을 다루므로, 학생의 개인 채팅이 Mindlogic 서버를 경유한다.
  → **데이터 흐름·보존 정책**을 한국어 개인정보처리방침으로 명시해야 한다 (PIPA 준수).
- 학교 발급 API key를 다수 학생이 사용하므로, **rate-limit / abuse 모니터링 게이트웨이**가 학교 측에 필요하다.

### 3.4 운영 부채

- `RELEASE_v0.2.0.md` ~ `v0.12.0.md`까지 upstream 릴리즈 노트가 그대로 잔존 → **혼란 유발**.
- `hermes-already-has-routines.md` 같은 upstream 내부 메모가 남아 있음.
- `AGENTS.md` (44KB), `cli.py` (555KB) 등 거대 단일 파일 — fork 측 수정 시 conflict zone.

---

## 4. 일반 사용자 배포 조건 (Release Readiness Checklist)

> **목표 상태**: 비전공 학부생도 5분 내 설치·인증·첫 대화까지 도달 가능.

### 4.1 필수 조건 (P0 — 미충족 시 배포 금지)

- [ ] **공식 학교 승인** — IT처/총학/관련 단과대 중 한 곳의 명시적 승인 문서.
- [ ] **AjouLLM Gateway endpoint 안정성 검증** — 100명 동시 사용 부하 테스트 통과.
- [ ] **개인정보처리방침** — 한국어, PIPA 준수, 학교 도메인에 호스팅된 페이지.
- [ ] **이용약관(ToS)** — 학생 abuse 시 제재 기준 포함.
- [ ] **API key 발급 자동화** — 포털 SSO 또는 최소한 학번 인증 기반 발급 페이지.
- [ ] **한국어 에러/도움말 100% 커버** — `locales/ko.po` 완성 및 default 설정.
- [ ] **upstream 브랜드 분리** — README/docs/installer에서 `nousresearch.com` 링크 제거 또는 "기반 기술"로 격하.

### 4.2 강력 권장 조건 (P1 — 정식 배포 전 충족)

- [ ] **GUI 설치 경로** — `.dmg` (macOS), `.exe` (Windows), 또는 웹 기반 설치 페이지.
- [ ] **첫 실행 튜토리얼** — `hermes` 첫 진입 시 3분 인터랙티브 가이드.
- [ ] **공식 문서 사이트** — `website/` Docusaurus를 `ajou-llm-agent.ajou.ac.kr` 류 도메인에 배포.
- [ ] **헬프데스크 채널** — 학내 카카오톡 오픈채팅 또는 Discord 서버 분리.
- [ ] **사용량 대시보드** — 학생별 토큰 소비량 확인 페이지 (남용 방지).
- [ ] **자동 업데이트** — `hermes update` 명령으로 안전하게 최신 버전 pull.
- [ ] **롤백 메커니즘** — 업데이트 실패 시 자동 직전 버전 복원.

### 4.3 차별화 조건 (P2 — 학교 전용 가치 제공)

- [ ] **LMS(블랙보드/Moodle) skill** — 강의 자료/과제 마감 자동 조회.
- [ ] **학사 정보 skill** — 시간표, 학점 조회, 학사 일정.
- [ ] **도서관 API skill** — 자료 검색, 대출 현황.
- [ ] **학내 식당 메뉴 skill** — 일상 사용성 강화.
- [ ] **학과별 지식 베이스** — 전공별 자주 묻는 질문, 선배 노하우 인덱스.
- [ ] **학생 간 skill 공유 마켓플레이스** — `hermes skill share/install <학번>/<skill>`.

---

## 5. 단계별 실행 로드맵 (Phased Roadmap)

### Phase 0 — 정리 및 정합성 확보 (1–2주)

**목표**: fork 흔적 제거, 신원(identity) 일관성 확보.

- README의 nousresearch.com 링크를 모두 검토 후 분리.
- upstream `RELEASE_v*.md` 파일 → `docs/upstream-history/`로 이동.
- `hermes` CLI 명령어 alias로 `ajou` 또는 `allm` 추가 검토.
- `.env.example`에서 본 프로젝트가 사용하지 않는 provider 키 자리표시자 제거.
- `LICENSE` 보존 + `NOTICE` 파일 추가 (Nous Research 원작 표기).

### Phase 1 — 학교 공식화 (2–4주, blocking)

**목표**: 정당성·법적 안전성 확보.

- IT처/총학에 프로젝트 제안서 제출 (본 문서 활용).
- AjouLLM 운영팀(Mindlogic 담당자)과 endpoint·rate-limit·계정 발급 방식 협의.
- 개인정보처리방침/이용약관 초안 작성 → 학교 법무 검토.
- 학교 로고 사용 승인 또는 비공식 색상만 사용으로 다운그레이드.

### Phase 2 — 사용성 재설계 (3–4주)

**목표**: 비전공 학생도 진입 가능한 UX.

- 한국어 locale 100% 완성 (특히 `hermes doctor`, 에러 메시지).
- 첫 실행 튜토리얼 skill 작성 (`skills/onboarding/`).
- `hermes setup` wizard에서 AjouLLM을 default 강조, 다른 provider는 "고급" 메뉴로 이동.
- 설치 스크립트에 한국어 진행 메시지 옵션 (`LANG=ko_KR.UTF-8` 자동 감지).
- 헬프데스크 링크를 doctor 출력 하단에 고정 노출.

### Phase 3 — 인증·배포 인프라 (4–6주)

**목표**: 학교 SSO 기반 제로-마찰 인증.

- 학교 포털 OAuth 또는 학번 인증 페이지 구축 (별도 web service).
- API key 자동 발급/회수 endpoint 학교 측 협업 구축.
- `hermes login` 명령 신설 — 브라우저 OAuth 플로우.
- 학생별 사용량 대시보드 web 페이지.
- 공식 문서 사이트 배포 (`website/` Docusaurus 활용).

### Phase 4 — 도메인 차별화 (지속)

**목표**: "아주대 학생만 누릴 수 있는 가치" 제공.

- 학사/LMS/도서관 skill 순차 구현.
- 학생 skill 공유 마켓플레이스 MVP.
- 정기적 upstream merge 자동화 (`scripts/upstream-sync.sh`).
- 학과별 ambassador 프로그램 — 분기마다 사용성 피드백 수집.

---

## 6. 측정 지표 (Success Metrics)

### 6.1 배포 직전 (Go/No-Go 판단)

- 사내 alpha 사용자 30명 — 7일 retention ≥ 60%.
- 설치 성공률 ≥ 95% (윈도우/macOS/리눅스 합산).
- 평균 첫 응답 도달 시간 ≤ 5분 (설치 시작 → 첫 채팅 응답).
- P0 체크리스트 100% 충족.

### 6.2 배포 후 (분기별 검토)

- 월간 활성 사용자(MAU) ≥ 학부생의 5%.
- 학생별 평균 일일 메시지 수 ≥ 10.
- 사용자가 직접 만든 skill 수 ≥ MAU의 20%.
- 학교 도메인 사용자 만족도(NPS) ≥ 30.
- AjouLLM Gateway 4xx/5xx 비율 ≤ 1%.

---

## 7. 위험 요인 요약 (Risk Register)

| ID | 위험 | 영향도 | 발생 확률 | 완화 전략 |
|---|---|---|---|---|
| R1 | 학교 미승인으로 "Exclusive" 표기 분쟁 | 치명 | 중 | Phase 1 선행 |
| R2 | Mindlogic Gateway 비용 초과로 서비스 중단 | 치명 | 중 | 학생별 토큰 cap 도입 |
| R3 | upstream divergence로 보안 패치 누락 | 높음 | 높음 | 분기별 자동 sync |
| R4 | 학생이 학교 키로 abuse | 높음 | 중 | 사용량 모니터링 + 자동 제재 |
| R5 | 비전공 학생 이탈로 PR 실패 | 중 | 높음 | Phase 2 UX 작업 우선 |
| R6 | 한국어 i18n 미완성으로 신뢰 하락 | 중 | 낮음 | locale 검증 CI 게이트 |
| R7 | 개인정보 유출 사고 | 치명 | 낮음 | 데이터 흐름도 + 외부 보안 감사 |

---

## 8. 결론 및 권고

본 프로젝트는 **기술적 토대(Hermes Agent)가 매우 견고**하지만, 현재 상태는
"리브랜딩된 fork" 단계에 머물러 있다. 일반 사용자(특히 비전공 학생)에게
배포하려면 다음 **세 가지 결정적 작업**이 선행되어야 한다:

1. **학교 공식화 (Phase 1)** — 정당성·법적 안전성·인프라 안정성을 동시에 확보.
2. **한국어 사용성 재설계 (Phase 2)** — CLI 도구의 본질적 진입장벽을 학생 친화적으로 재구성.
3. **upstream 분리 전략 정립** — 어느 부분을 따라가고 어느 부분을 발산시킬지 명문화.

이 세 축이 갖춰진 시점부터 본 프로젝트는 fork가 아닌 **AjouLLM 전용 1급 프로덕트**로
공식화될 자격을 가진다. 그 이전 단계에서의 "공식 배포"는 학생·학교·원작자 모두에게
부담을 전가하는 결과를 초래할 가능성이 높다.

> **다음 액션 아이템**:
> 1. 본 문서를 학교 IT처에 제안서 형태로 정리 → Phase 1 착수.
> 2. `docs/upstream-history/` 폴더 생성 후 `RELEASE_v*.md` 이동 (Phase 0 첫 작업).
> 3. `locales/ko.po` 진척도 측정 및 갭 분석.

---

*문서 관리: 본 로드맵은 분기 1회 업데이트한다. 변경 시 git history와
Phase 진척 체크박스를 함께 갱신한다.*
