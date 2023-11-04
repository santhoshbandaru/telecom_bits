from pydantic import BaseModel
from typing import List

class CustomerBase(BaseModel):
    lastname: str
    firstname: str
    id_type: str
    idnum: str
    address: str
    dob: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(BaseModel):
    customerid:int      
    lastname:str           
    firstname:str              
    id_type:str  
    idnum: str
    address: str
    dob: str
    email: str                 
    
class Customer(CustomerBase):
    customerid: int

    class Config:
        orm_mode = True

class ServiceRequestBase(BaseModel):
    #phone_number: int
    #customerid: int
    #staffid: int
    ticketstatus: str
    description: str

class ServiceResponse(BaseModel):
    ticketid:int
    phone_number:int
    customerid :int
    staffid :int
    ticketstatus:int
    description:int
class ServiceRequestCreate(ServiceRequestBase):
    pass

class ServiceRequest(ServiceRequestBase):
    ticketid: int

    class Config:
        orm_mode = True

class StaffBase(BaseModel):
    address: str
    id_type: str
    id_num: str
    firstname: str
    lastname: str
class StaffResponse(BaseModel):
    staffid:int
    address:str
    id_type:str
    id_num:str
    firstname:str
    lastname:str
class StaffCreate(StaffBase):
    pass

class Staff(StaffBase):
    staffid: int

    class Config:
        orm_mode = True

class PhoneNumberBase(BaseModel):
    type: str
    plan: str
class PhoneNumberResponse(BaseModel):
    customerid:int
    phone_number:int
    type:str
    plan:str

class PhoneNumberCreate(PhoneNumberBase):
    customerid: int
    

    

class PhoneNumber(PhoneNumberBase):
    customerid: int
    phone_number: int

    class Config:
        orm_mode = True

class BillBase(BaseModel):
    amount: int
    paymentid: int
class BillResponseModel(BaseModel):
    amount:int
    customerid:int
    # paymentid:int
    # billid:int
    

class BillCreate(BillBase):
    phone_number: int

class Bill(BillBase):
    phone_number: int
    customerid: int
    billid: int

    class Config:
        orm_mode = True

class TicketCreate(BaseModel):
    phone_number: int
    customerid: int
    description: str

class TicketResponse(BaseModel):
    ticketid:int|None
    phone_number: int
    customerid: int
    staffid: int|None
    ticketstatus: str|None
    description: str

class LoginRequest(BaseModel):
    random_string:str      

class StaffLoginRequest(BaseModel):
    id:int