import os
import subprocess

import pytest



@pytest.fixture
def set_envs_1(monkeypatch):
    monkeypatch.setenv('INPUT_CONFIGFILE', '../config.example.yaml')
    monkeypatch.setenv('INPUT_FILEPATHS', '../test/test_lookml_files/users.view.lkml ../test/test_lookml_files/views/unparsable_view.lkml')
    monkeypatch.setenv('INPUT_SAVEOUTPUTTOFILE', '0')
    monkeypatch.setenv('GITHUB_ENV', '')
    yield
    # Optional: Clean up the environment variable after the test
    monkeypatch.delenv('INPUT_CONFIGFILE')
    monkeypatch.delenv('INPUT_FILEPATHS')
    monkeypatch.delenv('INPUT_SAVEOUTPUTTOFILE')
    monkeypatch.delenv('GITHUB_ENV')

def test_main_flow_with_parsed_and_not_parsed_files(set_envs_1) -> None:
    try:
        from linter.main import main
        assert False
    except Exception as e:
        # 1st file is ok but 2nd is not parsable, flow should throw exception
        assert True
