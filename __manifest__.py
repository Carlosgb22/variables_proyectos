# -*- coding: utf-8 -*-
{
    "name": "Variables de Proyecto",
    "category": "Productivity",
    "version": "15.0.1.1.0",
    "sequence": -100,
    "description": """Variables de Proyecto""",
    "license": "LGPL-3",
    "author": "Carlos, Daniel, Ernesto",
    "depends": ['base','mail','report_xlsx'],
    "data": [
        "security/grupos.xml",
        "security/ir.model.access.csv",
        "data/reminder_cron.xml",
        "views/proyecto.xml",
        "views/categoria_proyecto.xml",
        "views/categoria_variable.xml",
        "views/variable.xml",
        "views/menu.xml",
        "report/rp_variables.xml",
        "views/permiso_proyecto.xml",
    ],
    "auto_install": True,
    "installable": True,
    "application": True,
}
