import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

def is_recent(file_path, cutoff_time):
    """Check if file was modified after the cutoff time."""
    file_mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
    return file_mod_time >= cutoff_time

def generate_unique_filename(dest_folder, filename):
    """Generate a unique filename if one already exists in the destination."""
    base, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename
    while os.path.exists(os.path.join(dest_folder, new_name)):
        new_name = f"{base}_copy{counter}{ext}"
        counter += 1
    return new_name

def transfer_recent_files(source_dir, dest_dir, days):
    # Get the current time and calculate the cutoff time
    current_time = datetime.now()
    cutoff_time = current_time - timedelta(days=days)

    print("===================================")
    print(f"Current Time:      {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Extracting files modified since: {cutoff_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("===================================")

    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    if not dest_path.exists():
        dest_path.mkdir(parents=True, exist_ok=True)

    count = 0
    for file_path in source_path.rglob('*'):
        if file_path.is_file() and is_recent(file_path, cutoff_time):
            dest_file_name = generate_unique_filename(dest_path, file_path.name)
            shutil.copy2(file_path, dest_path / dest_file_name)
            count += 1
    print("\nFinished transferring files!!!")
    print(f"{count} file(s) transferred to: {dest_path}")
