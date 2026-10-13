from fastapi import FastAPI, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException



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


@app.get("/post/{post_id}", include_in_schema=False, name="post_page")
def post_page(request: Request, post_id: int):
    for post in posts:
        title = post.get("title")[:20]
        if post.get("id") == post_id:
            return templates.TemplateResponse(request, "post.html", {"post": post, "title": title})
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Post not found")



@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
            exception.detail
            if exception.detail else "An error occured. Please check your request and try again"
            )

    if request.url.path.startswith("/api"):
        return JSONResponse(
                status_code = exception.status_code,
                content={"detail": message}
                )

    return templates.TemplateResponse(
            request,
            "error.html",
            {
                "status_code": exception.status_code,
                "title": exception.status_code,
                "message": message
            },
            status_code=exception.status_code
        )


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                content={"detail": exception.errors()},
                )
    return templates.TemplateResponse(
            request,
            "error.html",
            {
                "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
                "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
                "message": "Invalid request. Please check your input and try again"
                },
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            )

if __name__ == "__main__":
    home()

