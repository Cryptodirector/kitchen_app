from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from app.telegram.handlers import send_msg
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)


@app.get(
    "/",
    response_class=HTMLResponse
)
async def main(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="main_page.html"
    )


@app.get(
    '/form',
    response_class=HTMLResponse
)
async def handler_app(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='handler_app.html'
    )


@app.post(
    '/form',
    response_class=HTMLResponse
)
async def handler_app(
        name: str = Form(),
        phone: str = Form(),

):
    await send_msg(
        name,
        phone
    )
    return RedirectResponse(
        url='http://127.0.0.1:8000',
        status_code=302
    )