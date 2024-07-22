# Pydantic
from pydantic import Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models.models.resources.base_resource import (
    YoutubeBaseResource
)
from youtube_pydantic_models.models.part.snippet import (
    ChannelSnippet
)
from youtube_pydantic_models.models.part.content_details import (
    ChannelContentDetails
)
from youtube_pydantic_models.models.part.statistics import (
    ChannelStatistics
)
from youtube_pydantic_models.models.part.topic_details import (
    BaseTopicDetails
)
from youtube_pydantic_models.models.part.status import (
    ChannelStatus
)
from youtube_pydantic_models.models.part.branding_settings import (
    BaseBrandingSettings
)
from youtube_pydantic_models.models.part.audit_details import (
    BaseAuditDetails
)
from youtube_pydantic_models.models.part.content_owner_details import (
    BaseContentOwnerDetails
)
from youtube_pydantic_models.models.subpart.localization import (
    Localization
)


class YoutubeChannelResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: str | None = Field(default=None)
    snippet: ChannelSnippet | None = Field(default=None)
    content_details: ChannelContentDetails | None = Field(default=None)
    statistics: ChannelStatistics | None = Field(default=None)
    topic_details: BaseTopicDetails | None = Field(default=None)
    status: ChannelStatus | None = Field(default=None)
    branding_settings: BaseBrandingSettings | None = Field(default=None)
    audit_details: BaseAuditDetails | None = Field(default=None)
    content_owner_details: BaseContentOwnerDetails | None = Field(default=None)
    localizations: dict[str, Localization] | None = Field(default=None)
