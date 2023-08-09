from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import NSUKit


class UMiddlewareMeta(type):
    ...


class UMiddleware(metaclass=UMiddlewareMeta):
    def __init__(self, kit: "NSUKit", *args, **kwargs):
        self.kit = kit

    def config(self, **kwargs):
        """!
        可调用此方法配置Middleware里的各种参数，
        会在NSUKit.start_command中调用
        @param args:
        @param kwargs:
        @return:
        """
        ...


class BaseRegMw(UMiddleware):
    def get_param(self, param_name: str, default=0, fmt_type=int):
        ...

    def set_param(self, param_name: str, value, fmt_type=int):
        ...

    def fmt_command(self, command_name, file_name=None) -> bytes:
        ...

    def find_command(self, parm_name: str) -> list:
        """!
        根据参数名称,查找所有包含此参数的指令名

        @param parm_name: 参数名
        @return 包含此参数的的指令集合 list

        """
        ...


class BaseChnlMw(UMiddleware):
    def alloc_buffer(self, length, buf: int = None):
        ...

    def free_buffer(self, fd):
        ...

    def get_buffer(self, fd, length):
        ...

    def stream_read(self, chnl, fd, length, offset=0, stop_event=None, flag=1):
        ...

    def stream_send(self, chnl, fd, length, offset=0, stop_event=None, flag=1):
        ...