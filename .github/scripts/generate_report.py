import os
import markdown
from datetime import datetime
import json
from collections import defaultdict
import subprocess
import glob
import re

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

def get_workflow_runs():
    """Get GitHub Actions workflow run history."""
    try:
        workflow_logs = []
        log_files = glob.glob('.github/workflows/logs/*.json')
        for log_file in log_files:
            with open(log_file, 'r') as f:
                workflow_logs.append(json.load(f))
        return workflow_logs
    except Exception as e:
        print(f"Error reading workflow logs: {e}")
        return []

def count_student_files(folder, student):
    """Count files for a specific student in a given folder."""
    files = []
    try:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                file_lower = file.lower()
                if any(prefix in file_lower for prefix in student.file_prefixes):
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

def get_file_git_history(file_path):
    """Get git history for a specific file."""
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

def analyze_file(file_path):
    """Analyze a single file for detailed statistics."""
    stats = {
        "lines": 0,
        "code_lines": 0,
        "comment_lines": 0,
        "blank_lines": 0,
        "functions": 0,
        "classes": 0,
        "size_bytes": os.path.getsize(file_path),
        "last_modified": datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            in_multiline_comment = False
            for line in f:
                stats["lines"] += 1
                stripped = line.strip()
                
                if not stripped:
                    stats["blank_lines"] += 1
                    continue
                
                if stripped.startswith('"""') or stripped.startswith("'''"):
                    in_multiline_comment = not in_multiline_comment
                    stats["comment_lines"] += 1
                    continue
                
                if in_multiline_comment:
                    stats["comment_lines"] += 1
                    continue
                
                if stripped.startswith('#'):
                    stats["comment_lines"] += 1
                    continue
                
                if stripped.startswith('def '):
                    stats["functions"] += 1
                elif stripped.startswith('class '):
                    stats["classes"] += 1
                
                stats["code_lines"] += 1
                
    except Exception as e:
        print(f"Error analyzing file {file_path}: {e}")
    
    return stats

def save_historical_data(chart_data):
    """Save current data as historical record."""
    try:
        os.makedirs('.github/historical_data', exist_ok=True)
        
        date_str = datetime.now().strftime('%Y-%m-%d')
        file_path = f'.github/historical_data/data_{date_str}.json'
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(chart_data, f, indent=2)

        with open('chart_data.json', 'w', encoding='utf-8') as f:
            json.dump(chart_data, f, indent=2)

    except Exception as e:
        print(f"Error saving historical data: {e}")

def process_daily_files(files):
    """Process files for a specific day."""
    daily_stat = {
        "files": len(files),
        "total_lines": 0,
        "code_lines": 0,
        "comment_lines": 0,
        "functions": 0,
        "classes": 0,
        "file_details": [],
        "submission_time": None
    }

    for file in files:
        stats = file["stats"]
        daily_stat["file_details"].append({
            "name": file["name"],
            "lines": stats["lines"],
            "code_lines": stats["code_lines"],
            "comments": stats["comment_lines"],
            "functions": stats["functions"],
            "classes": stats["classes"],
            "size": stats["size_bytes"],
            "git_history": file["git_history"]
        })
        
        daily_stat["total_lines"] += stats["lines"]
        daily_stat["code_lines"] += stats["code_lines"]
        daily_stat["comment_lines"] += stats["comment_lines"]
        daily_stat["functions"] += stats["functions"]
        daily_stat["classes"] += stats["classes"]

        if file["git_history"]:
            latest_commit = max(commit["timestamp"] for commit in file["git_history"])
            latest_commit = datetime.fromtimestamp(latest_commit)
            if not daily_stat["submission_time"] or latest_commit > daily_stat["submission_time"]:
                daily_stat["submission_time"] = latest_commit

    return daily_stat

def generate_markdown_report(chart_data):
    """Generate a markdown progress report."""
    report = [
        "# Python 30-Day Project Progress Report\n",
        f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n",
        "## Overall Progress\n",
        "### Test Update - Checking Workflow\n"
    ]

    total_submissions = sum(chart_data["daily_submissions"].values())
    avg_completion = sum(chart_data["completion_rates"].values()) / len(chart_data["completion_rates"])
    
    report.extend([
        f"- Total Submissions: {total_submissions}",
        f"- Average Completion Rate: {avg_completion:.2f}%",
        f"- Active Students: {len(chart_data['student_progress'])}",
        f"- Total Days: {len(chart_data['daily_submissions'])}\n\n"
    ])

    report.append("## Individual Progress\n")
    for student_name, progress in chart_data["student_progress"].items():
        report.extend([
            f"### {student_name}\n",
            f"- Files Submitted: {progress['total_files']}",
            f"- Days Completed: {progress['completed_days']}",
            f"- Completion Rate: {chart_data['completion_rates'][student_name]:.2f}%",
            f"- Total Lines of Code: {progress['total_lines']}",
            "#### Code Quality Metrics",
            f"- Comments Ratio: {progress['code_quality']['comments_ratio']:.2f}%",
            f"- Functions: {progress['code_quality']['functions_count']}",
            f"- Classes: {progress['code_quality']['classes_count']}\n",
            "#### File Types",
        ])
        
        for ext, count in progress["file_types"].items():
            report.append(f"- {ext}: {count}")
        report.append("\n")

    with open('Progress_Report.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

def generate_report_index():
    """Generate an index of all historical reports."""
    reports_dir = '.github/reports'
    reports = sorted(glob.glob(f'{reports_dir}/Progress_Report_*.md'), reverse=True)
    
    index = [
        "# Progress Report History\n",
        "*Click on a report to view its contents*\n\n"
    ]
    
    for report in reports:
        filename = os.path.basename(report)
        timestamp = filename.replace('Progress_Report_', '').replace('.md', '')
        date = datetime.strptime(timestamp, '%Y%m%d_%H%M%S').strftime('%Y-%m-%d %H:%M:%S')
        index.append(f"- [{date}]({report})")
    
    with open(f'{reports_dir}/index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(index))

def analyze_code_quality(file_path):
    """Enhanced code analysis with advanced metrics."""
    stats = {
        "lines": 0,
        "code_lines": 0,
        "comment_lines": 0,
        "functions": 0,
        "classes": 0,
        "complexity": 0,
        "code_to_comment_ratio": 0,
        "avg_function_length": 0,
        "test_coverage": 0,
        "best_practices_score": 0
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            stats["complexity"] = content.count('if ') + content.count('while ') + content.count('for ')
            
            functions = re.findall(r'def \w+\([^)]*\):', content)
            if functions:
                total_length = sum(len(re.findall(r'\n\s+[^\n]+', func)) for func in functions)
                stats["avg_function_length"] = total_length / len(functions)
            

            stats["best_practices_score"] = (
                (content.count('try:') * 2) +  
                (content.count('def test_') * 3) + 
                (content.count('"""') * 2) +  
                (content.count('logging.') * 2)  
            )
            
    except Exception as e:
        print(f"Error in advanced analysis: {e}")
    
    return stats

def analyze_competitive_edge(student_data):
    """Calculate competitive advantages."""
    edge_metrics = {
        "code_efficiency": calculate_code_efficiency(student_data),
        "learning_curve": analyze_learning_progression(student_data),
        "innovation_score": measure_code_innovation(student_data),
        "consistency_rating": evaluate_submission_consistency(student_data)
    }
    return edge_metrics

def calculate_code_efficiency(data):
    """Measure code efficiency based on complexity vs functionality."""
    return {
        "algorithmic_efficiency": data["code_quality"]["complexity"] / max(data["total_lines"], 1),
        "function_density": data["code_quality"]["functions_count"] / max(data["total_lines"], 1),
        "maintainability_index": calculate_maintainability(data)
    }

def analyze_learning_progression(data):
    """Track improvement over time."""
    daily_stats = data["detailed_daily_stats"]
    progression = []
    
    for day, stats in sorted(daily_stats.items()):
        quality_score = (
            stats["functions"] * 2 +
            stats["comment_lines"] / max(stats["total_lines"], 1) * 100 +
            stats.get("best_practices_score", 0)
        )
        progression.append(quality_score)
    
    return {
        "growth_rate": calculate_growth_rate(progression),
        "consistency": calculate_consistency(progression),
        "trend": analyze_trend(progression)
    }

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
                "comment_lines": 0,  
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
                student_data["code_quality"]["comment_lines"] += daily_stat["comment_lines"]
                
                for file in files:
                    student_data["file_types"][file["extension"]] += 1
                    chart_data["language_distribution"][file["extension"]] += 1

        completion_rate = (student_data["completed_days"] / len(day_folders)) * 100
        if student_data["total_lines"] > 0:
            comments_ratio = (student_data["code_quality"]["comment_lines"] / 
                            student_data["total_lines"]) * 100
            student_data["code_quality"]["comments_ratio"] = comments_ratio

        chart_data["completion_rates"][student.full_name] = completion_rate
        chart_data["student_progress"][student.full_name] = student_data

    save_historical_data(chart_data)
    
    generate_markdown_report(chart_data)

if __name__ == "__main__":
    generate_report()
