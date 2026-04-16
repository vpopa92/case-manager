from fastapi import FastAPI

app = FastAPI(title="Case Manager API")

@app.get("/health")
def health():
    return {"status": "ok"}
