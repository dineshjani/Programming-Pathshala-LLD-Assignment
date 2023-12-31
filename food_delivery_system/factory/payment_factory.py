from food_delivery_system.manager.net_banking_manager import NetBankingManager
from food_delivery_system.manager.card_based_payment_manager import (
    CardBasedPymentManager,
)
from food_delivery_system.manager.payment_manager import PaymentManager
from food_delivery_system.data.payment_mode import PaymentMode
from typing import Dict


class PaymentFactory:
    @staticmethod
    def get_payment_manager(
        payment_mode, payment_info: Dict[str, str]
    ) -> PaymentManager:
        if payment_mode == PaymentMode.NET_BANKING:
            PaymentFactory.get_net_banking_based_payment_manager(payment_info)
        elif payment_mode == PaymentMode.CARD:
            PaymentFactory.get_card_based_payment_manager(payment_info)
        else:
            raise RuntimeError("Invalid payment_mode")

    @staticmethod
    def get_card_based_payment_manager(payment_info: Dict[str, str]) -> PaymentManager:
        return CardBasedPymentManager(
            payment_info.get("bank_name"),
            payment_info.get("card_number"),
            payment_info.get("pin"),
            payment_info.get("amount"),
        )

    @staticmethod
    def get_net_banking_based_payment_manager(
        payment_info: Dict[str, str]
    ) -> PaymentManager:
        return NetBankingManager(
            payment_info.get("bank_name"),
            payment_info.get("user_name"),
            payment_info.get("pin"),
            payment_info.get("password"),
            payment_info.get("amount"),
        )
