from os.path import abspath, normpath, join, commonpath, isfile
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = abspath(working_directory)
        target_file = normpath(join(working_dir_abs, file_path))
        valid_target_file = (
            commonpath([working_dir_abs, target_file]) == working_dir_abs
        )

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return content

    except Exception as e:
        return f"Error: {str(e)}"
