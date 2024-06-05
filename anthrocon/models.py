from uber.models import Session
from uber.models.types import DefaultColumn as Column, MultiChoice
from uber.config import c
from residue import CoerceUTF8 as UnicodeText


@Session.model_mixin
class Attendee:
    agent_notes = Column(UnicodeText)

    @property
    def num_free_event_shirts(self):
        return 1 if self.badge_type == c.STAFF_BADGE else self.volunteer_event_shirt_eligible

    @property
    def approved_panel_apps(self):
        return [panel.name for panel in self.panel_applications if panel.status == c.ACCEPTED]
    
