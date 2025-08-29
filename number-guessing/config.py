from pydantic import BaseModel


class LevelConfig(BaseModel):
    max_attempts: int
    upper_limit: int


levels = {
    "easy": LevelConfig(max_attempts=20, upper_limit=100),
    "normal": LevelConfig(max_attempts=15, upper_limit=200),
    "hard": LevelConfig(max_attempts=10, upper_limit=500),
}
