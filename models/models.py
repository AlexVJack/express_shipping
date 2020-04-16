# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StockMove(models.Model):
    '''Inserting Express Shipping checkbox into Stock Move'''
    _inherit = "stock.move"
    express_shipping = fields.Boolean('Express Shipping', default=False)


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def split_delivery(self):
        """Splits delivery order into two orders - express and usual"""        
        count_checks = 0
        count_lines = 0
        for picking in self:
            for move in picking.move_lines:
                count_lines += 1 
                if move.express_shipping:
                    count_checks += 1
        if count_lines > 1 and count_checks > 0 and count_lines != count_checks:          
            for picking in self:
                new_picking = picking.copy()
                for move in picking.move_lines:
                    if not move.express_shipping:
                        move.state = 'draft'
                        move.unlink()
                for move in new_picking.move_lines:
                    if move.express_shipping:
                        move.state = 'draft'
                        move.unlink()
                    else:
                        move._action_confirm()
                        move._action_assign()
