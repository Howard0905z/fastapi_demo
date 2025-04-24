from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # 前置處理：記錄請求
        print(f" {request.method} {request.url}")

        # 執行實際處理
        response = await call_next(request)

        # 後置處理：記錄花費時間與狀態碼
        process_time = time.time() - start_time
        print(f" Completed in {process_time:.2f}s | Status: {response.status_code}")

        return response
