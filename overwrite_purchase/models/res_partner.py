import re
from odoo import api, models, fields, _
from odoo.exceptions import UserError
from datetime import datetime

EMAIL_REGEX = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})*(\.\w{2,3})+$'
PHONE_REGEX = '^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$'

def regex_validation_message(field, regex, message):
    if field:
        if not re.search(regex, field):
            raise UserError(message)
    return True


def validation_email(email):
    message = _(
        'El correo "{}" no tiene el formato requerido: correo@dominio.dominio o correo@dominio.dominio.dominio')
    return regex_validation_message(email, EMAIL_REGEX, message.format(email))


def validation_phone(phone):
    message = _(
        'El teléfono {} no cumple con el formato. Por favor, escriba los dígitos del ' +
        'teléfono (entre 7 y 13 dígitos). El sistema automáticamente escribirá el ind' +
        'icativo del país, +57 en caso de Colombia.')
    return regex_validation_message(phone, PHONE_REGEX, message.format(phone))


def validation_mobile(mobile):
    message = _(
        'El teléfono celular {} no cumple con el formato. Por favor, escriba los dígi' +
        'tos del léfono (entre 7 y 13 dígitos). El sistema automáticamente escribirá ' +
        'el indicativo del país, +57 en caso de Colombia.')
    return regex_validation_message(mobile, PHONE_REGEX, message.format(mobile))


class Partner(models.Model):
    _inherit = 'res.partner'

    user_update_rut = fields.Many2one('res.users', string='Modificó RUT', required=False, copy=False)
    date_update_rut = fields.Datetime(string='Fecha Modificó RUT', copy=False)
    user_update_camara = fields.Many2one('res.users', string='Modificó Cámara de Comercio', required=False, copy=False)
    date_update_camara = fields.Datetime(string='Fecha Modificó Cámara de Comercio', copy=False)
    user_update_cedula_representante = fields.Many2one('res.users', string='Modificó Cédula Representante Legal', required=False, copy=False)
    date_update_cedula_representante = fields.Datetime(string='Fecha Modificó Cédula Representante Legal', copy=False)
    user_update_bancaria = fields.Many2one('res.users', string='Modificó Certificación Bancaria', required=False, copy=False)
    date_update_bancaria = fields.Datetime(string='Fecha Modificó Certificación Bancaria', copy=False)

    user_update_adj_1 = fields.Many2one('res.users', string='Modificó Adjunto 1', required=False, copy=False)
    date_update_adj_1 = fields.Datetime(string='Fecha Modificó Adjunto 1', copy=False)
    user_update_adj_2 = fields.Many2one('res.users', string='Modificó Adjunto 2', required=False, copy=False)
    date_update_adj_2 = fields.Datetime(string='Fecha Modificó Adjunto 2', copy=False)
    user_update_adj_3 = fields.Many2one('res.users', string='Modificó Adjunto 3', required=False, copy=False)
    date_update_adj_3 = fields.Datetime(string='Fecha Modificó Adjunto 3', copy=False)
    user_update_adj_4 = fields.Many2one('res.users', string='Modificó Adjunto 4', required=False, copy=False)
    date_update_adj_4 = fields.Datetime(string='Fecha Modificó Adjunto 4', copy=False)
    user_update_adj_5 = fields.Many2one('res.users', string='Modificó Adjunto 5', required=False, copy=False)
    date_update_adj_5 = fields.Datetime(string='Fecha Modificó Adjunto 5', copy=False)
    user_update_adj_6 = fields.Many2one('res.users', string='Modificó Adjunto 6', required=False, copy=False)
    date_update_adj_6 = fields.Datetime(string='Fecha Modificó Adjunto 6', copy=False)

    rut = fields.Binary(string='RUT', copy=False, tracking=1, track_visibility='onchange')
    rut_name = fields.Char("Normbre Documento RUT", tracking=1)
    camara = fields.Binary(string='Cámara de Comercio', copy=False, tracking=1, track_visibility='onchange')
    camara_name = fields.Char("Normbre Documento Cámara de Comercio", tracking=1)
    cedula_representante = fields.Binary(string='Cédula Representante Legal', copy=False, tracking=1, track_visibility='onchange')
    cedula_representante_name = fields.Char("Normbre Documento Cédula Representante Legal", tracking=1)
    bancaria = fields.Binary(string='Certificación Bancaria', copy=False, tracking=1, track_visibility='onchange')
    bancaria_name = fields.Char("Normbre Documento Certificación Bancaria", tracking=1)

    adj_1 = fields.Binary(string='Adjunto 1', copy=False, tracking=1, track_visibility='onchange')
    adj_1_name = fields.Char("Normbre Documento Adjunto 1", tracking=1)
    adj_2 = fields.Binary(string='Adjunto 2', copy=False, tracking=1, track_visibility='onchange')
    adj_2_name = fields.Char("Normbre Documento Adjunto 2", tracking=1)
    adj_3 = fields.Binary(string='Adjunto 3', copy=False, tracking=1, track_visibility='onchange')
    adj_3_name = fields.Char("Normbre Documento Adjunto 3", tracking=1)
    adj_4 = fields.Binary(string='Adjunto 4', copy=False, tracking=1, track_visibility='onchange')
    adj_4_name = fields.Char("Normbre Documento Adjunto 4", tracking=1)
    adj_5 = fields.Binary(string='Adjunto 5', copy=False, tracking=1, track_visibility='onchange')
    adj_5_name = fields.Char("Normbre Documento Adjunto 5", tracking=1)
    adj_6 = fields.Binary(string='Adjunto 6', copy=False, tracking=1, track_visibility='onchange')
    adj_6_name = fields.Char("Normbre Documento Adjunto 6", tracking=1)

    aditional_fields = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6')], string='Archivos Adicionales',
        copy=False)

    @api.onchange('x_studio_rut')
    def tracking_rut(self):
        self.user_update_rut = self.env.uid
        self.date_update_rut = datetime.now()

    @api.onchange('x_studio_camara_de_comercio')
    def tracking_camara(self):
        self.user_update_camara = self.env.uid
        self.date_update_camara = datetime.now()

    @api.onchange('x_studio_cedula_representante_legal')
    def tracking_cedula_representante(self):
        self.user_update_cedula_representante = self.env.uid
        self.date_update_cedula_representante = datetime.now()

    @api.onchange('x_studio_certificacion_bancaria')
    def tracking_bancaria(self):
        self.user_update_bancaria = self.env.uid
        self.date_update_bancaria = datetime.now()
    
    @api.onchange('adj_1')
    def tracking_adj_1(self):
        self.user_update_adj_1 = self.env.uid
        self.date_update_adj_1 = datetime.now()
    
    @api.onchange('adj_2')
    def tracking_adj_2(self):
        self.user_update_adj_2 = self.env.uid
        self.date_update_adj_2 = datetime.now()

    @api.onchange('adj_3')
    def tracking_adj_3(self):
        self.user_update_adj_3 = self.env.uid
        self.date_update_adj_3 = datetime.now()
    
    @api.onchange('adj_4')
    def tracking_adj_4(self):
        self.user_update_adj_4 = self.env.uid
        self.date_update_adj_4 = datetime.now()

    @api.onchange('adj_5')
    def tracking_adj_5(self):
        self.user_update_adj_5 = self.env.uid
        self.date_update_adj_5 = datetime.now()
    
    @api.onchange('adj_6')
    def tracking_adj_6(self):
        self.user_update_adj_6 = self.env.uid
        self.date_update_adj_6 = datetime.now()

    def check_name(self, vals):
        if vals.get('company_id', False):
            company_id = vals.get('company_id', False)
        else:
            company_id = self.company_id.id
        existing_query = [
            ('name', '=', vals['name']),
            ('id', '!=', self.id),
            ('company_id', '=', company_id)
        ]
        partner_model = self.env['res.partner']
        exists = partner_model.search(existing_query)
        if exists:
            message = _(
                'El contacto con nombre "{}" ya esta creado en la empresa, modifique' +
                ' el nombre')
            raise UserError(message.format(vals['name']))

    def check_vat(self, vals):
        if vals.get('company_id', False):
            company_id = vals.get('company_id', False)
        else:
            company_id = self.company_id.id
        if vals.get('parent_id', False):
            parent_id = vals.get('parent_id', False)
        else:
            parent_id = self.parent_id.id
        if not parent_id:
            existing_query = [
                ('vat', '=', vals['vat']),
                ('id', '!=', self.id),
                ('company_id', '=', company_id)
            ]
            partner_model = self.env['res.partner']
            exists = partner_model.search(existing_query)
            if exists:
                message = _(
                    'El proveedor con identificación "' + vals['vat'] +
                    '" ya esta creado en la empresa, modifique la identificación.')
                raise UserError(message.format(vals['vat']))

    def do_validations(self, vals):
        validation_email(vals.get('email', False))
        validation_phone(vals.get('phone', False))
        validation_mobile(vals.get('mobile', False))

    @ api.model
    def write(self, vals):
        if vals.get('name', False):
            self.check_name(vals)
            vals['name'] = vals['name'].title()
        if vals.get('vat', False):
            self.check_vat(vals)
        self.do_validations(vals)
        return super(Partner, self).write(vals)
