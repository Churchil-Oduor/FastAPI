from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") # gets the folder that Jinja2 will use in acquiring the templates

posts = [

{"title": "FastApi server",
"author": "Churchil",
 "statement": "Experimenting with fastapi has been so amazing especially when doing machine learning",
"age":  23},

{
    "title": "Python FastApi",
    "author": "Nick Numz",
    "statement": "I agree with you Churchil",
    "age": 34
    }

]




@app.get('/', include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Homey"})


@app.get('/api', include_in_schema=False)
def get_posts():
    return {"response": posts}


if __name__ == "__main__":
    home()
