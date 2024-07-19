from fastapi import FastAPI, HTTPException, Request
from fastapi import FastAPI, Depends
from fastapi import HTTPException
from pydantic import BaseModel, Field
from sqlmodel import Session
from datetime import datetime
import asyncio

from services.service import HelpDeskService
from adapters.db.common.base import get_db
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI, Depends
from fastapi import HTTPException
from pydantic import BaseModel, Field
from sqlmodel import Session
from datetime import datetime
import asyncio

from adapters.db.common.base import get_db

app = FastAPI()
app.title = "HELP DESK"
app.root_path = "/v1"

origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Orígenes que pueden realizar solicitudes
    allow_credentials=True,  # Permite cookies
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)

class HelpDeskModel(BaseModel):
    name: str = Field()
    case: str = Field()
    email: str = Field()
    status: str = Field(default="FK001")
    country: str = Field(default="MX")


def get_service():
    return HelpDeskService()

@app.post("/helpdesk")
async def save_helpdesk(hdm: HelpDeskModel, service: HelpDeskService = Depends(get_service),
                        db: Session = Depends(get_db)):
    await service.add_helpdesk(hd=hdm, db=db)
    return {"status": 200}


@app.get("/helpdesk")
def get_helpdesk(service: HelpDeskService = Depends(get_service), db: Session = Depends(get_db)):
    output = service.get_helpdesk(db=db)
    return {"data": output}
