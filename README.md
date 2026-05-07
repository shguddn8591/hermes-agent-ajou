<p align="center">
  <img src="assets/banner.png" alt="AjouLLM Agent" width="100%">
</p>

# AjouLLM Agent ☤

<p align="center">
  <a href="https://github.com/shguddn8591/hermes-agent-ajou"><img src="https://img.shields.io/badge/Docs-GitHub%20Wiki-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://github.com/shguddn8591/hermes-agent-ajou/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://github.com/NousResearch/hermes-agent"><img src="https://img.shields.io/badge/Based%20on-Hermes%20Agent-blueviolet?style=for-the-badge" alt="Based on Hermes Agent by Nous Research"></a>
  <a href="https://www.ajou.ac.kr"><img src="https://img.shields.io/badge/For-Ajou%20University-002F87?style=for-the-badge" alt="Ajou University"></a>
</p>

---

## 🇰🇷 한국어 소개 (Korean)

**AjouLLM Agent는 아주대학교 학생들을 위해 원본 Hermes Agent를 기반으로 완전히 새롭게 재구축된 독립형 AI 에이전트입니다.**  
기존의 Hermes Agent와는 별개의 경로(`~/.hermes/ajou-hermes`)에 설치되어 충돌 없이 독립적으로 작동하며, 아주대학교 전용 **AjouLLM API Gateway** 및 **Ajou Blue & Gold** 프리미엄 테마를 통해 학생들에게 최적화된 경험을 제공합니다. 단순히 대화하는 AI를 넘어, 사용자의 학업 경험으로부터 스스로 학습하고 성장하는 여러분만의 학업 동반자입니다.

### ✨ 주요 특징
*   **독립적 설치 환경:** 원본 Hermes와 충돌하지 않는 전용 경로(`~/.hermes/ajou-hermes`)에 설치됩니다.
*   **자가 학습 루프 (Closed Learning Loop):** 복잡한 작업을 수행한 후 스스로 스킬을 생성하고, 사용 과정에서 이를 지속적으로 개선합니다.
*   **아주대학교 전용 브랜딩:** 아주대학교의 상징색인 **Ajou Blue & Gold** 테마가 적용된 전용 스킨(`/skin ajou`)을 지원합니다.
*   **AjouLLM Gateway 연동:** 별도의 복잡한 설정 없이 `hermes setup`을 통해 아주대 전용 API를 즉시 연결할 수 있습니다.
*   **어디서나 접속 가능:** 터미널 UI(TUI)는 물론 Telegram, Discord, Slack, WhatsApp 등 다양한 플랫폼에서 하나의 에이전트와 대화하세요.
*   **강력한 자동화:** 자연어로 크론(Cron) 작업을 예약하여 매일 아침 뉴스 브리핑을 받거나, 정기적인 백업 및 감사 작업을 수행할 수 있습니다.

---

## 🇺🇸 English Introduction

**AjouLLM Agent is a completely rebuilt, standalone AI agent based on the original Hermes Agent, specifically designed for Ajou University.**  
It installs in a separate directory (`~/.hermes/ajou-hermes`) to ensure zero conflict with existing Hermes installations. Optimized with the exclusive **AjouLLM API Gateway** and premium **Ajou Blue & Gold** themes, it serves as a self-improving academic companion that learns from your research and coursework experience.

### ✨ Key Features
*   **Standalone Environment:** Installs in a dedicated path (`~/.hermes/ajou-hermes`) to avoid conflicts with original Hermes.
*   **Closed Learning Loop:** Automatically creates skills from complex tasks and improves them over time based on usage.
*   **Ajou University Exclusive Branding:** Supports the premium `ajou` skin (`/skin ajou`) featuring the university's signature **Ajou Blue & Gold** colors.
*   **AjouLLM Gateway Integration:** Connect instantly to the Ajou-exclusive API via `hermes setup` with zero friction.
*   **Multi-Platform Presence:** Interact with the same agent through a rich Terminal UI (TUI) or via Telegram, Discord, Slack, and more.
*   **Scheduled Automations:** Use natural language to schedule cron jobs for daily reports, nightly backups, or automated research tasks.

---

## 🚀 Quick Start (빠른 시작)

### 1. Installation (설치)
Linux, macOS, WSL2 환경에서 아래 명령어를 실행하세요. (Android Termux 지원)

```bash
curl -fsSL https://raw.githubusercontent.com/shguddn8591/hermes-agent-ajou/main/scripts/install.sh | bash
```

또는 수동으로 설치하려면:
```bash
git clone https://github.com/shguddn8591/hermes-agent-ajou.git
cd hermes-agent-ajou
./setup-hermes.sh
```

### 2. Setup (설정)
설치 완료 후, 아주대학교 전용 설정을 위해 다음 명령어를 입력하세요.

```bash
hermes setup
```
> **Tip:** 마법사에서 `Inference Provider`로 **AjouLLM**을 선택하고 발급받은 API Key를 입력하세요.

### 3. Start Chatting (대화 시작)
```bash
hermes              # 터미널에서 대화 시작
/skin ajou          # 아주대학교 전용 스킨 적용
```

---

## 🛠️ Commands (주요 명령어)

| Command | Description (KR) | Description (EN) |
|:---|:---|:---|
| `hermes` | 에이전트와 대화 시작 | Start an interactive session |
| `hermes model` | 사용할 모델 변경 (AjouLLM 전용) | Switch LLM provider/model |
| `hermes tools` | 활성화할 도구 설정 | Configure enabled tools |
| `hermes skin` | 테마 변경 (`/skin ajou` 추천) | Change CLI theme/skin |
| `hermes gateway` | 메시징 게이트웨이 시작 (Telegram 등) | Start messaging gateway |
| `hermes doctor` | 시스템 진단 및 오류 해결 | Diagnose and fix issues |

---

## 📖 Documentation (문서)

> AjouLLM Agent 전용 한국어 문서는 현재 준비 중입니다.
> 기반 기술(Hermes Agent)의 영어 원문 문서를 참고하시되, AjouLLM 전용 설정은 본 README를 우선하세요.

*   **[CLI 명령어 안내 (영어)](https://hermes-agent.nousresearch.com/docs/user-guide/cli):** CLI 명령어 및 단축키 (Upstream Hermes 문서)
*   **[메시징 게이트웨이 (영어)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging):** 텔레그램, 디스코드 연동 방법 (Upstream 문서)
*   **[스킬 시스템 (영어)](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills):** 에이전트의 스킬 생성 및 관리 (Upstream 문서)
*   **[AjouLLM 전용 가이드](https://github.com/shguddn8591/hermes-agent-ajou/wiki):** 아주대학교 전용 기능 안내 (준비 중)

---

## 🤝 Community & Support

*   💬 **Issues / 버그 신고:** [GitHub Issues](https://github.com/shguddn8591/hermes-agent-ajou/issues)
*   🏢 **개발:** 아주대학교 학생 커뮤니티
*   ⚖️ **License:** MIT License

---

## 🙏 Credits

*   **기반 기술:** [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com) (MIT License)
*   **LLM 인프라:** [AjouLLM Gateway](https://ajoullm.ajou.ac.kr/) by Mindlogic

---

<p align="center">
  <i>"Your self-improving academic companion at Ajou University."</i>
</p>
