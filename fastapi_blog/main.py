from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
        {
            "id": 1,
            "author": "Churchil Basil",
            "title": "Cows are White and Goats are Brown",
            "content": "Cows are big and goats are small",
            "date_posted": "Oct 11 2019"
            },
        {
            "id" : 2,
            "author": "Hope Xiwang",
            "title": "Enterpreneurship reloaded",
            "content": "up in the air",
            "date_posted": "Oct 12 2026"
            }
        ]

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title" : "Blog"})


if __name__ == "__main__":
    main()
