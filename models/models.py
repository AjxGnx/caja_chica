# -*- coding: utf-8 -*-

from odoo import models, fields, api

class salida(models.Model):
	# nombre del modele - nombre de la clase
    _name = 'caja_chica.salida'

    usuario = fields.Char()
    monto = fields.Integer()
    descripcion = fields.Char()
    fecha = fields.Datetime()
    # fecha_registro = fields.Date(auto_now_add=True, auto_now=False)

class entrada(models.Model):
    
    _name = 'caja_chica.entrada'

    usuario= fields.Char()
    monto= fields.Integer()
    descripcion= fields.Char()
    fecha= fields.Datetime()
        



