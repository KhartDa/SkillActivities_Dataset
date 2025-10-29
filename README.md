Activity Platform Data Model
A relational schema for publishing activities, scheduling occurrences, defining academic context, skill metrics, pricing, instructors/publishers, and social follows. It is defined in DBML for easy visualization and SQL generation.​

Overview
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

Key design choices
Normalization: Attributes that can be reused or extended across activities (difficulty, academics, skill metrics) live in their own tables to avoid duplication and enable evolution.​

Temporal data: activity_occurrence stores time-bound scheduling instead of embedding schedule in activity.​

Ownership: activity.Publisher_Id → activity_publisher.Publisher_Id models publishing authority while allowing multiple activities per publisher.​

Social graph: follows uses a composite primary key on (following_user_id, followed_user_id) to enforce uniqueness.​

Getting started
Open /dbml/schema.dbml in dbdiagram or your DBML tool to view and export the ERD. Keep docs scannable with headings and code blocks.​

Export SQL for your RDBMS and run migrations in your environment; keep the README concise and link out to deeper docs where needed.​

Seed reference tables (activity_difficulty, academics) before inserting activities.​

Table glossary
activity: id, title, publisher_id, price_id, description_id, academics_id, specifics_id; foreign keys to related tables.​

activity_occurrence: id, activity_id, start/end date and time, timezone.​

activity_skill_metrics: description_id PK; columns like critical_reasoning, problem_solving, decision_making, communications, strategic_thinking, collaboration, creativity, story_telling.​

activity_specifics: specifics_id PK; difficulty_id FK to activity_difficulty.​

activity_difficulty: difficulty_id PK; name, pressure, length, experience, expectations.​

academics: academics_id PK; academic_name, academics_difficulty, type.​

activity_price: price_id PK; currency, total.​

activity_publisher: publisher_id PK; user_id, primary_instructor_id, secondary_id, last_name.​

activity_primary_instructor: activity_primary_instructor_id PK; user_id, bio_id.​

User: user_id PK; first/last name, email, phone.​

User_Bio: bio_id PK; bio, education level, professional experience, website.​

follows: composite PK; created_at timestamp.​

Common queries
List an activity with its publisher, academics, difficulty, and skill metrics. Use joins from activity to each FK-target table for a clear, concise example.​

Upcoming occurrences for a given activity within a date range via activity_occurrence filters. Keep examples focused on core tasks.​

Followers feed: join follows to activity_publisher/User to fetch activities from followed publishers. Structure examples for readability.​

Discounts guidance
Simple case: Add discount_type, discount_amount, discount_expires_at to activity_price if there is at most one active, simple discount. Keep it concise.​

Complex case: Model discounts as a separate table with a bridge (activity_discounts) for multiple rules, windows, and reuse. Keep structure clear and link to deeper docs if needed.​

Contributing
Use branches with clear names, open PRs, and keep documentation changes small and focused; this improves readability and adoption.​

Follow the writing principles: clear language, concise scope, and structured headings and lists; prefer Markdown in README and /docs.​

Add ERD or SQL changes with matching README updates to prevent drift; keep nonessential details in separate docs.​

Repo structure
dbml/schema.dbml — canonical model and comments; keep short and link to guides.​

sql/ — exported DDL for supported databases; optional. Keep files organized.​

docs/ — deeper guides: data dictionary, migration guide, discount patterns, and query examples. Organize for scannability.​

Style notes
Use consistent naming (snake_case for columns, singular table names by convention); apply consistent highlighting sparingly for scan-friendly docs.​

Prefer integer surrogate keys for FKs; ensure FK/PK types match; keep DBML refs in the child column inline for clarity.​

Roadmap
Optional discount tables and price snapshots in orders to preserve historical pricing. Keep roadmap concise and outcome-focused.​

Add indexes for common filters on activity_occurrence dates and activity.publisher_id. Maintain a structured list for quick scanning.​

