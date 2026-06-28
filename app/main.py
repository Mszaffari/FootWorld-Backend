from fastapi import FastAPI

app = FastAPI(
    title="FootWorld API",
    description="Backend API for FootWorld",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "status": "success",
        "message": "FootWorld API is running 🚀",
    }