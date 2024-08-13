from fastapi import APIRouter, HTTPException, status
from logging_service.models import LogModel
from database import log_collection
from bson import ObjectId
from typing import List

router = APIRouter()


@router.post("/", response_model=LogModel, status_code=status.HTTP_201_CREATED)
async def create_log(log: LogModel):
    log_dict = log.dict(by_alias=True)
    result = await log_collection.insert_one(log_dict)
    created_log = await log_collection.find_one({"_id": result.inserted_id})
    return created_log


@router.get("/", response_model=List[LogModel])
async def get_logs():
    logs = await log_collection.find().to_list(1000)
    return logs


@router.get("/{id}", response_model=LogModel)
async def get_log(id: str):
    if ObjectId.is_valid(id):
        log = await log_collection.find_one({"_id": ObjectId(id)})
        if log:
            return log
    raise HTTPException(status_code=404, detail="Log not found")


@router.put("/{id}", response_model=LogModel)
async def update_log(id: str, log: LogModel):
    if ObjectId.is_valid(id):
        update_result = await log_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": log.dict(by_alias=True)}
        )
        if update_result.modified_count == 1:
            updated_log = await log_collection.find_one({"_id": ObjectId(id)})
            if updated_log:
                return updated_log
    raise HTTPException(status_code=404, detail="Log not found")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_log(id: str):
    if ObjectId.is_valid(id):
        delete_result = await log_collection.delete_one({"_id": ObjectId(id)})
        if delete_result.deleted_count == 1:
            return
    raise HTTPException(status_code=404, detail="Log not found")
