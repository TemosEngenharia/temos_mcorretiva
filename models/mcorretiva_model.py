# -*- coding: utf-8 -*-
# ATT Generated at 2017-06-06 18:56:00

from odoo import models, fields, api

class MCorretivaForm(models.Model):
    _name = 'mcorretiva.mco_form'
    _rec_name = 'mco_task_request_number'
    _sql_constraints = [('mcorretiva.mco_form', 'unique (xml_source_filename)', 'XML já foi importado anteriormente!')]

    mco_form_date_time = fields.Datetime(string = u'Data do Formulário')
    mco_form_report_flag = fields.Boolean(string = u'Relatório enviado', default = False)
    xml_source_filename = fields.Char(string = u'XML importado!!!', default = '')
    mco_location_date = fields.Datetime(string = u'Data da Localização')
    mco_form_checkin_call_datetime = fields.Datetime(string = u'Horário da ligação de Check-in')
    mco_form_checkout_call_datetime = fields.Datetime(string = u'Horário da ligação de Check-out')
    mco_task_external_creation_date = fields.Datetime(string = u'Início SLA')
    mco_delta_sla = fields.Char(string = u'Tempo Delta da SLA')
    mco_date_from_epoch = fields.Char(string = u'Data Epoch da Entrada')
    mco_location_address = fields.Char(string = u'Endereço')
    mco_location_x = fields.Char(string = u'longitude')
    mco_location_y = fields.Char(string = u'latitude')
    mco_location_date_from_epoch = fields.Char(string = u'Data Formulário')
    mco_form_name = fields.Char(string = u'Formulário')
    mco_form_version = fields.Integer(string = u'Versão')
    mco_form_checkin_call_timing = fields.Integer(string = u'Duração da ligação Check-in?')
    mco_form_checkin_attendant_by = fields.Char(string = u'Atendente que realizou o Check-in na PA')
    mco_form_station_responsible_name = fields.Char(string = u'Nome do responsável pelo Posto')
    mco_form_station_responsible_email = fields.Char(string = u'E-mail do posto')
    mco_form_station_first_line_flag = fields.Integer(string = u'PistaP')
    mco_form_station_first_line_activities = fields.Char(string = u'Atividades Realizadas na Pista Principal')
    mco_form_station_sec_line_flag = fields.Integer(string = u'PistaSec')
    mco_form_station_sec_line_activities = fields.Char(string = u'Atividades realizadas na Pista Secundária')
    mco_form_station_server_flag = fields.Integer(string = u'Serv')
    mco_form_station_server_activities = fields.Char(string = u'Atividades realizadas no Servidor')
    mco_form_station_roof_flag = fields.Integer(string = u'Teto')
    mco_form_station_equipment_flag = fields.Integer(string = u'Equip')
    mco_form_station_trouble_found = fields.Char(string = u'Problema encontrado no Local')
    mco_form_checkout_call_timing = fields.Integer(string = u'Duração da Ligação de Check-out')
    mco_form_checkout_attendant_by = fields.Char(string = u'Atendente que realizou o Check-out na PA')
    mco_form_employee_firstname = fields.Char(string = u'Nome do Funcionário')
    mco_form_employee_number = fields.Char(string = u'Nr. do Funcionário')
    mco_form_employee_driver_id = fields.Integer(string = u'Código do Motorista')
    mco_form_employee_group_name = fields.Char(string = u'Grupo do Funcionário')
    mco_task_number = fields.Char(string = u'NÚMERO DA TAREFA')
    mco_task_request_number = fields.Char(string = u'NÚMERO DO CHAMADO')
    mco_task_data1 = fields.Char(string = u'Data1')
    mco_task_data2 = fields.Char(string = u'Data2')
    mco_task_type_code = fields.Char(string = u'TaskTypeCode')
    mco_task_type_name = fields.Char(string = u'TaskTypeName')
    mco_task_category_code = fields.Char(string = u'TaskCategoryCode')
    mco_task_category_name = fields.Char(string = u'TaskCategoryName')
    mco_task_customer_city = fields.Char(string = u'Cidade')
    mco_task_customer_number = fields.Char(string = u'Código do Posto')
    mco_task_customer_address_number = fields.Char(string = u'Nr')
    mco_task_customer_name = fields.Char(string = u'Nome do Posto')
    mco_task_customer_state = fields.Char(string = u'Estado')
    mco_task_customer_street = fields.Char(string = u'Endereço')
    mco_form_file_pic01_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC01 - EPI')
    mco_form_file_pic01_img = fields.Char(related='mco_form_file_pic01_id.mco_form_file_data')
    mco_form_file_pic02_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC02 - EPC Pista Principal')
    mco_form_file_pic02_img = fields.Char(related='mco_form_file_pic02_id.mco_form_file_data')
    mco_form_file_pic03_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC03 - Selo de Manutenção Pista Principal antes do atendimento')
    mco_form_file_pic03_img = fields.Char(related='mco_form_file_pic03_id.mco_form_file_data')
    mco_form_file_pic04_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC04 - Armário Fechado com Moldura Pista Principal antes do atendimento')
    mco_form_file_pic04_img = fields.Char(related='mco_form_file_pic04_id.mco_form_file_data')
    mco_form_file_pic05_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC05 - Armário Aberto Pista Principal antes do atendimento')
    mco_form_file_pic05_img = fields.Char(related='mco_form_file_pic05_id.mco_form_file_data')
    mco_form_file_pic06_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC06 - Armário Aberto Pista Principal após atendimento')
    mco_form_file_pic06_img = fields.Char(related='mco_form_file_pic06_id.mco_form_file_data')
    mco_form_file_pic07_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC07 - Armário Fechado com Moldura Pista Principal após atendimento')
    mco_form_file_pic07_img = fields.Char(related='mco_form_file_pic07_id.mco_form_file_data')
    mco_form_file_pic08_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC08 - Selo de Manutenção Pista Principal após atendimento')
    mco_form_file_pic08_img = fields.Char(related='mco_form_file_pic08_id.mco_form_file_data')
    mco_form_file_pic09_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC09 - EPC Pista Secundária')
    mco_form_file_pic09_img = fields.Char(related='mco_form_file_pic09_id.mco_form_file_data')
    mco_form_file_pic10_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC10 - Selo de Manutenção Pista Secundária antes do atendimento')
    mco_form_file_pic10_img = fields.Char(related='mco_form_file_pic10_id.mco_form_file_data')
    mco_form_file_pic11_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC11 - Armário Fechado com Moldura Pista Secundária antes do atendimento')
    mco_form_file_pic11_img = fields.Char(related='mco_form_file_pic11_id.mco_form_file_data')
    mco_form_file_pic12_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC12 - Armário Aberto Pista Secundária antes do atendimento')
    mco_form_file_pic12_img = fields.Char(related='mco_form_file_pic12_id.mco_form_file_data')
    mco_form_file_pic13_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC13 - Armário Aberto Pista Secundária após atendimento')
    mco_form_file_pic13_img = fields.Char(related='mco_form_file_pic13_id.mco_form_file_data')
    mco_form_file_pic14_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC14 - Armário Fechado com Moldura Pista Secundária após atendimento')
    mco_form_file_pic14_img = fields.Char(related='mco_form_file_pic14_id.mco_form_file_data')
    mco_form_file_pic15_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC15 - Selo de Manutenção Pista Secundária após atendimento')
    mco_form_file_pic15_img = fields.Char(related='mco_form_file_pic15_id.mco_form_file_data')
    mco_form_file_pic16_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC16 - Selo Manutenção Rack do Servidor antes do atendimento')
    mco_form_file_pic16_img = fields.Char(related='mco_form_file_pic16_id.mco_form_file_data')
    mco_form_file_pic17_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC17 - Rack do Servidor fechado antes do atendimento')
    mco_form_file_pic17_img = fields.Char(related='mco_form_file_pic17_id.mco_form_file_data')
    mco_form_file_pic18_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC18 - Rack do Servidor aberto antes do atendimento')
    mco_form_file_pic18_img = fields.Char(related='mco_form_file_pic18_id.mco_form_file_data')
    mco_form_file_pic19_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC19 - Rack do Servidor aberto após atendimento')
    mco_form_file_pic19_img = fields.Char(related='mco_form_file_pic19_id.mco_form_file_data')
    mco_form_file_pic20_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC20 - Rack do Servidor fechado após atendimento')
    mco_form_file_pic20_img = fields.Char(related='mco_form_file_pic20_id.mco_form_file_data')
    mco_form_file_pic21_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC21 - Selo Manutenção Rack do Servidor após atendimento')
    mco_form_file_pic21_img = fields.Char(related='mco_form_file_pic21_id.mco_form_file_data')
    mco_form_file_pic22_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC22 - Luminárias Acessas Pista Principal antes do atendimento')
    mco_form_file_pic22_img = fields.Char(related='mco_form_file_pic22_id.mco_form_file_data')
    mco_form_file_pic23_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC23 - Luminárias Acessas Pista Principal após atendimento')
    mco_form_file_pic23_img = fields.Char(related='mco_form_file_pic23_id.mco_form_file_data')
    mco_form_file_pic24_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC24 - Luminárias Acessas Pista Secundária antes do atendimento')
    mco_form_file_pic24_img = fields.Char(related='mco_form_file_pic24_id.mco_form_file_data')
    mco_form_file_pic25_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC25 - Luminárias Acessas Pista Secundária após atendimento')
    mco_form_file_pic25_img = fields.Char(related='mco_form_file_pic25_id.mco_form_file_data')
    mco_form_file_pic26_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC26 - Teste de Abastecimento Pista Principal')
    mco_form_file_pic26_img = fields.Char(related='mco_form_file_pic26_id.mco_form_file_data')
    mco_form_file_pic27_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC27 - Teste de Abastecimento Pista Secundária')
    mco_form_file_pic27_img = fields.Char(related='mco_form_file_pic27_id.mco_form_file_data')
    mco_form_file_pic28_id = fields.Many2one('mcorretiva.mco_form_files', u'PIC28 - Assinatura do Responsável pelo posto')
    mco_form_file_pic28_img = fields.Char(related='mco_form_file_pic28_id.mco_form_file_data')
    mco_form_equipment_ids = fields.One2many('mcorretiva.mco_form_equipments', 'mco_form_equip_id', u'Equip Id')

class MCorretivaFormFiles(models.Model):
    _name = 'mcorretiva.mco_form_files'
    _rec_name = 'id'

    mco_form_file_guid = fields.Char(string = u'Guid da Foto')
    mco_form_filename = fields.Char(string = u'Nome do arquivo da Foto')
    mco_form_file_description = fields.Char(string = u'Descrição da Foto')
    mco_form_file_data = fields.Char(string = u'Foto')
    mco_form_file_ids = fields.One2many('mcorretiva.mco_form_files', 'mco_form_file_id', u'Form File Id')
    mco_form_file_id = fields.Many2one('mcorretiva.mco_form', u'Fotos', ondelete = 'cascade', required = True)

class MCorretivaFormEquipments(models.Model):
    _name = 'mcorretiva.mco_form_equipments'
    _rec_name = 'mco_form_equip_name'

    mco_form_equip_name = fields.Char(string = u'Equipamento', default = '')
    mco_form_equip_action = fields.Char(string = u'Ação', default = '')
    mco_form_equip_location = fields.Char(string = u'Local de Instalação ou Retirada', default = '')
    mco_form_equip_serial_number = fields.Char(string = u'Número de Série', default = '')
    mco_form_equip_id = fields.Many2one('mcorretiva.mco_form', u'Lista de Equipamentos', ondelete = 'cascade', required = True)
