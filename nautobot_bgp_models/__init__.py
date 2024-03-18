"""App declaration for nautobot_bgp_models."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class NautobotBGPModelsConfig(NautobotAppConfig):
    """App configuration for the nautobot_bgp_models app."""

    name = "nautobot_bgp_models"
    verbose_name = "BGP Models"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobot BGP Models App."
    base_url = "bgp"
    required_settings = []
    min_version = "2.0.3"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = NautobotBGPModelsConfig  # pylint:disable=invalid-name
