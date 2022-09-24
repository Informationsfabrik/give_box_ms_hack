from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine

from routers import giveboxes, comments, users, user_box_association, images

# Create DB
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# origins = [
#     "http://localhost", 
#     "http://localhost:5713", 
#     "http://127.0.0.1", 
#     "http://127.0.0.1:5713", 
#     "http://givebox-ms.de", 
#     "https://givebox-ms.de"
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


app.include_router(giveboxes.router, tags=["Givebox"])
app.include_router(comments.router, tags=["Comments"])
app.include_router(users.router, tags=["Users"])
app.include_router(user_box_association.router, tags=["User Givebox Association"])
app.include_router(images.router, tags=["Images"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8081, debug=True)
