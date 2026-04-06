from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from db.crud import get_json, get_all_operator_ids
from db.session import SessionLocal
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# app.add_middleware(
#     CORS
# )

@app.get("/operator/{operator_id}")
async def  operator_chat(operator_id: int):
    async with SessionLocal() as session:
        data = await get_json(session, operator_id)
        return data
    # return [
    #     {
    #         "operator_id": 123,
    #         "sender": 456,
    #         "who_sender": "user",
    #         "text": "hi I need help",
    #         "time": "16:25"
    #     },
    #     {
    #         "operator_id": 123,
    #         "sender": 456,
    #         "who_sender": "operator",
    #         "text": "hi, wots happened?",
    #         "time": "16:25"
    #     }
    # ]


@app.get("/IDs")
async def get_all_operator_id():
    async with SessionLocal() as session:
        operator_ids = await get_all_operator_ids(session)
        return operator_ids


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, operatorId: int = 1228798145):
    return templates.TemplateResponse(request, "index.html", {
        "operatorId": operatorId
    })

app.mount("/home", StaticFiles(directory="static", html=True), name="static")


# @app.get("/")
# async def main_site():
#     return 200