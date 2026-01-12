# Hijri Date Converter 📅

A multilingual desktop application for converting between Hijri (Islamic) and Gregorian calendars with support for Arabic, English, and Korean languages.

## Features ✨

- **Bidirectional Conversion**: Convert dates between Hijri and Gregorian calendars
- **Multilingual Support**: Full interface support for Arabic, English, and Korean
- **Modern GUI**: Clean and intuitive interface built with Tkinter
- **Accurate Calculations**: Uses reliable conversion algorithms
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Custom Fonts**: Includes IBM Plex Sans Arabic and Montserrat fonts for optimal typography


## File Structure 📁

```
Date Converter/
├── main.py                    # Application entry point
├── setup.py                   # Package setup script
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── src/                       # Source code directory
│   ├── __init__.py           # Package initialization
│   ├── config/               # Configuration module
│   │   ├── __init__.py
│   │   └── settings.py      # Application settings and constants
│   ├── core/                # Business logic
│   │   ├── __init__.py
│   │   └── calendar_converter.py  # Date conversion algorithms
│   ├── localization/        # Internationalization
│   │   ├── __init__.py
│   │   └── translations.py  # Multi-language support
│   ├── ui/                  # User interface
│   │   ├── __init__.py
│   │   └── main_window.py   # Main GUI application
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── logger.py        # Logging configuration
├── fonts/                    # Custom fonts directory
│   ├── IBMPlexSansArabic-Regular.ttf
│   ├── Montserrat-VariableFont_wght.ttf
│   ├── Cairo-Regular.ttf
│   └── YakoutLinotypeLight-Regular.ttf
├── images/                   # Application assets
│   ├── ico.ico              # Application icon
│   └── llogo.png            # Logo
├── legacy/                   # Legacy files (refactored)
│   ├── DateConverter.py     # Original monolithic GUI
│   ├── KuwaitiCalender.py   # Original calendar algorithm
│   ├── names.py             # Original translation data
│   └── hijricalendar-kuwaiti.js  # JavaScript version
└── logs/                     # Application logs (created at runtime)
```

## Installation 🚀

### Prerequisites

- Python 3.7 or higher
- Required packages: tkinter, tkcalendar, hijridate, pyglet

### Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

### Development Setup

For development, you can install the package in editable mode:
```bash
pip install -e .
```

## Usage 📖

1. **Launch the Application**: Run `python main.py`
2. **Select Language**: Choose between Arabic (عربي), English, or Korean (한국어)
3. **Choose Calendar Type**: Select either Hijri or Gregorian as input
4. **Enter Date**: Input the day, month, and year
5. **Convert**: Click the convert button to see the equivalent date in the other calendar
6. **View Results**: The converted date appears with weekday information

## Technical Details 🔧

### Architecture

The refactored application follows a clean, modular architecture with clear separation of concerns:

- **Configuration Management**: Centralized settings in `src/config/settings.py`
- **Business Logic**: Calendar conversion algorithms in `src/core/calendar_converter.py`
- **Internationalization**: Multi-language support in `src/localization/translations.py`
- **User Interface**: GUI components in `src/ui/main_window.py`
- **Utilities**: Helper functions and logging in `src/utils/logger.py`

### Core Components

- **main.py**: Application entry point with proper initialization and error handling
- **Calendar Converter**: Implements both Hijri-Gregorian conversion and Kuwaiti calendar algorithm
- **Translation System**: Type-safe multilingual support with easy extensibility
- **Resource Manager**: Handles fonts and images with proper path resolution
- **Configuration System**: Centralized settings with type hints and validation

### Design Patterns

- **Singleton Pattern**: Resource management for efficient memory usage
- **Strategy Pattern**: Pluggable calendar conversion algorithms
- **Factory Pattern**: Translation and UI component creation
- **Observer Pattern**: Language change notifications

### Conversion Algorithm

The application uses multiple conversion methods:
- **Primary**: hijridate library for reliable conversions
- **Alternative**: Kuwaiti calendar algorithm for historical accuracy
- **Validation**: Comprehensive date validation and error handling

### GUI Features

- **Responsive Layout**: Adapts to different languages and text directions (RTL/LTR)
- **Input Validation**: Real-time validation with user-friendly error messages
- **Dynamic Updates**: Seamless language switching without data loss
- **Modern Styling**: Clean white background with professional typography
- **Resource Management**: Efficient font and image loading

## Dependencies 📦

- `tkinter`: GUI framework (included with Python)
- `tkcalendar`: Calendar widget for date selection
- `hijridate`: Hijri-Gregorian date conversion library
- `pyglet`: Font loading and multimedia support

## Language Support 🌍

### Arabic (عربي)
- RTL layout support
- IBM Plex Sans Arabic font
- Full Arabic month and day names

### English
- LTR layout
- Montserrat font
- Standard English calendar terms

### Korean (한국어)
- LTR layout
- Montserrat font
- Korean month names and weekdays

## Author 👨‍💻

**Abdulrahman Aldayel**

**Readme markup was made with the hel0 of AI**