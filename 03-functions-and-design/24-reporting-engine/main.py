from pathlib import Path


print("=== Reporting Engine ===")


# ============================================================
# Sales Data
# ============================================================

sales = [
    {
        "id": 1,
        "product": "Mechanical Keyboard",
        "category": "Peripherals",
        "month": "January",
        "units": 12,
        "revenue": 54000.00
    },
    {
        "id": 2,
        "product": "Wireless Mouse",
        "category": "Peripherals",
        "month": "January",
        "units": 20,
        "revenue": 36000.00
    },
    {
        "id": 3,
        "product": "Gaming Headset",
        "category": "Audio",
        "month": "January",
        "units": 8,
        "revenue": 25600.00
    },
    {
        "id": 4,
        "product": "4K Monitor",
        "category": "Displays",
        "month": "February",
        "units": 5,
        "revenue": 140000.00
    },
    {
        "id": 5,
        "product": "Webcam",
        "category": "Peripherals",
        "month": "February",
        "units": 10,
        "revenue": 35000.00
    },
    {
        "id": 6,
        "product": "USB Microphone",
        "category": "Audio",
        "month": "February",
        "units": 7,
        "revenue": 43400.00
    },
    {
        "id": 7,
        "product": "1TB SSD",
        "category": "Storage",
        "month": "March",
        "units": 10,
        "revenue": 72000.00
    },
    {
        "id": 8,
        "product": "2TB HDD",
        "category": "Storage",
        "month": "March",
        "units": 14,
        "revenue": 81200.00
    },
    {
        "id": 9,
        "product": "Laptop Stand",
        "category": "Accessories",
        "month": "March",
        "units": 18,
        "revenue": 39600.00
    },
    {
        "id": 10,
        "product": "USB-C Hub",
        "category": "Accessories",
        "month": "April",
        "units": 20,
        "revenue": 52000.00
    }
]


REPORT_FILE = Path("sales_report.txt")


# ============================================================
# Calculation Functions
# ============================================================

def calculate_total_revenue(data):
    """Return total revenue."""

    return sum(
        record["revenue"]
        for record in data
    )


def calculate_total_units(data):
    """Return total units sold."""

    return sum(
        record["units"]
        for record in data
    )


def calculate_average_revenue(data):
    """Return average revenue per sales record."""

    if not data:
        return 0

    return calculate_total_revenue(data) / len(data)


def group_by_category(data):
    """Group sales by category."""

    result = {}

    for record in data:

        category = record["category"]

        if category not in result:

            result[category] = {
                "units": 0,
                "revenue": 0
            }

        result[category]["units"] += record["units"]
        result[category]["revenue"] += record["revenue"]

    return result


def group_by_month(data):
    """Group sales by month."""

    result = {}

    for record in data:

        month = record["month"]

        if month not in result:

            result[month] = {
                "units": 0,
                "revenue": 0
            }

        result[month]["units"] += record["units"]
        result[month]["revenue"] += record["revenue"]

    return result


def get_top_products(data, limit=5):
    """Return products ranked by revenue."""

    return sorted(
        data,
        key=lambda record: record["revenue"],
        reverse=True
    )[:limit]


def calculate_summary(data):
    """Return the main report metrics."""

    return {
        "records": len(data),
        "units": calculate_total_units(data),
        "revenue": calculate_total_revenue(data),
        "average_revenue": calculate_average_revenue(data)
    }


# ============================================================
# Report Functions
# ============================================================

def build_summary_report(data):
    """Build the overall sales summary."""

    summary = calculate_summary(data)

    lines = []

    lines.append("=== Sales Summary ===")
    lines.append(
        f"Sales records: {summary['records']}"
    )
    lines.append(
        f"Units sold: {summary['units']}"
    )
    lines.append(
        f"Total revenue: ₹{summary['revenue']:,.2f}"
    )
    lines.append(
        f"Average revenue per record: "
        f"₹{summary['average_revenue']:,.2f}"
    )

    return "\n".join(lines)


def build_category_report(data):
    """Build the category performance report."""

    category_data = group_by_category(data)

    ranked_categories = sorted(
        category_data.items(),
        key=lambda item: item[1]["revenue"],
        reverse=True
    )

    lines = []

    lines.append("=== Category Performance ===")

    for category, values in ranked_categories:

        lines.append(
            f"{category}: "
            f"{values['units']} units | "
            f"₹{values['revenue']:,.2f}"
        )

    return "\n".join(lines)


def build_monthly_report(data):
    """Build the monthly performance report."""

    monthly_data = group_by_month(data)

    ranked_months = sorted(
        monthly_data.items(),
        key=lambda item: item[1]["revenue"],
        reverse=True
    )

    lines = []

    lines.append("=== Monthly Performance ===")

    for month, values in ranked_months:

        lines.append(
            f"{month}: "
            f"{values['units']} units | "
            f"₹{values['revenue']:,.2f}"
        )

    return "\n".join(lines)


def build_top_products_report(data):
    """Build the top-product report."""

    top_products = get_top_products(data)

    lines = []

    lines.append("=== Top Products ===")

    for rank, record in enumerate(
        top_products,
        start=1
    ):

        lines.append(
            f"{rank}. "
            f"{record['product']} — "
            f"₹{record['revenue']:,.2f}"
        )

    return "\n".join(lines)


def build_full_report(data):
    """Build the complete report."""

    sections = [
        "========================================",
        "           SALES REPORT",
        "========================================",
        "",
        build_summary_report(data),
        "",
        build_category_report(data),
        "",
        build_monthly_report(data),
        "",
        build_top_products_report(data)
    ]

    return "\n".join(sections)


def save_report(report):
    """Save a generated report to a text file."""

    try:

        REPORT_FILE.write_text(
            report,
            encoding="utf-8"
        )

        print(
            f"Report saved to "
            f"{REPORT_FILE}"
        )

    except OSError as error:

        print(
            f"Could not save report: {error}"
        )


# ============================================================
# Display Functions
# ============================================================

def show_sales_data(data):
    """Display raw sales records."""

    print("\n=== Sales Data ===")

    for record in data:

        print(
            f"[{record['id']}] "
            f"{record['product']} | "
            f"{record['category']} | "
            f"{record['month']} | "
            f"{record['units']} units | "
            f"₹{record['revenue']:,.2f}"
        )


def show_summary(data):
    print("\n")
    print(build_summary_report(data))


def show_category_report(data):
    print("\n")
    print(build_category_report(data))


def show_monthly_report(data):
    print("\n")
    print(build_monthly_report(data))


def show_top_products(data):
    print("\n")
    print(build_top_products_report(data))


def show_full_report(data):
    print("\n")
    print(build_full_report(data))


# ============================================================
# Main Program
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View sales data")
    print("2. Sales summary")
    print("3. Category performance")
    print("4. Monthly report")
    print("5. Top products")
    print("6. Full report")
    print("7. Export full report")
    print("8. Exit")

    choice = input(
        "Choose an option: "
    ).strip()


    if choice == "1":

        show_sales_data(sales)


    elif choice == "2":

        show_summary(sales)


    elif choice == "3":

        show_category_report(sales)


    elif choice == "4":

        show_monthly_report(sales)


    elif choice == "5":

        show_top_products(sales)


    elif choice == "6":

        show_full_report(sales)


    elif choice == "7":

        report = build_full_report(sales)

        save_report(report)


    elif choice == "8":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 8."
        )