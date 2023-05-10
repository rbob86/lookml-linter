import pytest

from linter.file_validator import FileValidator
from linter.lookml_project_parser import LookMlProjectParser


def test_file_header_validation() -> None:
    LookMlProjectParser.root_file_path = './test/test_lookml_files/'
    parser = LookMlProjectParser()
    assert len(parser.parsed_lookml_files) == 3

    file_validator = FileValidator(parser.raw_files)
    assert False == file_validator.validate()
    assert len(file_validator.errors) == 1
