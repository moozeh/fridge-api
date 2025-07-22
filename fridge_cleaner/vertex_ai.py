import json
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig

# 프로젝트 초기화
vertexai.init(project='dauntless-loop-465318-d1', location='us-central1')

# JSON 모드를 위한 설정 객체 생성
__json_generation_config = GenerationConfig(
    response_mime_type="application/json"
)

__model = GenerativeModel('gemini-2.5-pro')
# example ai response : ai_response = model.generate_content('Hello from local test!')

def generate_from_model(prompt: str):
    response = __model.generate_content(
        prompt,
        generation_config=__json_generation_config
    )
    
    json_output = json.loads(response.text)
    return json_output