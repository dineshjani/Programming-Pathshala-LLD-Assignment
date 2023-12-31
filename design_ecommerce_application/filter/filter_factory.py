from design_ecommerce_application.data.filter_details import FilterDetails
from design_ecommerce_application.filter.product_filter import ProductFilter
from design_ecommerce_application.filter.idle_filter import IdleFilter
from design_ecommerce_application.filter.price_based_filter import PriceBasedFilter
from design_ecommerce_application.filter.rating_based_filter import RatingBasedFilter
from design_ecommerce_application.filter.pay_on_filter import PayOnDelFilter


class FilterFactory:
    """
    chaining design pattern
    """
    @staticmethod
    def get_product_filter(filter_details:FilterDetails):
        filter: ProductFilter = IdleFilter()
        if filter_details.price_filter is not None:
            filter:ProductFilter = PriceBasedFilter(filter_details.price_filter.get("upper_cap_price"), filter)
        if filter_details.rating_filter is not None:
            filter:ProductFilter = RatingBasedFilter(filter_details.rating_filter.get("min_rating"), filter)
        if filter_details.pay_on_delivery is not None:
            filter:ProductFilter = PayOnDelFilter(filter_details.pay_on_delivery.get("pay_on_delivery"), filter)

        return filter




