# -*- coding: utf-8 -*-
from odoo import http


class Library(http.Controller):
    @http.route('/library/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/library/books/', auth='public')
    def list(self, **kw):
        return http.request.render('library.book_list', {
            'root': '/library',
            'books': http.request.env['library.book'].search([]),
        })

    @http.route('/library/books/<model("library.book"):obj>/', auth='public')
    def detail(self, obj, **kw):
        return http.request.render('library.book_detail', {
            'book': obj
        })
