"""
Custom Qt widget to select range of date/times.

.. autosummary::

    ~DateTimeRangeSlider
"""

import utils

from PyQt5 import QtCore, QtWidgets

import range_slider

SECOND = 1
MINUTE = 60 * SECOND
DAY = 60 * MINUTE
WEEK = 7 * DAY

DEFAULT_MINIMUM = "1995-01-01"
DEFAULT_LOW = "2023-01-01"
DEFAULT_HIGH = "2024-05-01"
DEFAULT_MAXIMUM = "2035-12-31"


class DateTimeRangeSlider(QtWidgets.QWidget):
    """
    Choose a range of dates.

    This widget provides for the selection of a low date/time & a high date/time
    within a minimum & maximum.  Date/time entry boxes (with calendar pop-ups)
    are provided to select the low and high dates.  A slider provides a visual cue
    to the currently-selected range.

    ::

        minimum <= low < high <= maximum

    Note: Internally, times are represented as timestamps.  They are reported as
    ISO8601 date/time strings.

    PUBLIC

    .. autosummary::

        ~high
        ~low
        ~maximum
        ~minimum
        ~setHigh
        ~setLow
        ~setMaximum
        ~setMinimum

    INTERNAL

    .. autosummary::

        ~setup
        ~adjustDates
        ~adjustSlider
    """

    ui_file = utils.getUiFileName(__file__)

    def __init__(self, parent, minimum=None, low=None, high=None, maximum=None):
        from PyQt5 import uic

        super().__init__(parent)
        utils.myLoadUi(self.ui_file, baseinstance=self)

        # replace the placeholder "slider" with the custom one
        self.verticalLayout.removeWidget(self.slider)
        self.slider = range_slider.RangeSlider(QtCore.Qt.Horizontal)
        self.verticalLayout.addWidget(self.slider)
        self._locked = False

        self.setup()
        self.setMinimum(minimum or DEFAULT_MINIMUM)
        self.setMaximum(maximum or DEFAULT_MAXIMUM)
        self.setLow(low or DEFAULT_LOW)
        self.setHigh(high or DEFAULT_HIGH)

    def setup(self):
        """Configure the UI widgets."""
        self.slider.setMinimumHeight(30)
        self.slider.setSingleStep(DAY)
        self.slider.setPageStep(WEEK)

        self.slider.sliderMoved.connect(self.adjustDates)
        self.low_date.dateTimeChanged.connect(self.adjustSlider)
        self.high_date.dateTimeChanged.connect(self.adjustSlider)

    def adjustDates(self, low, high):
        """
        Called when slider widget has moved.

        low & high are integer timestamps
        """
        if not self._locked:
            self._locked = True
            self.setLow(utils.ts2iso(low))
            self.setHigh(utils.ts2iso(high))
            self._locked = False

    def adjustSlider(self, *args):
        """Called when either date widget was changed."""
        if not self._locked:
            self._locked = True
            self.setLow(str(self.low_date.dateTime().toPyDateTime()))
            self.setHigh(str(self.high_date.dateTime().toPyDateTime()))
            self._locked = False

    def high(self):
        """Return the latest date/time selected, in ISO8601 format."""
        return utils.ts2iso(self._high)

    def setHigh(self, value):
        """
        Set the latest selected date/time.

        PARAMETER:

        value *str* :
            Date & time in ISO8601 format, such as: "2021-03-04 21:55".
        """
        self._high = utils.iso2ts(value) if isinstance(value, str) else value
        self.high_date.setDate(utils.ts2dt(self._high))
        self.slider.setHigh(int(self._high))
        self.low_date.setMaximumDate(utils.iso2dt(value))

    def low(self):
        """Return the earliest date/time selected, in ISO8601 format."""
        return utils.ts2iso(self._low)

    def setLow(self, value):
        """
        Set the earliest selected date/time.

        PARAMETER:

        value *str* :
            Date & time in ISO8601 format, such as: "2021-03-04 21:55".
        """
        self._low = utils.iso2ts(value) if isinstance(value, str) else value
        self.low_date.setDate(utils.ts2dt(self._low))
        self.slider.setLow(int(self._low))
        self.high_date.setMinimumDate(utils.iso2dt(value))

    def maximum(self):
        """Return the latest possible date/time, in ISO8601 format."""
        return utils.ts2iso(self._maximum)

    def setMaximum(self, value):
        """
        Set the last possible date/time to be selected.

        PARAMETER:

        value *str* :
            Date & time in ISO8601 format, such as: "2021-03-04 21:55".
        """
        self._maximum = utils.iso2ts(value) if isinstance(value, str) else value
        self.slider.setMaximum(int(self._maximum))
        self.high_date.setMaximumDate(utils.iso2dt(value))

    def minimum(self):
        """Return the earliest possible date/time, in ISO8601 format."""
        return utils.ts2iso(self._minimum)

    def setMinimum(self, value):
        """
        Set the earliest possible date/time to be selected.

        PARAMETER:

        value *str* :
            Date & time in ISO8601 format, such as: "2021-03-04 21:55".
        """
        self._minimum = utils.iso2ts(value) if isinstance(value, str) else value
        self.slider.setMinimum(int(self._minimum))
        self.low_date.setMinimumDate(utils.iso2dt(value))


if __name__ == "__main__":
    import sys

    """Test this widget."""
    app = QtWidgets.QApplication(sys.argv)
    main = DateTimeRangeSlider(None)
    main.show()
    # main.raise_()
    app.exec()
    print(f"{main.low()=}  {main.high()=}")
