from odoo import api, fields, models
from datetime import datetime

class ReportKomponen(models.AbstractModel):
    _name = 'report.komponen_odoo.komponen'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, obj):
        sheet = workbook.add_worksheet('Report Komponen')

        # Style
        text_top_style = workbook.add_format({
            'font_size': 10, 'bold': True ,
            'font_color' : 'white', 
            'bg_color': '#000080', 
            'valign': 'vcenter', 
            'text_wrap': True})
        
        text_header_style = workbook.add_format({'font_size': 10,
            'bold': True ,
            'font_color' : 'white', 
            'bg_color': 'gray',
            'valign': 'vcenter', 
            'text_wrap': True, 
            'align': 'center'})
        
        text_style = workbook.add_format({'font_size': 10, 
            'valign': 'vcenter', 
            'text_wrap': True, 
            'align': 'center'})

        text_style2 = workbook.add_format({'font_size': 10, 
            'valign': 'vcenter', 
            'text_wrap': True, 
            'align': 'left'})

        number_style = workbook.add_format({'num_format': '#,##0',
            'font_size': 12, 
            'align': 'right', 
            'valign': 'vcenter', 
            'text_wrap': True}) 
        header = [
            'NAMA ITEM',
            'TANGGAL MULAI PENGERJAAN',
            'NAMA KOMPONEN',
            'WAKTU PENGERJAAN KOMPONEN',
            'BOBOT PERSENTASE KOMPONEN'
        ]

        sheet.write_row(0, 0, header, text_header_style)

        # Column Size
        sheet.set_column('A:E', 25)


        komponen = self.env['master.item']

        row = 1
        for i in komponen:
            sheet.write(row, 0, i.nama_item, text_style)
            sheet.write(row, 1, i.mulai_pengerjaan.strftime('%d-%m-%Y'), text_style)
            sheet.write(row, 2, i.nama_komponen, text_style)
            sheet.write(row, 3, i.waktu_pengerjaan, text_style)
            sheet.write(row, 4, i.bobot_persen, text_style)
            row += 1