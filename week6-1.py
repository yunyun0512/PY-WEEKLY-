class GameConfigManager:
	_instance = None
	def __init__(self):
		self.difficulty = "normal"
		self.sound_enabled = True
		self.max_levels = 10
	def __new__(cls):
		if not GameConfigManager._instance:
			GameConfigManager._instance=object.__new__(cls)
			GameConfigManager.__init__(GameConfigManager._instance)
		return GameConfigManager._instance
	def set_difficulty(self, difficulty):
		self.difficulty = difficulty
	def set_sound_enabled(self,enabled):
		self.sound_enabled = enabled
	def set_max_levels(self,levels):
		self.max_levels = levels
	def get_difficulty(self):
		return self.difficulty
	def is_sound_enabled(self):
		return self.sound_enabled
	def get_max_levels(self):
		return self.max_levels

if __name__ == "__main__":
    Manager1=GameConfigManager()
    Manager2=GameConfigManager()
    assert Manager1 is Manager2,"单例模式实现失败"
    difficulty,enabled,levels=input().split()
    Manager1.set_difficulty(difficulty)
    Manager1.set_sound_enabled(enabled)
    Manager1.set_max_levels(levels)
    print(f"{Manager2.get_difficulty()},{Manager2.is_sound_enabled()},{Manager2.get_max_levels()}")