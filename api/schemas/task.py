from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="Go to the supermarket to buy food")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="Complete flg")

    class Config:
        orm_mode = True