# xanoPull helper

Small helper to pull records from a Xano endpoint and pretty-print the JSON response.

Prerequisites
- Python 3.8+
- Create a `.env` file in the repository root with a line like:

```
XANO_GET=https://your-xano-endpoint.example/api/get_records
```

Install dependencies (PowerShell):

```powershell
python -m pip install -r requirements.txt
```

Run:

```powershell
python xanoPull.py
```

What changed
- `xanoPull.py` now prints HTTP status and Content-Type, handles error objects that look like {"code":"...","message":"..."}, and prints raw response when JSON parsing fails. This should make it clear why you're seeing the `code`/`message` object.

Debug tips
- If you see an object with exactly `code` and `message`, that's an error response from Xano. Common causes:
  - Wrong endpoint/path
  - Missing or invalid authentication (API key)
  - Required query parameters missing
  - You're hitting a 4xx/5xx endpoint

Check the printed HTTP status code and Content-Type first; they usually tell you what went wrong.Activity Platform Data Model
=
A relational schema for publishing activities, scheduling occurrences, defining academic context, skill metrics, pricing, instructors/publishers, and social follows. It is defined in DBML for easy visualization and SQL generation.​

Overview
--
Purpose: Model activities created by users, priced and scheduled, with associated difficulty, academic metadata, and competencies; support instructor bios and a follow system.​

Tech: DBML source of truth; export to SQL for your target RDBMS. Keep docs focused on core tasks and structure for readability.​
ERD summary


Core entities and relationships:​

activity: the canonical activity; links to publisher, price, academic category, skill metrics, and specifics.​

activity_occurrence: date/time instances of an activity; many-to-one with activity.​

activity_publisher: the publishing organization or person; references a user and primary/secondary instructors.​

activity_primary_instructor: instructor record tied to a user and optional bio.​

activity_skill_metrics: competency-style attributes (e.g., critical_reasoning, problem_solving) tied to an activity via Description_Id.​

activity_specifics: additional technical specifics, including difficulty linkage.​

activity_difficulty: normalized difficulty attributes for activities.​

academics: academic taxonomy for activities.​

activity_price: base list price and currency; discounts can be modeled separately if needed.​

User, User_Bio: user identity and biography for instructors/publishers.​

follows: user-to-user follow relationships with a composite PK to prevent duplicates.​
##
Roadmap
--
Optional discount tables and price snapshots in orders to preserve historical pricing. Keep roadmap concise and outcome-focused.​

Add indexes for common filters on activity_occurrence dates and activity.publisher_id. Maintain a structured list for quick scanning.​

