from typing import Mapping, Union, Optional

from pydantic import BaseModel


class LinkHref(BaseModel):
    href: str
    meta: dict


Link = Union[str, LinkHref]
ResourceLinks = Mapping[str, Optional[Link]]
ResourceLinks.__doc__ = "https://jsonapi.org/format/#document-links"
