import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal, engine
from models import Base, Task

Base.metadata.create_all(bind=engine)

db = SessionLocal()

sample_tasks = [
    # --- HIGH ---
    Task(title="Fix login bug", description="Resolve user login error on homepage", priority="High"),
    Task(title="Optimize database", description="Tune SQL queries to reduce latency", priority="High"),
    Task(title="Implement password reset", description="Add forgot password flow with email verification", priority="High"),
    Task(title="Integrate payment gateway", description="Enable Stripe for premium accounts", priority="High"),
    Task(title="Add rate limiting", description="Prevent API abuse with rate limits", priority="High"),
    Task(title="Set up monitoring", description="Add Prometheus metrics and Grafana dashboard", priority="High"),
    Task(title="Upgrade security", description="Fix OWASP vulnerabilities and enforce HTTPS", priority="High"),
    Task(title="Deploy to production", description="Prepare environment for stable release", priority="High"),
    Task(title="Implement 2FA", description="Add two-factor authentication for all users", priority="High"),
    Task(title="Refactor legacy code", description="Clean up authentication module", priority="High"),
    Task(title="Improve search", description="Add fuzzy and typo-tolerant search", priority="High"),
    Task(title="Add caching", description="Use Redis to cache API responses", priority="High"),
    Task(title="Add audit logging", description="Track admin actions for compliance", priority="High"),
    Task(title="Backup system", description="Automate database backups nightly", priority="High"),
    Task(title="Fix broken CI/CD", description="Resolve pipeline failure in deployment", priority="High"),
    Task(title="Improve accessibility", description="Ensure website passes accessibility checks", priority="High"),
    Task(title="Enhance image compression", description="Reduce load time on homepage images", priority="High"),
    Task(title="Add role-based permissions", description="Restrict access by user role", priority="High"),
    Task(title="Resolve API timeout", description="Fix slow response on search endpoint", priority="High"),
    Task(title="Upgrade dependencies", description="Patch critical security vulnerabilities", priority="High"),

    # --- MEDIUM ---
    Task(title="Write documentation", description="Add examples and API references", priority="Medium"),
    Task(title="Create blog feature", description="Add CMS for news and updates", priority="Medium"),
    Task(title="Improve dashboard UX", description="Simplify navigation and buttons", priority="Medium"),
    Task(title="Implement notifications", description="Add in-app alert system", priority="Medium"),
    Task(title="Customer feedback analysis", description="Analyze user sentiment data", priority="Medium"),
    Task(title="Add multilingual support", description="Support Vietnamese and Spanish languages", priority="Medium"),
    Task(title="Add pagination", description="Paginate user list in admin dashboard", priority="Medium"),
    Task(title="Run usability testing", description="Collect feedback from beta users", priority="Medium"),
    Task(title="Setup analytics", description="Track user flow with Google Analytics", priority="Medium"),
    Task(title="Implement auto-save", description="Save drafts automatically in forms", priority="Medium"),
    Task(title="Add markdown editor", description="Support markdown syntax in text fields", priority="Medium"),
    Task(title="Enhance email templates", description="Improve layout and design of emails", priority="Medium"),
    Task(title="Create onboarding tutorial", description="Guide users through first-time setup", priority="Medium"),
    Task(title="Add dark mode", description="Implement dark theme toggle in settings", priority="Medium"),
    Task(title="Add filters to tasks", description="Filter by status, assignee, and priority", priority="Medium"),
    Task(title="Optimize build process", description="Speed up webpack build times", priority="Medium"),
    Task(title="Redesign error pages", description="Improve 404 and 500 error UX", priority="Medium"),
    Task(title="Add keyboard shortcuts", description="Improve productivity with shortcuts", priority="Medium"),
    Task(title="Integrate calendar", description="Sync tasks with Google Calendar", priority="Medium"),
    Task(title="Add feedback widget", description="Allow users to submit feedback easily", priority="Medium"),

    # --- LOW ---
    Task(title="Clean old logs", description="Delete outdated server logs", priority="Low"),
    Task(title="Update dependencies", description="Upgrade minor versions of libraries", priority="Low"),
    Task(title="Fix typos", description="Correct spelling errors in UI", priority="Low"),
    Task(title="Design new logo", description="Create a modern version of company logo", priority="Low"),
    Task(title="Add tooltips", description="Provide contextual help for buttons", priority="Low"),
    Task(title="Improve spacing", description="Adjust margins and paddings in UI", priority="Low"),
    Task(title="Add footer links", description="Include privacy and contact links", priority="Low"),
    Task(title="Update README", description="Add setup instructions", priority="Low"),
    Task(title="Reorganize folders", description="Group components by feature", priority="Low"),
    Task(title="Add loading spinner", description="Show spinner while data loads", priority="Low"),
    Task(title="Update contact page", description="Add new office address", priority="Low"),
    Task(title="Fix favicon", description="Use high-resolution favicon for browsers", priority="Low"),
    Task(title="Add about page", description="Include team and mission statement", priority="Low"),
    Task(title="Recolor sidebar icons", description="Improve icon contrast", priority="Low"),
    Task(title="Update changelog", description="Document recent updates", priority="Low"),
    Task(title="Add social media links", description="Link to company’s social profiles", priority="Low"),
    Task(title="Reword button labels", description="Simplify text for clarity", priority="Low"),
    Task(title="Remove unused CSS", description="Clean up unnecessary styles", priority="Low"),
    Task(title="Optimize small assets", description="Compress SVG icons", priority="Low"),
    Task(title="Add copyright footer", description="Display © year in footer", priority="Low"),
]

db.add_all(sample_tasks)
db.commit()
db.close()  

print("Sample data seeded successfully.")