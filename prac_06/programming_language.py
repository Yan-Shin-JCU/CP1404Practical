class ProgrammingLanguage():
    """DocString"""

    def __init__(self,name, typing, reflection, year):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return '{}, {} Typing, Reflection={}, First appeared in {}'.format(self.name, self.typing,
                                                                           str(self.reflection), str(self.year))

    def is_dynamic(self):
        """Add amount to the car's fuel."""
        if self.typing == 'Dynamic':
            return True
        else:
            return False
