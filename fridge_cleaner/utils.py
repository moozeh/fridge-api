# JSON 파서
def _extract_json_from_response(response_text: str) -> dict:
    try:
        if response_text.startswith('```'):
            response_text = response_text.split('```json')[1].split('```')
        return json.loads(response_text.strip())
    except (json.JSONDecodeError, IndexError) as e:
        logging.error(f"Failed to parse JSON from response: {e}")
        raise HTTPException(status_code=500, detail="AI 응답에서 JSON 추출 실패")