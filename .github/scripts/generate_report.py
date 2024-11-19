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

    # Initialize chart data
    chart_data = {
        "daily_submissions": defaultdict(int),
        "student_progress": {},
        "completion_rates": {},
        "language_distribution": defaultdict(int)
    }

    # Collect statistics for each student
    for student in students:
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
            day_number = ''.join(filter(str.isdigit, folder))
            day_key = f"Day {day_number}"

            if files:
                student.submissions[folder] = files
                student_data["total_files"] += len(files)
                student_data["completed_days"] += 1
                student_data["daily_submissions"][day_key] = len(files)
                chart_data["daily_submissions"][day_key] += len(files)

                # Collect detailed statistics
                daily_stat = {
                    "files": len(files),
                    "file_details": [],
                    "total_lines": 0,
                    "submission_time": None
                }

                for file in files:
                    daily_stat["file_details"].append({
                        "name": file["name"],
                        "lines": file["stats"]["lines"],
                        "code_lines": file["stats"]["code_lines"],
                        "comments": file["stats"]["comment_lines"],
                        "size": file["stats"]["size_bytes"]
                    })
                    daily_stat["total_lines"] += file["stats"]["lines"]
                    student_data["total_lines"] += file["stats"]["lines"]
                    student_data["file_types"][file["extension"]] += 1
                    chart_data["language_distribution"][file["extension"]] += 1

                student_data["detailed_daily_stats"][day_key] = daily_stat

        # Calculate completion rate
        completion_rate = (student_data["completed_days"] / len(day_folders)) * 100
        chart_data["completion_rates"][student.full_name] = completion_rate
        chart_data["student_progress"][student.full_name] = student_data

    # Save the chart data
    with open('chart_data.json', 'w', encoding='utf-8') as f:
        json.dump(chart_data, f, indent=2)

if __name__ == "__main__":
    generate_report()
