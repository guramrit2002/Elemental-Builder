import re
import requests

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class JWTAuthMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        if (
            request.path.startswith('/admin/') 
            or request.path.startswith('/static/')
            or re.match(r"^/project/page/[0-9a-fA-F\-]+/?$", request.path)):
            return 

        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Missing token"}, status=401)

        try:
            response = requests.get(
                url=settings.USER_PROFILE_API_URL,
                headers={"Authorization": auth_header}
            )

            if response.status_code == 200:
                print("********** Core called Successfully **********")
                print(response.json())
                request.user_data = response.json()
            else:
                return JsonResponse({"error": response.text}, status=response.status_code)

        except requests.RequestException as e:
            return JsonResponse({"error": "Core service not reachable"}, status=500)
