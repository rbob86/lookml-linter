connection: "lookerplus"

include: "/views/*.view.lkml"
include: "/views_benchmarking/*.view"

datagroup: current {
  sql_trigger: select current_date() ;;
}

explore: 