from __future__ import unicode_literals
from nxm import _

def get_data():
	return [
		{
			"label": _("Tools"),
			"icon": "fa fa-star",
            "items": [
				{
					"color": "grey",
					"icon": "octicon octicon-key",
					"type": "formface",
					"name": "Password Management",
					"label": _("Password Management")
				},
				{
					"color": "grey",
					"icon": "octicon octicon-key",
					"type": "formface",
					"name": "Password Category",
					"label": _("Password Category")
				}
            ]
		}
	]
