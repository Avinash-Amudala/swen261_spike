# Automated Grading Script for Heroes API Spike Test

Hello everyone! This repository contains a Python script designed to automate the grading process for the Heroes API spike tests.

## :warning: Important Update regarding `HeroControllerTest#testCreateHeroFailed`

While grading, an important observation was made regarding the spike assignment on Heroes API. There appears to be a consistent test failure across multiple student submissions, specifically tied to the `HeroControllerTest#testCreateHeroFailed` test case. Given the widespread nature of this failure, it's believed that there might be an issue with the test case itself or potentially some ambiguity in the assignment specifications.

### Key Points:
- The test is designed to check if hero creation fails under specific conditions.
- This failure is prevalent in submissions across different sections.
- It could potentially impact the grades of numerous students.

### Recommendations:
1. **Reviewing the Test Case**: Before finalizing grades, please double-check the `HeroControllerTest#testCreateHeroFailed` test case.
2. **Adjusting Grading**: Consider adjusting the grading criteria for this specific test, to ensure fairness.
3. **Student Communication**: Inform students in your respective sections about this issue to alleviate concerns about this particular test failure.

## Usage of the Script

This Python script automates the grading process for the Heroes API spike tests, considering the specific test anomaly mentioned earlier. The script will unzip and test each student's project, excluding the `HeroControllerTest#testCreateHeroFailed` test, and then compile the results.

### Prerequisites:
1. Ensure you have `Python` installed on your machine.
2. Ensure you have `Maven` (`mvn`) installed as the script utilizes it for testing.
3. The script assumes that students' projects are submitted as `.zip` files with a specific naming convention (last name and first name present in the file name).

### Instructions:

1. **Setting up the Directory**:
    - Place the script in a directory of your choice.
    - Modify the `TEMP_DIR` variable in the script to point to the directory where you've stored the students' `.zip` files. 

    ```python
    TEMP_DIR = "/path/to/your/directory"
    ```

2. **Running the Script**:
    - Open a terminal or command prompt.
    - Navigate to the directory containing the script.
    - Execute the script by running:

    ```bash
    python evaluate_tests.py
    ```

    Replace `evaluate_tests.py` with the actual name of the Python script if you've renamed it.

3. **Interpreting Results**:
    - After the script finishes execution, a `test_results.txt` file will be created in the same directory. This file contains the grading results for each student.
    - In case of any debug information or errors, refer to the `debug_output.txt` file.

4. **Cleaning Up**:
    - The script creates a temporary directory for each student's project within the `TEMP_DIR`. You can safely remove these directories after reviewing the results, if desired.

