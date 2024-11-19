import os
import markdown
from datetime import datetime
import json
from collections import defaultdict

def count_files_in_directory(directory):
    """Count the number of files in a directory."""
    try:
        return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    except FileNotFoundError:
        return 0

def generate_report():
    """Generate a detailed markdown progress report for each student."""
    # Define students with their possible file name prefixes
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

    # Get all Day folders
    day_folders = [d for d in os.listdir('.') if os.path.isdir(d) and d.lower().startswith('day')]
    day_folders.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Initialize report content
    report = ["# 🎯 Python 30-Day Project Progress Report\n"]
    report.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*\n")

    # Initialize git repository information
    repo_info = {
        "total_commits": 0,
        "contributors": defaultdict(lambda: {
            "commits": 0,
            "files": 0,
            "lines": 0
        })
    }

    try:
        repo_info["total_commits"] = int(subprocess.check_output(
            ['git', 'rev-list', '--count', 'HEAD']
        ).decode('utf-8').strip())
    except subprocess.CalledProcessError:
        pass

    # Generate chart data with enhanced git information
    chart_data = {
        "daily_submissions": defaultdict(int),
        "student_progress": {},
        "completion_rates": {},
        "git_activity": defaultdict(list),
        "language_distribution": defaultdict(int),
        "contribution_stats": repo_info
    }

    # Collect detailed statistics
    for student in students:
        for folder in day_folders:
            day_number = ''.join(filter(str.isdigit, folder))
            files = count_student_files(folder, student)
            
            if files:
                student.submissions[folder] = files
                day_stats = student.daily_stats[folder]
                day_stats["files"] = files
                
                # Aggregate statistics
                for file in files:
                    day_stats["total_lines"] += file["stats"]["lines"]
                    day_stats["file_types"][file["extension"]] += 1
                    
                    # Track submission time
                    file_time = datetime.fromisoformat(file["stats"]["last_modified"])
                    if not day_stats["submission_time"] or file_time > day_stats["submission_time"]:
                        day_stats["submission_time"] = file_time

    # Generate individual progress reports
    for student in students:
        student_data = {
            "total_files": 0,
            "completed_days": 0,
            "daily_submissions": {},
            "file_types": defaultdict(int),
            "total_lines": 0,
            "git_stats": {
                "total_commits": 0,
                "first_contribution": None,
                "latest_contribution": None,
                "commit_history": []
            },
            "detailed_daily_stats": {}
        }

        for day, files in student.submissions.items():
            day_number = ''.join(filter(str.isdigit, day))
            day_key = f"Day {day_number}"
            
            daily_stat = {
                "files": len(files),
                "file_details": [
                    {
                        "name": f["name"],
                        "lines": f["stats"]["lines"],
                        "code_lines": f["stats"]["code_lines"],
                        "comments": f["stats"]["comment_lines"],
                        "size": f["stats"]["size_bytes"],
                        "git_history": f["stats"]["git_history"],
                        "blame_info": f["stats"]["blame_info"],
                        "first_commit": f["first_commit"],
                        "latest_commit": f["latest_commit"]
                    } for f in files
                ],
                "total_lines": student.daily_stats[day]["total_lines"],
                "commits": student.daily_stats[day]["commits"],
                "first_submission": student.daily_stats[day]["first_submission"],
                "last_submission": student.daily_stats[day]["last_submission"]
            }
            
            student_data["detailed_daily_stats"][day_key] = daily_stat
            student_data["daily_submissions"][day_key] = len(files)
            student_data["total_lines"] += daily_stat["total_lines"]

        chart_data["student_progress"][student.full_name] = student_data

    # Save the enhanced chart data
    with open('chart_data.json', 'w', encoding='utf-8') as f:
        json.dump(chart_data, f, indent=2)

if __name__ == "__main__":
    generate_report()

