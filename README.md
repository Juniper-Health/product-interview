# Juniper Final Round Full Stack Interview

Welcome to the Juniper Final Round Interview! The interview prompt can be accessed [here](https://juniperplatform.notion.site/Product-Programming-Interview-5599d3c1fc6642e39071c4ad569eedf0)

## Frontend
The frontend is written in React using `create-react-app`, and we use `npm` for package management.

For your convenience, we have included some packages that may be useful in this assessment:
- `@mui/material` for basic components [docs](https://mui.com/material-ui/all-components/)
- `@tanstack/react-query` for querying the provided server [docs](https://tanstack.com/query/v5/docs/framework/react/quick-start)

### Initialize
```
>> npm i
>> npm start
```
The server will be running on port `http://localhost:3000/`

## Backend
The backend is written in Python 3, using FastAPI for the server [docs](https://fastapi.tiangolo.com/#example).

We provide a pre-seeded SQLite Database located at `data.db` and can be accessed using SQLAlchemy [docs](https://docs.sqlalchemy.org/en/14/orm/query.html) in the boilerplate server provided

### Initialize
```
>> pip install -r ./requirements.txt
>> fastapi dev main.py
```

The server will be running on port `http://localhost:8000/` and interactive OpenAPI docs can be accessed at `http://localhost:8000/docs`

Refer to `main.py` for prewritten routes, but feel free to add more if you feel it is helpful!

# Submission
Send a `.zip` of your project to the email provided by the interviewer.
