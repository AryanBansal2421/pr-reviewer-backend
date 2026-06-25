import os
from github import Github
from dotenv import load_dotenv
from backend.agents.security_agent import security_agent
from backend.agents.quality_agent import quality_agent
from backend.agents.architect_agent import architect_agent
import concurrent.futures

load_dotenv()

def get_pr_diff(repo_name: str, pr_number: int):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    files = pr.get_files()
    diff_text = ""
    for f in files:
        diff_text += f"\n### File: {f.filename}\n"
        if f.patch:
            diff_text += f.patch
    
    return repo, pr, diff_text

def post_comments(pr, comments: list):
    for comment in comments:
        if comment:
            if isinstance(comment, dict):
                text = comment.get("content", str(comment))
            else:
                text = comment
            pr.create_issue_comment(text)

def run_review(repo_name: str, pr_number: int):
    print(f"Starting review for PR #{pr_number} in {repo_name}")
    
    repo, pr, diff = get_pr_diff(repo_name, pr_number)
    
    if not diff:
        print("No diff found, skipping review")
        return

    # Run all 3 agents in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future_security = executor.submit(security_agent, diff)
        future_quality = executor.submit(quality_agent, diff)
        future_architect = executor.submit(architect_agent, diff)

        security_review = future_security.result()
        quality_review = future_quality.result()
        architect_review = future_architect.result()

    # Post comments on PR
    comments = [security_review, quality_review, architect_review]
    post_comments(pr, comments)
    
    print(f"Review complete for PR #{pr_number}")