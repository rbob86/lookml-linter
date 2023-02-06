import pytest
from jsonschema.exceptions import ValidationError
from linter.config_validator import ConfigValidator


def test_init_raises_error_if_no_file_specified() -> None:
    with pytest.raises(FileNotFoundError):
        ConfigValidator('')


def test_init_raises_error_if_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        ConfigValidator('nonexistent-file.yml')


def test_validate_raises_error_if_invalid_rules() -> None:
    filename = 'test/test_config_files/invalid-rule.config.yaml'
    validator = ConfigValidator(filename)
    with pytest.raises(ValidationError):
        validator.validate()


def test_validate_raises_error_if_invalid_severity() -> None:
    filename = 'test/test_config_files/invalid-severity.config.yaml'
    validator = ConfigValidator(filename)
    with pytest.raises(ValidationError):
        validator.validate()


def test_validate_raises_error_if_severity_not_specified() -> None:
    filename = 'test/test_config_files/invalid-severity.config.yaml'
    validator = ConfigValidator(filename)
    with pytest.raises(ValidationError):
        validator.validate()


def test_validate_succeeds_if_some_rules_present() -> None:
    filename = 'test/test_config_files/valid-some-rules.config.yaml'
    ConfigValidator(filename).validate()


def test_validate_succeeds_if_all_rules_present() -> None:
    filename = 'test/test_config_files/valid-all-rules.config.yaml'
    ConfigValidator(filename).validate()


def test_validate_succeeds_if_extra_arbitrary_properties() -> None:
    filename = 'test/test_config_files/valid-extra-properties.config.yaml'
    ConfigValidator(filename).validate()
