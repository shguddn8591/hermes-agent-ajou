# Phase 1 공식화 계획서 — AjouLLM Agent

> **Phase 1 목표**: 학교 공식 승인 + 법적 안전성 + 인프라 안정성을 동시에 확보하여
> "비공식 fork"에서 **"아주대 공인 AI Agent"**로 전환한다.
>
> **기준일**: 2026-05-07  
> **예상 기간**: 2–4주 (학교 기관 협의 속도에 종속)  
> **Phase 0 전제**: 완료 ✅ (commit `a4cae4fa`)

---

## 1. 이해관계자 지도 (Stakeholder Map)

| 이해관계자 | 역할 | 필요한 것 | 우리가 줄 수 있는 것 |
|---|---|---|---|
| **IT처 / 정보통신처** | 학교 인프라·보안 정책 관할 | 보안 검토서, 데이터 흐름도 | PIPA 준수 설계, 소스 공개(MIT) |
| **AjouLLM 운영팀 (Mindlogic)** | Gateway 운영, API 제공자 | 사용량 예측, 남용 방지 정책 | Rate-limit 설계, 모니터링 연동 |
| **학생처 / 총학생회** | 학생 서비스 채널 | 민원 대응 채널, 이용 가이드 | FAQ, 헬프데스크 SLA |
| **법무팀 / 개인정보보호담당** | PIPA·저작권 검토 | 개인정보처리방침, 이용약관 초안 | 법무 검토용 초안 문서 |
| **학부생 Alpha 사용자** | 실사용 검증 | 쉬운 설치, 한국어 UI, 학업 연관 기능 | 설치 스크립트, ko locale, 튜토리얼 |

---

## 2. 승인 트랙 (Approval Track)

### 2-1. 제안서 제출 (1주차)

**제출 대상**: IT처 or 산학협력단 (담당 창구 확인 필요)

**제안서 구성 요소**:

```
1. 프로젝트 개요 (2페이지)
   - 목적: 아주대 학생의 AjouLLM 접근성 향상
   - 기반 기술: Hermes Agent (MIT, Nous Research)
   - 현재 상태: fork 완료, AjouLLM provider 통합 완료
   - GitHub: https://github.com/shguddn8591/hermes-agent-ajou

2. 기술 아키텍처 (1페이지)
   - 데이터 흐름: 학생 단말 → AjouLLM Gateway → Mindlogic 서버
   - 로컬 저장 데이터: ~/.ajou-hermes (설정·스킬·로그)
   - 외부 전송 데이터: 사용자 프롬프트·응답 (Gateway 경유, 암호화)

3. 보안·개인정보 (1페이지)
   - MIT 오픈소스, 소스 전체 공개
   - PIPA 준수 설계 계획
   - API key 관리 방침

4. 운영 계획 (1페이지)
   - 학생 지원 채널
   - 업데이트 주기
   - 서비스 종료 시 데이터 삭제 절차

5. 요청 사항 (명확히)
   - 학교 로고·명칭 사용 승인 (또는 대안: "아주대학교 학생 개발" 문구)
   - AjouLLM Gateway rate-limit 정책 협의 채널
   - 공식 배포 채널(학교 공지 시스템) 접근
```

**제안서 파일**: `docs/proposal/AJOU_PROPOSAL_v1.md` ← Phase 1 중 작성

### 2-2. 학교 로고·명칭 사용 승인 (병렬 진행)

**두 가지 경로 중 선택**:

| 경로 A (권장) | 경로 B (대안) |
|---|---|
| 홍보팀/시각디자인처에 공문 제출 | "Ajou Blue & Gold" 색상만 사용, 공식 로고 제거 |
| 승인 시: 배지·스킨에 공식 UI 사용 가능 | 승인 없이도 배포 가능 (단, "아주대 공인" 문구 불가) |
| 예상 소요: 2–3주 | 즉시 적용 가능 |

> **권고**: 배포 초기에는 경로 B로 선행 배포하고, 승인 후 공식 브랜딩으로 업그레이드.

---

## 3. AjouLLM Gateway 협의 (Mindlogic)

### 3-1. 협의 필요 항목

| 항목 | 현재 상태 | 필요한 결정 |
|---|---|---|
| Endpoint 안정성 | `factchat-cloud.mindlogic.ai/v1/gateway` (검증 미완) | SLA 보장 여부, 점검 시간 정책 |
| Model catalog | fallback models 3개 하드코딩 | `/models` endpoint 지원 여부, 자동 갱신 방식 |
| Rate limit | 정책 불명 | 학생별 일일 토큰 cap, 초과 시 응답 형식 |
| 인증 방식 | raw API key | 학번 기반 발급 API 지원 여부 |
| 비용 | 학생 부담 여부 불명 | 무료/저비용 정책, 학교 계약 여부 |
| 데이터 보존 | 불명 | 프롬프트·응답 로그 보존 기간, 삭제 요청 처리 |

### 3-2. 기술 검증 작업

```bash
# Gateway endpoint 연결 확인
curl -s https://factchat-cloud.mindlogic.ai/v1/gateway/models \
  -H "Authorization: Bearer $AJOULLM_API_KEY"

# 모델 목록 응답 형식 확인 → plugin.yaml fallback_models 갱신 근거
```

**검증 결과에 따른 후속 작업**:
- `/models` 지원 → `plugins/model-providers/ajoullm/__init__.py`에 `fetch_models()` 오버라이드 추가
- 미지원 → fallback_models 목록을 Mindlogic과 협의해 최신화

---

## 4. 법적 문서 작성 (개인정보·이용약관)

### 4-1. 개인정보처리방침 (PIPA 준수)

**필수 포함 항목** (개인정보보호법 제30조):

```markdown
1. 개인정보의 처리 목적
   - AI 에이전트 서비스 제공
   - 학업 보조 기능(스킬 자동 생성·개선)

2. 처리하는 개인정보의 항목
   - 필수: 학번(인증 시), AjouLLM API key
   - 자동 수집: 프롬프트 텍스트, 응답 텍스트, 사용 시각
   - 로컬 저장: ~/.ajou-hermes/ (단말기 내, 외부 미전송)

3. 개인정보의 처리 및 보유 기간
   - API key: 사용자가 삭제할 때까지
   - Gateway 전송 데이터: Mindlogic 정책에 따름 (협의 결과 반영)

4. 개인정보의 제3자 제공
   - Mindlogic (AjouLLM Gateway 운영사): 프롬프트·응답 처리 목적

5. 개인정보처리방침의 변경
   - 변경 시 GitHub 및 설치 경로의 NOTICE 파일에 고지

6. 정보주체의 권리·의무 및 행사방법
   - 데이터 삭제: rm -rf ~/.ajou-hermes 또는 GitHub Issues 접수
```

**파일 위치**: `docs/PRIVACY_POLICY.md` → 향후 웹사이트 호스팅

### 4-2. 이용약관 (ToS)

**핵심 조항**:

```markdown
1. 서비스 대상: 유효한 AjouLLM API key를 보유한 아주대학교 구성원

2. 금지 행위
   - API key 타인 공유·대여
   - 자동화를 이용한 대량 요청(abuse)
   - 학문적 부정행위 목적 사용 (표절, 대리 과제 등)

3. 면책
   - AI 응답의 정확성 미보증
   - Gateway 장애로 인한 서비스 중단

4. 제재
   - API key 비활성화 (Mindlogic 협의)
   - GitHub 계정 차단
```

**파일 위치**: `docs/TERMS_OF_SERVICE.md`

---

## 5. Phase 1 실행 체크리스트

### Week 1 (제안 준비)
- [ ] `docs/proposal/AJOU_PROPOSAL_v1.md` 초안 작성
- [ ] 데이터 흐름도 다이어그램 (`docs/proposal/data-flow.png`)
- [ ] AjouLLM Gateway endpoint 연결 테스트 (`curl` 검증)
- [ ] Mindlogic 담당자 연락처 확보 (학교 IT처 경유 또는 직접)

### Week 2 (제출 및 협의 착수)
- [ ] IT처에 제안서 제출 (이메일 or 공문)
- [ ] Mindlogic과 첫 기술 미팅 요청
- [ ] `docs/PRIVACY_POLICY.md` 초안 작성
- [ ] `docs/TERMS_OF_SERVICE.md` 초안 작성
- [ ] Alpha 사용자 10명 모집 (CS 전공 지인 위주)

### Week 3 (기술 검증 + 법무)
- [ ] Gateway `/models` endpoint 지원 여부 확인 → 코드 반영
- [ ] Rate-limit 정책 확정 → `plugins/model-providers/ajoullm/__init__.py` 업데이트
- [ ] 법무팀(또는 법과대학 교수 자문) 개인정보처리방침 검토
- [ ] 학교 로고 사용 승인 요청 or 경로 B 결정

### Week 4 (완료 조건 확인)
- [ ] 학교 IT처 승인 문서(이메일·공문) 수령
- [ ] Mindlogic Gateway SLA 문서 수령
- [ ] 개인정보처리방침 최종본 확정
- [ ] Alpha 사용자 10명 → 7일 retention 측정 (≥60% 목표)
- [ ] Phase 2 착수 결정 회의

---

## 6. 블로킹 이슈 및 대응

| 블로킹 이슈 | 가능성 | 대응책 |
|---|---|---|
| IT처가 승인 거부 | 낮음 | 경로 B(비공식 배포)로 전환, 오픈소스 커뮤니티 배포 |
| Mindlogic이 학생 대상 API 미지원 | 중간 | OpenRouter/Anthropic 등 대안 provider fallback 강화 |
| 법무 검토 지연 | 높음 | 경로 B로 선행 배포 후 법무 완료 시 정식 전환 |
| Gateway 불안정(5xx 빈발) | 중간 | doctor 명령에 Gateway 헬스체크 추가, retry 로직 보강 |

---

## 7. Phase 1 완료 기준 (Definition of Done)

아래 중 **최소 4개** 충족 시 Phase 2 착수 승인:

1. [ ] 학교 IT처 또는 관련 기관의 서면(이메일 포함) 승인
2. [ ] AjouLLM Gateway SLA 또는 운영 정책 문서 수령
3. [ ] 개인정보처리방침 한국어 최종본 공개
4. [ ] Alpha 10명 / 7일 retention ≥ 60%
5. [ ] Gateway `/models` 연동 검증 완료 (또는 fallback 목록 최신화)

> 5개 모두 충족 시 → Phase 2(사용성 재설계) 즉시 착수  
> 4개 충족 + 학교 승인 미완 → 경로 B로 제한 배포하며 Phase 2 병행

---

*다음 문서: `docs/PHASE2_UX_REDESIGN.md` (Phase 1 완료 후 작성)*
