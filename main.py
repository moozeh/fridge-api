import os
import logging
from typing import List
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from fridge_cleaner import prompt
from fridge_cleaner import vertex_ai
from fridge_cleaner.dtos import IngredientItem

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/api/fridges/analyze")
async def analyze_fridge(image: UploadFile = File(...)):
    response = vertex_ai.generate_from_model(prompt.IMAGE_RECOGNITION_PROMPT)
    return response

@app.post("/api/recipes")
async def create_recipes(data: List[IngredientItem]):
    # 받은 데이터 처리 예시
    items_list = []
    for item in data:
        items_list.append(item.name)
        
    response = vertex_ai.generate_from_model(", ".join(items_list) + prompt.RECIPE_PROMPT)
    
    return response

static_files_path = os.path.join(os.path.dirname(__file__), "frontend", "build", "static")
app.mount(
    "/static",
    StaticFiles(directory=static_files_path),
    name="static"
)

# 2. 모든 경로에 대해 React의 index.html을 반환하는 Catch-all 라우트
#    이 라우트는 항상 모든 API 라우트와 StaticFiles 마운트 다음에 위치해야 합니다.
@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    index_path = os.path.join(os.path.dirname(__file__), "frontend", "build", "index.html")
    if not os.path.exists(index_path):
        raise HTTPException(status_code=404, detail="React app not found. Did you run 'npm run build'?")
    return FileResponse(index_path)