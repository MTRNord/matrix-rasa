from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.executor import CollectingDispatcher
from typing import Text


class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "matrix_room", lambda obj: "https://matrix.to/#/" + obj["matrix_room"]
        )
        knowledge_base.set_key_attribute_of_object("client", "name")
        knowledge_base.set_key_attribute_of_object("provider", "name")

        super().__init__(knowledge_base)

    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
    ):
        """
        Utters a response that informs the user about the attribute value of the
        attribute of interest.

        Args:
            dispatcher: the dispatcher
            object_name: the name of the object
            attribute_name: the name of the attribute
            attribute_value: the value of the attribute
        """
        # TODO: Make this work with the true/false lists of features and make it pretty
        if attribute_value:
            dispatcher.utter_message(
                text=(
                    f"'{object_name}' has the value '{attribute_value}' "
                    f"for attribute '{attribute_name}'."
                )
            )
        else:
            dispatcher.utter_message(
                text=(
                    f"Did not find a valid value for attribute '{attribute_name}' "
                    f"for object '{object_name}'."
                )
            )
