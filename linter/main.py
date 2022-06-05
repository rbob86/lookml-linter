import os
from linter.config_validator import ConfigValidator
from linter.lookml_linter import LookMlLinter
from linter.lookml_project_parser import LookMlProjectParser
from linter.rules_engine import RulesEngine


def main():
    config_file = os.environ['INPUT_CONFIGFILE']
    #path = os.environ['INPUT_LOOKMLPROJECT']

    validator = ConfigValidator(config_file)
    validator.validate()
    config = validator.config
    rules = RulesEngine(config).rules
    #LookMlProjectParser.root_file_path = path
    data = LookMlProjectParser().get_parsed_lookml_files()
    linter = LookMlLinter(data, rules)
    linter.run()
    linter.print_errors()
    assert linter.has_errors == False, 'LookML Linter detected an error warning, please resolve any error warning to complete Pull Request'


main()
