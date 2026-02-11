from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class PreOrder:
    pass


@dataclass
class PostOrder:
    pass


# Each of these other types is technically a product type. However, since none of them
# contains any fields, there's at most one value of each of these three types.
#
# We use this 'Order' ADT in the function below as a type of an argument.
# This way, we tell the type checker that the argument must be an object
# of one of these three classes. In other words, the value of the argument
# must be of one of these three types.

# to specify the two ways (orders) of [Tree traversal](https://en.wikipedia.org/wiki/Tree_traversal)
# we have not a binary tree

type Order = PreOrder | PostOrder


class OrderShortName(str, Enum):
    pre_order = "pre"
    post_order = "post"


# ==

# Pure functions that parse Order from a str


def parse_order(order: str) -> Optional[Order]:
    """
    Parse `Order` from a `str`.
    """

    match order:
        case OrderShortName.pre_order:
            return PreOrder()
        case OrderShortName.post_order:
            return PostOrder()
        case _:
            return None


def parse_order_default(order: str, default: Order) -> Order:
    """
    Parse `Order` from a `str`.
    Use the `default` value if couldn't parse.
    """
    if (parsed := parse_order(order)) is not None:
        return parsed
    return default
