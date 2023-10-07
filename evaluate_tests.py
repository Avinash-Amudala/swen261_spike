import os
import zipfile
import subprocess
import shutil

# Directory to store the unzipped projects
TEMP_DIR = "/Users/avinashamudala/Downloads/spikeassgn"

# Results file and debug file
RESULTS_FILE = "test_results.txt"
DEBUG_FILE = "debug_output.txt"

# Ensure the directory exists
if not os.path.exists(TEMP_DIR):
    print(f"The directory {TEMP_DIR} does not exist.")
    exit(1)

# Clear previous results and debug output
with open(RESULTS_FILE, 'w') as f:
    f.write("")

with open(DEBUG_FILE, 'w') as f:
    f.write("")

results_list = []

# Iterate over each zip file in the TEMP_DIR directory
for zip_file in os.listdir(TEMP_DIR):
    if zip_file.endswith(".zip"):
        zip_path = os.path.join(TEMP_DIR, zip_file)
        last_name, first_name = zip_file.split(" ")[3:5]
        student_info = f"{last_name}, {first_name}"

        # Create a temporary directory for the current project
        project_dir = os.path.join(TEMP_DIR, student_info)
        if os.path.exists(project_dir):
            shutil.rmtree(project_dir)
        os.makedirs(project_dir)

        # Unzip the project into the temporary directory
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(project_dir)

        # Run mvn test and capture the output, excluding the failing test
        try:
            test_output = subprocess.check_output(
                ['mvn', 'test', '-Dtest=!HeroControllerTest#testCreateHeroFailed'],
                cwd=project_dir,
                stderr=subprocess.STDOUT,
                text=True
            )
        except subprocess.CalledProcessError as e:
            test_output = e.output

        if "BUILD SUCCESS" in test_output:
            result = "SUCCESS"
        else:
            failed_tests = [line.split("  ")[-1] for line in test_output.split("\n") if line.startswith("[ERROR]   ")]
            if failed_tests:
                failed_tests_str = ", ".join(failed_tests)
                result = f"FAILED (Failed Tests: {failed_tests_str})"
            else:
                result = "FAILED"

        # Append the result to a list to be sorted later
        results_list.append((student_info, result))

# Sort results by last name and write to file
sorted_results = sorted(results_list, key=lambda x: x[0].split(",")[0])
with open(RESULTS_FILE, 'w') as f:
    for student, result in sorted_results:
        f.write(f"{student}: {result}\n")

# Print the sorted results
with open(RESULTS_FILE, 'r') as f:
    print(f.read())
