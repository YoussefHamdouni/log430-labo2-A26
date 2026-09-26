"""
Report view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.template_view import get_template, get_param
from controllers.order_controller import get_report_best_sellers

def show_highest_spending_users():
    """ Show report of highest spending users """
    return get_template("<h2>Les plus gros acheteurs</h2><p>(TODO: Liste avec nom, total depensé)</p>")

def show_best_sellers():
    """ Show report of best selling products """
    products = get_report_best_sellers()
    rows = [f"<li>{name} : {quantity} vendu(s)</li>" for name, quantity in products]
    return get_template(f"<h2>Les articles les plus vendus</h2><ul>{''.join(rows)}</ul>")