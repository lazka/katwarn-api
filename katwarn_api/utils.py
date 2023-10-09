# SPDX-License-Identifier: MIT

import base64
import hashlib
import hmac
import os
import random
import secrets
from dataclasses import dataclass
from datetime import datetime, timezone

import requests
from requests.auth import AuthBase


class KatwarnAuth(AuthBase):
    def __init__(self, api_keys: list[str]):
        self.api_keys = api_keys

    def __call__(self, r):
        parts = [
            r.method,
            r.headers["Content-Type"],
            r.headers["X-KWRN-Date"],
            r.headers["X-KWRN-Device-ID"],
            r.headers.get("If-Match", r.headers.get("If-None-Match", "")),
            hashlib.sha1((r.body or "").encode("utf-8")).hexdigest(),
        ]
        key, value = random.choice(self.api_keys).split(":", 1)
        mac = hmac.new(value.encode("utf-8"), digestmod=hashlib.sha256)
        mac.update("\n".join(parts).encode("utf-8"))
        auth_string = base64.b64encode(mac.digest()).decode("utf-8").strip()
        r.headers["Authorization"] = f"KWRN {key}:{auth_string}"
        return r


@dataclass
class Service:
    url: str
    content_type: str
    api_keys: list[str]

    @classmethod
    def create(self, name: str) -> "Service":
        return _SERVICES[name]

    def get(self, *args, **kwargs):
        kwargs.setdefault("headers", {}).update(self.get_headers())
        kwargs.setdefault("verify", self.get_verify())
        kwargs.setdefault("auth", self.get_auth())
        return requests.get(*args, **kwargs)

    def get_verify(self) -> str:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), "kwrn-ca.pem")

    def get_auth(self) -> AuthBase:
        return KatwarnAuth(api_keys=self.api_keys)

    def get_headers(self) -> dict[str, str]:
        return {
            "User-Agent": "KATWARN-API",
            "Accept": self.content_type,
            "Content-Type": self.content_type,
            "X-KWRN-Device-ID": hashlib.sha1(secrets.token_bytes()).hexdigest(),
            "X-KWRN-Date": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        }


_SERVICES: dict[str, Service] = {
    "content": Service(
        url="https://content.omega.kwrn.eu",
        content_type="application/vnd.kwrn.v2+json",
        api_keys=[
            "40741e29:ID/4b+B6Cy8kPw2PsWqueOobCcg8+iyYWnk5ilXJiJk=",
            "7ab52540:ixXM2MVT+9ZEMZOeUXBZeL/JVodRToSfaEiLCQqx+gE=",
            "25f1f9e3:Vzh75oYZP7F1hSz9jsMVA32FvJEk3kA0KYEVSBNHDwE=",
        ],
    ),
    "servicearea": Service(
        url="https://service.omega.kwrn.eu",
        content_type="application/vnd.kwrn+json",
        api_keys=[
            "32b68da0:4Cp336oyoEbPbTtVePrkm912diDQ2rbG6/IC1vfzTZ8=",
            "166ce2ab:71ZGJNnwkMi32O9tReKCzXtNMOUGDPpnDdzkdGBT26k=",
            "9dc020f3:FSf6QqeO+uKmj8CIc4RJGuZIIHEIf24c27MLQUdapW0=",
        ],
    ),
}
