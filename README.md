# 냉장고\_파먹기 Project

> **AI 기반 이미지 분석 & 레시피 추천 서비스**

**냉장고를 열어 사진 한 장 찍으면, 뭘 해먹을지 알려준다.**  
남은 재료를 활용한 스마트한 요리 제안을 통해 음식물 낭비를 줄이고,  
개인의 건강을 고려한 레시피 및 영양정보도 함께 제공하는 인공지능 서비스이다.

---

## Installation

This project is managed by `uv` and `fastapi` with standard dependencies.

You could run this project via this command below.

```bash
uv install # install dependencies
uv run fastapi dev
```

## 프로젝트 개요

-   **프로젝트명**: 냉장고 파먹기 (Eat Your Fridge)
-   **기획 배경**:  
    매일 뭘 먹을지 고민하는 요리알못인 20대들을 위해,  
    냉장고 속 재료를 인식하고 즉석에서 맞춤형 요리를 추천해주는 AI 앱을 개발

-   **주요 기능**
    -   냉장고 속 사진 업로드
    -   재료 인식 (이미지 분석)
    -   Gemini API 기반 요리 및 레시피 생성
    -   칼로리, 알러지 정보 등 영양정보 제공
    -   영수증?
    -   1차 사진 인식 못하면 -> 2차 사진 받기 전 user에게 컨펌 받기
    -
    -

## 기술 스택

| 분류     | 사용 기술                                            |
| -------- | ---------------------------------------------------- |
| Backend  | Python, FastAPI                                      |
| AI API   | Google Gemini Vision API (PaLM or Gemini Pro Vision) |
| Infra    | Docker, GCP Cloud Run, Cloud Build                   |
| Dev Tool | VS Code                                              |

## 개발자 소개

경민 (Kyungmin Kang)
인공지능전공 3학년 | 관심 분야: Vision, NLP, Reinforcement Learning, 실전형 AI 서비스, real-world AI
Email : digd6382@gmail.com
