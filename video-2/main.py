from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello'}

@app.get('/about')
def about():
    return {'message':'hello this is the second function'}

"""
to run this file we will run the command
uvicorn main:app --reload

--reload is used here because if we make changes to the code and save it the webpage will automatically update

http://127.0.0.1:8000/docs to see the auto generated documents


"""
