# Repository
import sqlite3
import sys
from DAO import _Hats, _Orders, _Suppliers
import atexit


class _Repository:

    def __init__(self, db_file):
        self._conn=sqlite3.connect(db_file);
        self.hats=_Hats(self._conn);
        self.suppliers=_Suppliers(self._conn);
        self.orders=_Orders(self._conn);

    def _close(self):
        self._conn.commit();
        self._conn.close();

    def create_tables(self):
        cur = self._conn.cursor()
        cur.executescript("""
                create table suppliers( id INTEGER PRIMARY KEY, name STRING NOT NULL);
                
                create table hats( id INTEGER PRIMARY KEY, topping STRING NOT NULL,
                    supplier INEGER REFERENCES suppliers(id), quantity INTGER NOY NULL);
                    
                create table orders(id INTEGER PRIMARY KEY, location STRING NOT NULL,
                    hat INTEGER REFERENCES hats(id));
                """)


# the repository singleton
repo = _Repository(sys.argv[4])
atexit.register(repo._close)