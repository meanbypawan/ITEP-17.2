from http.client import ResponseNotReady

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, RedirectResponse


class Auth(BaseHTTPMiddleware):
   async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
      public_url = ["/signin","/signup","/"]
      requested_url = request.url.path

      if requested_url in public_url:
         return await call_next(request)

      if request.session.get("is_logged_in",None):
         return await call_next(request)
      else:
         return RedirectResponse("/signin",status_code=303)





