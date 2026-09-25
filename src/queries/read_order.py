"""
Orders (read-only model)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from db import get_sqlalchemy_session, get_redis_conn
from sqlalchemy import desc
from models.order import Order

def get_order_by_id(order_id):
    """Get order by ID from Redis"""
    r = get_redis_conn()
    return r.hgetall(order_id)

def get_orders_from_mysql(limit=9999):
    """Get last X orders"""
    session = get_sqlalchemy_session()
    return session.query(Order).order_by(desc(Order.id)).limit(limit).all()

def get_orders_from_redis(limit=9999):
    """Get last X orders from Redis"""
    r = get_redis_conn()
    keys = r.keys("order:*")

    ids = sorted((int(k.split(":")[1]) for k in keys), reverse=True)[:limit]
    pipe = r.pipeline()
    for order_id in ids:
        pipe.hgetall(f"order:{order_id}")
    results = pipe.execute()

    orders = []
    for order_id, data in zip(ids, results):
        if data:
            data["id"] = int(data.get("id", order_id))
            data["user_id"] = int(data["user_id"])
            data["total_amount"] = float(data["total_amount"])
            orders.append(data)
    return orders

def get_highest_spending_users():
    """Get report of best selling products"""
    # TODO: écrivez la méthode
    # triez le résultat par nombre de commandes (ordre décroissant)
    return []