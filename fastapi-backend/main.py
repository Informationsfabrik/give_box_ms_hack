from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from routers import comments, giveboxes, images, user_box_association, users

app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(giveboxes.router, tags=["Givebox"])
app.include_router(comments.router, tags=["Comments"])
app.include_router(users.router, tags=["Users"])
app.include_router(user_box_association.router, tags=["User Givebox Association"])
app.include_router(images.router, tags=["Images"])


def main():
    print("Hello World")

if __name__ == "__main__":
    main()
