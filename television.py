class Television:
    """
    Class to hold 8 methods for a Television object
    :Var MIN_VOLUME: Sets minimum limit for TV Volume
    :Var MAX_VOLUME: Sets maximum limit for TV Volume
    :Var MIN_CHANNEL: Sets minimum limit for TV Channel
    :Var MAX_CHANNEL: Sets maximum limit for TV Channel
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3
    MIN_CHANNEL = 0


    def __init__(self) -> None:
        """
        Method to define 5 instance variables.
        :var self.__status: Determines if TV Power is On/Off (True/False Boolean).
        :var self.__muted: Determines if TV Volume Mute is Toggled On/Off (True/False Boolean).
        :var self.__volume: Determines what integer TV Volume is set to.
        :var self.__channel: Determines what integer TV Channel is set to.
        :var self.__hold: Holds TV Volumes set integer when method mute() is called.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = 0
        self.__hold = 0

    def power(self) -> None:
        """
        Method to toggle TV Power on/off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self) -> None:
        """
        Method to toggle mute on/off.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__hold
            else:
                self.__muted = True
                self.__hold = self.__volume
                self.__volume = 0

    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """

        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self) -> None:
        """
        Method to lower the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self) -> None:
        """
        Method to increase the tv volume.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__hold
            self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to lower the tv volume.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__hold
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"