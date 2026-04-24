from httpx import AsyncClient
from my_api.main import app

async def test_process():
    async with AsyncClient(app=app, base_url="http://test") as client:
        r = await client.post("/process/42")
    assert r.status_code == 200