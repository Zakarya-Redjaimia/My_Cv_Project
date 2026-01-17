import os

def prevent_file_deletion(file_path):
    # Get the current file permissions
    current_permissions = os.stat(file_path).st_mode

    # Set the read-only permission
    new_permissions = current_permissions & ~0o222

    # Update the file permissions
    os.chmod(file_path, new_permissions)

# Example usage
file_path = input('Enter PAth: ')
prevent_file_deletion(file_path)