from typing import Literal

class Person:
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __default_or_custom_phrase(method):
        def wrapper(self, phrase):
            print(phrase) if phrase else method(self, phrase)
        
        return wrapper 
    
    @__default_or_custom_phrase
    def _greeting(self, phrase: str) -> None:
        print("Hello, my name is " + self._name + ". Nice to meet you. How are you?")

    @__default_or_custom_phrase
    def _conversation(self, phrase: str) -> None:
        print("The weather is good today.")
    
    @__default_or_custom_phrase
    def _farewell(self, phrase: str) -> None:
        print("It was good to see you. Bye!")

    def say(self, context_of_message: Literal["greating", "conversation", "farewell"], phrase: str=None) -> None:
        match context_of_message:
            case "greeting":
                self._greeting(phrase)
            case "conversation":
                self._conversation(phrase)
            case "farewell":
                self._farewell(phrase)
            case _:
                raise ValueError("Unknown context_of_message")
            
class Programmer(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

programmer = Programmer(_name="John", _sex="male", _level="junior")
programmer.say("greeting", "> phrase 1")
programmer.say("conversation", "> phrase 2")
programmer.say("farewell", "> phrase 3")

