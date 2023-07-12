#здесь находится платёжка
from yookassa import Configuration
from yookassa import Payment
import uuid
import json
class YouMoney:
    def __init__(self, account_id: str, secret_key: str, test: bool):
        Configuration.account_id = account_id
        Configuration.secret_key = secret_key
        self.test = test

    def create_payment_1_month(self, uid: int):
        payment = Payment.create({
            "amount": {
                "value": "149.00",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://web.telegram.org/k/#@god_vpn_bot"
            },
            "metadata": {
                'orderUId': uid
            },
            "capture": True,
            "description": "оплата подписки на 1 месяц",
            "test": self.test
            }, uuid.uuid4())
        return json.loads(payment.json())["confirmation"]["confirmation_url"]

    def create_payment_1_year(self, uid: int):
        payment = Payment.create({
            "amount": {
                "value": "349.00",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://web.telegram.org/k/#@god_vpn_bot"
            },
            "metadata": {
                'orderUId': uid
            },
            "capture": True,
            "description": "оплата подписки на 1 год",
            "test": self.test
            }, uuid.uuid4())
        return json.loads(payment.json())["confirmation"]["confirmation_url"]

    def create_payment_3_month(self, uid: int):
        payment = Payment.create({
            "amount": {
                "value": "349.00",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://web.telegram.org/k/#@god_vpn_bot"
            },
            "metadata": {
                'orderUId': uid
            },
            "capture": True,
            "description": "оплата подписки на 3 месяца",
            "test": self.test
            }, uuid.uuid4())
        return json.loads(payment.json())["confirmation"]["confirmation_url"]

y = YouMoney('504164',"test_*g9J7spURPRNlPk8pBBQ6BtuErAr0ON0RYorrTh0C2NN4", "true")
print(y.create_payment_1_month(2))
print(y.create_payment_3_month(3))
print(y.create_payment_1_year(2))

