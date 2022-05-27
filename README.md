# **LookML Linter**


## 
**Overview**

The LookML Linter serves as a tool to enforce LookML security and style best practices as  part of a CI/CD pipeline. This specific version was designed to leverage Github Actions (for more information about Github Actions, check out this blog [post](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/)). The recommendation is to use this linter with a series of other open-source scripts in your Github Action workflow. This will run on push events and need to pass before a developer can merge his/her/their pull request. 

A typical workflow would look like this linter being initiated on push events. A developer would make his/her/their changes and submit a pull request. Upon this action the linter would run and print out any warnings or errors. The linter does scan all the code, not just new changes. If there were just warnings, the developer could still merge the PR, but if there were errors the linter would fail and they would not be able to merge their PR. This would work best with a Github PullRequest checklist. 

For more information on how to set up the Github action, see the steps outlined in this [repo](https://github.com/eric-lyons/github_actions_looker_cicd). 


### **Rules**

The linter parses the LookML files in the project and checks if there are any exceptions to the rules defined in the `/linter/rules` directory. There are some predefined rules built into the linter, but **_please customize_** them as needed and contribute your own rules which you and your team find helpful for security and style best practices. **We implore you to extend this and use this repo as a framework to structure your own governance practices around.** This can even be accompanied by the [lmanage](https://github.com/looker-open-source/lmanage) library which helps maintain security best practices or Security as Code. 


## Prebuilt Rules



*   DimensionGroupOfTypeTimeRequiresDatatype
    *   This rule checks to see if dimension\_groups of type time have a datatype parameter specified. 
*   DimensionGroupOfTypeTimeRequiresTimeframe 
    *   This rule checks if dimension\_groups of type time have a timeframe parameter explicitly specified. 
*   ExploreJoinsRequireRelationship
    *   This rule checks that a relationship parameter is explicitly used on joins in explore objects. 
*   ExploreRequiresDescription
    *   This rule checks if all explore objects have a description parameter defined. 
*   FieldRequiresDescription
    *   This rule checks that all fields (measures, dimensions, and dimension\_groups) have descriptions added. 
*   FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFound
    *   This rule checks fields with the search term in the name use a specific user\_attribute to limit the field access. 
*   ViewWithDimensionsAndMeasuresHasOnePrimaryKey
    *   This rule checks to make sure that views have one field defined as the primary key. 
*   ViewWithManyFieldsRequiresFieldsHiddenByDefault
    *   This rule checks that views with over 50 fields enumerated have the hidden\_by\_default parameter set. 

### Adding a rule

Create file in the rule directory. Be very explicit about the rule name.

In that file we define a class with that rule. This always accepts the arg rule. The class needs an apply\_to for the objects it applies to and a run method. 

Update the import statements in the rule\_factory.py file. 

Finally update the config file to have the rule run. If a rule is not explicitly listed in the config file it will not run. 

### **Configuration File**

Required to run the linter is a configuration file in YAML format.  Included in the repository is a config.example.yaml file. Copy this file to config.yaml (or another filename of your choice) and customize appropriately. Every rule in `/linter/rules` must be specified here, with each having at least a `severity` attribute, as such:

``` \
- rule: field\_requires\_description

  severity: warning

- rule: view\_with\_many\_fields\_requires\_fields\_hidden\_by\_default

  severity: error

```

Severity** **attributes can be one of the following:



*   error - rules with error severities that don’t pass validation will cause the …
*   warning - warnings will be reported but will not stop the…
*   ignore - these rules will not be applied during linting

Rules can also accept custom parameters.  To specify a series of parameters that should be applied to a rule, add a `param\_sets` array to the configuration file, e.g.:

``` \
- rule: field\_sql\_html\_requires\_user\_attribute\_when\_search\_terms\_found

  severity: error

  param\_sets:

    - user\_attribute: test

      search\_terms:

        - a

          b

          c

    - user\_attribute: test2

      search\_terms:

        - x

          y

```


### AIn this example, the `field\_sql\_html\_requires\_user\_attribute\_when\_search\_terms\_found` rule will be run once per param set, and the rule’s run method will be able to access `user\_attribute` and `search\_terms`:

``` 
\user\_attribute = self.params['user\_attribute']

search\_terms = self.params['search\_terms'] \
```


## 
**Requirements**



*   [Python 3.8x+](https://www.python.org/downloads/)
*   [pipenv](https://pipenv.pypa.io/en/latest/install/)

## 
**Installation**

*   Run pipenv install to install third-party requirements inside the pipenv virtual environment.

## 
**Running**

*   Configure your config.yaml file to reflect the severities and parameters you want to apply to each rule.
*   Run pipenv shell to enter the virtual environment.
*   Run python -m linter.main &lt;path\_to\_config\_file.yaml> to run the program.

## 
**Tests**

A full unit test suite has been added to ensure quality and accuracy of the linter. 




