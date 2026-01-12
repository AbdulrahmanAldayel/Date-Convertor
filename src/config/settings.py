"""Application settings and configuration."""

from dataclasses import dataclass
from typing import Dict, Tuple
from enum import Enum


class Language(Enum):
    """Supported languages."""
    ARABIC = "ar"
    ENGLISH = "en"
    KOREAN = "kr"


class CalendarType(Enum):
    """Calendar types."""
    HIJRI = "hijri"
    GREGORIAN = "gregorian"


@dataclass
class UIConfig:
    """UI configuration settings."""
    window_width: int = 550
    window_height: int = 600
    background_color: str = "white"
    font_arabic: str = "IBM Plex Sans Arabic"
    font_latin: str = "Montserrat"
    
    # Font sizes
    title_font_size: int = 30
    label_font_size: int = 14
    button_font_size: int = 10
    frame_font_size: int = 16
    radio_font_size: int = 15


@dataclass
class Paths:
    """Resource paths configuration."""
    fonts_dir: str = "fonts"
    images_dir: str = "images"
    
    # Font files
    arabic_font: str = "IBMPlexSansArabic-Regular.ttf"
    latin_font: str = "Montserrat-VariableFont_wght.ttf"
    
    # Image files
    icon_file: str = "ico.ico"
    logo_file: str = "llogo.png"


class AppConfig:
    """Main application configuration."""
    
    def __init__(self):
        self.ui = UIConfig()
        self.paths = Paths()
        self.default_language = Language.ARABIC
        self.supported_languages = list(Language)
        
    def get_font_path(self, font_name: str) -> str:
        """Get full path to font file."""
        return f"{self.paths.fonts_dir}/{font_name}"
    
    def get_image_path(self, image_name: str) -> str:
        """Get full path to image file."""
        return f"{self.paths.images_dir}/{image_name}"


# Global configuration instance
config = AppConfig()
