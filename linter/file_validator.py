from typing import Dict


class FileValidator:

    def __init__(self, raw_files: Dict) -> None:
        super().__init__()
        self.__raw_files = raw_files
        self.__errors = []

    def validate(self) -> bool:
        result = True
        for raw_file_path, raw_file_lines in self.__raw_files.items():
            if '.view.lkml' in raw_file_path or '.explore.lkml' in raw_file_path:
                valid = self.validate_comment_in_the_header(raw_file_lines)
                if not valid:
                    result = False
                    self.__errors.append(raw_file_path)
        return result

    @property
    def errors(self):
        return self.__errors

    def error_log(self):
        messages = []
        for er in self.errors:
            messages.append(f":information_source: File `{er}` has no comment on top with Team/Squad, Owned by and Created")
        return '\n'.join(messages)

    @staticmethod
    def validate_comment_in_the_header(raw_file_lines) -> bool:
        return len(raw_file_lines) >= 4 \
            and '###' in raw_file_lines[0] \
            and '# Squad/Team:' in raw_file_lines[1] \
            and '# Owned by:' in raw_file_lines[2] \
            and '# Created:' in raw_file_lines[3]