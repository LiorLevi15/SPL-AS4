# DAO
from DTO import Hat, Supplier, Order


class _Hats:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, _hat):
        self.conn.execute("insert into hats(id, topping, supplier, quantity) VALUES (?, ?, ?, ?)",
                          [_hat.id, _hat.topping, _hat.supplier, _hat.quantity])

    def find(self, _topping):
        c = self.conn.cursor()
        c.execute("select id, topping, supplier, quantity from hats where topping = ?", [_topping])
        return Hat(*c.fetchone())

    def order(self, _topping):
        c = self.conn.cursor()
        c.execute("select id,  supplier, quantity from hats where topping = ? order by supplier", [str(_topping)])
        _hat = c.fetchone()
        if _hat[2] == 1:
            c.execute("delete from hats where id = ?", [_hat[0]])
        else:
            c.execute("update hats set quantity =? where id = ?", [_hat[2]-1, _hat[0]])
        return _hat


class _Suppliers:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, _supplier):
        self.conn.execute("insert into suppliers(id, name) VALUES (?, ?)",
                          [_supplier.id, _supplier.name])

    def find(self, _id):
        c = self.conn.cursor()
        c.execute("select id, name from suppliers where id = ?", [_id])
        return Supplier(*c.fetchone())


class _Orders:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, _order):
        self.conn.execute("insert into orders(id, location, hat) VALUES (?, ?, ?)",
                          [_order.id, _order.location, _order.hat])

    def find(self, _id):
        c = self.conn.cursor()
        c.execute("select id, name from orders where id = ?", [_id])
        return Order(*c.fetchone())
