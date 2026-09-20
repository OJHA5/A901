from fastapi import FastAPI, HTTPException

app = FastAPI(title="Employee API")

employees = [
    {"id": 1, "name": "Amit", "department": "Technology"},
    {"id": 2, "name": "John", "department": "Finance"},
    {"id": 3, "name": "Sarah", "department": "Operations"}
]


@app.get("/")
def home():
    return {"message": "Employee API is running"}


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )