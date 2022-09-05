"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

story = Story(
['verb', 'body part', 'family member', 'activity', 'animal', 'verb / olympic sport', 'noise'],
     """ {verb} up and down the floor, my {body part} is an animal. And once there was an animal. It had a {family member} that {activity} the lawn. The {family member} was an okay person. They had a pet {animal}. The {animal} {verb / olympic sport} away. But it came back with a story to {noise}. """
)

