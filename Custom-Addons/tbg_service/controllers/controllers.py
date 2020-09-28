# -*- coding: utf-8 -*-
from odoo import http


class TobagoService(http.Controller):
    @http.route('/tbg_service/order/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/tbg_service/order/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('tbg_service.listing', {
            'root': '/tbg_service/order',
            'objects': http.request.env['tbg_service.order'].search([]),
        })

    @http.route('/tbg_service/order/objects/<model("tbg_service.order"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('order.object', {
            'object': obj
        })