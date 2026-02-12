from dataclasses import dataclass
from typing import Optional, final

# We define the ADT `Order`` similar to `Item` (defined in src/app/models/item.py)
#
# ====
# 
# We want the value of the `short_name` attribute 
# to never change in objects of these types.
# 
# Therefore, we disallow modifying objects of these types 
# using the `@dataclass(frozen=True)` annotation.
# 
# ===
# 
# Each of these types is a product type.
# There's at most one unique value of each of these types
# From the point of view of the data that we want to store
# in these objects.

class OrderBase():
    short_name: str

@final
@dataclass(frozen=True)
class PreOrder(OrderBase):
    short_name = "pre"


@final
@dataclass(frozen=True)
class PostOrder(OrderBase):
    short_name = "post"

type Order = PreOrder | PostOrder


# ==

def parse_order(order: str) -> Optional[Order]:
    """
    Parse `Order` from a `str`.
    """

    match order:
        case PreOrder.short_name:
            return PreOrder()
        case PostOrder.short_name:
            return PostOrder()
        case _:
            return None


def parse_order_default(order: str, default: Order) -> Order:
    """
    Parse `Order` from a `str`.
    
    Return the `default` value if couldn't parse.
    """
    if (parsed := parse_order(order)) is not None:
        return parsed
    return default
