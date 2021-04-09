# -*- coding: utf-8 -*-

from odoo import models, fields, api
DEFAULT_CFDI_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'

class AccountInvoice(models.Model):
    _inherit = 'account.move'
        
    attachment_id = fields.Many2one("ir.attachment", 'Attachment')
    l10n_mx_edi_cfdi_uuid_cusom = fields.Char(string='Fiscal Folio UUID', copy=False, readonly=True, compute="_compute_cfdi_uuid", store=True)
    
    
    @api.depends('edi_document_ids')
    def _compute_cfdi_uuid(self):
        for inv in self:
            attachment_id = inv._get_l10n_mx_edi_signed_edi_document()
            if not attachment_id:
#                 inv.l10n_mx_edi_cfdi_uuid_cusom=False
                attachments = inv.attachment_ids
                results = []
                results += [rec for rec in attachments if rec.name.endswith('.xml')]
                if results:
                    domain = [('res_id', '=', inv.id),
                              ('res_model', '=', inv._name),
                              ('name', '=', results[0].name)]
                    
                    attachment = inv.env['ir.attachment'].search(domain)[0]
                    for edi in inv.edi_document_ids:
                        if not edi.attachment_id:
                            vals=({'attachment_id':attachment.id,'move_id':inv.id})
                            edi.write(vals)
                    #inv.write({'l10n_mx_edi_cfdi_name': attachment.name})
                
            else:
                cfdi_infos = inv._l10n_mx_edi_decode_cfdi()
                inv.l10n_mx_edi_cfdi_uuid_cusom = cfdi_infos.get('UUID')
    
   