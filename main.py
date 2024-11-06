from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - tiny-bar--coll-0aaf5d5dad394ef9b8ca7a32d3db3435',debug=False,docs_url='/dazzling-bassi-e8ccb5ca9c0f11efabb90242c0a8900239/docs',openapi_url='/dazzling-bassi-e8ccb5ca9c0f11efabb90242c0a8900239/openapi.json')

app.include_router(router, prefix='/dazzling-bassi-e8ccb5ca9c0f11efabb90242c0a8900239/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()