from fastapi import APIRouter

from app.api.api_v1.endpoints import snakes, login, clutches, cycles, matings, excretions, feeds, sheds, weights, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(snakes.router, prefix="/snakes", tags=["snakes"])
api_router.include_router(weights.router, prefix="/weights", tags=["weights"])
api_router.include_router(sheds.router, prefix="/sheds", tags=["sheds"])
api_router.include_router(feeds.router, prefix="/feeds", tags=["feeds"])
api_router.include_router(excretions.router, prefix="/excretions", tags=["excretions"])
api_router.include_router(matings.router, prefix="/matings", tags=["matings"])
api_router.include_router(cycles.router, prefix="/cycles", tags=["cycles"])
api_router.include_router(clutches.router, prefix="/clutches", tags=["clutches"])
