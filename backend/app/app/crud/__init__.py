from .crud_snake import snake
from .crud_user import user
from .crud_shed import shed
from .crud_feed import feed
from .crud_weight import weight
from .crud_excretion import excretion
from .crud_mating import mating
from .crud_cycle import cycle
from .crud_clutch import clutch

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.snake import Snake
# from app.schemas.snake import SnakeCreate, SnakeUpdate

# snake = CRUDBase[Snake, SnakeCreate, SnakeUpdate](Snake)
