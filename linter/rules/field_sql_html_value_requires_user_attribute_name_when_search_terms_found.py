from linter.rule import Rule
from linter.severity import Severity


class FieldSqlHtmlValueRequiresUserAttributeNameWhenSearchTermsFound(Rule):
    def default_severity():
        return Severity.ERROR.value

    def applies_to():
        return ('dimension', 'measure', 'dimension_group')

    def run(self, field, user_attribute, search_terms):
        search_strings = []
        user_attribute_search_term = '_user_attributes[""' + \
            user_attribute + '""]'
        search_strings.extend([field.get(key, '')
                              for key in ['name', 'label', 'description']])
        if any(word in ' '.join(search_strings) for word in search_terms):
            if all(user_attribute_search_term in string for string in
                [field.get(key, []) for key in ['sql', 'html']]):
                return True    
            return False
        return True
