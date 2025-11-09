from database import SessionLocal, engine
from models import Base, Task

Base.metadata.create_all(bind=engine)

db = SessionLocal()

sample_tasks = [
    Task(title="Fix login bug", description="Resolve user login error on homepage", priority="High"),
    Task(title="Write documentation", description="Add usage examples to the README", priority="Medium"),
    Task(title="Refactor database module", description="Improve performance of SQL queries", priority="High"),
    Task(title="Design new logo", description="Create a modern logo for the website", priority="Low"),
    Task(title="Email marketing", description="Send product update email to subscribers", priority="Medium"),
    Task(title="Add dark mode", description="Implement dark theme in settings", priority="Low"),
    Task(title="Optimize image loading", description="Compress and lazy load homepage images", priority="High"),
    Task(title="Fix mobile layout", description="Correct alignment issues on mobile view", priority="Medium"),
    Task(title="Write unit tests", description="Add more test cases for CRUD endpoints", priority="Low"),
    Task(title="Setup CI/CD pipeline", description="Integrate GitHub Actions for automatic deployment", priority="High"),
    Task(title="Customer feedback analysis", description="Analyze feedback forms for sentiment", priority="Medium"),
    Task(title="Add multilingual support", description="Add Vietnamese and Spanish translations", priority="High"),
    Task(title="Clean old logs", description="Delete outdated server logs", priority="Low"),
    Task(title="UI redesign", description="Modernize dashboard layout and buttons", priority="High"),
    Task(title="Blog feature", description="Implement blog section for company updates", priority="Medium"),
]

db.add_all(sample_tasks)
db.commit()
db.close()  

print("Sample data seeded successfully.")