# from ..plugins.disk import DiskPlugin

from client.conf import settings

def pack():
    # # 第一种方法
    # obj1 = DiskPlugin()
    # disk_info = obj1.execute()
    #
    # response = {
    #     'disk':disk_info
    # }
    #第二种方法
    response = {}
    for k,v in settings.PLUGINS.items():
        #v = "src.plugins.disk.DiskPlugin"
        import importlib
        m_path,classname = v.rsplit('.',1)
        m = importlib.import_module(m_path)
        cls = getattr(m,classname)
        # print('####333',obj.)
        #v是字符串，不可以执行方法，要用反射的方法
        response[k]=cls().execute()
    print('response',response)
    return response
