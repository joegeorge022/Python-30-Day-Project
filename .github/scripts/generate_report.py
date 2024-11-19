import os
import markdown
from datetime import datetime
import json
from collections import defaultdict
import subprocess

class Student:
    def __init__(self, full_name, github_username, file_prefixes):
        self.full_name = full_name
        self.github_username = github_username
        self.file_prefixes = file_prefixes
        self.submissions = defaultdict(list)
        self.activity_history = []

def count_files_in_directory(directory):
    """Count the number of files in a directory."""
    try:
        return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    except FileNotFoundError:
        return 0

def get_git_history():
    """Get complete git history for the repository."""
    try:
        git_log = subprocess.check_output([
            'git', 'log', 
            '--all',
            '--format=%H|%an|%ae|%at|%s',
            '--reverse'
        ]).decode('utf-8').strip()
        
        commits = []
        for line in git_log.split('\n'):
            if line:
                hash, author, email, timestamp, message = line.split('|')
                commits.append({
                    "hash": hash,
                    "author": author,
                    "email": email,
                    "date": datetime.fromtimestamp(int(timestamp)).isoformat(),
                    "message": message
                })
        return commits
    except Exception as e:
        print(f"Error getting git history: {e}")
        return []

def generate_report():
    """Generate a detailed markdown progress report for each student."""
    students = [
        Student(
            "Joe George",
            "joegeorge022",
            ["joe_g", "joeg", "george", "joe.g", "joegeorge"]
        ),
        Student(
            "Joe Martin",
            "JoeMartinRince",
            ["joe_m", "joem", "martin", "joe.m", "joemartin"]
        ),
        Student(
            "Ganesh Chandran",
            "Ganesh-Chandran005",
            ["ganesh", "chandran", "ganesh_c", "ganeshc"]
        ),
        Student(
            "Job Thomas",
            "Jobthomas10",
            ["job", "thomas", "job_t", "jobt"]
        ),
        Student(
            "Indhu Subash",
            "IndhuSubash-2007",
            ["indhu", "subash", "indhu_s", "indhus"]
        )
    ]

    day_folders = [d for d in os.listdir('.') if os.path.isdir(d) and d.lower().startswith('day')]
    day_folders.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    git_history = get_git_history()
    workflow_runs = get_workflow_runs()

    chart_data = {
        "daily_submissions": defaultdict(int),
        "student_progress": {},
        "completion_rates": {},
        "language_distribution": defaultdict(int),
        "repository_activity": {
            "commits": git_history,
            "workflow_runs": workflow_runs,
            "activity_timeline": defaultdict(int),
            "contribution_history": defaultdict(lambda: defaultdict(int))
        }
    }

    for commit in git_history:
        date = commit["date"][:10]  
        chart_data["repository_activity"]["activity_timeline"][date] += 1
        author = commit["author"]
        chart_data["repository_activity"]["contribution_history"][author][date] += 1

    for student in students:
        student_data = {
            "total_files": 0,
            "completed_days": 0,
            "daily_submissions": {},
            "file_types": defaultdict(int),
            "total_lines": 0,
            "code_quality": {
                "comments_ratio": 0,
                "functions_count": 0,
                "classes_count": 0
            },
            "submission_timeline": [],
            "detailed_daily_stats": {}
        }

        for folder in day_folders:
            files = count_student_files(folder, student)
            if files:
                day_number = ''.join(filter(str.isdigit, folder))
                day_key = f"Day {day_number}"
                
                student_data["total_files"] += len(files)
                student_data["completed_days"] += 1
                student_data["daily_submissions"][day_key] = len(files)
                chart_data["daily_submissions"][day_key] += len(files)

                daily_stat = process_daily_files(files)
                student_data["detailed_daily_stats"][day_key] = daily_stat
                student_data["total_lines"] += daily_stat["total_lines"]
                
                student_data["code_quality"]["functions_count"] += daily_stat["functions"]
                student_data["code_quality"]["classes_count"] += daily_stat["classes"]
                
                for file in files:
                    student_data["file_types"][file["extension"]] += 1
                    chart_data["language_distribution"][file["extension"]] += 1

        completion_rate = (student_data["completed_days"] / len(day_folders)) * 100
        if student_data["total_lines"] > 0:
            comments_ratio = (student_data["code_quality"]["comments"] / 
                            student_data["total_lines"]) * 100
            student_data["code_quality"]["comments_ratio"] = comments_ratio

        chart_data["completion_rates"][student.full_name] = completion_rate
        chart_data["student_progress"][student.full_name] = student_data

    save_historical_data(chart_data)

if __name__ == "__main__":
    generate_report()
