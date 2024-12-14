from decoratoren.vereinfache_meine_try_except_bloecke import test, mein_test_mit_prognose


@mein_test_mit_prognose(True)
def importiert_aus_collection():
    from collections import namedtuple
    Foo = namedtuple('Foo', ('x', 'y'))

    print(f" {type(Foo(1,2)) = }")
    print(f" {isinstance(Foo(1,2), tuple) = }")
    test.assertIsInstance(Foo(1,2), tuple)


@mein_test_mit_prognose(True)
def importiert_aus_typing():
    from typing import NamedTuple

    class Foo(NamedTuple):
        x: int
        y: int

    print(f" {type(Foo(1,2)) = }")
    print(f" {isinstance(Foo(1,2), tuple) = }")
    test.assertIsInstance(Foo(1,2), tuple)

# map(Foo._make,  [(1,2), (5,6)])
# Foo(1,2)._asdict()
# Foo(1,2)._replace(x=20)
# Foo(1,2)._replace(x=20, y=1)
# Pixel = namedtuple('Pixel', Point._fields + Color._fields)
# Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
# Account._field_defaults
# Foo = namedtuple('Foo', ('x', 'y'), defaults=[None, 0])
# Point3D = namedtuple('Point3D', Point._fields + ('z',))
""" Docstrings
Book = namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'"""

def new_add(self, obj):
    return Foo(self.x + obj.x, self.y + obj.y)

if __name__ == '__main__':
    # importiert_aus_collection()
    importiert_aus_typing()