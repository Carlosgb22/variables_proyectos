# -*- coding: utf-8 -*-
from odoo import models

class reporteXlsx(models.AbstractModel):
    _name = 'report.variables_productos.report_variable_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, proyecto):
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})

        for obj in proyecto:
            sheet = workbook.add_worksheet(obj.nombre)
            row = 3
            col = 3
            sheet.set_column('D:D', 12)
            sheet.set_column('E:E', 13)
            row += 1
            sheet.merge_range(row, col, row, col + 1, 'ID Card', format_1)
            row += 1
            sheet.write(row, col, 'Nombre', bold)
            sheet.write(row, col + 1, obj.nombre)
            row += 1
            sheet.write(row, col, 'Categoria', bold)
            for categoria in obj.categoria:
                sheet.write(row, col + 1, categoria.nombre)
                row+=1
            sheet.write(row, col, 'Variables', bold)
            for variable in obj.variables:
                sheet.write(row, col + 1, variable.nombre)
                row+=1
            row += 2
            sheet.merge_range(row, col, row + 1, col + 1, '', format_1)
