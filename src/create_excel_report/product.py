from openpyxl.chart import BarChart, Reference


def create_product_sheet(wb, report):

    ws = wb.create_sheet(
        "Product Performance"
    )


    # -------------------------
    # Summary
    # -------------------------

    ws.append([
        "Product Performance Summary",
        "Value"
    ])


    summary_rows = [
        (
            "Total Products",
            report.menu.total_products
        )
    ]


    for row in summary_rows:
        ws.append(row)


    ws.append([])


    # -------------------------
    # Product Rankings
    # -------------------------

    ws.append([
        "Rank",
        "Product",
        "Units Sold",
        "Contribution %"
    ])


    for product in report.menu.product_rankings:

        name = product["Menu"]
        units = product["Units_Sold"]

        contribution = (
            report.menu.product_contribution
            .get(name, 0)
        )


        ws.append([
            product["Rank"],
            name,
            units,
            f"{contribution}%"
        ])


    # -------------------------
    # Top Products Chart
    # -------------------------

    chart = BarChart()

    chart.title = (
        "Top Products by Sales"
    )

    chart.y_axis.title = (
        "Units Sold"
    )

    chart.x_axis.title = (
        "Product"
    )


    # Only top 5 products
    data = Reference(
        ws,
        min_col=3,
        min_row=4,
        max_row=8
    )


    categories = Reference(
        ws,
        min_col=2,
        min_row=5,
        max_row=9
    )


    chart.add_data(
        data,
        titles_from_data=True
    )


    chart.set_categories(
        categories
    )


    ws.add_chart(
        chart,
        "F2"
    )
  