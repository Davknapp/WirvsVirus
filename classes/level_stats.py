

class LevelStats:

    def __init__(self, stat_names : list, stat_texts : dict):
        self.end_reason = None

        self.stats = stat_names
        self.stat_texts = stat_texts
        self.stat_values = dict()

        for st in self.stats:
            self.stat_values[st] = 0

    def increment(self, stat_name):
        """
            Increases the stat stat_name by one.
        """
        self.stat_values[stat_name] += 1

    def set_value(self, stat_name, value):
        """
            Sets the value of a specific stat.
        """
        self.stat_values[stat_name] = value

    def get_value(self, stat_name):
        """
            Returns the value of a specific stat.
        """
        return self.stat_values[stat_name]

    def get_text(self, stat_name):
        """
            Returns the UI text for a specific stat.
        """
        return self.stat_texts[stat_name]
