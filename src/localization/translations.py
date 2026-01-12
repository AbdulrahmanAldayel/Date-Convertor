"""Translation data for all supported languages."""

from typing import Dict, List
from ..config.settings import Language


class TranslationData:
    """Centralized translation data."""
    
    # Gregorian months
    GREGORIAN_MONTHS: Dict[Language, List[str]] = {
        Language.ARABIC: [
            'يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو',
            'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسبمر'
        ],
        Language.ENGLISH: [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ],
        Language.KOREAN: [
            '일월', '이월', '삼월', '사월', '오월', '유월',
            '칠월', '팔월', '구월', '시월', '십일월', '십이월'
        ]
    }
    
    # Gregorian months with numbers
    GREGORIAN_MONTHS_NUMBERED: Dict[Language, List[str]] = {
        Language.ARABIC: [
            '1 - يناير', '2 - فبراير', '3 - مارس', '4 - أبريل', '5 - مايو', '6 - يونيو',
            '7 - يوليو', '8 - أغسطس', '9 - سبتمبر', '10 - أكتوبر', '11 - نوفمبر', '12 - ديسبمر'
        ],
        Language.ENGLISH: [
            '1 - January', '2 - February', '3 - March', '4 - April', '5 - May', '6 - June',
            '7 - July', '8 - August', '9 - September', '10 - October', '11 - November', '12 - December'
        ],
        Language.KOREAN: [
            '1월', '2월', '3월', '4월', '5월', '6월',
            '7월', '8월', '9월', '10월', '11월', '12월'
        ]
    }
    
    # Hijri months
    HIJRI_MONTHS: Dict[Language, List[str]] = {
        Language.ARABIC: [
            'محرم', 'صفر', 'ربيع أول', 'ربيع ثاني', 'جمادى الأولى', 'جمادى الآخرة',
            'رجب', 'شعبان', 'رمضان', 'شوال', 'ذو القعدة', 'ذو الحجة'
        ],
        Language.ENGLISH: [
            'Muharram', 'Safar', 'Rabīʿ al-Awwal', 'Rabīʿ al-Thānī', 'Jumādā al-Awwal', 'Jumādā al-Thānī',
            'Rajab', 'Shaʿbān', 'Ramaḍān', 'Shawwāl', 'Dhū al-Qaʿdah', 'Dhū al-Ḥijjah'
        ],
        Language.KOREAN: [
            '무하람', '사파르', '라비 알아우왈', '라비 알타니', '주마다 알아우왈', '주마다 알타니',
            '라자브', '샤아반', '라마단', '샤우왈', '두 알카이다', '두 알히자'
        ]
    }
    
    # Hijri months with numbers
    HIJRI_MONTHS_NUMBERED: Dict[Language, List[str]] = {
        Language.ARABIC: [
            '1 - محرم', '2 - صفر', '3 - ربيع أول', '4 - ربيع ثاني', '5 - جمادى الأولى', '6 - جمادى الآخرة',
            '7 - رجب', '8 - شعبان', '9 - رمضان', '10 - شوال', '11 - ذو القعدة', '12 - ذو الحجة'
        ],
        Language.ENGLISH: [
            '1 - Muharram', '2 - Safar', '3 - Rabīʿ al-Awwal', '4 - Rabīʿ al-Thānī', '5 - Jumādā al-Awwal', '6 - Jumādā al-Thānī',
            '7 - Rajab', '8 - Shaʿbān', '9 - Ramaḍān', '10 - Shawwāl', '11 - Dhū al-Qaʿdah', '12 - Dhū al-Ḥijjah'
        ],
        Language.KOREAN: [
            '1 - 무하람', '2 - 사파르', '3 - 라비 알아우왈', '4 - 라비 알타니', '5 - 주마다 알아우왈', '6 - 주마다 알타니',
            '7 - 라자브', '8 - 샤아반', '9 - 라마단', '10 - 샤우왈', '11 - 두 알카이다', '12 - 두 알히자'
        ]
    }
    
    # Weekdays
    WEEKDAYS: Dict[Language, Dict[str, str]] = {
        Language.ARABIC: {
            'Monday': 'الإثنين', 'Tuesday': 'الثلاثاء', 'Wednesday': 'الأربعاء',
            'Thursday': 'الخميس', 'Friday': 'الجمعة', 'Saturday': 'السبت', 'Sunday': 'الأحد'
        },
        Language.ENGLISH: {
            'Monday': 'Monday', 'Tuesday': 'Tuesday', 'Wednesday': 'Wednesday',
            'Thursday': 'Thursday', 'Friday': 'Friday', 'Saturday': 'Saturday', 'Sunday': 'Sunday'
        },
        Language.KOREAN: {
            'Monday': '월요일', 'Tuesday': '화요일', 'Wednesday': '수요일',
            'Thursday': '목요일', 'Friday': '금요일', 'Saturday': '토요일', 'Sunday': '일요일'
        }
    }
    
    # UI Text
    UI_TEXT: Dict[Language, Dict[str, str]] = {
        Language.ARABIC: {
            'title': 'محول التاريخ الهجري',
            'calendar': 'التقويم',
            'hijri': 'هجري',
            'gregorian': 'غريغوري',
            'year': 'عام',
            'month': 'شهر',
            'day': 'اليوم',
            'convert': 'حول',
            'info': 'معلومات',
            'hijri_date': ':التاريخ الهجري',
            'gregorian_date': ':التاريخ الغريغوري',
            'error_invalid_date': 'التاريخ المدخل غير صحيح',
            'error': 'خطأ',
            'info_content': 'تطوير عبدالرحمن الدايل \n\nMIT رخصة\nحقوق النشر (c) 2024 Abdulrahman Aldayel',
            'month_placeholder': 'الشهر',
            'day_placeholder': 'اليوم'
        },
        Language.ENGLISH: {
            'title': 'Hijri Date Converter',
            'calendar': 'Calendar',
            'hijri': 'Hijri',
            'gregorian': 'Gregorian',
            'year': 'Year',
            'month': 'Month',
            'day': 'Day',
            'convert': 'Convert',
            'info': 'Info',
            'hijri_date': 'Hijri:',
            'gregorian_date': 'Gregorian:',
            'error_invalid_date': 'Invalid date entered!',
            'error': 'Error',
            'info_content': 'Developed by Abdulrahman Aldayel \n\nMIT License\nCopyright (c) 2024 Abdulrahman Aldayel',
            'month_placeholder': 'Month',
            'day_placeholder': 'Day'
        },
        Language.KOREAN: {
            'title': '히즈리 날짜 변환기',
            'calendar': '달력',
            'hijri': '히즈라력',
            'gregorian': '그레고리력',
            'year': '년',
            'month': '월',
            'day': '일',
            'convert': '변환',
            'info': '정보',
            'hijri_date': '히즈라력:',
            'gregorian_date': '그레고리력:',
            'error_invalid_date': '잘못된 날짜 입력!',
            'error': '에러',
            'info_content': '압도라만 아다엘에 의해 개발됨\n\nMIT 허가서\n\n저작권 (c) 2024 Abdulrahman Aldayel',
            'month_placeholder': '월',
            'day_placeholder': '날'
        }
    }


class Translator:
    """Translation service."""
    
    def __init__(self, language: Language = Language.ARABIC):
        self.language = language
        self.data = TranslationData()
    
    def set_language(self, language: Language):
        """Set the current language."""
        self.language = language
    
    def get_text(self, key: str) -> str:
        """Get translated text for UI elements."""
        return self.data.UI_TEXT[self.language].get(key, key)
    
    def get_gregorian_month(self, month_index: int, numbered: bool = False) -> str:
        """Get Gregorian month name."""
        months = (self.data.GREGORIAN_MONTHS_NUMBERED if numbered 
                 else self.data.GREGORIAN_MONTHS)
        return months[self.language][month_index - 1]
    
    def get_hijri_month(self, month_index: int, numbered: bool = False) -> str:
        """Get Hijri month name."""
        months = (self.data.HIJRI_MONTHS_NUMBERED if numbered 
                 else self.data.HIJRI_MONTHS)
        return months[self.language][month_index - 1]
    
    def get_weekday(self, english_weekday: str) -> str:
        """Get translated weekday name."""
        return self.data.WEEKDAYS[self.language].get(english_weekday, english_weekday)
    
    def get_gregorian_months(self, numbered: bool = False) -> List[str]:
        """Get all Gregorian month names."""
        return (self.data.GREGORIAN_MONTHS_NUMBERED if numbered 
                else self.data.GREGORIAN_MONTHS)[self.language]
    
    def get_hijri_months(self, numbered: bool = False) -> List[str]:
        """Get all Hijri month names."""
        return (self.data.HIJRI_MONTHS_NUMBERED if numbered 
                else self.data.HIJRI_MONTHS)[self.language]
