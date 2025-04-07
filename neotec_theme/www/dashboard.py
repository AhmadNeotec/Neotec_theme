import frappe

def get_context(context):
    # Fetch the first company (or a specific one by name)
    try:
        # company = frappe.get_all("Company", fields=["name", "company_name", "custom_company_arabic_name"], limit=1)
        company = frappe.get_all(
        "Company",
        fields=["name", "company_name", "custom_company_arabic_name", "company_logo"],
        limit=1)
        if not company:
            context.company_name = "Alphax Saas"
            context.company_logo = "/assets/neotec_theme/images/alphaxsaas.jpg"
        else:
            company = company[0]
            context.company_name = company.get("custom_company_arabic_name") or company.get("company_name")
            context.company_logo = company.get("company_logo") or "/assets/neotec_theme/images/alphaxsaas.jpg"
    except Exception as e:
        frappe.log_error(f"Error fetching company: {str(e)}")
        context.company_name = "Alphax Saas"
        context.company_logo = "/assets/neotec_theme/images/alphaxsaas.jpg"

    # Brand logo
    context.brand_logo = context.company_logo  # Update this if needed

    # Menu structure
    context.menu_items = [
         {
            "label": "Accounting",
            "icon": "fas fa-calculator",
            "url": "/app/accounting"
        },
        {
            "label": "Dashboard",
            "icon": "fas fa-tachometer-alt",
            "submenu": [
                {"label": "Main Dashboard", "url": "/app/dashboard/main"},
                {"label": "Secondary Dashboard", "url": "/app/dashboard/secondary"},
            ]
        },
        {
            "label": "Customers",
            "icon": "fas fa-users",
            "submenu": [
                {"label": "Add Customer", "url": "/app/customer/new"},
                {"label": "View Customers", "url": "/app/customer"},
                {"label": "Refund History", "url": "/app/customer/refund-history"},
            ]
        },
        {
            "label": "Suppliers",
            "icon": "fas fa-boxes",
            "submenu": [
                {"label": "View Suppliers", "url": "/app/supplier"},
                {"label": "Add Supplier", "url": "/app/supplier/new"},
                {"label": "Refund History", "url": "/app/supplier/refund-history"},
                {"label": "View Email Templates", "url": "/app/supplier/email-templates"},
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
                {"label": "Credit Note", "url": "/app/credit-note"},
            ]
        },
        {
            "label": "Purchases",
            "icon": "fas fa-shopping-cart",
            "submenu": [
                {"label": "Create Invoice", "url": "/app/purchase-invoice/new"},
                {"label": "View Invoices", "url": "/app/purchase-invoice"},
                {"label": "View Recurring Invoice", "url": "/app/recurring-purchase-invoice"},
            ]
        },
        {
            "label": "Orders",
            "icon": "fas fa-clipboard-list",
            "url": "/app/orders"
        },
        {
            "label": "Payments",
            "icon": "fas fa-credit-card",
            "url": "/app/payments"
        },
        {
            "label": "Products",
            "icon": "fas fa-box-open",
            "url": "/app/products"
        },
        {
            "label": "Expenses",
            "icon": "fas fa-money-bill-wave",
            "url": "/app/expenses"
        },
        {
            "label": "Banking",
            "icon": "fas fa-university",
            "url": "/app/banking"
        },
        {
            "label": "Point Of Sale",
            "icon": "fas fa-cash-register",
            "url": "/app/point-of-sale"
        },
        {
            "label": "Reports",
            "icon": "fas fa-chart-line",
            "url": "/app/reports"
        },
        {
            "label": "Settings",
            "icon": "fas fa-cog",
            "url": "/app/settings"
        }
    ]
