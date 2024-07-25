from __future__ import unicode_literals
from nxm import _

def get_data():
	return [
		{
			"label": _("Tools"),
			"icon": "octicon octicon-briefcase",
			"items": [
				{
					"type": "formface",
					"name": "Password Management",
					"label": _("Password Management"),
					"description": _("Password Management"),
					"onboard": 1,
				}
			]
		}
	]
