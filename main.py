"""
Customer Management REST API
Built with FastAPI + Pydantic | In-memory storage
Run: uvicorn main:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

# ---------------------------------------------------------------------------
# App initialization
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Customer Management API",
    description="A simple CRUD API for managing customer data.",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# In-memory "database" (dict keyed by customer id) — pre-seeded with sample data
# ---------------------------------------------------------------------------
customers_db: dict[int, dict] = {
    1: {"id": 1, "name": "Alice Johnson",   "email": "alice.johnson@example.com",   "age": 28},
    2: {"id": 2, "name": "Bob Smith",       "email": "bob.smith@example.com",       "age": 35},
    3: {"id": 3, "name": "Carol Williams",  "email": "carol.williams@example.com",  "age": 42},
    4: {"id": 4, "name": "David Brown",     "email": "david.brown@example.com",     "age": 23},
    5: {"id": 5, "name": "Eva Martinez",    "email": "eva.martinez@example.com",    "age": 31},
    6: {"id": 6, "name": "Frank Lee",       "email": "frank.lee@example.com",       "age": 55},
    7: {"id": 7, "name": "Grace Kim",       "email": "grace.kim@example.com",       "age": 19},
    8: {"id": 8, "name": "Henry Davis",     "email": "henry.davis@example.com",     "age": 47},
    9: {"id": 9, "name": "Isla Thompson",   "email": "isla.thompson@example.com",   "age": 26},
   10: {"id": 10,"name": "Jack Wilson",     "email": "jack.wilson@example.com",     "age": 38},
}
_next_id: int = 11  # Auto-increment counter (starts after seeded data)


# ---------------------------------------------------------------------------
# Pydantic Models
# ---------------------------------------------------------------------------

class CustomerCreate(BaseModel):
    """Schema for creating / fully updating a customer (input)."""
    name: str = Field(..., min_length=3, description="Customer name (min 3 chars)")
    email: EmailStr = Field(..., description="Valid email address")
    age: int = Field(..., ge=18, le=100, description="Age between 18 and 100")


class CustomerUpdate(BaseModel):
    """Schema for partial updates — all fields are optional."""
    name: Optional[str] = Field(None, min_length=3)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=18, le=100)


class CustomerResponse(BaseModel):
    """Schema returned to the client (output)."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    age: int


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _get_or_404(customer_id: int) -> dict:
    """Return the customer dict or raise a 404 HTTPException."""
    customer = customers_db.get(customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with id {customer_id} not found.",
        )
    return customer


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get(
    "/customers",
    response_model=list[CustomerResponse],
    status_code=status.HTTP_200_OK,
    summary="List all customers",
)
def get_all_customers():
    """Return every customer stored in memory."""
    return list(customers_db.values())


@app.get(
    "/customers/{customer_id}",
    response_model=CustomerResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a single customer",
)
def get_customer(customer_id: int):
    """Fetch a single customer by their ID. Returns 404 if not found."""
    return _get_or_404(customer_id)


@app.post(
    "/customers",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new customer",
)
def create_customer(payload: CustomerCreate):
    """
    Create a new customer record.
    - **name**: at least 3 characters
    - **email**: must be a valid email
    - **age**: must be between 18 and 100
    """
    global _next_id
    new_customer = {
        "id": _next_id,
        "name": payload.name,
        "email": payload.email,
        "age": payload.age,
    }
    customers_db[_next_id] = new_customer
    _next_id += 1
    return new_customer


@app.put(
    "/customers/{customer_id}",
    response_model=CustomerResponse,
    status_code=status.HTTP_200_OK,
    summary="Update an existing customer",
)
def update_customer(customer_id: int, payload: CustomerUpdate):
    """
    Partially update a customer. Only the fields you supply are changed.
    Returns 404 if the customer does not exist.
    """
    customer = _get_or_404(customer_id)

    # Apply only the fields that were explicitly provided
    update_data = payload.model_dump(exclude_unset=True)
    customer.update(update_data)
    customers_db[customer_id] = customer
    return customer


@app.delete(
    "/customers/{customer_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a customer",
)
def delete_customer(customer_id: int):
    """
    Delete a customer by ID.
    Returns a confirmation message or 404 if not found.
    """
    _get_or_404(customer_id)
    del customers_db[customer_id]
    return {"message": f"Customer {customer_id} deleted successfully."}
