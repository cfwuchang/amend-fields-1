from odoo import api,fields,models,_
# from odoo.tools.misc import clean_context, format_date, OrderedSet
class StockMove(models.Model):
    _inherit = "stock.move"

    def movement (self):
        # moves_to_unreserve = OrderedSet()
        for move in self:
            move.quantity_done= move.product_uom_qty