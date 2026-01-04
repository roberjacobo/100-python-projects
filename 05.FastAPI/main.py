from db import SessionDep, create_all_tables
from fastapi import FastAPI, HTTPException
from models import Customer, CustomerCreate, Transaction, Invoice
from datetime import datetime
import zoneinfo


app = FastAPI(title="Learning FastAPI", version="1.0.0", lifespan=create_all_tables)

# In-memory database (simple list)
db_customers: list[Customer] = []


# ================================================================================
# BASIC ENDPOINTS
# ================================================================================


@app.get("/")
async def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to FastAPI!", "docs": "/docs"}


@app.get("/health")
async def health_check():
    """Check if the API is running"""
    return {"status": "ok", "customers_count": len(db_customers)}


# ================================================================================
# PATH PARAMETERS & QUERY PARAMETERS EXAMPLE
# ================================================================================

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """
    Example of path parameter (item_id) and query parameter (q).
    Try: /items/5?q=search
    """
    return {"item_id": item_id, "query": q}


# ================================================================================
# TIMEZONE EXAMPLE
# ================================================================================

COUNTRY_TIMEZONES = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}")
async def get_time(iso_code: str):
    """
    Get current time for a country.
    Try: /time/CO or /time/MX
    """
    iso = iso_code.upper()
    timezone_str = COUNTRY_TIMEZONES.get(iso)

    if not timezone_str:
        raise HTTPException(
            status_code=404,
            detail=f"Country code '{iso}' not supported. Available: {list(COUNTRY_TIMEZONES.keys())}"
        )

    tz = zoneinfo.ZoneInfo(timezone_str)
    return {
        "country": iso,
        "timezone": timezone_str,
        "current_time": datetime.now(tz).isoformat()
    }


# ================================================================================
# CUSTOMERS CRUD (Create, Read, Update, Delete)
# ================================================================================

@app.post("/customers", response_model=Customer, status_code=201)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    """Create a new customer"""
    customer = Customer.model_validate(customer_data.model_dump())
    customer.id = len(db_customers) + 1
    db_customers.append(customer)
    return customer


@app.get("/customers", response_model=list[Customer])
async def list_customers():
    """Get all customers"""
    return db_customers


@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int):
    """Get a specific customer by ID"""
    for customer in db_customers:
        if customer.id == customer_id:
            return customer

    raise HTTPException(
        status_code=404,
        detail=f"Customer with ID {customer_id} not found"
    )


@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):
    """Delete a customer by ID"""
    for index, customer in enumerate(db_customers):
        if customer.id == customer_id:
            db_customers.pop(index)
            return {"message": f"Customer {customer_id} deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail=f"Customer with ID {customer_id} not found"
    )


# ================================================================================
# TRANSACTIONS & INVOICES (Basic examples)
# ================================================================================

@app.post("/transactions", response_model=Transaction)
async def create_transaction(transaction_data: Transaction):
    """Create a transaction (example endpoint)"""
    return transaction_data


@app.post("/invoices", response_model=Invoice)
async def create_invoice(invoice_data: Invoice):
    """Create an invoice (example endpoint)"""
    return invoice_data
