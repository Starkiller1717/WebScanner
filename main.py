import os
import subprocess

OUTPUT = "outputs"
REPORTS = "reports"

os.makedirs(OUTPUT, exist_ok=True)
os.makedirs(REPORTS, exist_ok=True)


def run(cmd, outfile):
    print(f"[+] Running: {cmd}")
    with open(outfile, "w") as f:
        subprocess.run(cmd, shell=True, stdout=f, stderr=f)


def recon(target):
    run(f"nmap -sV {target}", f"{OUTPUT}/nmap.txt")
    run(f"whois {target}", f"{OUTPUT}/whois.txt")
    run(f"dig {target}", f"{OUTPUT}/dig.txt")


def web(url):
    if url.strip() == "":
        return
    run(f"sqlmap -u \"{url}\" --batch", f"{OUTPUT}/sqlmap.txt")


def report(target):
    print("[+] Building report...")

    report_md = f"{REPORTS}/report.md"

    with open(report_md, "w") as f:
        f.write("# Automated Security Assessment Report\n\n")
        f.write(f"## Target: {target}\n\n")

        f.write("## Network Scan (Nmap)\n")
        f.write(open("outputs/nmap.txt").read())

        f.write("\n## Whois Information\n")
        f.write(open("outputs/whois.txt").read())

        f.write("\n## DNS Information\n")
        f.write(open("outputs/dig.txt").read())

        if os.path.exists("outputs/sqlmap.txt"):
            f.write("\n## Web Vulnerabilities (SQLmap)\n")
            f.write(open("outputs/sqlmap.txt").read())

    os.system("pandoc reports/report.md -o reports/report.pdf")


def main():
    print("=== OffSec Automation Framework ===\n")

    target = input("Target IP: ")
    url = input("Target URL (optional): ")

    recon(target)
    web(url)
    report(target)

    print("\n[+] Scan Complete")
    print("[+] Report saved to reports/report.pdf")


if __name__ == "__main__":
    main()
