from fastapi import FastAPI, Request, HTTPException, status
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

@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title" : "Blog"})

@app.get("/api/posts/{post_id}")
def get_posts(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.get("/api/post/{post_id}", include_in_schema=False, name="post_page")
def post_page(request: Request, post_id: int):
    for post in posts:
        title = post.get("title")[:20]
        if post.get("id") == post_id:
            return templates.TemplateResponse(request, "post.html", {"post": post, "title": title})
    raise HTTPException(status_code = status.HTTP_404_FOUND, detail="Post not found")



if __name__ == "__main__":
    home()

