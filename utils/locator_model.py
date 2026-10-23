from pydantic import BaseModel
# 单个元素定位模型
class LocatorItem(BaseModel):
    username: str
    password: str
    submit: str
    message: str

