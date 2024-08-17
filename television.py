class Television:
    """
    Represents a television-like remote with functional buttons
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes the TV to be Off, unmuted, lowest volume, lowest channel
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power button of the TV
        """
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Toggles the mute of the TV if it's on
        """
        if self.__status:
            if self.__muted is False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Increase the channel value by 1 unless it's the max value, then wrap around
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the value of the TV's channel, unless it's the smallest channel, then wrap around
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
         Increase volume of TV unless it's reached the maximum
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the value of the volume unless it's reached the minimum
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return: a string representing the current state of the power, channel, and volume
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
