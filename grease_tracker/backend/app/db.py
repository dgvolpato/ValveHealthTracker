import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class PressureReadings(ormar.Model):
    class Meta(BaseMeta):
        tablename = "pressure_readings"

    id: int = ormar.Integer(primary_key=True)
    reading_date: str = ormar.String(max_length=16, unique=True, nullable=False)
    reading_value: float = ormar.Float(default=0.00, nullable=False)
    valve_id: int = ormar.Integer(default=1, nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
