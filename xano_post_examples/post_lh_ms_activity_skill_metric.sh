# POST to lh_ms_activity_skill_metric (curl)
# Usage: Load your API key from .env and run:
# export XANO_API_KEY=$(grep XANO_API_KEY .env | cut -d= -f2)
# curl -X POST ${URL}/tables/lh_ms_activity_skill_metric \
#   -H "Authorization: Bearer ${XANO_API_KEY}" \
#   -H "Content-Type: application/json" \
#   -d '{
    # "id": integer (auto-generated, omit on POST),
    # "created_at": timestamp (auto-generated, omit on POST),
    "critical_reasoning": "example_value",
    "problem_solving": "example_value",
    "decision_making": "example_value",
    "communication": "example_value",
    "strategic_thinking": "example_value",
    "collaboration": "example_value",
    "creativity": "example_value"
}}