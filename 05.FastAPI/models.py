from pydantic import BaseModel

class Email(BaseModel):
  id: int
  email: str

class CustomerBase(BaseModel):
  name: str
  description: str | None
  email: Email
  age: int

class CustomerCreate(CustomerBase):
  pass

class Customer(CustomerBase):
  id: int | None = None

class Transaction(BaseModel):
  id: int
  amount: int
  description: str

class Invoice(BaseModel):
  id: int
  customer: CustomerBase
  transactions: list[Transaction]
  total: int

  @property
  def amount_total(self):
    return sum(transaction.amount for transaction in self.transactions)
