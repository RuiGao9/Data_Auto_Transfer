import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

def is_recent(file_path, days):
    """Check if file is modified within N days."""
    file_mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
    return datetime.now() - file_mod_time <= timedelta(days=days)

def generate_unique_filename(dest_folder, filename):
    """Generate a unique filename if one already exists."""
    base, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename
    while os.path.exists(os.path.join(dest_folder, new_name)):
        new_name = f"{base}_copy{counter}{ext}"
        counter += 1
    return new_name

def transfer_recent_files(source_dir, dest_dir, days):
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    if not dest_path.exists():
        dest_path.mkdir(parents=True, exist_ok=True)

    count = 0
    for file_path in source_path.rglob('*'):
        if file_path.is_file() and is_recent(file_path, days):
            dest_file_name = generate_unique_filename(dest_path, file_path.name)
            shutil.copy2(file_path, dest_path / dest_file_name)
            count += 1

    print(f"✅ {count} file(s) transferred to: {dest_path}")
