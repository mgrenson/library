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

    def check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        for rec in self:
            if rec.isbn and not rec.check_isbn():
                raise Warning('%s Is an invalid ISBN' % rec.isbn)
