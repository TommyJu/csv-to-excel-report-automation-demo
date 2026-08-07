def create_promotion_sheet(wb, report):

    ws = wb.create_sheet(
        "Promotions"
    )


    # -------------------------
    # Summary
    # -------------------------

    ws.append([
        "Promotion Summary",
        "Value"
    ])


    summary_rows = [
        (
            "Promotion Sales",
            report.promotions.promotion_sales
        ),

        (
            "Regular Sales",
            report.promotions.regular_sales
        ),

        (
            "Best Promotion Item",
            report.promotions.best_promotion_item
        )
    ]


    for row in summary_rows:
        ws.append(row)


    ws.append([])


    # -------------------------
    # Product Promotion Lift
    # -------------------------

    ws.append([
        "Product",
        "Promotion Lift (%)"
    ])


    # Sort highest impact first
    sorted_lift = sorted(
        report.promotions.promotion_lift.items(),
        key=lambda x: x[1],
        reverse=True
    )


    for product, lift in sorted_lift:

        ws.append([
            product,
            f"{lift}%"
        ])
    