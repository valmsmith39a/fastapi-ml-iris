## Iris Flowers Classification

#### Dependencies:

- FastAPI
- uvicorn
- scikit-learn

#### API

##### POST request

```
curl -X 'POST'   8000/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "sepal_length": 5,
  "sepal_width": 3,
  "petal_length": 1,
  "petal_width": 0.2
}'
```

##### Response

```
{"class":"setosa"}
```
