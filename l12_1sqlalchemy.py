import sqlalchemy
import sqlalchemy.orm


class Base(sqlalchemy.orm.DeclarativeBase):
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)

    engine = sqlalchemy.engine.create_engine('postgresql://belhard:belhard@localhost:5432/belhard')
    session = sqlalchemy.orm.sessionmaker(bind=engine)

    @sqlalchemy.orm.declared_attr
    def __tablename__(cls):
        return ''.join([f'_{i.lower()}' if i.isupper() else i for i in cls.__name__]).strip('_')


class Shop(Base):
    address = sqlalchemy.Column(sqlalchemy.VARCHAR(128), nullable=False)


class ShopProduct(Base):
    # __tablename__ = 'shop_product'

    product_id = sqlalchemy.Column(sqlalchemy.ForeignKey('product.id'))
    shop_id = sqlalchemy.Column(sqlalchemy.ForeignKey(Shop.id))
    count = sqlalchemy.Column(sqlalchemy.INTEGER, default=0, nullable=False)

    __table_args__ = (
        sqlalchemy.UniqueConstraint('product_id', 'shop_id'),
    )


class Product(Base):
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(64), unique=True, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.VARCHAR(256))
    slug = sqlalchemy.Column(sqlalchemy.VARCHAR(64))
    category_id = sqlalchemy.Column(sqlalchemy.ForeignKey('category.id'))
    price = sqlalchemy.Column(sqlalchemy.DECIMAL(10, 2))
    image = sqlalchemy.Column(sqlalchemy.VARCHAR(256))


class Category(Base):
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(64), unique=True, nullable=False)
    slug = sqlalchemy.Column(sqlalchemy.VARCHAR(64), unique=True, nullable=False)
    parent_id = sqlalchemy.Column(sqlalchemy.ForeignKey('category.id'))


class Customer(Base):
    username = sqlalchemy.Column(sqlalchemy.VARCHAR(64), unique=True, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.VARCHAR(120), unique=True, )
    role_id = sqlalchemy.Column(sqlalchemy.ForeignKey('role.id'))
    refferer_id = sqlalchemy.Column(sqlalchemy.ForeignKey('customer.id'))
    points = sqlalchemy.Column(sqlalchemy.INTEGER, default=0)


class Role(Base):
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(64), unique=True, nullable=False)

# alembic init alembic
# in alembic.ini change sqlalchemy.url
# in alembic/env.py change target_metadata
# alembic revision --autogenerate -m "initial"
# alembic upgrade head
