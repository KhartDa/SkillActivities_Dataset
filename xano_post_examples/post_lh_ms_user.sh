# POST to lh_ms_user (curl)
# Usage: Load your API key from .env and run:
# export XANO_API_KEY=$(grep XANO_API_KEY .env | cut -d= -f2)
# curl -X POST ${URL}/tables/lh_ms_user \
#   -H "Authorization: Bearer ${XANO_API_KEY}" \
#   -H "Content-Type: application/json" \
#   -d '{
    # "id": integer (auto-generated, omit on POST),
    # "created_at": timestamp (auto-generated, omit on POST),
    "email": "example_value",
    "password": "example_value",
    "account_id": "example_value",
    "role": "example_value",
    "password_reset": {,
      "token": "example_token",
      "expiration": "example_expiration",
    },
}}