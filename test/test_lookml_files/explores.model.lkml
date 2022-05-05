connection: "lookerplus"

include: "/views/*.view.lkml"
include: "/views_benchmarking/*.view"

datagroup: current {
  sql_trigger: select current_date() ;;
}

explore: order_items {
  sql_always_where:
  ${products.category} in
  (select ${products.category} from ${products.SQL_TABLE_NAME} products
  where ${products.brand} = 'Allegra K'
  group by 1)
  ;;

  # Users
  join: users {
    type: left_outer
    sql_on: ${order_items.user_id} = ${users.id} ;;
    relationship: many_to_one
  }

  # Inventory Items
  join: inventory_items {
    fields: [inventory_items.id]
    type: left_outer
    sql_on: ${order_items.inventory_item_id} = ${inventory_items.id} ;;
    relationship: many_to_one
  }

  # Products
  join: products {
    type: left_outer
    sql_on: ${inventory_items.product_id} = ${products.id} ;;
    relationship: many_to_one
  }
}

explore: order_items_benchmark {

  sql_always_where: ${order_items_benchmark.product_brand} = 'Allegra K' ;;
  join: benchmark {
    relationship: many_to_one
    sql:
    {% assign dim_is_in_query = 0 %}
    left join benchmark on

    {% if order_items_benchmark.order_created._in_query %}
    {% assign dim_is_in_query = 1 %}
    ${benchmark.order_created_date} = ${order_items_benchmark.created_date}
    {% endif %}

    {% if order_items_benchmark.country._in_query %}
    {% assign dim_is_in_query = 1 %}
    ${benchmark.country} = ${order_items_benchmark.country}
    {% endif %}

    {% if order_items_benchmark.product_category._in_query %}
    {% assign dim_is_in_query = 1 %}
    ${benchmark.product_category} = ${order_items_benchmark.product_category}
    {% endif %}

    {% if order_items_benchmark.status._in_query %}
    {% assign dim_is_in_query = 1 %}
    ${benchmark.status} = ${order_items_benchmark.status}
    {% endif %}

    {% if order_items_benchmark.state._in_query %}
    {% assign dim_is_in_query = 1 %}
    ${benchmark.state} = ${order_items_benchmark.state}
    {% endif %}

    {% if dim_is_in_query == 0 %}
    true
    {% endif %}

    ;;
  }
}

explore: order_facts_pdt {}
