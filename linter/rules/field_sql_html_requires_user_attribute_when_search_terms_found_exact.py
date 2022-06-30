from linter.rule import Rule


class FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFoundExact(Rule):
    def applies_to():
        return ('dimension', 'measure', 'dimension_group')

    def run(self, field):
        user_attribute = self.params['user_attribute']
        search_terms = self.params['search_terms']
        search_pattern = ' '.join([field.get(key, '')
                                   for key in ['name', 'label', 'description']])
        user_attribute_search_term = f'_user_attributes["{user_attribute}"]'
        search_terms_match_in_name_label_description = any(
            [word == search_pattern.strip() for word in search_terms])
        user_attribute_check_in_sql_html = not all([user_attribute_search_term in string for
                                                    string in [field.get('sql', ''), field.get('html', '')]])
        if search_terms_match_in_name_label_description and user_attribute_check_in_sql_html:
            return False
        return True
