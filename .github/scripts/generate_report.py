import os
import markdown
from datetime import datetime
import json
from collections import defaultdict
import subprocess
import glob
import re

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class Student:
    def __init__(self, full_name, github_username, file_prefixes):
        self.full_name = full_name
        self.github_username = github_username
        self.file_prefixes = file_prefixes
        self.submissions = defaultdict(list)
        self.activity_history = []
        
        # Get first and last name
        name_parts = full_name.split()
        first_name = name_parts[0].lower()
        last_name = name_parts[-1].lower()
        
        # Create more specific patterns to avoid conflicts
        self.file_prefixes.extend([
            f"{first_name}_{last_name[0]}",  # joe_m
            f"{first_name}.{last_name[0]}",  # joe.m
            f"{first_name[0]}_{last_name}",  # j_martin
            f"{first_name[0]}.{last_name}",  # j.martin
            f"{last_name}_{first_name[0]}",  # martin_j
            f"{last_name}.{first_name[0]}",  # martin.j
            f"{first_name}{last_name[0]}",   # joem
            f"{first_name[0]}{last_name}",   # jmartin
            f"{last_name}{first_name[0]}",   # martinj
            f"{first_name}_{last_name}",     # joe_martin
            f"{first_name}.{last_name}",     # joe.martin
            f"{last_name}_{first_name}",     # martin_joe
            f"{last_name}.{first_name}"      # martin.joe
        ])

def count_student_files(folder, student):
    files = []
    try:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                file_lower = file.lower()
                normalized_filename = file_lower.replace('_', '.').replace(' ', '.')
                
                # Get file name without extension for matching
                file_without_ext = os.path.splitext(normalized_filename)[0]
                
                # Check if any pattern matches exactly
                if any(
                    pattern == file_without_ext or  # Exact match
                    f"{pattern}." in normalized_filename or  # Pattern with separator
                    normalized_filename.startswith(f"{pattern}_") or  # Pattern at start
                    normalized_filename.startswith(f"{pattern}.")  # Pattern at start with dot
                    for pattern in student.file_prefixes
                ):
                    extension = os.path.splitext(file)[1].lower()
                    files.append({
                        "name": file,
                        "path": file_path,
                        "extension": extension,
                        "stats": analyze_file(file_path),
                        "git_history": get_file_git_history(file_path)
                    })
                    
    except Exception as e:
        print(f"Error processing folder {folder}: {e}")
    return files

def analyze_file(file_path):
    stats = {
        "lines": 0,
        "code_lines": 0,
        "comment_lines": 0,
        "functions": 0,
        "classes": 0,
        "size_bytes": os.path.getsize(file_path)
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            stats["lines"] = len(content.splitlines())
            stats["functions"] = len(re.findall(r'def \w+\s*\(', content))
            stats["classes"] = len(re.findall(r'class \w+\s*[:\(]', content))
            stats["comment_lines"] = len(re.findall(r'^\s*#.*$', content, re.MULTILINE))
            stats["code_lines"] = stats["lines"] - stats["comment_lines"]
    except Exception as e:
        print(f"Error analyzing file {file_path}: {e}")
    
    return stats

def get_file_git_history(file_path):
    try:
        git_log = subprocess.check_output([
            'git', 'log',
            '--follow',
            '--format=%H|%an|%ae|%at|%s',
            file_path
        ]).decode('utf-8').strip()
        
        commits = []
        for line in git_log.split('\n'):
            if line:
                hash, author, email, timestamp, message = line.split('|')
                commits.append({
                    "hash": hash,
                    "author": author,
                    "email": email,
                    "timestamp": int(timestamp),
                    "message": message
                })
        return commits
    except Exception as e:
        print(f"Error getting git history for {file_path}: {e}")
        return []

def process_daily_files(files):
    """Process files for a single day."""
    daily_stat = {
        "total_lines": 0,
        "code_lines": 0,
        "comment_lines": 0,
        "functions": 0,
        "classes": 0,
        "files": len(files),
        "file_details": []
    }
    
    for file in files:
        stats = file["stats"]
        daily_stat["total_lines"] += stats["lines"]
        daily_stat["code_lines"] += stats["code_lines"]
        daily_stat["comment_lines"] += stats["comment_lines"]
        daily_stat["functions"] += stats["functions"]
        daily_stat["classes"] += stats["classes"]
        
        daily_stat["file_details"].append({
            "name": file["name"],
            "path": file["path"],
            "extension": file["extension"],
            "lines": stats["lines"],
            "code_lines": stats["code_lines"],
            "comment_lines": stats["comment_lines"],
            "functions": stats["functions"],
            "classes": stats["classes"],
            "size": stats["size_bytes"]
        })
    
    return daily_stat

def save_chart_data(chart_data):
    try:
        with open('chart_data.json', 'w', encoding='utf-8') as f:
            json.dump(chart_data, f, indent=2, cls=DateTimeEncoder)
    except Exception as e:
        print(f"Error saving chart data: {e}")
        raise

def generate_markdown_report(chart_data):
    report = [
        "# Python 30-Day Project Progress Report\n",
        f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n",
        "## Overall Progress\n"
    ]
    
    with open('Progress_Report.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

def generate_report():
    students = [
        Student("Joe Martin", "JoeMartinRince", ["joe_m", "joe.m", "martin"]),
        Student("Joe George", "joegeorge022", ["joe_g", "joeg", "george"]),
        Student("Ganesh Chandran", "Ganesh-Chandran005", ["ganesh", "chandran"]),
        Student("Job Thomas", "Jobthomas10", ["job", "thomas", "job_t"]),
        Student("Indhu Subash", "IndhuSubash-2007", ["indhu", "subash"])
    ]

    day_folders = [d for d in os.listdir('.') if os.path.isdir(d) and d.lower().startswith('day')]
    day_folders.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    chart_data = {
        "daily_submissions": defaultdict(int),
        "student_progress": {},
        "completion_rates": {},
        "language_distribution": defaultdict(int),
        "repository_activity": {
            "activity_timeline": defaultdict(int),
            "contribution_history": defaultdict(lambda: defaultdict(int))
        }
    }

    print("Processing students:")
    for student in students:
        print(f"\nStudent: {student.full_name}")
        print(f"GitHub username: {student.github_username}")
        print(f"File prefixes: {student.file_prefixes}")
        
        student_data = {
            "total_files": 0,
            "completed_days": 0,
            "daily_submissions": {},
            "file_types": defaultdict(int),
            "total_lines": 0,
            "detailed_daily_stats": {}
        }

        for folder in day_folders:
            files = count_student_files(folder, student)
            if files:
                print(f"Found files in {folder}: {[f['name'] for f in files]}")
                day_number = ''.join(filter(str.isdigit, folder))
                day_key = f"Day {day_number}"
                student_data["total_files"] += len(files)
                student_data["completed_days"] += 1
                student_data["daily_submissions"][day_key] = len(files)
                chart_data["daily_submissions"][day_key] += len(files)
                daily_stat = process_daily_files(files)
                student_data["detailed_daily_stats"][day_key] = daily_stat
                student_data["total_lines"] += daily_stat["total_lines"]
                
                for file in files:
                    student_data["file_types"][file["extension"]] += 1
                    chart_data["language_distribution"][file["extension"]] += 1

        completion_rate = (student_data["completed_days"] / len(day_folders)) * 100
        chart_data["completion_rates"][student.full_name] = completion_rate
        chart_data["student_progress"][student.full_name] = student_data
        print(f"Completion rate for {student.full_name}: {completion_rate}%")

    print("\nFinal chart data:")
    print(f"Students in progress data: {list(chart_data['student_progress'].keys())}")
    print(f"Students in completion rates: {list(chart_data['completion_rates'].keys())}")

    save_chart_data(chart_data)
    generate_markdown_report(chart_data)

if __name__ == "__main__":
    generate_report()
