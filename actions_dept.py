from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions import Action
from rasa_core.events import SlotSet
class ActionCheckDepartments(Action):
  def name(self):
    # type: () -> Text
    return "action_check_depts"
 
  def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
    if tracker.get_slot('department') in weather_domain['slots']['department']['values']:
       return [SlotSet("account_check","False")]
