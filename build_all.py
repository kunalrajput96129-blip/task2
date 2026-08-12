import os
import subprocess
import sys

def run_step(description, command):
    print(f"\n==================================================")
    print(f"  {description}")
    print(f"==================================================")
    res = subprocess.run([sys.executable] + command, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    if res.returncode != 0:
        print(f"ERROR: Step failed - {description}!")
        sys.exit(res.returncode)
    print(f"SUCCESS: {description} completed successfully.")

if __name__ == "__main__":
    base_dir = r"c:\Users\Vicky\OneDrive\Desktop\task2"
    os.chdir(base_dir)

    print("STARTING WEEK 2 PROTOTYPE & DOCUMENTATION BUILD PROCESS")

    # Step 1: Generate Visual Wireframe Diagrams
    run_step("1. Generating Visual Wireframes & Diagrams", ["generate_visual_wireframes.py"])

    # Step 2: Generate Word Document (.docx)
    run_step("2. Compiling Digital_Services_Portal_Design_Doc.docx", ["generate_doc_report.py"])

    print("\n==================================================")
    print("  ALL WEEK 2 DELIVERABLES SUCCESSFULLY CREATED!")
    print("==================================================")
    print("Deliverables Summary:")
    print("1. DOC Documentation File: c:\\Users\\Vicky\\OneDrive\\Desktop\\task2\\Digital_Services_Portal_Design_Doc.docx")
    print("2. Visual Wireframe Assets: c:\\Users\\Vicky\\OneDrive\\Desktop\\task2\\assets\\ (5 PNG files)")
    print("3. Web Prototype Files:    c:\\Users\\Vicky\\OneDrive\\Desktop\\task2\\prototype\\ (index.html, styles.css, app.js)")
