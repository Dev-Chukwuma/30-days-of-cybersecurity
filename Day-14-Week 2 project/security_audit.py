import subprocess


def get_current_user():
    result = subprocess.run(["whoami"], capture_output=True, text=True)
    return result.stdout


def get_running_processes():
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    return result.stdout


def get_active_services():
    result = subprocess.run(
        ["systemctl", "list-units", "--type=service"],
        capture_output=True,
        text=True
    )
    return result.stdout


def get_recent_errors():
    result = subprocess.run(
        ["journalctl", "-p", "err", "-b"],
        capture_output=True,
        text=True
    )
    return result.stdout


def generate_report():
    report = ""
    
    report += "===== CURRENT USER =====\n"
    report += get_current_user() + "\n"
    
    report += "===== RUNNING PROCESSES =====\n"
    report += get_running_processes() + "\n"
    
    report += "===== ACTIVE SERVICES =====\n"
    report += get_active_services() + "\n"
    
    report += "===== RECENT ERRORS =====\n"
    report += get_recent_errors() + "\n"
    
    return report


def save_report(report):
    filename = "security_audit_report.txt"
    
    with open(filename, "w") as f:
        f.write(report)
    
    print(f"Report saved to {filename}")


def main():
    print("Running Linux Security Audit...\n")
    report = generate_report()
    save_report(report)
    print("Audit complete.")


if __name__ == "__main__":
    main()
