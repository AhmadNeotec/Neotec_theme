import frappe

def get_context(context):
    # Fetch the first company (or a specific one by name)
    try:
        company = frappe.get_all("Company", fields=["name", "company_name", "custom_company_arabic_name", "company_logo"], limit=1)
        if not company:
            # Fallback if no company exists
            context.company_name = "Alphax Saas"
            context.company_logo = "/files/default-logo.png"
        else:
            company = company[0]  # Get the first company
            context.company_name = company.get("custom_company_arabic_name") or company.get("company_name")
            context.company_logo = company.get("company_logo") or "/files/default-logo.png"
    except Exception as e:
        # Handle any unexpected errors gracefully
        frappe.log_error(f"Error fetching company: {str(e)}")
        context.company_name = "Alphax Saas"
        context.company_logo = "/files/default-logo.png"

    # Define menu items
    context.menu_items = [
        {
            "label": "Dashboard",
            "icon": "fas fa-tachometer-alt",
            "submenu": [
                {"label": "Main Dashboard", "url": "/app/dashboard/main"},
                {"label": "Secondary Dashboard", "url": "/app/dashboard/secondary"}
            ]
        },
        {
            "label": "Customers",
            "icon": "fas fa-users",
            "submenu": [
                {"label": "Add Customer", "url": "/app/customer/new"},
                {"label": "View Customers", "url": "/app/customer"},
                {"label": "Refund History", "url": "/app/customer/refund-history"}
            ]
        },
        {
            "label": "Sales",
            "icon": "fas fa-file-invoice-dollar",
            "active": True,
            "submenu": [
                {"label": "Create Invoice", "url": "/app/sales-invoice/new"},
                {"label": "View Invoices", "url": "/app/sales-invoice"},
                {"label": "Recurring Invoice", "url": "/app/recurring-sales-invoice"},
                {"label": "Credit Note", "url": "/app/credit-note"}
            ]
        }
    ]

    # Brand logo
    context.brand_logo = ""  # Ensure this file exists