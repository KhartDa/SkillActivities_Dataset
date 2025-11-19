# POST to lh_ms_activity (curl)
# Usage: Load your API key from .env and run:
# export XANO_API_KEY=$(grep XANO_API_KEY .env | cut -d= -f2)
# curl -X POST ${URL}/tables/lh_ms_activity \
#   -H "Authorization: Bearer ${XANO_API_KEY}" \
#   -H "Content-Type: application/json" \
#   -d '{
    # "id": integer (auto-generated, omit on POST),
    # "created_at": timestamp (auto-generated, omit on POST),
    "publisher_id": "example_value",
    "price_id": "example_value",
    "academics_id": "example_value",
    "title": "example_value",
    "activity_metric_id": "example_value",
    "specifics_id": "example_value"
}}