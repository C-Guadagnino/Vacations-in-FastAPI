from fastapi import APIRouter, Depends, Response
from typing import Optional, Union, List
from queries.vacations import (
    VacationIn,
    VacationRepository,
    VacationOut,
    Error
)


router = APIRouter()


@router.post("/vacations", response_model=Union[VacationOut, Error])
def create_vacations(
    vacation: VacationIn,
    response: Response,
    repo: VacationRepository = Depends()
):
    response.status_code = 200
    return repo.create(vacation)


@router.get("/vacations", response_model=Union[List[VacationOut], Error])
def get_all(
    repo: VacationRepository = Depends(),
):
    return repo.get_all()


@router.put(
    "/vacations/{vacation_id}", response_model=Union[VacationOut, Error]
)
def update_vacation(
    vacation_id: int,
    vacation: VacationIn,
    repo: VacationRepository = Depends(),
) -> Union[Error, VacationOut]:
    return repo.update(vacation_id, vacation)


@router.delete("/vacations/{vacation_id}", response_model=bool)
def delete_vacation(
    vacation_id: int,
    repo: VacationRepository = Depends(),
) -> bool:
    return repo.delete(vacation_id)


@router.get("/vacations/{vacation_id}", response_model=Optional[VacationOut])
def get_one(
    vacation_id: int,
    response: Response,
    repo: VacationRepository = Depends(),
) -> VacationOut:
    vacation = repo.get_one(vacation_id)
    if vacation is None:
        response.status_code = 404
    return vacation
