# **LookML Linter**


## 
**Overview**

The LookML Linter serves as a tool to enforce LookML security and style best practices as  part of a CI/CD pipeline. This specific version was designed to leverage Github Actions (for more information about Github Actions, check out this blog [post](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/)). The recommendation is to use this linter with a series of other open-source github action scripts in your Github Action workflow ([repo](https://github.com/eric-lyons/github_actions_looker_cicd)). This will run on push or pull request (PR) events.

A typical workflow would look like this: the linter gets triggered when a developer creates a PR with the latest feature changes. A pipeline is triggered and the linter would run and print out any warnings or errors. The linter scans all the lkml files passed into the working directory where the action is run.  If there are just linter warnings, the developer could still merge the PR, but if there were errors the linter will fail and the developer is blocked from merging the PR. 


### **How to set up config file**

Below is a sample configuration file for a github action workflow yaml file. 


```
name: LookML Linter Run

on:
 pull_request:
   branches: [ main ]
jobs:
 lookml_linter:
   runs-on: ubuntu-latest
   name: LookML Linter
   steps:
     - name: Checkout
       uses: actions/checkout@v1
     - name: Run LookML Liniter
       id: linter
       uses: rbob86/lookml-linter@main


```



### **Rules**

The linter parses the LookML files in the project and checks if there are any exceptions to the rules defined in the `/linter/rules` directory. There are some predefined rules built into the linter, but **_please customize_** them as needed and contribute your own rules which you and your team find helpful for security and style best practices. **We implore you to extend this and use this repo as a framework to structure your own governance practices around.** This can even be accompanied by the [lmanage](https://github.com/looker-open-source/lmanage) library which helps maintain security best practices or Security as Code. 


## Prebuilt Rules



*   DimensionGroupOfTypeTimeRequiresDatatype
    *   This rule checks to see if dimension_groups of type time have a datatype parameter specified. 
*   DimensionGroupOfTypeTimeRequiresTimeframe 
    *   This rule checks if dimension_groups of type time have a timeframe parameter explicitly specified. 
*   ExploreJoinsRequireRelationship
    *   This rule checks that a relationship parameter is explicitly used on joins in explore objects. 
*   ExploreRequiresDescription
    *   This rule checks if all explore objects have a description parameter defined. 
*   FieldRequiresDescription
    *   This rule checks that all fields (measures, dimensions, and dimension_groups) have descriptions added. 
*   FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFound
    *   This rule checks fields with the search term in the name use a specific user_attribute to limit the field access. 
*   ViewWithDimensionsAndMeasuresHasOnePrimaryKey
    *   This rule checks to make sure that views have one field defined as the primary key. 
*   ViewWithManyFieldsRequiresFieldsHiddenByDefault
    *   This rule checks that views with over 50 fields enumerated have the hidden_by_default parameter set. 


### **Configuration File**

Required to run the linter is a configuration file in YAML format. This file needs to be added directly to the .github/workflows directory otherwise you would need to update the actions yaml file where this is specified in the with clause.  Included in the repository is a config.example.yaml file. Copy this file to config.yaml (or another filename of your choice) and customize appropriately. Every rule in `/linter/rules` must be specified here, with each having at least a `severity` attribute, as such:

``` \
- rule: field_requires_description

  severity: warning

- rule: view_with_many_fields_requires_fields_hidden_by_default

  severity: error

```

Severity** **attributes can be one of the following:



*   error - rules with error severities that don’t pass validation will cause the …
*   warning - warnings will be reported but will not stop the…
*   ignore - these rules will not be applied during linting

Rules can also accept custom parameters.  To specify a series of parameters that should be applied to a rule, add a `param_sets` array to the configuration file, e.g.:

``` 
- rule: field_sql_html_requires_user_attribute_when_search_terms_found

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


### AIn this example, the `field_sql_html_requires_user_attribute_when_search_terms_found` rule will be run once per param set, and the rule’s run method will be able to access `user_attribute` and `search_terms`:

``` 
user_attribute = self.params['user_attribute']

search_terms = self.params['search_terms'] \
```


## 
**Notable Requirements**



*   [Python 3.8x+](https://www.python.org/downloads/)
*   [Pipenv](https://pipenv.pypa.io/en/latest/install/)
*   Lkml
*   [Looker-sdk](https://docs.looker.com/reference/api-and-integration/api-sdk)
*   [Argparse](https://docs.python.org/3/library/argparse.html)
*   [pyyaml](https://pyyaml.org/)

For a full list of the requirements, please see this [page](https://github.com/rbob86/lookml-linter/blob/main/requirements.txt). 


## 
**Installation**



*   To run this locally, run pipenv install to install third-party requirements inside the pipenv virtual environment.
*   Run

## 
**Running**

*   Configure your config.yaml file to reflect the severities and parameters you want to apply to each rule.
*   Run pipenv shell to enter the virtual environment.
*   Run python -m linter.main &lt;path_to_config_file.yaml> to run the program.

## 
**Output**




<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>  GDC alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


The output will begin with the file name, followed by the list of errors and warnings. THis will show the object name and the violated rule. 


## 
**Tests**


## 
A full unit test suite has been added to ensure quality and accuracy of the linter. 


## Adding a rule

Create file in the rule directory. Be very explicit about the rule name.

In that file we define a class for that rule. This always accepts the arg rule. The class needs an apply_to for the objects it applies to and a run method. 

Update the import statements in the rule_factory.py file. 

Finally update the config file to have the rule run. If a rule is not explicitly listed in the config file it will not run. 

We recommend adding unit tests for each additional rule. 
