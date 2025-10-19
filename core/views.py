import requests
import logging
from datetime import datetime, timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from config import CAT_FACT_API, API_TIMEOUT


logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['GET'])
def me(request):
    """Return user info and a random cat fact."""
    
    try:
        response = requests.get(CAT_FACT_API, timeout=API_TIMEOUT)
        response.raise_for_status()  

        data = response.json()
        fact = data.get("fact", "Cats are mysterious creatures.")
    except requests.exceptions.Timeout:
        #Handle timeout error
        logger.warning("Cat Facts API timed out.")
        fact = "The cat facts server took too long to respond."
    except requests.exceptions.RequestException as e:
        # Handle other network errors
        logger.error(f"Cat Facts API error: {e}")
        fact = "Unable to fetch a cat fact right now. Please try again later."

    # Construct the response payload
    payload = {
        "status": "success",
        "user": {
            "email": "amajuogbe@gmail.com",
            "name": "Ogbe Amaju",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": fact
    }

    return Response(payload, status=status.HTTP_200_OK)

