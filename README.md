# Hijri Date Converter

A desktop application for converting between Hijri (Islamic) and Gregorian calendars with support for Arabic, English, and Korean languages.

## Features

- Bidirectional conversion between Hijri and Gregorian calendars
- Full interface support for Arabic, English, and Korean
- Clean, modern GUI built with Tkinter
- Accurate conversion algorithms
- Cross-platform (Windows, macOS, Linux)
- Custom fonts for optimal display in all languages

## File Structure

```
Date Converter/
├── main.py                    # Application entry point
├── setup.py                   # Package setup script
├── requirements.txt           # Python dependencies
├── README.md
├── src/                       # Source code
│   ├── __init__.py
│   ├── config/               # Settings and constants
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core/                 # Business logic
│   │   ├── __init__.py
│   │   └── calendar_converter.py
│   ├── localization/         # Translations
│   │   ├── __init__.py
│   │   └── translations.py
│   ├── ui/                   # GUI components
│   │   ├── __init__.py
│   │   └── main_window.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── fonts/                    # Custom fonts
│   ├── IBMPlexSansArabic-Regular.ttf
│   ├── Montserrat-VariableFont_wght.ttf
│   ├── Cairo-Regular.ttf
│   └── YakoutLinotypeLight-Regular.ttf
├── images/
│   ├── ico.ico
│   └── llogo.png
├── legacy/                   # Original files (refactored)
│   ├── DateConverter.py
│   ├── KuwaitiCalender.py
│   ├── names.py
│   └── hijricalendar-kuwaiti.js
└── logs/                     # Generated at runtime
```

## Installation

### Requirements

- Python 3.7+
- tkinter, tkcalendar, hijridate, pyglet

### Setup

1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

For development, install in editable mode:
```bash
pip install -e .
```

## Usage

1. Run `python main.py`
2. Select your language (Arabic, English, or Korean)
3. Choose input calendar type (Hijri or Gregorian)
4. Enter the date (day, month, year)
5. Click convert to see the equivalent date
6. Results show the converted date with weekday

## Technical Details

### Architecture

The application uses a modular structure with separation of concerns:

- **Configuration**: Centralized settings in `src/config/settings.py`
- **Core Logic**: Calendar conversion in `src/core/calendar_converter.py`
- **Translations**: Multi-language support in `src/localization/translations.py`
- **UI**: GUI components in `src/ui/main_window.py`
- **Utilities**: Logging and helpers in `src/utils/`

### Components

**main.py** - Entry point with initialization and error handling

**Calendar Converter** - Implements Hijri-Gregorian conversion using the hijridate library and Kuwaiti calendar algorithm

**Translation System** - Type-safe multilingual support for easy language additions

**Resource Manager** - Handles fonts and images with proper path resolution

### Design Patterns

The code uses several patterns for maintainability:
- Singleton for resource management
- Strategy for conversion algorithms
- Factory for UI component creation
- Observer for language change updates

### GUI

- Responsive layout with RTL/LTR support
- Real-time input validation
- Language switching without data loss
- Clean white background with professional fonts
- Efficient resource loading

## Dependencies

- `tkinter` - GUI framework (bundled with Python)
- `tkcalendar` - Calendar widget
- `hijridate` - Date conversion library
- `pyglet` - Font loading

## Language Support

**Arabic (عربي)**
- Right-to-left layout
- IBM Plex Sans Arabic font
- Arabic month and day names

**English**
- Left-to-right layout
- Montserrat font
- Standard calendar terminology

**Korean (한국어)**
- Left-to-right layout
- Montserrat font
- Korean calendar terms

## Author

Abdulrahman Aldayel
