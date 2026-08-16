from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from schemas import PostCreate, PostResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") # gets the folder that Jinja2 will use in acquiring the templates

posts = [

{
    "id" : 1,
    "title": "FastApi server",
    "author": "Churchil",
    "content": "Experimenting with fastapi",
    "date_posted":  "23 July 2023"},

{
    "id": 2,
    "title": "Python FastApi",
    "author": "Nick Numz",
    "content": "I agree with you Churchil",
    "date_posted": " 23 June 2000"}
]


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Homey"})


@app.get('/api/posts', response_model=list[PostResponse])
def get_posts():
    return {"response": posts}


@app.get('/api/posts/{post_id}', include_in_schema=False)
def get_post(request: Request, post_id: int):
    for post in posts:
        if post.get('id') == post_id:
            return post
        return {"error": "Post not found"}


@app.post(
        "/api/posts",
        response_model=PostResponse,
        status_code=status.HTTP_201_CREATED
        )
def create_post(post: PostCreate):
    new_id = max(p["id"] for p in posts) + 1 if posts else 1
    new_post = {
            "id": new_id,
            "date_created": "Aug 12 2026",
            "authour": post.authour,
            "title": post.title,
            "content": post.content
            }

    posts.append(new_post)
    return new_post

if __name__ == "__main__":
    home()
