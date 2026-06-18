from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()
expenses = []
class Expense(BaseModel):
    id :int
    description: str = Field(..., min_length=1, description="Expense description must be at least 1 character long")
    amount: float = Field(..., gt=0, description="Expense amount must be greater than 0")
    category: str = Field(..., min_length=1, description="Expense category must be at least 1 character long")
@app.post("/expenses")
def add_expense(expense: Expense):
    for existing_expense in expenses:
        if existing_expense.id == expense.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Expense with this ID already exists")
    expenses.append(expense)
    return {
        "message": "Expense added successfully",
        "expense": expense
    }
@app.get("/expenses")
def get_all_expenses():
    return {
        "message": "List of all expenses",
        "total_expenses": len(expenses),
        "all_expenses": expenses
    }
@app.get("/expenses/{expense_id}")
def get_expense_by_id(expense_id: int):
    for expense in expenses:
        if expense.id == expense_id:
            return {
                "message": "Expense found",
                "expense": expense
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
@app.get("/budget")
def get_budget():
    total_expenses = sum(expense.amount for expense in expenses)
    return {
        "message": "Budget information",
        "total_expenses": total_expenses
    }