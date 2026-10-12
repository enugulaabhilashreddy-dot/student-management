
from fastapi import FastAPI, Request
from langfuse import get_client

from routers.student import student_router
from routers.course import course_router
from routers.marks import marks_router

app = FastAPI(title="student management system")

langfuse = get_client()


@app.middleware("http")
async def trace_api_requests(request: Request, call_next):
    if request.url.path in {"/docs", "/redoc", "/openapi.json"}:
        return await call_next(request)

    with langfuse.start_as_current_observation(
        as_type="span",
        name=f"{request.method} {request.url.path}",
    ) as span:
        response = await call_next(request)

        span.update(metadata={
            "http_method": request.method,
            "http_path": request.url.path,
            "http_status_code": response.status_code,
        })

        return response


app.include_router(student_router)
app.include_router(course_router)
app.include_router(marks_router)
