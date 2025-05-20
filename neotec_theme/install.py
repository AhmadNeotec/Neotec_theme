# apps/neotec_theme/neotec_theme/install.py
import frappe

def set_default_theme():
    """Set Alphax Theme for all users without a theme or with Light"""
    users = frappe.get_all("User", filters={"desk_theme": ["in", [None, "", "Light"]]}, fields=["name"])
    for user in users:
        frappe.db.set_value("User", user.name, "desk_theme", "Alphax Theme")
    frappe.db.commit()
    frappe.log("Set default theme to Alphax Theme for all users")