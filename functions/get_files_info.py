from os.path import abspath, join, normpath, commonpath, isdir, getsize
from os import listdir


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = abspath(working_directory)
        target_dir = normpath(join(working_dir_abs, directory))
        valid_target_dir = commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        record = []
        for content in listdir(target_dir):
            current_target = normpath(join(target_dir, content))
            record.append(
                f"- {content}: file_size={getsize(current_target)} bytes, is_dir={isdir(current_target)}"
            )
        return "\n".join(record)
    except Exception as e:
        return f"Error: {str(e)}"
