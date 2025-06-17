from fastapi import APIRouter, Body, UploadFile
import uuid


from services.s3.s3 import s3_storage

products_router = APIRouter()

@products_router.post('/')
async def create_product(
    main_image: UploadFile,
    images: list[UploadFile] = None,
    title: str = Body(max_length=100),
    description: str = Body(max_length=1000),
    price: float = Body(gt=1),

):
    products_uuid = uuid.uuid4()
    products_uuid_str = str(products_uuid)

    return

@products_router.get('/{pk}')
async def get_product(pk: int):
    return


@products_router.get('/')
async def get_products():
    return
