from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv

# بارگذاری env
load_dotenv()

# Import مدل‌ها
from app.db.base import Base  # جای مسیر رو با پروژه‌ت یکی کن
from app.models import *            # همه مدل‌ها

# کانفیگ
config = context.config
fileConfig(config.config_file_name)

# متادیتا
target_metadata = Base.metadata

# گرفتن URL از env
DATABASE_URL = os.getenv("DATABASE_URL")

def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        {"sqlalchemy.url": DATABASE_URL},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
