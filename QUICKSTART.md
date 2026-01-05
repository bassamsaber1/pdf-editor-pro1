# Quick Start Guide - دليل البداية السريعة

<div dir="rtl">

## البداية السريعة

### 1. التثبيت السريع
```bash
# استنساخ المستودع
git clone https://github.com/bassamsaber1/pdf-editor-pro1.git
cd pdf-editor-pro1

# تثبيت المكتبات
pip install -r requirements.txt

# تشغيل البرنامج
python pdf_editor.py
```

### 2. أمثلة الاستخدام

#### مثال 1: إضافة نص عربي إلى PDF
1. افتح التبويب "إضافة نص"
2. اختر ملف PDF
3. اكتب: "هذا نص تجريبي"
4. الموضع: X=100, Y=100
5. حجم الخط: 16
6. اللون: #0000FF (أزرق)
7. اضغط "إضافة النص إلى PDF"

#### مثال 2: دمج 3 ملفات PDF
1. افتح التبويب "دمج ملفات"
2. اضغط "إضافة ملفات"
3. اختر الملفات: file1.pdf, file2.pdf, file3.pdf
4. اضغط "دمج الملفات"
5. احفظ باسم: merged_document.pdf

#### مثال 3: استخراج صفحات 1-5 و 10
1. افتح التبويب "استخراج صفحات"
2. اختر ملف PDF
3. أدخل: 1-5, 10
4. اضغط "استخراج الصفحات"
5. احفظ الملف

#### مثال 4: إضافة علامة مائية نصية
1. افتح التبويب "علامة مائية"
2. اختر ملف PDF
3. اختر "نص"
4. اكتب: "سري - Confidential"
5. الشفافية: 0.3
6. اضغط "إضافة العلامة المائية"

#### مثال 5: تحويل PDF إلى صور عالية الجودة
1. افتح التبويب "تحويل لصور"
2. اختر ملف PDF
3. الصيغة: PNG
4. الدقة: 300 DPI
5. اختر مجلد الحفظ
6. اضغط "تحويل إلى صور"

### 3. نصائح وحيل

#### للحصول على أفضل النتائج:
- استخدم ملفات PDF أصلية (غير ممسوحة ضوئياً) للحصول على أفضل جودة
- اختر حجم خط مناسب (12-16 للنصوص العادية)
- استخدم ألواناً متباينة للنصوص لسهولة القراءة
- عند تحويل لصور، استخدم DPI 200-300 للجودة العالية
- احفظ نسخة احتياطية من الملف الأصلي قبل التعديل

#### لتحسين الأداء:
- أغلق البرامج الأخرى عند معالجة ملفات كبيرة
- استخدم ملفات PDF أصغر من 50 ميجابايت للحصول على أداء أفضل
- قلل دقة الصور (DPI) إذا كانت الجودة العالية غير ضرورية

#### حل مشاكل شائعة:
- **النص العربي يظهر مقلوباً**: لا تقلق، البرنامج يعالج هذا تلقائياً
- **الصور كبيرة جداً**: اضبط حجم الصورة في الخيارات قبل الإضافة
- **ملف PDF لا يفتح**: تأكد أن الملف غير محمي بكلمة مرور

</div>

---

## Quick Start

### 1. Quick Installation
```bash
# Clone the repository
git clone https://github.com/bassamsaber1/pdf-editor-pro1.git
cd pdf-editor-pro1

# Install libraries
pip install -r requirements.txt

# Run the program
python pdf_editor.py
```

### 2. Usage Examples

#### Example 1: Add Arabic Text to PDF
1. Open "Add Text" tab
2. Choose PDF file
3. Type: "هذا نص تجريبي" (This is test text)
4. Position: X=100, Y=100
5. Font size: 16
6. Color: #0000FF (blue)
7. Click "Add Text to PDF"

#### Example 2: Merge 3 PDF Files
1. Open "Merge PDFs" tab
2. Click "Add Files"
3. Select files: file1.pdf, file2.pdf, file3.pdf
4. Click "Merge Files"
5. Save as: merged_document.pdf

#### Example 3: Extract Pages 1-5 and 10
1. Open "Extract Pages" tab
2. Choose PDF file
3. Enter: 1-5, 10
4. Click "Extract Pages"
5. Save the file

#### Example 4: Add Text Watermark
1. Open "Watermark" tab
2. Choose PDF file
3. Select "Text"
4. Type: "Confidential - سري"
5. Opacity: 0.3
6. Click "Add Watermark"

#### Example 5: Convert PDF to High-Quality Images
1. Open "Convert to Images" tab
2. Choose PDF file
3. Format: PNG
4. Quality: 300 DPI
5. Choose output folder
6. Click "Convert to Images"

### 3. Tips and Tricks

#### For Best Results:
- Use original PDFs (not scanned) for best quality
- Choose appropriate font size (12-16 for normal text)
- Use contrasting colors for text readability
- For image conversion, use DPI 200-300 for high quality
- Keep backup copy of original file before editing

#### Performance Optimization:
- Close other programs when processing large files
- Use PDF files smaller than 50 MB for better performance
- Reduce image quality (DPI) if high quality not needed

#### Common Issues:
- **Arabic text appears reversed**: Don't worry, program handles this automatically
- **Images too large**: Adjust image size in options before adding
- **PDF won't open**: Ensure file is not password protected

---

## Command Line Usage (Advanced)

For advanced users, you can use Python directly:

```python
# Example: Merge PDFs programmatically
import PyPDF2

merger = PyPDF2.PdfMerger()
merger.append('file1.pdf')
merger.append('file2.pdf')
merger.write('merged.pdf')
merger.close()
```

---

## Keyboard Shortcuts

- **Ctrl+Tab**: Switch between tabs
- **Ctrl+O**: Open file dialog (in active tab)
- **Ctrl+S**: Save file dialog (in active tab)
- **Esc**: Close dialog boxes

---

## Video Tutorials (Coming Soon)

We're working on video tutorials in Arabic and English to help you get started quickly!

---

## Need Help?

- 📖 Check the [README.md](README.md) for detailed documentation
- 🐛 Found a bug? [Open an issue](https://github.com/bassamsaber1/pdf-editor-pro1/issues)
- 💡 Have a suggestion? Let us know!
- 📧 Contact us via email

---

**Happy PDF Editing! - تحرير PDF سعيد!** 🎉
