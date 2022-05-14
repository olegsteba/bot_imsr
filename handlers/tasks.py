import aiohttp
from config import API


async def all_task():
    link = API + '/main/get_tasks'
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as res:
            res_data = await res.json()
            return res_data["data"]

async def text_task(task_id):
    link = API + '/main/get_tasks'
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as res:
            res_data = await res.json()
            for task in res_data["data"]:
                if task["id"] == int(task_id):
                    return task