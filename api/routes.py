from fastapi import APIRouter

from .services import CaseService

case_router = APIRouter(prefix="/cases")


@case_router.get("/")
async def get_cases():
    pass


@case_router.get("/{case_id}")
async def get_case(case_id):
    pass


@case_router.post("/")
async def add_case():
    pass


@case_router.put("/{case_id}")
async def update_case():
    pass


@case_router.delete("/{case_id}")
async def delete_case():
    pass
