
# AjouLLM Agent ☤

<p align="center">
  <a href="https://hermes-agent.nousresearch.com/docs/"><img src="https://img.shields.io/badge/Docs-hermes--agent.nousresearch.com-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://github.com/NousResearch/hermes-agent/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://nousresearch.com"><img src="https://img.shields.io/badge/Built%20by-Nous%20Research-blueviolet?style=for-the-badge" alt="Built by Nous Research"></a>
  <a href="https://www.ajou.ac.kr"><img src="https://img.shields.io/badge/Exclusive-Ajou%20University-002F87?style=for-the-badge" alt="Ajou University"></a>
</p>

---

## 🇰🇷 한국어 소개 (Korean)

**AjouLLM Agent는 아주대학교 학생들을 위해 최적화된 차세대 자가 학습형 AI 에이전트입니다.**  
Nous Research의 강력한 Hermes Agent를 기반으로 하며, 아주대학교 전용 **AjouLLM API Gateway**를 통해 최신 LLM(Claude, Gemini 등)을 무료로 또는 효율적으로 사용할 수 있습니다. 단순히 대화하는 AI를 넘어, 사용자의 경험으로부터 스스로 스킬을 배우고 개선하며, 터미널(CLI)과 메시징 앱(Telegram, Discord 등)을 오가며 여러분의 학업과 연구를 돕습니다.

### ✨ 주요 특징
*   **자가 학습 루프 (Closed Learning Loop):** 복잡한 작업을 수행한 후 스스로 스킬을 생성하고, 사용 과정에서 이를 지속적으로 개선합니다.
*   **아주대학교 전용 브랜딩:** 아주대학교의 상징색인 **Ajou Blue & Gold** 테마가 적용된 전용 스킨(`/skin ajou`)을 지원합니다.
*   **AjouLLM Gateway 연동:** 별도의 복잡한 설정 없이 `hermes setup`을 통해 아주대 전용 API를 즉시 연결할 수 있습니다.
*   **어디서나 접속 가능:** 터미널 UI(TUI)는 물론 Telegram, Discord, Slack, WhatsApp 등 다양한 플랫폼에서 하나의 에이전트와 대화하세요.
*   **강력한 자동화:** 자연어로 크론(Cron) 작업을 예약하여 매일 아침 뉴스 브리핑을 받거나, 정기적인 백업 및 감사 작업을 수행할 수 있습니다.

---

## 🇺🇸 English Introduction

**AjouLLM Agent is a next-generation, self-improving AI agent optimized for Ajou University students.**  
Built upon the robust Hermes Agent by Nous Research, it provides exclusive access to the **AjouLLM API Gateway**, enabling seamless use of state-of-the-art LLMs (Claude, Gemini, etc.). It’s more than just a chatbot; it learns from experience, builds its own skills, and assists your academic and research endeavors across Terminal (CLI) and messaging platforms (Telegram, Discord, etc.).

### ✨ Key Features
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
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
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

자세한 사용법은 공식 문서 사이트를 참고하세요: **[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/docs/)**

*   **[User Guide](https://hermes-agent.nousresearch.com/docs/user-guide/cli):** CLI 명령어 및 단축키 안내
*   **[Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging):** 텔레그램, 디스코드 연동 방법
*   **[Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills):** 에이전트의 스킬 생성 및 관리
*   **[AjouLLM Guide](https://hermes-agent.nousresearch.com/docs/partners/ajou):** 아주대학교 전용 기능 안내 (준비 중)

---

## 🤝 Community & Support

*   💬 **Discord:** [Nous Research Discord](https://discord.gg/NousResearch)
*   🏢 **Built by:** [Nous Research](https://nousresearch.com) & Ajou University Students
*   ⚖️ **License:** MIT License

---

<p align="center">
  <i>"Your self-improving academic companion at Ajou University."</i>
</p>
