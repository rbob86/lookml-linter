import pytest
from linter.lookml_project_parser import LookMlProjectParser


def test_get_parsed_lookml_files_method_returns_test_dict_parsed_files() -> None:
    LookMlProjectParser.root_file_path = "./test/test_lookml_files/"
    parser = LookMlProjectParser()

    assert len(parser.get_parsed_lookml_files()) == 3


def test_get_unparsable_lookml_files_method_returns_test_list_unparsed_files() -> None:
    LookMlProjectParser.root_file_path = "./test/test_lookml_files/"
    parser = LookMlProjectParser()

    assert len(parser.get_unparsable_lkml_files()) == 3


def test_lookmlprojectparser_raises_error_if_root_dir_does_not_exist() -> None:
    LookMlProjectParser.root_file_path = "./test/fake_dir/"
    with pytest.raises(IOError):
        LookMlProjectParser()
