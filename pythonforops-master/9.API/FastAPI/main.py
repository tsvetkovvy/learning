import logging
from logging.config import dictConfig
from typing import Optional

from fastapi import FastAPI, Header
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse

dictConfig({
    "version": 1,
    "formatters": {"default": {
        "format": '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    }},
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        }
    },
    "root": {
      "level": "DEBUG",
      "handlers": ['wsgi']
    }
})

logger = logging.getLogger("webapp")
app = FastAPI()


COURSES = {}


class Course(BaseModel):
    name: str
    desc: str = Field("None", title="Description of course", description="Description of course", max_length=255)


class Status(BaseModel):
    status: str


@app.get("/")
async def hello_world():
    return "Hello world\n"


# string/int/float/path/uuid
@app.get("/course/{course_name}", response_model=Course)
async def show_course_by_name(course_name: str, sort: str = "asc", content_type: Optional[str] = Header(None)):
    logger.info(content_type)
    logger.info(sort)
    return {"name": course_name, "desc": COURSES[course_name]}


@app.delete("/course/{course_name}", response_model=Status)
async def delete_course_by_name(course_name):
    del COURSES[course_name]
    return {"status": "ok"}


@app.put("/course", response_model=Status, responses={400: {"model": Status}})
async def create_course(course: Course):
    logger.info(course)
    logger.info(type(course))
    if course.name.isdigit():
        return JSONResponse(status_code=400, content={"status": "Course names with only digits are not allowed"})
    COURSES[course.name] = course.desc
    return {"status": "ok"}
