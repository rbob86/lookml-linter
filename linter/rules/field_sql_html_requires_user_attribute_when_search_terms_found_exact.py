from pprint import pprint
from linter.rule import Rule


class FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFoundExact(Rule):
    def applies_to():
        return ("dimension", "measure", "dimension_group")

    def run(self, field):
        user_attribute = self.params["user_attribute"]
        search_terms = self.params["search_terms"]
        search_pattern = " ".join(
            [field.get(key, "") for key in ["name", "label", "description"]]
        )
        user_attribute_search_term = f'_user_attributes["{user_attribute}"]'
        search_terms_match_in_name_label_description = any(
            [word == search_pattern.strip() for word in search_terms]
        )
        user_attribute_check_in_sql_html = not all(
            [
                user_attribute_search_term in string
                for string in [field.get("sql", ""), field.get("html", "")]
            ]
        )
        if (
            search_terms_match_in_name_label_description
            and user_attribute_check_in_sql_html
        ):
            return False
        return True

    def get_hint(self, field, object_type):
        search_pattern = " ".join(
            [field.get(key, "") for key in ["name", "label", "description"]]
        )
        matched_user_attribute = [
            self.params["user_attribute"]
            for word in self.params["search_terms"]
            if word == search_pattern.strip()
        ][0]
        pprint(field)
        hint = f"""*** error hint: replace lkml field definition with the following (include _hidden field if it does not already exist. ensure type, sql and other attributes are set correctly): ***
        

        {object_type}: {field['name']}_hidden {{
            group_label: "THISSHOULDBEHIDDEN"
            hidden: yes
            sql: ${{TABLE}}.{field['name']}
            type: {field['type']}
        }}

        {object_type}: {field['name']} {{
        sql:
            CASE WHEN {{ _user_attributes["{matched_user_attribute}"] }} = 1 THEN
                ${{{field['name']}_hidden}}
            ELSE
                -1
            END ;;
        html:
            {{% if _user_attributes["{matched_user_attribute}"] == 1 %}}
            <a href="#drillmenu" target="_self"> {{ rendered_value }}
            {{% else %}}
            [Insufficient Permissions]
            {{% endif %}} ;;
        }}"""

        return hint
