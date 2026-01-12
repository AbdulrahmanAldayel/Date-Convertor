"""Main application window."""

import tkinter as tk
from tkinter import ttk, messagebox
import pyglet
import os
import sys
import logging
from typing import Optional

from ..config.settings import config, Language, CalendarType
from ..core.calendar_converter import HijriGregorianConverter, DateResult
from ..localization.translations import Translator


logger = logging.getLogger(__name__)


class ResourceManager:
    """Manages application resources like fonts and images."""
    
    def __init__(self):
        self._resource_base = self._get_resource_base()
        self._loaded_fonts = set()
    
    def _get_resource_base(self) -> str:
        """Get the base path for resources."""
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return base_path
    
    def get_resource_path(self, relative_path: str) -> str:
        """Get full path to a resource."""
        return os.path.join(self._resource_base, relative_path)
    
    def load_font(self, font_path: str) -> bool:
        """Load a font file."""
        if font_path not in self._loaded_fonts:
            try:
                full_path = self.get_resource_path(font_path)
                pyglet.font.add_file(full_path)
                self._loaded_fonts.add(font_path)
                logger.info(f"Loaded font: {font_path}")
                return True
            except Exception as e:
                logger.error(f"Failed to load font {font_path}: {e}")
                return False
        return True


class DateConverterUI:
    """Main application UI."""
    
    def __init__(self):
        self.resource_manager = ResourceManager()
        self.translator = Translator()
        self.converter = HijriGregorianConverter()
        
        # Load fonts
        self.resource_manager.load_font(
            config.get_font_path(config.paths.arabic_font)
        )
        self.resource_manager.load_font(
            config.get_font_path(config.paths.latin_font)
        )
        
        # Initialize UI
        self._setup_window()
        self._create_widgets()
        self._setup_layout()
        
        # Set default language
        self.set_language(Language.ARABIC)
    
    def _setup_window(self):
        """Setup the main window."""
        self.root = tk.Tk()
        self.root.geometry(f"{config.ui.window_width}x{config.ui.window_height}")
        self.root.configure(background=config.ui.background_color)
        
        # Set icon
        try:
            icon_path = self.resource_manager.get_resource_path(
                config.get_image_path(config.paths.icon_file)
            )
            self.root.iconbitmap(icon_path)
        except Exception as e:
            logger.warning(f"Could not load icon: {e}")
        
        # Setup styles
        self.style = ttk.Style()
        self._setup_styles()
    
    def _setup_styles(self):
        """Configure ttk styles."""
        self.style.configure('TLabelframe', background=config.ui.background_color)
        self.style.configure('TLabelframe.Label', background=config.ui.background_color)
        self.style.configure('TRadiobutton', background=config.ui.background_color)
        self.style.configure('TLabel', background=config.ui.background_color, 
                           bd=0, highlightthickness=0, relief='flat')
        self.style.configure('TFrame', background=config.ui.background_color)
        self.style.configure('TPhotoImage', highlightthickness=0)
    
    def _create_widgets(self):
        """Create all UI widgets."""
        # Language buttons frame
        self.language_frame = tk.Frame(self.root, background=config.ui.background_color)
        
        self.english_button = tk.Button(
            self.language_frame, text="English",
            command=lambda: self.set_language(Language.ENGLISH)
        )
        self.korean_button = tk.Button(
            self.language_frame, text="한국어",
            command=lambda: self.set_language(Language.KOREAN)
        )
        self.arabic_button = tk.Button(
            self.language_frame, text="عربي",
            command=lambda: self.set_language(Language.ARABIC)
        )
        
        # Title
        self.title_label = tk.Label(self.root)
        
        # Calendar selection frame
        self.calendar_frame = ttk.LabelFrame(self.root)
        self.selected_calendar = tk.StringVar()
        
        self.hijri_radio = ttk.Radiobutton(
            self.calendar_frame, variable=self.selected_calendar,
            value=CalendarType.HIJRI.value, command=self._on_calendar_change
        )
        self.gregorian_radio = ttk.Radiobutton(
            self.calendar_frame, variable=self.selected_calendar,
            value=CalendarType.GREGORIAN.value, command=self._on_calendar_change
        )
        
        # Date input frame
        self.date_input_frame = tk.Frame(self.root, background=config.ui.background_color)
        
        self.year_label = tk.Label(self.date_input_frame)
        self.year_entry = tk.Entry(self.date_input_frame, width=10, justify='center')
        
        self.month_label = tk.Label(self.date_input_frame)
        self.selected_month = tk.StringVar()
        self.month_dropdown = ttk.Combobox(self.date_input_frame, width=10, 
                                          textvariable=self.selected_month, justify='center')
        
        self.day_label = tk.Label(self.date_input_frame)
        self.day_dropdown = ttk.Combobox(self.date_input_frame, width=5, justify='center')
        
        self.convert_button = tk.Button(self.date_input_frame, command=self._convert_date)
        
        # Result display
        self.result_label = tk.Label(self.root)
        self.result_detail_label = tk.Label(self.root)
        
        # Bottom frame with logo and info
        self.bottom_frame = tk.Frame(self.root, background=config.ui.background_color)
        
        try:
            logo_path = self.resource_manager.get_resource_path(
                config.get_image_path(config.paths.logo_file)
            )
            self.logo = tk.PhotoImage(file=logo_path)
            self.logo_label = tk.Label(self.bottom_frame, image=self.logo)
        except Exception as e:
            logger.warning(f"Could not load logo: {e}")
            self.logo_label = None
        
        self.info_button = tk.Button(self.bottom_frame, command=self._show_info)
    
    def _setup_layout(self):
        """Setup widget layout."""
        # Language buttons
        self.language_frame.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)
        self.english_button.pack(side=tk.RIGHT, padx=5)
        self.korean_button.pack(side=tk.RIGHT, padx=5)
        self.arabic_button.pack(side=tk.RIGHT, padx=5)
        
        # Title
        self.title_label.pack(pady=(0, 0))
        
        # Calendar selection
        self.calendar_frame.pack(pady=10, padx=50, anchor=tk.CENTER)
        self.hijri_radio.pack(side=tk.RIGHT, anchor=tk.E, padx=10)
        self.gregorian_radio.pack(side=tk.RIGHT, anchor=tk.E, padx=10)
        
        # Date input
        self.date_input_frame.pack(pady=20)
        
        # Results
        self.result_label.pack(pady=10)
        self.result_detail_label.pack(pady=10)
        
        # Bottom frame
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, ipadx=10, ipady=10)
        if self.logo_label:
            self.logo_label.pack(side="right", anchor=tk.SE, pady=10, padx=10)
        self.info_button.pack(side="left", anchor=tk.SW, pady=10, padx=10)
    
    def _on_calendar_change(self):
        """Handle calendar type change."""
        self._update_date_inputs()
        self._clear_results()
    
    def _update_date_inputs(self):
        """Update date input fields based on selected calendar."""
        # Clear current layout
        for widget in self.date_input_frame.winfo_children():
            widget.grid_forget()
        
        # Get month options
        if self.selected_calendar.get() == CalendarType.HIJRI.value:
            months = self.translator.get_hijri_months(numbered=True)
        else:
            months = self.translator.get_gregorian_months(numbered=True)
        
        self.month_dropdown['values'] = months
        self.month_dropdown.set(self.translator.get_text('month_placeholder'))
        
        # Set day options
        self.day_dropdown['values'] = list(range(1, 32))
        self.day_dropdown.set(self.translator.get_text('day_placeholder'))
        
        # Layout based on language
        if self.translator.language == Language.ARABIC:
            self._layout_arabic()
        else:
            self._layout_latin()
        
        self.convert_button.config(state=tk.NORMAL)
    
    def _layout_arabic(self):
        """Layout for Arabic (RTL)."""
        self.year_label.grid(row=0, column=3)
        self.year_entry.grid(row=1, column=3, padx=10)
        self.month_label.grid(row=0, column=2)
        self.month_dropdown.grid(row=1, column=2, padx=10)
        self.day_label.grid(row=0, column=1)
        self.day_dropdown.grid(row=1, column=1, padx=10)
        self.convert_button.grid(row=1, column=0, padx=10)
        
        self.result_label.pack(pady=10, padx=(10, 40), side=tk.RIGHT, 
                              justify='right')
        self.result_detail_label.pack(pady=10, padx=10, side=tk.RIGHT, 
                                     justify='right')
    
    def _layout_latin(self):
        """Layout for English/Korean (LTR)."""
        self.year_label.grid(row=0, column=0)
        self.year_entry.grid(row=1, column=0, padx=10)
        self.month_label.grid(row=0, column=1)
        self.month_dropdown.grid(row=1, column=1, padx=10)
        self.day_label.grid(row=0, column=2)
        self.day_dropdown.grid(row=1, column=2, padx=10)
        self.convert_button.grid(row=1, column=3, padx=10)
        
        self.result_label.pack(pady=10, padx=(40, 10), side=tk.LEFT, 
                              justify='left')
        self.result_detail_label.pack(pady=10, padx=10, side=tk.LEFT, 
                                     justify='left')
    
    def _convert_date(self):
        """Convert the selected date."""
        try:
            year = int(self.year_entry.get())
            month_name = self.month_dropdown.get()
            day = int(self.day_dropdown.get())
            
            # Get month index
            if self.selected_calendar.get() == CalendarType.HIJRI.value:
                months = self.translator.get_hijri_months(numbered=True)
            else:
                months = self.translator.get_gregorian_months(numbered=True)
            
            month = months.index(month_name) + 1
            
            # Perform conversion
            if self.selected_calendar.get() == CalendarType.GREGORIAN.value:
                gregorian_result = DateResult(day, month, year, "", "", "")
                hijri_result = self.converter.to_hijri(day, month, year)
                self._display_results(gregorian_result, hijri_result)
            else:
                hijri_result = DateResult(day, month, year, "", "", "")
                gregorian_result = self.converter.to_gregorian(day, month, year)
                self._display_results(gregorian_result, hijri_result)
                
        except (ValueError, IndexError) as e:
            messagebox.showerror(
                self.translator.get_text('error'),
                self.translator.get_text('error_invalid_date')
            )
            logger.warning(f"Conversion error: {e}")
    
    def _display_results(self, gregorian: DateResult, hijri: DateResult):
        """Display conversion results."""
        # Format dates with proper month names
        gregorian_month = self.translator.get_gregorian_month(gregorian.month)
        hijri_month = self.translator.get_hijri_month(hijri.month)
        weekday = self.translator.get_weekday(gregorian.weekday)
        
        if self.translator.language == Language.ARABIC:
            result_text = f"{self.translator.get_text('hijri_date')}\n{self.translator.get_text('gregorian_date')}"
            detail_text = f"{hijri.year} {weekday}، {hijri.day} {hijri_month}\n{gregorian.year} {weekday}، {gregorian.day} {gregorian_month}"
        elif self.translator.language == Language.KOREAN:
            result_text = f"{self.translator.get_text('hijri_date')}\n{self.translator.get_text('gregorian_date')}"
            detail_text = f"{weekday}, {hijri.year}년 {hijri_month} {hijri.day}일\n{weekday}, {gregorian.year}년 {gregorian_month} {gregorian.day}일"
        else:
            result_text = f"{self.translator.get_text('hijri_date')}\n{self.translator.get_text('gregorian_date')}"
            detail_text = f"{weekday}, {hijri.day} {hijri_month} {hijri.year}\n{weekday}, {gregorian.day} {gregorian_month} {gregorian.year}"
        
        self.result_label.config(text=result_text)
        self.result_detail_label.config(text=detail_text)
    
    def _clear_results(self):
        """Clear result display."""
        self.result_label.config(text="")
        self.result_detail_label.config(text="")
    
    def _show_info(self):
        """Show about information."""
        messagebox.showinfo(
            self.translator.get_text('info'),
            self.translator.get_text('info_content')
        )
    
    def set_language(self, language: Language):
        """Set application language."""
        self.translator.set_language(language)
        self._update_ui_text()
        self._update_fonts()
        self._update_date_inputs()
        
        # Trigger default selection
        if language == Language.ARABIC:
            self.arabic_button.invoke()
    
    def _update_ui_text(self):
        """Update all UI text based on current language."""
        # Window title
        self.root.title(self.translator.get_text('title'))
        
        # Widgets
        self.title_label.config(
            text=self.translator.get_text('title'),
            font=self._get_title_font()
        )
        
        self.calendar_frame.config(text=self.translator.get_text('calendar'))
        self.hijri_radio.config(text=self.translator.get_text('hijri'))
        self.gregorian_radio.config(text=self.translator.get_text('gregorian'))
        
        self.year_label.config(
            text=self.translator.get_text('year'),
            font=self._get_label_font()
        )
        self.month_label.config(
            text=self.translator.get_text('month'),
            font=self._get_label_font()
        )
        self.day_label.config(
            text=self.translator.get_text('day'),
            font=self._get_label_font()
        )
        
        self.convert_button.config(
            text=self.translator.get_text('convert'),
            font=self._get_button_font()
        )
        
        self.info_button.config(text=self.translator.get_text('info'))
        
        # Frame title font
        self.style.configure('TLabelframe.Label', font=self._get_frame_font())
        self.style.configure('TRadiobutton', font=self._get_radio_font())
    
    def _update_fonts(self):
        """Update fonts based on language."""
        if self.translator.language == Language.ARABIC:
            font_family = config.ui.font_arabic
        else:
            font_family = config.ui.font_latin
        
        # Update result labels
        self.result_label.config(font=(font_family, 15, 'bold'))
        self.result_detail_label.config(font=(font_family, 15))
    
    def _get_title_font(self):
        """Get title font based on language."""
        family = (config.ui.font_arabic if self.translator.language == Language.ARABIC 
                 else config.ui.font_latin)
        return (family, config.ui.title_font_size, 'bold')
    
    def _get_label_font(self):
        """Get label font based on language."""
        family = (config.ui.font_arabic if self.translator.language == Language.ARABIC 
                 else config.ui.font_latin)
        return (family, config.ui.label_font_size, 'bold')
    
    def _get_button_font(self):
        """Get button font based on language."""
        family = (config.ui.font_arabic if self.translator.language == Language.ARABIC 
                 else config.ui.font_latin)
        return (family, config.ui.button_font_size, 'bold')
    
    def _get_frame_font(self):
        """Get frame font based on language."""
        family = (config.ui.font_arabic if self.translator.language == Language.ARABIC 
                 else config.ui.font_latin)
        return (family, config.ui.frame_font_size, 'bold')
    
    def _get_radio_font(self):
        """Get radio button font based on language."""
        family = (config.ui.font_arabic if self.translator.language == Language.ARABIC 
                 else config.ui.font_latin)
        return (family, config.ui.radio_font_size)
    
    def run(self):
        """Start the application."""
        self.root.mainloop()
