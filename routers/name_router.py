from fastapi import APIRouter
from schemas.name_schemas import NameIn, NameOut
from core.agent import generate_names


router = APIRouter(prefix="/name")


@router.post("/", response_model=NameOut)
async def take_ainame(data: NameIn):
    name_result = await generate_names(data)
    return NameOut(names=name_result.names)