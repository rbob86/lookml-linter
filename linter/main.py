import os
from linter.config_validator import ConfigValidator
from linter.lookml_linter import LookMlLinter
from linter.lookml_project_parser import LookMlProjectParser
from linter.rules_engine import RulesEngine


def main():
    # Read in input variables
    config_file = os.environ['INPUT_CONFIGFILE']
    filepaths = os.environ['INPUT_FILEPATHS']
    filepaths = filepaths.split(' ') if filepaths != None else None
    save_output_to_file = os.environ['INPUT_SAVEOUTPUTTOFILE']

    # Validate config.yaml file
    validator = ConfigValidator(config_file)
    validator.validate()

    # Retrieve rules from config and data from LookML files
    rules = RulesEngine(validator.config).rules
    data = LookMlProjectParser(filepaths).get_parsed_lookml_files()

    if data:
        # Run linter and print output
        linter = LookMlLinter(data, rules)
        linter.run()
        error_log = linter.get_errors()
        print(error_log)

        # Save output to file, if enabled
        if save_output_to_file == 'true' or save_output_to_file == 'True':
            linter.save_errors(error_log, '_lookml-linter-output.txt')

        # Fail GitHub Action only if linter has errors (warnings do not count)
        assert linter.has_errors == False, 'LookML Linter detected an error.'
    elif filepaths:
        print('No .lkml files changed.')
    else:
        print('No .lkml files found in project.')

main()
