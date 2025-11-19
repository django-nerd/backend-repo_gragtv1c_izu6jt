"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class Consultation(BaseModel):
    """
    Consultation requests from businesses wanting a full package
    Collection name: "consultation"
    """
    name: str = Field(..., description="Contact name")
    email: str = Field(..., description="Contact email")
    company: Optional[str] = Field(None, description="Company name")
    phone: Optional[str] = Field(None, description="Phone number")
    preferred_date: Optional[date] = Field(None, description="Preferred consultation date")
    preferred_time: Optional[str] = Field(None, description="Preferred time window, e.g., 2-4pm ET")
    budget_range: Optional[str] = Field(None, description="Rough budget range")
    message: Optional[str] = Field(None, description="Project goals and context")

class Order(BaseModel):
    """
    Orders for small automatic packages
    Collection name: "order"
    """
    package_id: str = Field(..., description="ID of the selected package")
    package_name: str = Field(..., description="Human-friendly name of the package")
    price: float = Field(..., ge=0, description="Price at time of order")
    buyer_name: str = Field(..., description="Buyer name")
    buyer_email: str = Field(..., description="Buyer email")
    company: Optional[str] = Field(None, description="Company name")
    notes: Optional[str] = Field(None, description="Additional notes from buyer")
