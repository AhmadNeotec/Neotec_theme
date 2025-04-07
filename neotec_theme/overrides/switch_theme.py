# apps/neotec_theme/neotec_theme/overrides/switch_theme.py
import frappe

@frappe.whitelist()
def switch_theme(theme):
    valid_themes = ["dark", "light", "automatic", "alphax_theme"]  
    if theme.lower() in valid_themes:  
        frappe.db.set_value("User", frappe.session.user, "desk_theme", theme.lower())
        frappe.db.commit()
        frappe.log(f"Theme switched to {theme.lower()} for user {frappe.session.user}")
    else:
        frappe.throw(f"Invalid theme: {theme}")