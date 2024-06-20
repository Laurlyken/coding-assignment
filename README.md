# Text File Scanner

This project provides a Python script and GitHub Actions workflow for scanning text files in a specified directory for lines matching a given regular expression.

## Python Script

The `script.py` file contains a Python script that:

1. Takes two command-line arguments:
   - A full path to a directory
   - A regular expression pattern
2. Scans all `.txt` files in the specified directory
3. Outputs the filename and line number of the first line in each file that matches the regular expression

## GitHub Actions Workflow

The `.github/workflows/scan_files.yml` file defines a GitHub Actions workflow that:

1. Runs on pushes to the main branch or can be manually triggered
2. Sets up a Python environment
3. Creates a test directory with sample text files
4. Runs the scanning script
5. Displays the results directly in the GitHub Actions console output

### Manual Trigger

You can manually trigger the workflow from the Actions tab in the GitHub repository. When doing so, you can specify:

- The directory to scan (default: './test_directory')
- The regular expression to use (default: 'example.*pattern')

## Setup

1. Clone this repository
2. Ensure `script.py` is in the root directory
3. Create the `.github/workflows` directory if it doesn't exist
4. Place the `scan_files.yml` workflow file in the `.github/workflows` directory
5. Push these changes to your GitHub repository

## Viewing Results

After the workflow runs (either automatically on push or manually triggered):

1. Go to the Actions tab in your GitHub repository
2. Click on the specific workflow run
3. In the workflow run summary, expand the "Run scanner script" step
4. The scan results will be visible directly in the log

## Customization

We can modify the `script.py` file to change how files are scanned or results are reported.
