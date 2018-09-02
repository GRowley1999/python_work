import json

class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score = 0
        try:
            filename = 'high_score.json'
            with open(filename) as f_obj:
                self.high_score = json.load(f_obj)
        except FileNotFoundError:
            pass
            
        # Start Alien Invasion in an active state.
        self.game_active = False

    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0