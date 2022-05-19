view: products {
  sql_table_name: public.products ;;

  dimension: id {
    primary_key: yes
    type: number
    sql:
        CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN
            ${TABLE}.id
        ELSE
            -1
        END ;;
    html:
        {% if _user_attributes[""permissions_financial_row_level""] == 1 %}
        {{ rendered_value }}
        {% else %}
        [Insufficient Permissions]
        {% endif %} ;;
    }

  dimension: brand {
    label: "Brand"
    description: "Branding lots"
    type: string
    sql: ${TABLE}.brand ;;
  }

  dimension: category {
    type: string
    sql: ${TABLE}.category ;;
  }

  dimension: cost {
    type: number
    sql: ${TABLE}.cost ;;
  }

  dimension: department {
    type: string
    sql: ${TABLE}.department ;;
  }

  dimension: distribution_center_id {
    type: number
    # hidden: yes
    sql: ${TABLE}.distribution_center_id ;;
  }

  dimension: name {
    type: string
    sql: ${TABLE}.name ;;
  }

  dimension: retail_price {
    type: number
    sql: ${TABLE}.retail_price ;;
  }

  dimension: sku {
    type: string
    sql: ${TABLE}.sku ;;
  }

  dimension: brand_cat{
    type: string
    sql: ${brand}||' ' || ${category} ;;

  }

  measure: count {
    type: count
    drill_fields: [id, name, distribution_centers.id, distribution_centers.name, inventory_items.count]
  }

  measure: total_cost {
    type: sum
    sql: ${cost} ;;
    value_format_name: usd
    drill_fields: [id, name, category, distribution_centers.name, department]

  }
}