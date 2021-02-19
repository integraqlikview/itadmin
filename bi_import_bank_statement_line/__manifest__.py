# -*- coding: utf-8 -*-

{
    'name': 'Importar líneas de extracto bancario desde un archivo Excel / CSV',
    'version': '14.0.0.1',
    'summary': 'Este módulo le ayuda a importar la línea de extracto bancario en Odoo usando Excel y archivo CSV ',
    'description': """

Importar líneas de extracto bancario de Excel
Importación de líneas de extracto de efectivo de Excel
Este módulo le permite importar líneas de extracto bancario desde el archivo de Excel.
Este módulo permitirá la importación de extractos bancarios y de efectivo de EXCEL.
Este módulo permitirá la importación de extractos de caja de Excel.
Importar líneas de extracto bancario de CSV
Importar líneas de extracto de caja de CSV
Este módulo le permite importar líneas de extracto bancario desde un archivo CSV.
Este módulo permitirá Importar estados de cuenta bancarios y de efectivo de CSV.
Este módulo permitirá la importación de extractos de caja de CSV.
Importación de extracto bancario de Excel
Importación de extracto bancario CSV
Importación de extracto de efectivo de Excel
Importación de extracto de caja de CSV
línea de extracto a granel de importación, líneas de extracto de importación
Este módulo se usa para importar líneas de extracto bancario a granel del archivo de Excel. Importar líneas de extracto de archivo CSV o Excel.
Importar declaraciones, Importar línea de extracto, Importar extracto bancario, Agregar extracto bancario de Excel.Añadir líneas de extracto bancario de Excel. Agregar archivo CSV.Importar datos de factura. Importar archivo de Excel

Importar líneas de extracto bancario de XLS
Importar líneas de extracto de caja de XLS
Este módulo le permite importar líneas de extractos bancarios del archivo XLS.
Este módulo permitirá la importación de estados de cuenta bancarios y de efectivo de XLS.
Este módulo permitirá la importación de extractos de caja de XLS.
xls importación de extracto bancario
xls Importación de extracto de caja

    """,
    'author': 'IT Admin',
    "price": 0.00,
    "currency": 'USD',
    'website': 'www.itadmin.com.mx',
    'depends': ['base','account'],
    'data': [
    		'security/ir.model.access.csv',
    		"views/bank_statement.xml"
             ],
	'qweb': ['static/src/xml/account_reconciliation.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
