#!/usr/bin/env python

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "HPS rulz !!!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
