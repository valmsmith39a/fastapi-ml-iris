from fastapi import FastAPI
import uvicorn
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from pydantic import BaseModel

# declare FastAPI instance
app = FastAPI()


class request_body(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# load Iris dataset
iris = load_iris()

# get features and targets from dataset
X = iris.data
Y = iris.target

# fit model on dataset - train model
clf = GaussianNB()
clf.fit(X, Y)


@app.get("/")
def main():
    return {"message": "Welcome to Iris ML Project"}


@app.get("/{name}")
def hello_name(name: str):
    return {"message": f'Welcome to Iris ML Project, {name}'}


@app.post("/predict")
def predict(data: request_body):
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # predict the class of iris flower
    class_idx = clf.predict(test_data)[0]

    return {"class": iris.target_names[class_idx]}
