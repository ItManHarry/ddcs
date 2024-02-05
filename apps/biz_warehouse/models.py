from ddcs.sys.db import models, BaseModel
'''
仓库信息表
'''
class WareHouse(BaseModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.name}({self.code})'

    class Meta(BaseModel.Meta):
        db_table = 'biz_warehouse'