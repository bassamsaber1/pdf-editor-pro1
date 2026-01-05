# PDF Editor Pro - محرر PDF الاحترافي

<div dir="rtl">

## نظرة عامة

PDF Editor Pro هو برنامج شامل ومجاني لتحرير ملفات PDF مع واجهة رسومية سهلة الاستخدام. يدعم البرنامج اللغة العربية بشكل كامل ويوفر جميع الأدوات الأساسية لمعالجة ملفات PDF.

</div>

---

## Overview

PDF Editor Pro is a comprehensive and free PDF editing program with an easy-to-use graphical interface. The program fully supports Arabic language and provides all essential tools for PDF file manipulation.

---

<div dir="rtl">

## الميزات الرئيسية

### 1. إضافة النصوص
- إضافة نصوص في أي مكان على صفحات PDF
- دعم كامل للغة العربية
- التحكم في حجم الخط واللون والموضع
- معاينة النتيجة قبل الحفظ

### 2. إضافة الصور
- إضافة صور إلى صفحات PDF
- التحكم في حجم وموضع الصورة
- دعم صيغ متعددة (PNG, JPG, JPEG, GIF, BMP)

### 3. دمج ملفات PDF
- دمج عدة ملفات PDF في ملف واحد
- الحفاظ على جودة المحتوى الأصلي
- إمكانية اختيار ملفات متعددة وترتيبها

### 4. تقسيم ملفات PDF
- تقسيم ملف PDF إلى ملفات منفصلة
- تقسيم كل صفحة في ملف منفصل
- تقسيم حسب نطاق صفحات محدد

### 5. استخراج صفحات معينة
- استخراج صفحات محددة من ملف PDF
- دعم نطاقات الصفحات (مثال: 1-5, 7, 9-12)
- حفظ الصفحات المستخرجة في ملف جديد

### 6. إضافة علامة مائية
- إضافة نص كعلامة مائية
- إضافة صورة كعلامة مائية
- التحكم في الشفافية والموضع

### 7. تحويل PDF إلى صور
- تحويل صفحات PDF إلى صور (PNG, JPG)
- التحكم في دقة الصور الناتجة (DPI)
- حفظ كل صفحة كصورة منفصلة

</div>

---

## Main Features

### 1. Add Text
- Add text anywhere on PDF pages
- Full Arabic language support
- Control font size, color, and position
- Preview results before saving

### 2. Add Images
- Add images to PDF pages
- Control image size and position
- Support multiple formats (PNG, JPG, JPEG, GIF, BMP)

### 3. Merge PDF Files
- Merge multiple PDF files into one
- Maintain original content quality
- Select and arrange multiple files

### 4. Split PDF Files
- Split PDF into separate files
- Split each page into separate file
- Split by specific page range

### 5. Extract Specific Pages
- Extract specific pages from PDF
- Support page ranges (e.g., 1-5, 7, 9-12)
- Save extracted pages to new file

### 6. Add Watermark
- Add text as watermark
- Add image as watermark
- Control transparency and position

### 7. Convert PDF to Images
- Convert PDF pages to images (PNG, JPG)
- Control output image quality (DPI)
- Save each page as separate image

---

<div dir="rtl">

## متطلبات النظام

### نظام التشغيل
- Windows 10 أو أحدث (موصى به)
- Linux (مدعوم)
- macOS (مدعوم)

### البرامج المطلوبة
- Python 3.8 أو أحدث
- مساحة تخزين: 100 ميجابايت على الأقل
- ذاكرة RAM: 2 جيجابايت على الأقل (4 جيجابايت موصى بها)

</div>

---

## System Requirements

### Operating System
- Windows 10 or newer (recommended)
- Linux (supported)
- macOS (supported)

### Software Requirements
- Python 3.8 or newer
- Storage: At least 100 MB
- RAM: At least 2 GB (4 GB recommended)

---

<div dir="rtl">

## التثبيت والإعداد

### الخطوة 1: تحميل الملفات
قم بتحميل أو استنساخ المستودع:
```bash
git clone https://github.com/bassamsaber1/pdf-editor-pro1.git
cd pdf-editor-pro1
```

### الخطوة 2: إنشاء بيئة افتراضية (اختياري لكن موصى به)
```bash
# على Windows
python -m venv venv
venv\Scripts\activate

# على Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### الخطوة 3: تثبيت المكتبات المطلوبة
```bash
pip install -r requirements.txt
```

**ملاحظة:** قد تحتاج لتثبيت Poppler لاستخدام ميزة تحويل PDF إلى صور:

**على Windows:**
1. قم بتحميل Poppler من: https://github.com/oschwartz10612/poppler-windows/releases
2. استخرج الملفات وأضف مجلد `bin` إلى متغيرات البيئة PATH

**على Linux:**
```bash
sudo apt-get install poppler-utils
```

**على Mac:**
```bash
brew install poppler
```

### الخطوة 4: تشغيل البرنامج
```bash
python pdf_editor.py
```

</div>

---

## Installation and Setup

### Step 1: Download Files
Download or clone the repository:
```bash
git clone https://github.com/bassamsaber1/pdf-editor-pro1.git
cd pdf-editor-pro1
```

### Step 2: Create Virtual Environment (optional but recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Libraries
```bash
pip install -r requirements.txt
```

**Note:** You may need to install Poppler for PDF to image conversion feature:

**On Windows:**
1. Download Poppler from: https://github.com/oschwartz10612/poppler-windows/releases
2. Extract files and add the `bin` folder to PATH environment variable

**On Linux:**
```bash
sudo apt-get install poppler-utils
```

**On Mac:**
```bash
brew install poppler
```

### Step 4: Run the Program
```bash
python pdf_editor.py
```

---

<div dir="rtl">

## دليل الاستخدام

### إضافة نص إلى PDF
1. افتح تبويب "إضافة نص"
2. اختر ملف PDF المراد التعديل عليه
3. اكتب النص المراد إضافته (يدعم العربية)
4. حدد رقم الصفحة والموضع (X, Y)
5. اختر حجم الخط واللون
6. اضغط "إضافة النص إلى PDF"
7. سيتم حفظ الملف الجديد باسم ينتهي بـ `_with_text.pdf`

### إضافة صورة إلى PDF
1. افتح تبويب "إضافة صورة"
2. اختر ملف PDF
3. اختر ملف الصورة
4. حدد رقم الصفحة والموضع (X, Y)
5. حدد حجم الصورة (عرض × ارتفاع)
6. اضغط "إضافة الصورة إلى PDF"
7. سيتم حفظ الملف الجديد باسم ينتهي بـ `_with_image.pdf`

### دمج ملفات PDF
1. افتح تبويب "دمج ملفات"
2. اضغط "إضافة ملفات" واختر ملفات PDF المراد دمجها
3. يمكنك إضافة ملفات متعددة
4. يمكنك إزالة ملف من القائمة بتحديده والضغط "إزالة المحدد"
5. اضغط "دمج الملفات"
6. اختر اسم ومكان حفظ الملف المدموج

### تقسيم ملف PDF
1. افتح تبويب "تقسيم ملف"
2. اختر ملف PDF المراد تقسيمه
3. اختر طريقة التقسيم:
   - "تقسيم كل صفحة في ملف منفصل": لإنشاء ملف منفصل لكل صفحة
   - "تقسيم حسب النطاق": لاستخراج نطاق معين من الصفحات
4. اختر مجلد الحفظ
5. اضغط "تقسيم الملف"

### استخراج صفحات معينة
1. افتح تبويب "استخراج صفحات"
2. اختر ملف PDF
3. أدخل أرقام الصفحات المراد استخراجها (مثال: 1-5, 7, 9-12)
4. اضغط "استخراج الصفحات"
5. اختر اسم ومكان حفظ الملف الجديد

### إضافة علامة مائية
1. افتح تبويب "علامة مائية"
2. اختر ملف PDF
3. اختر نوع العلامة المائية:
   - **نص**: اكتب النص المراد إضافته كعلامة مائية
   - **صورة**: اختر صورة لاستخدامها كعلامة مائية
4. اضبط الشفافية (0 = شفاف تماماً، 1 = غير شفاف)
5. اضغط "إضافة العلامة المائية"
6. سيتم حفظ الملف الجديد باسم ينتهي بـ `_watermarked.pdf`

### تحويل PDF إلى صور
1. افتح تبويب "تحويل لصور"
2. اختر ملف PDF المراد تحويله
3. اختر صيغة الصورة (PNG أو JPG)
4. اختر دقة الصور (DPI) - كلما زادت كانت الجودة أعلى
5. اختر مجلد الحفظ
6. اضغط "تحويل إلى صور"
7. سيتم حفظ كل صفحة كصورة منفصلة

</div>

---

## User Guide

### Add Text to PDF
1. Open "Add Text" tab
2. Choose PDF file to edit
3. Enter text to add (Arabic supported)
4. Specify page number and position (X, Y)
5. Choose font size and color
6. Click "Add Text to PDF"
7. New file will be saved with name ending in `_with_text.pdf`

### Add Image to PDF
1. Open "Add Image" tab
2. Choose PDF file
3. Choose image file
4. Specify page number and position (X, Y)
5. Set image size (width × height)
6. Click "Add Image to PDF"
7. New file will be saved with name ending in `_with_image.pdf`

### Merge PDF Files
1. Open "Merge PDFs" tab
2. Click "Add Files" and select PDF files to merge
3. You can add multiple files
4. You can remove a file by selecting it and clicking "Remove Selected"
5. Click "Merge Files"
6. Choose name and location for merged file

### Split PDF File
1. Open "Split PDF" tab
2. Choose PDF file to split
3. Choose split method:
   - "Split each page": create separate file for each page
   - "Split by range": extract specific page range
4. Choose output folder
5. Click "Split File"

### Extract Specific Pages
1. Open "Extract Pages" tab
2. Choose PDF file
3. Enter page numbers to extract (e.g., 1-5, 7, 9-12)
4. Click "Extract Pages"
5. Choose name and location for new file

### Add Watermark
1. Open "Watermark" tab
2. Choose PDF file
3. Choose watermark type:
   - **Text**: Enter text to add as watermark
   - **Image**: Choose image to use as watermark
4. Adjust opacity (0 = fully transparent, 1 = opaque)
5. Click "Add Watermark"
6. New file will be saved with name ending in `_watermarked.pdf`

### Convert PDF to Images
1. Open "Convert to Images" tab
2. Choose PDF file to convert
3. Choose image format (PNG or JPG)
4. Choose image quality (DPI) - higher means better quality
5. Choose output folder
6. Click "Convert to Images"
7. Each page will be saved as separate image

---

<div dir="rtl">

## بناء ملف EXE

لإنشاء ملف EXE قابل للتوزيع والتشغيل بدون Python:

### الطريقة 1: استخدام سكريبت البناء (موصى به)
```bash
python build_exe.py
```

سيقوم السكريبت بـ:
1. تنظيف ملفات البناء السابقة
2. بناء ملف EXE مستقل
3. حفظ الملف في مجلد `dist/`

### الطريقة 2: استخدام PyInstaller مباشرة
```bash
pyinstaller --onefile --windowed --name=PDFEditorPro pdf_editor.py
```

### بعد البناء
- ستجد ملف `PDFEditorPro.exe` في مجلد `dist/`
- يمكنك نسخ هذا الملف وتوزيعه بشكل مستقل
- لا يحتاج المستخدمون إلى تثبيت Python أو أي مكتبات

### ملاحظات مهمة
1. حجم ملف EXE قد يكون كبيراً (50-100 ميجابايت) لأنه يحتوي على جميع المكتبات
2. قد يظهر تحذير من Windows Defender عند التشغيل الأول - هذا طبيعي
3. يمكنك إضافة أيقونة مخصصة باستخدام الخيار `--icon=icon.ico`

</div>

---

## Building EXE File

To create a distributable EXE file that runs without Python:

### Method 1: Using Build Script (recommended)
```bash
python build_exe.py
```

The script will:
1. Clean previous build files
2. Build standalone EXE file
3. Save file to `dist/` folder

### Method 2: Using PyInstaller Directly
```bash
pyinstaller --onefile --windowed --name=PDFEditorPro pdf_editor.py
```

### After Building
- You'll find `PDFEditorPro.exe` in `dist/` folder
- You can copy and distribute this file independently
- Users don't need to install Python or any libraries

### Important Notes
1. EXE file size may be large (50-100 MB) as it contains all libraries
2. Windows Defender may show warning on first run - this is normal
3. You can add custom icon using `--icon=icon.ico` option

---

<div dir="rtl">

## حل المشاكل الشائعة

### المشكلة: خطأ في استيراد المكتبات
**الحل:**
```bash
pip install -r requirements.txt --upgrade
```

### المشكلة: لا تظهر النصوص العربية بشكل صحيح
**الحل:**
- تأكد من تثبيت مكتبات `arabic-reshaper` و `python-bidi`
- البرنامج يقوم بمعالجة النصوص العربية تلقائياً

### المشكلة: خطأ في تحويل PDF إلى صور
**الحل:**
- تأكد من تثبيت Poppler (انظر قسم التثبيت)
- على Windows، تأكد من إضافة Poppler إلى PATH

### المشكلة: البرنامج بطيء مع ملفات PDF الكبيرة
**الحل:**
- استخدم ملفات PDF أصغر حجماً
- قلل دقة الصور (DPI) عند التحويل
- تأكد من توفر ذاكرة RAM كافية

### المشكلة: خطأ في بناء ملف EXE
**الحل:**
```bash
pip install pyinstaller --upgrade
python build_exe.py
```

### المشكلة: ملف EXE لا يعمل على أجهزة أخرى
**الحل:**
- تأكد من بناء EXE على نفس نظام التشغيل المستهدف
- استخدم خيار `--onefile` لتضمين جميع الملفات
- ضع ملفات DLL المطلوبة في نفس مجلد EXE

</div>

---

## Troubleshooting

### Problem: Library import errors
**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Problem: Arabic text not displaying correctly
**Solution:**
- Ensure `arabic-reshaper` and `python-bidi` are installed
- Program processes Arabic text automatically

### Problem: Error converting PDF to images
**Solution:**
- Ensure Poppler is installed (see Installation section)
- On Windows, ensure Poppler is added to PATH

### Problem: Program slow with large PDF files
**Solution:**
- Use smaller PDF files
- Reduce image quality (DPI) when converting
- Ensure sufficient RAM is available

### Problem: Error building EXE file
**Solution:**
```bash
pip install pyinstaller --upgrade
python build_exe.py
```

### Problem: EXE doesn't work on other machines
**Solution:**
- Build EXE on same target operating system
- Use `--onefile` option to include all files
- Place required DLL files in same folder as EXE

---

<div dir="rtl">

## المساهمة

نرحب بجميع المساهمات! إذا كنت ترغب في المساهمة:

1. افتح Fork للمستودع
2. أنشئ فرع للميزة الجديدة (`git checkout -b feature/AmazingFeature`)
3. قم بعمل Commit للتغييرات (`git commit -m 'Add some AmazingFeature'`)
4. ادفع إلى الفرع (`git push origin feature/AmazingFeature`)
5. افتح Pull Request

### أفكار للتطوير
- إضافة ميزة حماية PDF بكلمة مرور
- دعم توقيع رقمي للمستندات
- إضافة ميزة ضغط ملفات PDF
- تحسين الأداء للملفات الكبيرة
- إضافة قوالب جاهزة للنصوص والصور

</div>

---

## Contributing

All contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Development Ideas
- Add PDF password protection feature
- Support digital document signatures
- Add PDF compression feature
- Improve performance for large files
- Add ready-made templates for text and images

---

<div dir="rtl">

## الرخصة

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

</div>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div dir="rtl">

## الدعم والتواصل

إذا واجهت أي مشاكل أو لديك اقتراحات:
- افتح Issue على GitHub
- راسلنا على البريد الإلكتروني
- شارك تجربتك مع البرنامج

</div>

## Support and Contact

If you encounter any problems or have suggestions:
- Open an Issue on GitHub
- Email us
- Share your experience with the program

---

<div dir="rtl">

## شكر وتقدير

شكراً لاستخدام PDF Editor Pro! نأمل أن يكون البرنامج مفيداً لك.

</div>

## Acknowledgments

Thank you for using PDF Editor Pro! We hope the program is useful for you.

---

**Made with ❤️ for the Arabic-speaking community**

**صُنع بكل ❤️ للمجتمع العربي**