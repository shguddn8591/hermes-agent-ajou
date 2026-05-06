# 📋 아주LLM 학생용 Agent 변환 계획 (G-Plan)

아주대학교 학생들이 아주LLM API Gateway를 통해 Hermes Agent를 원활하고 강력하게 사용할 수 있도록 코드베이스를 변환하고, 아주대학교 전용 브랜딩과 스킨을 적용합니다.

---

## 🎯 목표
1. **아주LLM API Gateway 연동**: `https://factchat-cloud.mindlogic.ai/v1/gateway`를 기본 Base URL로 설정하고, OpenAI 호환 API 방식을 통한 아주LLM 모델들(`claude-sonnet-4-6`, `gemini-3-flash-preview` 등)을 지원합니다.
2. **아주대학교 전용 브랜딩 및 스킨 구현**: 아주대학교의 상징색인 **Ajou Blue (코발트 블루 #002F87)** 와 **Ajou Gold (#D4AF37)** 를 메인 테마로 하는 프리미엄 터치 `ajou` 스킨을 탑재하여 시각적으로 WOW 요소를 제공합니다.
3. **설정 마법사 및 설정 파일 연동**: `.env` 및 `config.yaml`에 아주LLM 전용 API 키(`AJOULLM_API_KEY`) 및 기본 프로바이더 설정을 빌트인으로 탑재하여, 학생들이 `hermes setup`만으로도 즉시 아주LLM을 사용할 수 있도록 구성합니다.

---

## 🛠️ 세부 태스크

### Phase 1: 설정 및 인증 통합 (Configuration & Authentication)
- [x] `hermes_cli/config.py`의 `_EXTRA_ENV_KEYS`에 아주LLM 전용 API 키 `AJOULLM_API_KEY` 추가
- [x] `hermes_cli/config.py`의 `OPTIONAL_ENV_VARS`에 `AJOULLM_API_KEY` 입력 메타데이터 및 설명 추가
- [x] `DEFAULT_CONFIG`에 아주LLM 기본 모델 및 프로바이더 설정 구조 추가
  - 프로바이더 이름: `ajoullm`
  - Base URL: `https://factchat-cloud.mindlogic.ai/v1/gateway`
  - 기본 모델 ID: `claude-sonnet-4-6` (또는 `gemini-3-flash-preview` 등)
### Phase 2: 에이전트 연동 및 에러 안내 수정 (Agent & CLI UI Integration)
- [x] `run_agent.py` 및 `model_tools.py`에서 아주LLM 프로바이더 연동 확인 및 `AJOULLM_API_KEY` 환경 변수 우선순위 지정
- [x] 아주LLM API 호출 에러 발생 시 아주LLM 연동 가이드 문서를 참고할 수 있도록 에러 핸들러 개선
- [x] `cli.py`에서 세션 시작 시 아주LLM 로고 및 아주대학교 학생을 위한 환영 메시지 출력

### Phase 3: 아주대학교 프리미엄 `ajou` 스킨 구현 (Premium Design Aesthetics)
- [x] `hermes_cli/skin_engine.py`에 `ajou` 스킨 정의 추가
  - **Ajou Blue (#0041AD)**, **Ajou Gold (#E6B800)**, **Sky Blue (#81D4FA)** 색상 조화
  - 아주대학교 마스코트나 학업/연구 관련 스피너 얼굴 및 동사 세트 적용
  - 에이전트 이름: `"Ajou LLM Agent"`

### Phase 4: 아주LLM 전용 셋업 마법사 지원 (Setup Wizard Customization)
- [x] `hermes_cli/setup.py`에 아주LLM 전용 셋업 플로우 추가
  - 마법사에서 아주LLM API 키 입력을 유도하고, 학생들이 간편하게 입력하도록 유도

### Phase 5: 최종 검증 및 배포 준비 (Verification & Handover)
- [x] 아주LLM API Gateway 연동 테스트 (Mock 또는 실제 호출)
- [x] `ajou` 스킨 로드 및 UI 표시 확인
- [x] `tasks/lessons.md`에 이번 변환 과정의 교훈 기록
- [x] Obsidian `Memory.md` 및 `Action Tracker.md` 최신화

---

## 💡 우아한 설계 제안
- **Ajou Blue 프리미엄 스킨**: CLI에서 아주대학교 학생 전용 테마를 적용할 수 있도록 `/skin ajou` 명령어를 지원하고, 기본 스킨으로 활성화할 수도 있습니다.
- **자동 AI Slop Cleaner**: 에이전트 코드 및 주석에 있는 불필요한 Slop들을 정리하여 프로덕션 품질을 유지합니다.
