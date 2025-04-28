app_name = "neotec_theme"
app_title = "Neotec Theme"
app_publisher = "Neotev"
app_description = "theme"
app_email = "neotec@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "neotec_theme",
# 		"logo": "/assets/neotec_theme/logo.png",
# 		"title": "Neotec Theme",
# 		"route": "/neotec_theme",
# 		"has_permission": "neotec_theme.api.permission.has_app_permission"
# 	}
# ]
after_install = "neotec_theme.install.set_default_theme"
# on_login = "neotec_theme."
# on_login = "neotec_theme.overrides.user_login.set_alphax_theme_on_login"
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/neotec_theme/css/neotec_theme.css"
# app_include_js = "/assets/neotec_theme/js/neotec_theme.js"
# apps/neotec_theme/neotec_theme/hooks.py
app_include_css = "/assets/neotec_theme/css/theme.css"
# app_include_css = "/assets/neotec_theme/css/login.css"
# apps/neotec_theme/neotec_theme/hooks.py
app_include_js = "/assets/neotec_theme/js/theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/neotec_theme/css/neotec_theme.css"
# web_include_js = "/assets/neotec_theme/js/neotec_theme.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "neotec_theme/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "neotec_theme/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "neotec_theme.utils.jinja_methods",
# 	"filters": "neotec_theme.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "neotec_theme.install.before_install"
# after_install = "neotec_theme.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "neotec_theme.uninstall.before_uninstall"
# after_uninstall = "neotec_theme.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "neotec_theme.utils.before_app_install"
# after_app_install = "neotec_theme.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "neotec_theme.utils.before_app_uninstall"
# after_app_uninstall = "neotec_theme.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "neotec_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
override_whitelisted_methods = {
    "frappe.core.doctype.user.user.switch_theme": "neotec_theme.overrides.switch_theme.switch_theme"
}

on_login = [
    # ... other login hooks if any ...
    "neotec_theme.overrides.switch_theme.set_default_theme_on_login"
]
# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"neotec_theme.tasks.all"
# 	],
# 	"daily": [
# 		"neotec_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"neotec_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"neotec_theme.tasks.weekly"
# 	],
# 	"monthly": [
# 		"neotec_theme.tasks.monthly"
# 	],
# }
# Testing
# -------

# before_tests = "neotec_theme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "neotec_theme.event.get_events"
# }
#
# override_whitelisted_methods = {
#     "frappe.core.doctype.user.user.switch_theme": "neotec_theme.overrides.switch_theme"
# }
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "neotec_theme.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["neotec_theme.utils.before_request"]
# after_request = ["neotec_theme.utils.after_request"]

# Job Events
# ----------
# before_job = ["neotec_theme.utils.before_job"]
# after_job = ["neotec_theme.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	},
#     {
# 		"item_label": "Toggle Theme",
# 		"item_type": "Action",
# 		"action": "new frappe.ui.ThemeSwitcher().show()",
# 		"is_standard": 1,
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"neotec_theme.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

