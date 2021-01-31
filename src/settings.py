from environs import Env

env = Env()
env.read_env()

# vk settings
VK_TOKEN = env.str("VK_TOKEN")
VK_WALL_ID = env.int("VK_WALL_ID")
# telegram settings
TARGET_CHANNEL = env.int("TARGET_CHANNEL")
TEST_CHANNEL = env.int("TEST_CHANNEL", 0)
TG_BOT_TOKEN = env.str("TG_BOT_TOKEN")
TG_ME = env.int("TG_ME")
LOG_CHANNEL = env.int("LOG_CHANNEL", TG_ME)
# postgres settings
POSTGRES_HOST = env.str("POSTGRES_HOST", "localhost")
POSTGRES_PORT = env.int("POSTGRES_PORT", 5432)
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD" "")
POSTGRES_USER = env.str("POSTGRES_USER", "postgres")
POSTGRES_DB = env.str("POSTGRES_DB", "postgres")
POSTGRES_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
