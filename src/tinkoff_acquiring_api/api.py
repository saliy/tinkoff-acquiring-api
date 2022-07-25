from collections import OrderedDict
from hashlib import sha256

import requests as requests


class TinkoffAcquiring:
    def __init__(self, terminal: str, secret_key: str):
        self.terminal = terminal
        self.secret_key = secret_key

    def init(self, payload: dict) -> dict:
        """The method creates payment: the seller receives a link to the payment form and must redirect the buyer to it"""
        return self._call('Init', payload=payload)

    def state(self, payment_id: str) -> dict:
        """Returns the current payment status"""
        return self._call('GetState', payload={'PaymentId': payment_id})

    def _call(self, method: str, payload: dict) -> dict:
        payload.update({'TerminalKey': self.terminal})

        response = requests.post(
            f'https://securepay.tinkoff.ru/v2/{method}/',
            json={
                'Token': self._get_token(payload),
                **payload,
            },
        )

        if response.status_code != 200:
            raise Exception(
                f'Incorrect HTTP-status code for {method}: {response.status_code}',
            )

        parsed = response.json()

        if not parsed['Success']:
            raise Exception(
                f'Non-success request for {method}: {parsed["ErrorCode"]}, {parsed["Message"]} ({parsed["Details"]}',
            )

        return parsed

    def _get_token(self, request: dict) -> str:
        params = {k: v for k, v in request.items() if k not in ['Shops', 'DATA', 'Receipt']}

        params['Password'] = self.secret_key

        sorted_params = OrderedDict(
            sorted((k, v) for k, v in params.items() if k not in ['Shops', 'DATA', 'Receipt']),
        )

        return sha256(''.join(str(value) for value in sorted_params.values()).encode()).hexdigest()
