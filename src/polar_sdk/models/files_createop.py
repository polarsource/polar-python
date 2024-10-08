"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .downloadablefilecreate import (
    DownloadableFileCreate,
    DownloadableFileCreateTypedDict,
)
from .organizationavatarfilecreate import (
    OrganizationAvatarFileCreate,
    OrganizationAvatarFileCreateTypedDict,
)
from .productmediafilecreate import (
    ProductMediaFileCreate,
    ProductMediaFileCreateTypedDict,
)
from polar_sdk.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated


FilesCreateFileCreateTypedDict = Union[
    DownloadableFileCreateTypedDict,
    ProductMediaFileCreateTypedDict,
    OrganizationAvatarFileCreateTypedDict,
]


FilesCreateFileCreate = Annotated[
    Union[
        Annotated[DownloadableFileCreate, Tag("downloadable")],
        Annotated[ProductMediaFileCreate, Tag("product_media")],
        Annotated[OrganizationAvatarFileCreate, Tag("organization_avatar")],
    ],
    Discriminator(lambda m: get_discriminator(m, "service", "service")),
]
