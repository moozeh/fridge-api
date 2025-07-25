import json
from pydantic import BaseModel
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig, Image

# 프로젝트 초기화
vertexai.init(project='dauntless-loop-465318-d1', location='us-central1')

# JSON 모드를 위한 설정 객체 생성
__json_generation_config = GenerationConfig(
    response_mime_type="application/json"
)

__model = GenerativeModel('gemini-2.5-pro')
# example ai response : ai_response = model.generate_content('Hello from local test!')

# 이미지를 함께 처리하도록 수정된 함수
def generate_from_model(prompt: str, image_bytes: bytes = None):
    
    if image_bytes is None:
        # 4. 텍스트 프롬프트와 이미지 객체를 리스트에 담아 모델에 전달합니다.
        # GenerativeModel의 generate_content는 다양한 유형의 입력을 리스트로 받습니다.
        response = __model.generate_content(
            prompt,
            generation_config=__json_generation_config
        )
        
        json_output = json.loads(response.text)
        return json_output
    
    
    input_image = Image.from_bytes(image_bytes)
    
    response = __model.generate_content(
        [prompt, input_image], # [텍스트, 이미지] 형태로 전달
        generation_config=__json_generation_config
    )
    
    json_output = json.loads(response.text)
    return json_output
