from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "pr_reviewer",
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://localhost:6379/0")
)

celery_app.conf.task_routes = {
    "backend.workers.celery_app.review_pr_task": {"queue": "pr_review"}
}

@celery_app.task(name="backend.workers.celery_app.review_pr_task")
def review_pr_task(repo_name: str, pr_number: int):
    from backend.workers.reviewer import run_review
    run_review(repo_name, pr_number)