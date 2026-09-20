from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Employee API")

class EmployeeCreate(BaseModel):
    name: str
    department: str


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


@app.post("/employees")
def create_employee(employee: EmployeeCreate):
    new_id = max((emp["id"] for emp in employees), default=0) + 1
    new_employee = {
        "id": new_id,
        "name": employee.name,
        "department": employee.department
    }
    employees.append(new_employee)
    return new_employee

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            return {"message": "Employee deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )