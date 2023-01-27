from fastapi import FastAPI, Path
from typing import Optional, List
from pydantic import BaseModel

from API.Users import router

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing users.",
    version="0.0.1",
    contact={
        "name": "Gilbert E. Tineo",
        "email": "tineogilbert@gail.com",
    },
    license_info={
        "name": "MIT"
    }

)


app.include_router(router)

