# POST to lh_ms_activity_specifics (curl)
# Usage: Load your API key from .env and run:
# export XANO_API_KEY=$(grep XANO_API_KEY .env | cut -d= -f2)
# curl -X POST ${URL}/tables/lh_ms_activity_specifics \
#   -H "Authorization: Bearer ${XANO_API_KEY}" \
#   -H "Content-Type: application/json" \
#   -d '{
    # "id": integer (auto-generated, omit on POST),
    # "created_at": timestamp (auto-generated, omit on POST),
    "difficulty_level": "example_value",
    "arts_offered": "example_value",
    "language_offered": "example_value",
    "math_offered": "example_value",
    "science_offered": "example_value",
    "life_skills_offered": "example_value",
    "tech_end_offered": "example_value"
}}