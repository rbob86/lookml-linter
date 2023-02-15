# LookML Linter

## Overview

The LookML Linter serves as a tool to enforce LookML security and style best practices as part of a CI/CD pipeline. This specific version was designed to leverage Github Actions (for more information about Github Actions, check out this blog [post](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/)). The recommendation is to use this linter with a series of other open-source scripts in your Github Action workflow. This will run on push events and need to pass before a developer can merge his/her/their pull request.

A typical workflow would look like this linter being initiated on push events. A developer would make his/her/their changes and submit a pull request. Upon this action the linter would run and print out any warnings or errors. The linter does scan all the code, not just new changes. If there were just warnings, the developer could still merge the PR, but if there were errors the linter would fail and they would not be able to merge their PR. This would work best with a Github PullRequest checklist.

For more information on how to set up the Github action, see the steps outlined in this [repo](https://github.com/eric-lyons/github_actions_looker_cicd).

### Rules

The linter parses the LookML files in the project and checks if there are any exceptions to the rules defined in the `/linter/rules` directory. There are some predefined rules built into the linter, but **_please customize_** them as needed and contribute your own rules which you and your team find helpful for security and style best practices. **We implore you to extend this and use this repo as a framework to structure your own governance practices around.** This can even be accompanied by the [lmanage](https://github.com/looker-open-source/lmanage) library which helps maintain security best practices or Security as Code.

## Prebuilt Rules

- DimensionGroupOfTypeTimeRequiresDatatype
  - This rule checks to see if dimension_groups of type time have a datatype parameter specified.
- DimensionGroupOfTypeTimeRequiresTimeframes
  - This rule checks if dimension_groups of type time have a timeframes parameter explicitly specified.
- ExploreJoinsRequireRelationship
  - This rule checks that a relationship parameter is explicitly used on joins in explore objects.
- ExploreRequiresDescription
  - This rule checks if all explore objects have a description parameter defined.
- ExploreTagRequiresOwner
  - This rule checks that each explore has an owner defined in its [tag parameter](https://cloud.google.com/looker/docs/reference/param-explore-tags)
    - `tags: ['owner:your_name'] `
- FieldRequiresDescription
  - This rule checks that all fields (measures, dimensions, and dimension_groups) have descriptions added.
- FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFound
  - This rule checks fields with the search term in the name use a specific user_attribute to limit the field access.
- ViewWithDimensionsAndMeasuresHasOnePrimaryKey
  - This rule checks to make sure that views have one field defined as the primary key.
- ViewWithManyFieldsRequiresFieldsHiddenByDefault
  - This rule checks that views with over 50 fields enumerated have the hidden_by_default parameter set.
- CountMeasureNameMustStartWithCount
  - This rule checks that the name of type count / count_distinct measures start with `count_`.
- AverageMeasureNameMustStartWithAvgOrAverage
  - This rule checks that the name of type average / average_distinct measures starts with `avg_` or `average_`.
- SumMeasureNameMustStartWithSumOrTotal
  - This rule checks that the name of type sum / sum_distinct measures starts with `sum_` or `total_`.
- YesnoFieldNameMustStartWithIsOrHas
  - This rule checks that the name of type yesno fields starts with `is_` or `has_`.

### Adding a rule

Create file in the rule directory. Be very explicit about the rule name.

In that file we define a class with that rule. This always accepts the arg rule. The class needs an apply_to for the objects it applies to and a run method.

Update the import statements in the rule_factory.py file.

Finally update the config file to have the rule run. If a rule is not explicitly listed in the config file it will not run.

### Configuration File

Required to run the linter is a configuration file in YAML format. Included in the repository is a config.example.yaml file. Copy this file to config.yaml (or another filename of your choice) and customize appropriately. Every rule in `/linter/rules` must be specified here, with each having at least a `severity` attribute, as such:

```
- rule: field_requires_description

  severity: warning

- rule: view_with_many_fields_requires_fields_hidden_by_default

  severity: error

```

Severity attributes can be one of the following:

- error - rules with error severities that don’t pass validation will cause the …
- warning - warnings will be reported but will not stop the…
- ignore - these rules will not be applied during linting

Rules can also accept custom parameters. To specify a series of parameters that should be applied to a rule, add a `param_sets` array to the configuration file, e.g.:

```
- rule: field_sql_html_requires_user_attribute_when_search_terms_found_exact
  severity: error
  param_sets:
    - user_attribute: test
      search_terms:
        - a
          b
          c
    - user_attribute: test2
      search_terms:
        - x
          y
```

In this example, the `field_sql_html_requires_user_attribute_when_search_terms_found_exact` rule will be run once per param set, and the rule’s run method will be able to access `user_attribute` and `search_terms`:

```
user_attribute = self.params['user_attribute']
search_terms = self.params['search_terms']
```

## Requirements

- [Python 3.8x+](https://www.python.org/downloads/)
- [pipenv](https://pipenv.pypa.io/en/latest/install/)

## Installation

- Run pipenv install to install third-party requirements inside the pipenv virtual environment.

## Running

- Configure your config.yaml file to reflect the severities and parameters you want to apply to each rule.
- Run pipenv shell to enter the virtual environment.
- Run python -m linter.main <path_to_config_file.yaml> to run the program.

## Tests

A full unit test suite has been added to ensure quality and accuracy of the linter.
