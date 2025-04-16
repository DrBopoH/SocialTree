from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app: FastAPI = FastAPI()
app.mount('/static', StaticFiles(directory='main/static/'), name='static')

templates: Jinja2Templates = Jinja2Templates(directory='main/templates/')

@app.get("/", response_class=HTMLResponse)
async def tong(request: Request):
	return templates.TemplateResponse('index.html', {"request": request, 'title': "Hello world! Its FastAPI!"})