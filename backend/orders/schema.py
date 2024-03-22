import graphene
from graphene_django.types import DjangoObjectType
from orders.models import Order, Product, OrderHistory


class OrderType(DjangoObjectType):
    class Meta:
        model = Order


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class OrderHistoryType(DjangoObjectType):
    class Meta:
        model = OrderHistory


class Query(graphene.ObjectType):
    orders = graphene.List(OrderType)
    products = graphene.List(ProductType)
    order_histories = graphene.List(OrderHistoryType)

    def resolve_orders(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Log in to see your orders')
        return Order.objects.all()

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_order_histories(self, info):
        return OrderHistory.objects.all()


schema = graphene.Schema(query=Query)
