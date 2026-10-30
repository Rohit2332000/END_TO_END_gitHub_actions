
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="CI/CD Learning API",
    description="FastAPI application for learning GitHub Actions",
    version="1.0.0"
)


class CalculatorInput(BaseModel):
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")


@app.get("/")
def root():
    return {"message": "FastAPI CI/CD Learning Project"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/add")
def addition(data: CalculatorInput):
    return {"operation": "addition", "result": data.a + data.b}


@app.post("/multiply")
def multiplication(data: CalculatorInput):
    return {"operation": "multiplication", "result": data.a * data.b}
