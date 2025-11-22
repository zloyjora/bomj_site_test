from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
templates = Jinja2Templates(directory=templates_dir)
app.mount('/static', StaticFiles(directory='static'), name='static')



vacancies = [
    {'id': 2, 'title': 'Python разработчик', 'company': 'ООО ТехноСофт', 'location': 'Москва', 'salary': '150000 руб.'},
    {'id': 3, 'title': 'Менеджер по продажам', 'company': 'ИП Сидоров', 'location': 'Санкт-Петербург', 'salary': '80000 руб. + бонусы'},
    {'id': 4, 'title': 'Дизайнер UX/UI', 'company': 'CreativeStudio', 'location': 'удаленно', 'salary': '120000 руб.'},
    {'id': 5, 'title': 'Аналитик данных', 'company': 'DataPro Analytics', 'location': 'Новосибирск', 'salary': '140000 руб.'},
    {'id': 6, 'title': 'Маркетолог', 'company': 'AdvertGroup', 'location': 'Казань', 'salary': '90000 руб.'}
]



@app.get('/vacancies', response_class=HTMLResponse)
async def get_vacancies(request: Request):
    context = {
        'request': request,
        'page_title': 'Рабочие услуги',
        'vacancies': vacancies
    }
    return templates.TemplateResponse('index.html', context)