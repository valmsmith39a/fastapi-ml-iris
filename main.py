from fastapi import FastAPI
import uvicorn

# Declare FastAPI instance 
app = FastAPI()

@app.get("/")
def main():
	return {"message": "Welcome to Iris ML Project"}

@app.get("/{name}")
def hello_name(name : str):
	return { "message": f'Welcome to Iris ML Project, {name}'}
