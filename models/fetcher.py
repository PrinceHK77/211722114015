import httpx
from typing import List

URL_MAP = {
    "p": "http://20.244.56.144/evaluation-service/primes",
    "f": "http://20.244.56.144/evaluation-service/fibo",
    "e": "http://20.244.56.144/evaluation-service/even",
    "r": "http://20.244.56.144/evaluation-service/rand",
}

async def fetch_numbers(number_type: str) -> List[int]:
    url_map = {
        "p": "http://20.244.56.144/evaluation-service/primes",
        "f": "http://20.244.56.144/evaluation-service/fibo",
        "e": "http://20.244.56.144/evaluation-service/even",
        "r": "http://20.244.56.144/evaluation-service/rand"
    }
    
    url = url_map.get(number_type)
    if not url:
        raise ValueError(f"Invalid number type: {number_type}")
    
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQ5NzkwOTcyLCJpYXQiOjE3NDk3OTA2NzIsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjBjZjk2N2QwLTBmNjYtNGYzYy05OTcwLTdlMWNiOTE2MjkxZiIsInN1YiI6ImhyaXRoaWNra3VtYXIubC4yMDIyLm1lY2hAcml0Y2hlbm5haS5lZHUuaW4ifSwiZW1haWwiOiJocml0aGlja2t1bWFyLmwuMjAyMi5tZWNoQHJpdGNoZW5uYWkuZWR1LmluIiwibmFtZSI6ImhyaXRoaWNrIGt1bWFyIGwiLCJyb2xsTm8iOiIyMTE3MjIxMTQwMTUiLCJhY2Nlc3NDb2RlIjoicFRUcXhtIiwiY2xpZW50SUQiOiIwY2Y5NjdkMC0wZjY2LTRmM2MtOTk3MC03ZTFjYjkxNjI5MWYiLCJjbGllbnRTZWNyZXQiOiJwRnFoQkpIVGV6aHRxckRyIn0.JoAz_QoDjubpm-S3aNsczzGlbJl0vgH6KRpzinwo2Ow"
    }
    
    try: 
        async with httpx.AsyncClient(time=0.5) as client:
            response = await client.get(url, headers=headers)
            data = response.json()
            return data.get("numbers", [])
    except httpx.RequestError as e:
        print(f"Request error: {e}")
        return []
    except httpx.HTTPStatusError as e:
        print(f"HTTP status error: {e}")
        return []
    
        