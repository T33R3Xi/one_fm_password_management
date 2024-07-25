# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "one_fm_password_management"
app_title = "One Fm Password Management"
app_publisher = "ONE FM"
app_description = "Password Management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "develop@one-fm.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/one_fm_password_management/css/one_fm_password_management.css"
# app_include_js = "/assets/one_fm_password_management/js/one_fm_password_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/one_fm_password_management/css/one_fm_password_management.css"
# web_include_js = "/assets/one_fm_password_management/js/one_fm_password_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in formface views
# formface_js = {"formface" : "public/js/formface.js"}
# formface_list_js = {"formface" : "public/js/formface_list.js"}
# formface_tree_js = {"formface" : "public/js/formface_tree.js"}
# formface_calendar_js = {"formface" : "public/js/formface_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "one_fm_password_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this formface
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "one_fm_password_management.install.before_install"
# after_install = "one_fm_password_management.install.after_install"

# Desk Notifications
# ------------------
# See nxm.core.notifications.get_notification_config

# notification_config = "one_fm_password_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "nxm.desk.formface.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "nxm.desk.formface.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"one_fm_password_management.tasks.all"
# 	],
# 	"daily": [
# 		"one_fm_password_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"one_fm_password_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"one_fm_password_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"one_fm_password_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "one_fm_password_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"nxm.desk.formface.event.event.get_events": "one_fm_password_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the formface dashboard,
# along with any modifications made in other Nxm apps
# override_formface_dashboards = {
# 	"Task": "one_fm_password_management.task.get_dashboard_data"
# }

# exempt linked formfaces from being automatically cancelled
#
# auto_cancel_exempted_formfaces = ["Auto Repeat"]

