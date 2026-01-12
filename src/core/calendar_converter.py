"""Calendar conversion logic."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional
import logging

from hijridate import Gregorian, Hijri


logger = logging.getLogger(__name__)


@dataclass
class DateResult:
    """Result of date conversion."""
    day: int
    month: int
    year: int
    month_name: str
    weekday: str
    formatted_date: str


class CalendarConverter(ABC):
    """Abstract base class for calendar converters."""
    
    @abstractmethod
    def to_gregorian(self, day: int, month: int, year: int) -> DateResult:
        """Convert to Gregorian calendar."""
        pass
    
    @abstractmethod
    def to_hijri(self, day: int, month: int, year: int) -> DateResult:
        """Convert to Hijri calendar."""
        pass


class HijriGregorianConverter(CalendarConverter):
    """Concrete implementation of Hijri-Gregorian converter."""
    
    def __init__(self):
        self._validate_date = self._create_validator()
    
    def _create_validator(self):
        """Create date validation function."""
        def validate_date(year: int, month: int, day: int) -> bool:
            try:
                datetime(year, month, day)
                return True
            except ValueError as e:
                logger.warning(f"Invalid date: {year}-{month}-{day}, Error: {e}")
                return False
        return validate_date
    
    def to_gregorian(self, day: int, month: int, year: int) -> DateResult:
        """Convert Hijri date to Gregorian."""
        if not self._validate_date(year, month, day):
            raise ValueError(f"Invalid Hijri date: {year}-{month}-{day}")
        
        try:
            hijri_date = Hijri(year, month, day)
            gregorian = hijri_date.to_gregorian()
            
            return DateResult(
                day=gregorian.day,
                month=gregorian.month,
                year=gregorian.year,
                month_name="",  # Will be filled by localization
                weekday=gregorian.strftime("%A"),
                formatted_date=f"{gregorian.day}/{gregorian.month}/{gregorian.year}"
            )
        except Exception as e:
            logger.error(f"Error converting Hijri to Gregorian: {e}")
            raise
    
    def to_hijri(self, day: int, month: int, year: int) -> DateResult:
        """Convert Gregorian date to Hijri."""
        if not self._validate_date(year, month, day):
            raise ValueError(f"Invalid Gregorian date: {year}-{month}-{day}")
        
        try:
            gregorian_date = Gregorian(year, month, day)
            hijri = gregorian_date.to_hijri()
            
            return DateResult(
                day=hijri.day,
                month=hijri.month,
                year=hijri.year,
                month_name="",  # Will be filled by localization
                weekday="",  # Hijri weekdays not commonly used in same way
                formatted_date=f"{hijri.day}/{hijri.month}/{hijri.year}"
            )
        except Exception as e:
            logger.error(f"Error converting Gregorian to Hijri: {e}")
            raise


class KuwaitiCalendarConverter:
    """Alternative converter using Kuwaiti calendar algorithm."""
    
    @staticmethod
    def gmod(n: int, m: int) -> int:
        """Modulo function that handles negative numbers."""
        return ((n % m) + m) % m
    
    def convert_to_hijri(self, gregorian_date: date) -> DateResult:
        """Convert Gregorian date to Hijri using Kuwaiti algorithm."""
        day = gregorian_date.day
        month = gregorian_date.month
        year = gregorian_date.year
        
        m = month + 1
        y = year
        if m < 3:
            y -= 1
            m += 12
        
        a = y // 100
        b = 2 - a + a // 4
        if y < 1583:
            b = 0
        if y == 1582:
            if m > 10:
                b = -10
            if m == 10:
                b = 0
                if day > 4:
                    b = -10
        
        jd = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + day + b - 1524
        
        b = 0
        if jd > 2299160:
            a = int((jd - 1867216.25) / 36524.25)
            b = 1 + a - a // 4
        bb = jd + b + 1524
        cc = int((bb - 122.1) / 365.25)
        dd = int(365.25 * cc)
        ee = int((bb - dd) / 30.6001)
        day = bb - dd - int(30.6001 * ee)
        month = ee - 1
        if ee > 13:
            cc += 1
            month = ee - 13
        year = cc - 4716
        
        wd = self.gmod(jd + 1, 7) + 1
        
        iyear = 10631 / 30
        epochastro = 1948084
        shift1 = 8.01 / 60
        
        z = jd - epochastro
        cyc = z // 10631
        z -= 10631 * cyc
        j = (z - shift1) // iyear
        iy = 30 * cyc + j
        z -= j * iyear + shift1
        im = int((z + 28.5001) / 29.5)
        if im == 13:
            im = 12
        id = z - int(29.5001 * im - 29)
        
        return DateResult(
            day=int(id),
            month=int(im),
            year=int(iy),
            month_name="",
            weekday=["Ahad", "Ithnin", "Thulatha", "Arbaa", "Khams", "Jumuah", "Sabt"][wd - 1],
            formatted_date=f"{int(id)}/{int(im)}/{int(iy)}"
        )
