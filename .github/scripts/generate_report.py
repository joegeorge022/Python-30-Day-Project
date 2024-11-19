import os
import json
import markdown
from datetime import datetime
from collections import defaultdict

# Define Student class first
class Student:
    def __init__(self, full_name, github_username, file_prefixes):
        self.full_name = full_name
        self.github_username = github_username
        self.file_prefixes = file_prefixes
        self.submissions = defaultdict(list)

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

    # Get all Day folders
    day_folders = [d for d in os.listdir('.') if os.path.isdir(d) and d.lower().startswith('day')]
    day_folders.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Initialize chart data
    chart_data = {
        "daily_submissions": defaultdict(int),
        "student_progress": {},
        "completion_rates": {},
        "language_distribution": defaultdict(int)
    }

    # Process each student
    for student in students:
        student_data = process_student_data(student, day_folders)
        completion_rate = (student_data["completed_days"] / len(day_folders)) * 100
        chart_data["completion_rates"][student.full_name] = completion_rate
        chart_data["student_progress"][student.full_name] = student_data

    # Save the chart data
    with open('chart_data.json', 'w', encoding='utf-8') as f:
        json.dump(chart_data, f, indent=2)

def process_student_data(student, day_folders):
    """Process data for a single student."""
    student_data = {
        "total_files": 0,
        "completed_days": 0,
        "daily_submissions": {},
        "file_types": defaultdict(int),
        "total_lines": 0,
        "detailed_daily_stats": {}
    }

    for folder in day_folders:
        files = get_student_files(folder, student)
        if files:
            day_number = ''.join(filter(str.isdigit, folder))
            day_key = f"Day {day_number}"
            
            student_data["total_files"] += len(files)
            student_data["completed_days"] += 1
            student_data["daily_submissions"][day_key] = len(files)
            
            daily_stats = analyze_files(files)
            student_data["detailed_daily_stats"][day_key] = daily_stats
            student_data["total_lines"] += daily_stats["total_lines"]
            
            for ext in daily_stats["file_types"]:
                student_data["file_types"][ext] += 1

    return student_data

def get_student_files(directory, student):
    """Get files for a specific student in a directory."""
    try:
        files = []
        for f in os.listdir(directory):
            file_path = os.path.join(directory, f)
            if not os.path.isfile(file_path):
                continue
            
            lower_filename = f.lower()
            if any(lower_filename.startswith(prefix.lower()) for prefix in student.file_prefixes):
                files.append({
                    "name": f,
                    "path": file_path,
                    "extension": os.path.splitext(f)[1].lower()
                })
        return files
    except FileNotFoundError:
        return []

def analyze_files(files):
    """Analyze a list of files."""
    stats = {
        "files": len(files),
        "file_details": [],
        "total_lines": 0,
        "file_types": defaultdict(int)
    }

    for file in files:
        file_stats = analyze_single_file(file["path"])
        stats["file_details"].append({
            "name": file["name"],
            "lines": file_stats["lines"],
            "code_lines": file_stats["code_lines"],
            "comments": file_stats["comment_lines"],
            "size": file_stats["size_bytes"]
        })
        stats["total_lines"] += file_stats["lines"]
        stats["file_types"][file["extension"]] += 1

    return stats

def analyze_single_file(file_path):
    """Analyze a single file."""
    stats = {
        "lines": 0,
        "code_lines": 0,
        "comment_lines": 0,
        "blank_lines": 0,
        "size_bytes": os.path.getsize(file_path)
    }

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stats["lines"] += 1
                stripped = line.strip()
                if not stripped:
                    stats["blank_lines"] += 1
                elif stripped.startswith(('#', '//', '/*', '*', '"""', "'''")):
                    stats["comment_lines"] += 1
                else:
                    stats["code_lines"] += 1
    except Exception as e:
        print(f"Error analyzing file {file_path}: {e}")

    return stats

if __name__ == "__main__":
    generate_report()
