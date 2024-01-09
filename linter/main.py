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
    parsed_lookml_files = lookml_parser.parsed_lookml_files

    file_validator = FileValidator(lookml_parser.raw_files)
    files_are_valid = file_validator.validate()

    output = ''
    outcome_fail = False
    if not lookml_parser.lkml_filepaths:
        if filepaths:
            output = f'No .lkml files found in paths: {filepaths}'
            outcome_fail = True
        else:
            output = 'No .lkml files found in project.'
    else:
        if parsed_lookml_files:
            # Run linter and print output
            linter = LookMlLinter(parsed_lookml_files, rules)
            linter.run()
            error_log = linter.get_errors()
            if not files_are_valid:
                error_log = file_validator.error_log() + '\n' + error_log
            print(error_log)

            output = error_log.replace('    ', '- ')

            # Save output to file, if enabled
            if save_output_to_file == 'true' or save_output_to_file == 'True':
                linter.save_errors(error_log, '_lookml-linter-output.txt')

            if linter.has_errors:
                outcome_fail = True

        if lookml_parser.not_parsed_lookml_files:
            for not_parsed_lookml_file_path in lookml_parser.not_parsed_lookml_files.keys():
                print(f"File {not_parsed_lookml_file_path} could not be parsed: "
                      f"{lookml_parser.not_parsed_lookml_files[not_parsed_lookml_file_path]}\n")
                output += f"\n:x: File `{not_parsed_lookml_file_path}` could not be parsed.\n"
            outcome_fail = True

    if output:
        print(output)
        write_output_to_gha_env(output=output, gha_env_name='error_log')
    if outcome_fail:
        raise Exception('LookML Linter detected an error')

def write_output_to_gha_env(output: str, gha_env_name: str):
    """
    Save output to GHA environment variable
    :param output: output value
    :param gha_env_name: GitHub env name
    :return:
    """
    gha = os.getenv('GITHUB_ENV')
    if gha:
        with open(gha, 'a') as fh:
            fh.write(f"{gha_env_name}<<EOF\n")
            fh.write(output)
            fh.write("EOF\n")


main()
