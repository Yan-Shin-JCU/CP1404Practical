class ProgrammingLanguage():
    """Represents a Programming Language Object"""

    def __init__(self,name, typing, reflection, year):
        """Initialise the ProgrammingLanguage instance.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return '{}, {} Typing, Reflection={}, First appeared in {}'.format(self.name, self.typing,
                                                                           str(self.reflection), str(self.year))

    def is_dynamic(self):
        """Checks if dynamic and returns Boolean value"""
        if self.typing == 'Dynamic':
            return True
        else:
            return False
