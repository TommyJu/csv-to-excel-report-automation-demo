def create_dashboard_sheet(wb, report):

    ws = wb.active
    ws.title = "Dashboard"


    # -------------------------
    # Title
    # -------------------------

    ws.append([
        "☕ Coffee Shop Sales Dashboard"
    ])

    ws.append([])


    # -------------------------
    # Overall Metrics
    # -------------------------

    ws.append([
        "Business Overview",
        "Value"
    ])


    overview_metrics = [

        (
            "Total Items Sold",
            report.summary.total_items_sold
        ),

        (
            "Unique Products",
            report.summary.unique_products
        ),

        (
            "Sales Days Recorded",
            report.summary.total_sales_days
        ),

        (
            "Average Daily Sales",
            report.summary.average_daily_sales
        )
    ]


    for metric, value in overview_metrics:

        ws.append([
            metric,
            value
        ])


    ws.append([])


    # -------------------------
    # Top Performers
    # -------------------------

    ws.append([
        "Top Performers",
        "Value"
    ])


    performance_metrics = [

        (
            "Best Selling Item",
            f"{report.summary.best_selling_item} "
            f"({report.summary.best_selling_item_qty} units)"
        ),

        (
            "Best Sales Day",
            f"{report.summary.best_sales_day} "
            f"({report.summary.best_sales_day_qty} units)"
        ),

        (
            "Best Sales Month",
            f"{report.summary.best_sales_month} "
            f"({report.summary.best_sales_month_qty} units)"
        )
    ]


    for metric, value in performance_metrics:

        ws.append([
            metric,
            value
        ])