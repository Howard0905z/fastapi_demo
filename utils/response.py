from fastapi.responses import JSONResponse

def api_response(data=None, message="Success", status="success", code=200):
    return JSONResponse(
        status_code=code,
        content={
            "status": status,
            "message": message,
            "data": data
        }
    )
