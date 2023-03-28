from fastapi import FastAPI

from address import api

app = FastAPI()

app.include_router(api.router)

@app.get("/")
async def health_check():
    return {"Message": "To access APIs put /docs in the url"}
