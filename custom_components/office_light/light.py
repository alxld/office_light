"""Platform for light integration"""
from __future__ import annotations
import sys

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = OfficeLight()
    add_entities([ent])


class OfficeLight(NewLight):
    """Office Light."""

    def __init__(self) -> None:
        """Initialize Office Light."""
        self._name = "Office"
        self.entities["light.office_group"] = None
        self._has_switch = True
        self.switch_action = "zigbee2mqtt/Office Switch/action"
        super(OfficeLight, self).__init__(self._name, debug=True)
