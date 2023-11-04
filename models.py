from database import Base, engine
from sqlalchemy import Column, String, Integer, ForeignKey,Table
from sqlalchemy.orm import relationship

# Define a secondary table for the many-to-many relationship between Staff and ServiceRequest
service_requests_staff = Table(
    "service_requests_staff",
    Base.metadata,
    Column("service_request_id", Integer, ForeignKey("service_requests.ticketid")),
    Column("staff_id", Integer, ForeignKey("staff.staffid")),
)
class Customer(Base):
    __tablename__ = "customer"
    customerid = Column(Integer, primary_key=True)
    lastname = Column(String)
    firstname = Column(String)
    password = Column(String)
    id_type = Column(String)
    idnum = Column(String)
    address = Column(String)
    dob = Column(String)
    email = Column(String)
    phone_numbers = relationship("PhoneNumber", back_populates="customer")
    service_requests = relationship("ServiceRequest", back_populates="customer")

class ServiceRequest(Base):
    __tablename__ = "service_requests"
    ticketid = Column(Integer, primary_key=True)
    phone_number = Column(Integer, ForeignKey("phonenumber.phone_number"))
    customerid = Column(Integer, ForeignKey("customer.customerid"))
    staffid = Column(Integer, ForeignKey("staff.staffid"))
    ticketstatus = Column(String)
    description = Column(String)
    customer = relationship("Customer", back_populates="service_requests")
    staff = relationship("Staff", secondary=service_requests_staff, back_populates="service_requests")

class Staff(Base):
    __tablename__ = "staff"
    staffid = Column(Integer, primary_key=True)
    address = Column(String)
    id_type = Column(String)
    id_num = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    service_requests = relationship("ServiceRequest", secondary=service_requests_staff, back_populates="staff")

class PhoneNumber(Base):
    __tablename__ = "phonenumber"
    phone_number = Column(Integer, primary_key=True)
    type = Column(String)
    plan = Column(String)
    customerid = Column(Integer, ForeignKey("customer.customerid"))
    customer = relationship("Customer", back_populates="phone_numbers")
    bills = relationship("Bill", back_populates="phone_number")

class Bill(Base):
    __tablename__ = "bill"
    phone_number = Column(Integer, ForeignKey("phonenumber.phone_number"))
    amount = Column(Integer)
    paymentid = Column(Integer, primary_key=True)
    billid = Column(Integer, primary_key=True)
    customerid = Column(Integer, ForeignKey("phonenumber.customerid"))
    phone_number = relationship("PhoneNumber", back_populates="bills")

class PhoneNumbers(Base):
    __tablename__ = "phonenumbers"
    phone_number = Column(Integer, primary_key=True)
    customerid = Column(Integer, ForeignKey("customer.customerid"))
    
Base.metadata.create_all(bind=engine)
