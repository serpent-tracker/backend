# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.snake import Snake  # noqa
from app.models.weight import Weight  # noqa
from app.models.shed import Shed  # noqa
from app.models.feed import Feed  # noqa
from app.models.excretion import Excretion  # noqa
from app.models.mating import Mating  # noqa
from app.models.user import User  # noqa
from app.models.clutch import Clutch  # noqa
