import time

class CountTimer:
    def __init__(self, duration) -> None:
        """
        初始化计时器。

        :param duration: 计时的持续时间（秒）
        """
        self.duration = duration
        self.start_time = None

    def start(self) -> None:
        """
        开始计时。
        """
        self.start_time = time.time()

    def is_done(self) -> bool:
        """
        检查是否计时完成。

        :return: 如果计时完成，返回 True；否则返回 False
        """
        if not self.start_time is None:
            current_time = time.time()
            return (current_time - self.start_time) >= self.duration

    def ret(self):
        self.start_time = None
    
class CountdownTimer:
    def __init__(self, duration) -> None:
        """
        初始化倒计时器。

        :param duration: 倒计时的持续时间（秒）
        """
        self.duration = duration
        self.start_time = None

    def start(self) -> None:
        """
        开始倒计时。
        """
        self.start_time = time.time()

    def is_done(self) -> bool:
        """
        检查是否倒计时完成。

        :return: 如果倒计时完成，返回 True；否则返回 False
        """
        if self.start_time is None:
            raise RuntimeError("倒计时器尚未启动")
        current_time = time.time()
        return (current_time - self.start_time) >= self.duration

    def remaining_time(self, is_int: bool=False) -> int | float:
        """
        返回剩余时间（秒）。

        :return: 剩余时间（秒）
        """
        if self.start_time is None:
            raise RuntimeError("倒计时器尚未启动")
        current_time = time.time()
        remaining = self.duration - (current_time - self.start_time)
        remaining = float(f'{remaining: .2f}')
        return max(0, int(remaining) if is_int else remaining)