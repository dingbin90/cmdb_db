#
# PLUGINS = {
#     'disk':"src.plugins.disk.DiskPlugin",
#
# }
#
#
# class DiskPlugin:
#     def execute(self):
#         return "123123123123"
# # response = {}
# # for k,v in PLUGINS.items():
# #
# #     cls = v.rsplit('.',1)[1]
# #     function = getattr(cls,'execute')
# # #     function()
# # A = 'Linux'
# # print(type(A))
#
#
#
# class A(object):
#
#     def foo(self, x):
#         print("executing foo(%s,%s)" % (self, x))
#         print('self:', self)
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s,%s)" % (cls, x))
#         print('cls:', cls)
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % x)
# print(A.foo(1,1))