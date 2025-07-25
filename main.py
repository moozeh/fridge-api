import os
import logging
from typing import List
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from fridge_api import prompt
from fridge_api import vertex_ai
from fridge_api.dtos import RecipeRequest

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.post("/api/fridges/analyze")
async def analyze_fridge(image: UploadFile = File(...)):
    image_bytes = await image.read()
    response = vertex_ai.generate_from_model(prompt.IMAGE_RECOGNITION_PROMPT, image_bytes=image_bytes)
    return response

@app.post("/api/recipes")
async def create_recipes(data: RecipeRequest):
    # 받은 데이터 처리 예시
    # 실제 레시피 생성 로직
    ingredients = []
    for ingredient in data.ingredients:
        ingredients.append(ingredient)
        
    response = vertex_ai.generate_from_model(", ".join(ingredients) + prompt.RECIPE_PROMPT)
    
    return response
# --- 정적 파일 경로 설정 및 검증 (중요!) ---
# React 빌드 파일이 있는 루트 디렉토리
# 사용자의 프로젝트 구조에 따라 'spa'가 포함될 수도, 안될 수도 있습니다.
# 이 경로가 가장 중요합니다.
build_dir = os.path.join(os.path.dirname(__file__), "frontend", "dist", "spa")
assets_dir = os.path.join(build_dir, "assets")

# 서버 시작 시 경로가 올바른지 확인하는 디버깅 코드
print(f"React build directory: {os.path.abspath(build_dir)}")
print(f"Assets directory: {os.path.abspath(assets_dir)}")

if not os.path.isdir(build_dir):
    raise RuntimeError(f"Build directory not found at: {build_dir}")
if not os.path.isdir(assets_dir):
    raise RuntimeError(f"Assets directory not found at: {assets_dir}. Did you run 'npm run build'?")


# --- 정적 파일 마운트 (API 라우트 다음) ---
# index.html이 요청하는 '/assets' 경로를 명시적으로 마운트합니다.

app.mount("/", StaticFiles(directory=build_dir, html=True), name="static")