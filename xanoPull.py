from dotenv import load_dotenv
import os, requests,json

load_dotenv()
point = os.getenv("XANO_POST")


"""
api requieres following information:

#price >> currency, total.

#activity skill metric >> critical reasoning, problem solving,
    decision making, communication, strategic thinking, collaboration, creativity.

#activity specifics >> driving question, difficulty level, arts offered, language offered, math offered
science offered, life skills offered difficulty level,
start time, end time, max participants.

structure :

{
  "price": {},
  "activity_skill_metric": {},
  "activity_specifics": {}
  
}

"""
data = {
    "activity_attributes": {
        "title": "Ocean Plastic Cleanup Workshop",
        "price": {
            "currency": "USD",
            "total": 100
        },
        "skill_metric": {
            "critical_reasoning": 4,
            "problem_solving": 5,
            "decision_making": 3,
            "communication": 4,
            "strategic_thinking": 5,
            "collaboration": 4,
            "creativity": 5
        },
        "specifics": {
            "driving_question": "How can we solve the problem of plastic waste in our oceans?",
            "description":"",
            "skills_will_gain":[],
            "modules":[],
            "difficulty_level": "Intermediate",
            "arts_offered": ["Painting"],
            "language_offered": ["English", "Spanish"],
            "math_offered": ["Algebra", "Geometry"],
            "science_offered": ["Biology", "Chemistry"],
            "life_skills_offered": ["Time Management", "Communication"],
            "start_date": "2024-07-01",
            "end_date": "2024-07-01",
            "start_time": "09:00",
            "end_time": "12:00",
            "participants": 20
        }
    }
}

data1 = {
    "activity_attributes": {
        "title": "Python Programming Fundamentals for Problem Solving",
        "price": {
            "currency": "USD",
            "total": 120
        },
        "skill_metric": {
            "critical_reasoning": 5,
            "problem_solving": 5,
            "decision_making": 4,
            "communication": 3,
            "strategic_thinking": 4,
            "collaboration": 4,
            "creativity": 4
        },
        "specifics": {
            "driving_question": "How can we use Python to solve real-world problems and develop computational thinking skills?",
            "description": "This comprehensive Python programming course is inspired by Harvard's CS50 Introduction to Programming with Python and focuses on teaching students how to think algorithmically and write clean, correct code. Learners start with the core building blocks of programming, including variables, data types, conditionals, loops, functions, and Boolean expressions, gradually progressing to more advanced concepts like exceptions, file I/O, libraries, and object-oriented programming. Throughout the course, students complete hands-on exercises and problem sets inspired by real-world scenarios such as data processing, automation, and simple web tasks. They learn to debug their programs, test edge cases, and use third-party libraries to extend Python's capabilities. By the end of the course, participants will have built a portfolio of small projects that demonstrate their ability to read, write, test, and debug Python code, preparing them for further study in computer science, data science, or software engineering.",
            "skills_will_gain": [
                "Python Programming",
                "Algorithmic Thinking",
                "Debugging",
                "Problem Decomposition",
                "Object-Oriented Programming"
            ],
            "modules": [
                "Variables, Types, and Expressions",
                "Conditionals and Boolean Logic",
                "Loops and Iteration",
                "Functions and Scope",
                "Data Structures in Python",
                "Files, Exceptions, and Libraries",
                "Intro to Object-Oriented Programming"
            ],
            "difficulty_level": "Intermediate",
            "arts_offered": [],
            "language_offered": ["English"],
            "math_offered": ["Logic"],
            "science_offered": ["Computer Science"],
            "life_skills_offered": ["Problem Solving", "Persistence", "Attention to Detail"],
            "start_date": "2025-01-13",
            "end_date": "2025-04-21",
            "start_time": "17:00",
            "end_time": "19:00",
            "participants": 40
        }
    }
}

data2 = {
    "activity_attributes": {
        "title": "Machine Learning Specialization: Theory and Applications",
        "price": {
            "currency": "USD",
            "total": 180
        },
        "skill_metric": {
            "critical_reasoning": 5,
            "problem_solving": 5,
            "decision_making": 5,
            "communication": 3,
            "strategic_thinking": 5,
            "collaboration": 3,
            "creativity": 4
        },
        "specifics": {
            "driving_question": "How can machines learn patterns from data and make accurate predictions without being explicitly programmed?",
            "description": "This advanced machine learning activity is modeled on popular ML specializations and focuses on both the mathematical foundations and practical implementation of modern algorithms. Students begin with core supervised learning techniques, such as linear and logistic regression, learning how to define loss functions, optimize with gradient descent, and regularize models to prevent overfitting. The course then moves into more powerful approaches like decision trees, random forests, and ensemble methods, as well as unsupervised learning techniques including clustering and dimensionality reduction. Learners gain hands-on experience by building models in Python using libraries such as NumPy, scikit-learn, and TensorFlow. Through applied projects, they work on tasks like classification, regression, anomaly detection, and recommendation systems. Emphasis is placed on best practices, including data preprocessing, feature engineering, cross-validation, hyperparameter tuning, and evaluating model performance using appropriate metrics. By the end, students will understand how to choose, train, and deploy machine learning models on real-world datasets and will have a solid foundation for further study in AI and deep learning.",
            "skills_will_gain": [
                "Supervised Learning",
                "Unsupervised Learning",
                "Model Evaluation",
                "Feature Engineering",
                "TensorFlow and scikit-learn"
            ],
            "modules": [
                "Introduction to Machine Learning",
                "Linear and Logistic Regression",
                "Decision Trees and Ensembles",
                "Clustering and Dimensionality Reduction",
                "Neural Networks Basics",
                "Model Evaluation and Tuning",
                "Applied Machine Learning Project"
            ],
            "difficulty_level": "Advanced",
            "arts_offered": [],
            "language_offered": ["English"],
            "math_offered": ["Linear Algebra", "Calculus", "Probability", "Statistics"],
            "science_offered": ["Computer Science", "Data Science"],
            "life_skills_offered": ["Critical Thinking", "Analytical Reasoning", "Research"],
            "start_date": "2025-01-20",
            "end_date": "2025-06-30",
            "start_time": "18:30",
            "end_time": "21:00",
            "participants": 35
        }
    }
}

data3 = {
    "activity_attributes": {
        "title": "Cellular Biology Fundamentals: From Cells to Organisms",
        "price": {
            "currency": "USD",
            "total": 95
        },
        "skill_metric": {
            "critical_reasoning": 5,
            "problem_solving": 4,
            "decision_making": 3,
            "communication": 4,
            "strategic_thinking": 3,
            "collaboration": 5,
            "creativity": 4
        },
        "specifics": {
            "driving_question": "What structures and processes at the cellular level make life possible in plants and animals?",
            "description": "This biology activity is inspired by middle school and AP-level cell biology units and provides a deep exploration of cells as the basic unit of life. Students investigate the structure and function of key organelles, such as the nucleus, mitochondria, ribosomes, endoplasmic reticulum, Golgi apparatus, and chloroplasts, and learn how these components work together to keep cells alive. The course compares prokaryotic and eukaryotic cells and examines how cell membranes control the movement of materials through diffusion, osmosis, and active transport. Learners explore processes like photosynthesis and cellular respiration to understand how cells transform energy, and they study cell division through mitosis and meiosis to see how growth, repair, and reproduction occur. Hands-on activities may include microscope work, slide preparation, and simple experiments demonstrating membrane transport. The activity also connects cell-level processes to whole organisms by tracing how cells form tissues, organs, and organ systems in the human body. By the end, students will have a strong conceptual model of how cells function, interact, and scale up to complex living systems.",
            "skills_will_gain": [
                "Understanding Cell Structure",
                "Microscopy Basics",
                "Scientific Observation",
                "Data Recording and Analysis",
                "Conceptual Modeling of Biological Systems"
            ],
            "modules": [
                "Introduction to Cells",
                "Organelles and Their Functions",
                "Membranes, Transport, and Homeostasis",
                "Photosynthesis and Cellular Respiration",
                "Mitosis, Meiosis, and Cell Reproduction",
                "From Cells to Tissues and Organs",
                "Cells, Genetics, and Evolution"
            ],
            "difficulty_level": "Intermediate",
            "arts_offered": ["Scientific Illustration"],
            "language_offered": ["English"],
            "math_offered": ["Basic Statistics"],
            "science_offered": ["Biology", "Chemistry"],
            "life_skills_offered": ["Observation", "Critical Thinking", "Collaboration"],
            "start_date": "2025-02-03",
            "end_date": "2025-05-12",
            "start_time": "15:00",
            "end_time": "17:30",
            "participants": 28
        }
    }
}

data4 = {
    "activity_attributes": {
        "title": "Full-Stack Web Development: From Frontend to Backend",
        "price": {
            "currency": "USD",
            "total": 200
        },
        "skill_metric": {
            "critical_reasoning": 4,
            "problem_solving": 5,
            "decision_making": 4,
            "communication": 4,
            "strategic_thinking": 4,
            "collaboration": 5,
            "creativity": 5
        },
        "specifics": {
            "driving_question": "How can we design and build modern, scalable web applications that real users will love to use?",
            "description": "This web development activity is inspired by full-stack curricula that combine front-end and back-end skills into a project-based experience. Students start on the client side by learning HTML5, CSS3, and modern JavaScript, then progress to frameworks such as React for building responsive, interactive user interfaces. On the server side, they work with Python and a web framework like Django or Flask to design RESTful APIs, connect to relational databases, and implement authentication and authorization. Learners practice using Git and GitHub for version control and collaboration, and they deploy applications to cloud platforms such as Heroku or similar services. Along the way, they address accessibility, responsive design, and basic security practices to protect user data. Capstone projects include building real-world style applications like blogs, dashboards, e-commerce prototypes, or social platforms. By the end of the activity, participants will have a complete understanding of how the front end and back end interact and will have deployed at least one full-stack application accessible on the web.",
            "skills_will_gain": [
                "HTML and CSS",
                "JavaScript and React",
                "Python Web Development",
                "RESTful API Design",
                "Database Modeling and SQL",
                "Git and Version Control",
                "Cloud Deployment"
            ],
            "modules": [
                "Web Foundations (HTML, CSS)",
                "Interactive Frontend with JavaScript",
                "Single-Page Apps with React",
                "Backend with Python and Django/Flask",
                "Relational Databases and SQL",
                "Authentication and Security Basics",
                "Deployment and Capstone Project"
            ],
            "difficulty_level": "Intermediate",
            "arts_offered": ["Web Design", "UI/UX Design"],
            "language_offered": ["English", "Spanish"],
            "math_offered": [],
            "science_offered": ["Computer Science"],
            "life_skills_offered": ["Collaboration", "Project Management", "Communication"],
            "start_date": "2025-02-01",
            "end_date": "2025-05-31",
            "start_time": "17:00",
            "end_time": "20:00",
            "participants": 30
        }
    }
}

data5 = {
    "activity_attributes": {
        "title": "Data Science Fundamentals: Python Analytics and Visualization",
        "price": {
            "currency": "USD",
            "total": 175
        },
        "skill_metric": {
            "critical_reasoning": 5,
            "problem_solving": 5,
            "decision_making": 5,
            "communication": 4,
            "strategic_thinking": 5,
            "collaboration": 3,
            "creativity": 4
        },
        "specifics": {
            "driving_question": "How can we transform raw data into meaningful insights that support real-world decisions?",
            "description": "This data science activity introduces students to the full analytics workflow using Python and common open-source tools. Learners begin with data handling in Python, then dive into libraries such as NumPy for numerical computation and Pandas for data wrangling, cleaning, and transformation. They explore datasets from domains like finance, health, environment, and social media, performing exploratory data analysis to uncover patterns and anomalies. Visualization libraries such as Matplotlib and Seaborn are used to create clear, compelling charts and plots that communicate findings. The course also introduces basic statistical concepts, including distributions, hypothesis testing, correlation, and simple regression models, and shows how these tools are applied to real datasets. Students build small machine learning models using scikit-learn for tasks like classification and regression to make predictions. Throughout the activity, emphasis is placed on documenting work in Jupyter notebooks, interpreting results, and presenting insights to non-technical audiences. The final project requires students to pose a question, analyze a dataset, and deliver a data story with visualizations and recommendations.",
            "skills_will_gain": [
                "Python for Data Analysis",
                "Pandas and NumPy",
                "Data Cleaning and Wrangling",
                "Statistical Thinking",
                "Data Visualization",
                "Introductory Machine Learning"
            ],
            "modules": [
                "Python Refresher for Data Work",
                "Working with Data in Pandas",
                "Exploratory Data Analysis",
                "Statistical Concepts and Hypothesis Testing",
                "Regression and Basic ML Models",
                "Visualization with Matplotlib and Seaborn",
                "End-to-End Data Project"
            ],
            "difficulty_level": "Intermediate",
            "arts_offered": [],
            "language_offered": ["English"],
            "math_offered": ["Statistics", "Probability"],
            "science_offered": ["Data Science", "Computer Science"],
            "life_skills_offered": ["Analytical Thinking", "Communication", "Problem Solving"],
            "start_date": "2025-01-25",
            "end_date": "2025-05-15",
            "start_time": "18:30",
            "end_time": "21:00",
            "participants": 35
        }
    }
}

data6 = {
    "activity_attributes": {
        "title": "Artificial Intelligence: Principles, Algorithms, and Ethics",
        "price": {
            "currency": "USD",
            "total": 190
        },
        "skill_metric": {
            "critical_reasoning": 5,
            "problem_solving": 5,
            "decision_making": 5,
            "communication": 4,
            "strategic_thinking": 5,
            "collaboration": 4,
            "creativity": 5
        },
        "specifics": {
            "driving_question": "How can we design intelligent systems that learn, reason, and act ethically in the real world?",
            "description": "This artificial intelligence activity combines classic AI topics with modern machine learning and a strong focus on ethics. Students study foundational AI techniques such as state-space search, heuristic search (including A*), and constraint satisfaction, along with probabilistic reasoning using basic Bayesian ideas. They then connect these foundations to current practice by looking at machine learning and deep learning techniques used for perception and decision-making, including neural networks, natural language processing, and computer vision. Projects may involve building simple game-playing agents, recommendation systems, or chatbots using Python. A major component of the course is examining the societal and ethical implications of AI: bias in datasets and models, fairness and accountability, transparency and explainability, privacy concerns, and the impact of automation on work and society. Students analyze real case studies where AI systems failed or caused harm, and they explore frameworks for responsible and human-centered AI design. By the end, learners will understand not only how AI systems work technically, but also how to think critically about deploying them responsibly.",
            "skills_will_gain": [
                "Artificial Intelligence Fundamentals",
                "Search and Planning",
                "Basic Probabilistic Reasoning",
                "Neural Network Concepts",
                "AI Ethics and Responsible Design"
            ],
            "modules": [
                "Introduction to AI and Intelligent Agents",
                "Search Algorithms and Games",
                "Knowledge Representation Basics",
                "Machine Learning and Neural Networks Overview",
                "Natural Language and Vision (High-Level Overview)",
                "Ethics, Fairness, and Accountability in AI",
                "AI Case Studies and Responsible Design Project"
            ],
            "difficulty_level": "Advanced",
            "arts_offered": [],
            "language_offered": ["English"],
            "math_offered": ["Linear Algebra", "Probability", "Statistics"],
            "science_offered": ["Computer Science", "Cognitive Science"],
            "life_skills_offered": ["Critical Thinking", "Ethical Reasoning", "Innovation"],
            "start_date": "2025-01-10",
            "end_date": "2025-06-10",
            "start_time": "19:00",
            "end_time": "21:30",
            "participants": 40
        }
    }
}


resp = requests.post(point,json=data6)
print(resp.status_code)
print(resp.text)
