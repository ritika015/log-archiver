import os
import tarfile
import datetime
import sys  # Import sys to read command-line arguments

def compress_logs(log_directory, archive_directory, log_file):
    # Make sure the log folder exists
    if not os.path.exists(log_directory):
        print(f"Error: The folder '{log_directory}' does not exist.")
        return

    # Create the archive folder if it doesn't exist
    os.makedirs(archive_directory, exist_ok=True)

    # Create a filename with the current date & time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(archive_directory, archive_name)

    # Compress logs into a tar.gz file
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_directory, arcname="logs")

    print(f"Logs archived successfully: {archive_path}")

    # Log the archive details (date, time, filename)
    log_entry = f"{timestamp} - Archived: {archive_name}\n"

    # Save the log entry to archive_log.txt
    with open(log_file, "a") as log:
        log.write(log_entry)

# Check if the user provided a log folder as an argument
if len(sys.argv) < 2:
    print("Usage: python3 log_archive.py <log_directory>")
    sys.exit(1)  # Exit with an error code

log_directory = sys.argv[1]  # Get the log directory from command line
archive_directory = "archived_logs"  # Folder to store compressed logs
log_file = "archive_log.txt"  # Log file for tracking archives

compress_logs(log_directory, archive_directory, log_file)
