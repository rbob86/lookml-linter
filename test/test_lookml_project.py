import pytest
from linter.lookml_file_parser import LookMlFilesParser

def  test_lookml_project_method_returns_test_lookml_files_dict() -> None:
    LookMlFilesParser.root_file_path = "./test/test_lookml_files/"
    parsed_lookml_files = LookMlFilesParser()
    assert len(parsed_lookml_files.get_lookml_project()) == 3
