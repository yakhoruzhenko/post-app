import os

from fastapi import FastAPI

from app.controllers import authentication, posts, users

ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev').lower()

app = FastAPI(title='Post Application', version=os.getenv('APP_VERSION', '0.1.0'),
              docs_url='/docs' if ENVIRONMENT == 'dev' else None)


@app.get('/health', include_in_schema=False)
async def health() -> dict[str, str]:  # pragma: no cover
    '''
    Basic health check implementation
    '''
    return {'status': 'ok'}


app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(posts.router)
