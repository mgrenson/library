# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    _inherits = {'product.template': 'product_id'}

    product_id = fields.Many2one('product.template',
                                  string='Related product',
                                  required=True,
                                  ondelete='restrict',
                                  # auto_join=True,  # See later if need to auto join the 2 tables
                                  )
    isbn = fields.Char('ISBN')
    date_published = fields.Date('Date published')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')
