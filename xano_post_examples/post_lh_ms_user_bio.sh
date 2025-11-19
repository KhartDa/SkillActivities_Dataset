# POST to lh_ms_user_bio (curl)
# Usage: Load your API key from .env and run:
# export XANO_API_KEY=$(grep XANO_API_KEY .env | cut -d= -f2)
# curl -X POST ${URL}/tables/lh_ms_user_bio \
#   -H "Authorization: Bearer ${XANO_API_KEY}" \
#   -H "Content-Type: application/json" \
#   -d '{
    # "id": integer (auto-generated, omit on POST),
    # "created_at": timestamp (auto-generated, omit on POST),
    "formal_education": "example_value",
    "professional_experience": "example_value",
    "linkedin": "example_value",
    "website": "example_value"
}}