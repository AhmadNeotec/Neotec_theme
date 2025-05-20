# apps/neotec_theme/neotec_theme/overrides/switch_theme.py
import frappe

ALLOWED_THEMES = ["Light", "Dark", "Automatic", "Alphax Theme"]

@frappe.whitelist()
def switch_theme(theme):
    if theme not in ALLOWED_THEMES:
        frappe.throw(f'Desk Theme cannot be "{theme}". It should be one of {", ".join(ALLOWED_THEMES)}')
    if theme in ALLOWED_THEMES:
        frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)
        frappe.db.commit()
        frappe.log(f"Theme switched to {theme} for user {frappe.session.user}")
    else:
        frappe.throw(f"Invalid theme: {theme}")

def set_default_theme_on_login():
    """Set Alphax Theme for user on login"""
    frappe.log("DEBUG: Login hook triggered")
    user = frappe.session.user
    if user and user != "Guest":
        frappe.db.set_value("User", user, "desk_theme", "Alphax Theme")
        frappe.db.commit()
        frappe.log(f"Set Alphax Theme for user {user} on login")