# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


------------------------------------------------------------------------------------------------------------------------------------------------------------------

## API

GET \categories Fetches a dictionary of all available categories

Request parameters: none
Example response:
```
{
  "categories": [
    {
      "id": 3, 
      "type": "Art"
    }, 
    {
      "id": 6, 
      "type": "Entertainment"
    }, 
    {
      "id": 4, 
      "type": "Geography"
    }, 
    {
      "id": 5, 
      "type": "History"
    }, 
    {
      "id": 2, 
      "type": "Science"
    }, 
    {
      "id": 7, 
      "type": "Sports"
    }, 
    {
      "id": 1, 
      "type": "test"
    }
  ], 
  "success": true
}


```

GET `\questions?page=<page_number>` Fetches a paginated dictionary of questions of all available categories

Request parameters (optional): page:int
Example response:
 ```
 {
  "categories": {
    "1": "test", 
    "2": "Science", 
    "3": "Art", 
    "4": "Geography", 
    "5": "History", 
    "6": "Entertainment", 
    "7": "Sports"
  }, 
  "questions": [
    {
      "answer": "Mona Lisa", 
      "category": "2", 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": "2", 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": "2", 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": "1", 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": "1", 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": "1", 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": "4", 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }, 
    {
      "answer": "QQQQQQQQQQQ", 
      "category": "2", 
      "difficulty": 3, 
      "id": 1, 
      "question": "QQQQQQQQQQ"
    }, 
    {
      "answer": "qqqqqqqqqq", 
      "category": "1", 
      "difficulty": 3, 
      "id": 47, 
      "question": "qqqqqqqqqq"
    }, 
    {
      "answer": "eeeeeeeeee", 
      "category": "1", 
      "difficulty": 1, 
      "id": 49, 
      "question": "eeeeeeeeee"
    }
  ], 
  "success": true, 
  "total_questions": 20
}

```

DELETE `/questions/<question_id>` Delete an existing questions from the repository of available questions

Request arguments: question_id:int
Example response:
```
{
  "deleted": 47, 
  "success": true, 
  "total_question": 19
}
```
POST `/questions` Add a new question to the repository of available questions

Request body: {question:string, answer:string, difficulty:int, category:string}
Example response:
```
{
  "created": 20, 
  "success": true
}

```
GET `/categories/<int:category_id>/questions` Fetches a dictionary of questions for the specified category

Request argument: category_id:int
Example response:
```
{
  "categories": 3, 
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "totalQuestions": 3
}

```
POST `/quizzes` Fetches one random question within a specified category. Previously asked questions are not asked again.

Request body: {previous_questions: arr, quiz_category: {id:int, type:string}}
Example response:
```
{
  "question": {
    "answer": "Uruguay", 
    "category": 6, 
    "difficulty": 4, 
    "id": 10, 
    "question": "Which country won the first ever soccer World Cup in 1930?"
  }, 
  "success": true
}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## File directory tree structure
```
.
├── README.md
├── __pycache__
│   ├── models.cpython-38.pyc
│   └── models.cpython-39.pyc
├── flaskr
│   ├── __init__.py
│   └── __pycache__
│       ├── __init__.cpython-38.pyc
│       └── __init__.cpython-39.pyc
├── models.py
├── pip
├── requirements.txt
├── test_flaskr.py
└── trivia.psql
```

3 directories, 11 files
