import os
from linter.config_validator import ConfigValidator
from linter.file_validator import FileValidator
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
    lookml_parser = LookMlProjectParser(filepaths)
    data = lookml_parser.parsed_lookml_files

    file_validator = FileValidator(lookml_parser.raw_files)
    files_are_valid = file_validator.validate()

    if data:
        # Run linter and print output
        linter = LookMlLinter(data, rules)
        linter.run()
        error_log = linter.get_errors()
        if not files_are_valid:
            error_log += file_validator.error_log() + '\n'

        # Save output to GHA environment variable
        with open(os.getenv('GITHUB_ENV'), 'a') as fh:
            error_log = error_log.replace('    ', '&nbsp;&nbsp;&nbsp;&nbsp;')
            fh.write("error_log<<EOF\n")
            fh.write(error_log)
            fh.write("EOF\n")
        
        # Save output to file, if enabled
        if save_output_to_file == 'true' or save_output_to_file == 'True':
            linter.save_errors(error_log, '_lookml-linter-output.txt')

        print(error_log)

        # Fail GitHub Action only if linter has errors (warnings do not count)
        assert linter.has_errors == False, 'LookML Linter detected an error.'
    elif filepaths:
        print('No .lkml files changed.')
    else:
        print('No .lkml files found in project.')

main()
