#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for creating standalone EXE file
سكريبت لإنشاء ملف EXE مستقل
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def clean_build_directories():
    """Clean previous build directories"""
    print("تنظيف ملفات البناء السابقة... - Cleaning previous build files...")
    
    dirs_to_clean = ['build', 'dist', '__pycache__']
    files_to_clean = ['pdf_editor.spec']
    
    for directory in dirs_to_clean:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"تم حذف {directory} - Deleted {directory}")
    
    for file in files_to_clean:
        if os.path.exists(file):
            os.remove(file)
            print(f"تم حذف {file} - Deleted {file}")

def build_exe():
    """Build EXE file using PyInstaller"""
    print("\nبدء بناء ملف EXE... - Starting EXE build...")
    print("=" * 60)
    
    # Check if LICENSE file exists
    add_data_args = []
    if os.path.exists('LICENSE'):
        if sys.platform == 'win32':
            add_data_args.append('--add-data=LICENSE;.')
        else:
            add_data_args.append('--add-data=LICENSE:.')
    else:
        print("⚠ Warning: LICENSE file not found, skipping...")
    
    # PyInstaller command with options
    cmd = [
        'pyinstaller',
        '--onefile',                    # Create a single EXE file
        '--windowed',                   # No console window (GUI only)
        '--name=PDFEditorPro',          # Name of the EXE
        '--clean',                      # Clean cache before building
        '--noconfirm',                  # Replace output directory without asking
        
        # Add hidden imports for packages that might not be detected
        '--hidden-import=PyPDF2',
        '--hidden-import=reportlab',
        '--hidden-import=fitz',
        '--hidden-import=pdf2image',
        '--hidden-import=arabic_reshaper',
        '--hidden-import=bidi',
        
        # Main script
        'pdf_editor.py'
    ]
    
    # Add LICENSE file if it exists
    cmd[8:8] = add_data_args
    
    print(f"تنفيذ الأمر - Executing command: {' '.join(cmd)}\n")
    
    try:
        # Run PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        
        print("\n" + "=" * 60)
        print("✓ تم بناء ملف EXE بنجاح! - EXE built successfully!")
        print(f"✓ الملف موجود في: dist/PDFEditorPro.exe")
        print(f"✓ File location: dist/PDFEditorPro.exe")
        print("=" * 60)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 60)
        print("✗ فشل بناء ملف EXE - EXE build failed!")
        print("=" * 60)
        print(f"خطأ - Error: {e}")
        if e.stdout:
            print(f"\nOutput: {e.stdout}")
        if e.stderr:
            print(f"\nError output: {e.stderr}")
        return False
    
    except FileNotFoundError:
        print("\n" + "=" * 60)
        print("✗ PyInstaller غير مثبت - PyInstaller not installed!")
        print("=" * 60)
        print("الرجاء تثبيته أولاً باستخدام:")
        print("Please install it first using:")
        print("pip install pyinstaller")
        return False

def display_info():
    """Display build information"""
    print("\n" + "=" * 60)
    print("PDF Editor Pro - EXE Builder")
    print("محرر PDF الاحترافي - بناء ملف EXE")
    print("=" * 60)
    print("\nهذا السكريبت سيقوم بإنشاء ملف EXE مستقل للبرنامج")
    print("This script will create a standalone EXE file for the application")
    print("\nالمتطلبات - Requirements:")
    print("1. Python 3.8 or higher")
    print("2. All dependencies from requirements.txt installed")
    print("3. PyInstaller installed")
    print("\n" + "=" * 60 + "\n")

def main():
    """Main build process"""
    display_info()
    
    # Check if pdf_editor.py exists
    if not os.path.exists('pdf_editor.py'):
        print("✗ خطأ: ملف pdf_editor.py غير موجود!")
        print("✗ Error: pdf_editor.py not found!")
        print("الرجاء التأكد من وجود الملف في نفس المجلد")
        print("Please ensure the file exists in the same directory")
        sys.exit(1)
    
    # Ask user for confirmation
    response = input("هل تريد المتابعة؟ (y/n) - Do you want to continue? (y/n): ")
    if response.lower() not in ['y', 'yes', 'نعم', 'ن']:
        print("تم الإلغاء - Cancelled")
        sys.exit(0)
    
    # Clean previous builds
    clean_build_directories()
    
    # Build EXE
    success = build_exe()
    
    if success:
        print("\nملاحظات مهمة - Important Notes:")
        print("=" * 60)
        print("1. ملف EXE موجود في مجلد dist/")
        print("   The EXE file is in the dist/ folder")
        print("\n2. يمكنك نسخه وتوزيعه بشكل مستقل")
        print("   You can copy and distribute it independently")
        print("\n3. في حالة ظهور تحذيرات من Windows Defender:")
        print("   If Windows Defender shows warnings:")
        print("   - هذا طبيعي للبرامج الجديدة")
        print("   - This is normal for new programs")
        print("   - يمكنك إضافة استثناء أو السماح بالتشغيل")
        print("   - You can add an exception or allow it to run")
        print("=" * 60)
    else:
        print("\nفشل بناء ملف EXE. الرجاء التحقق من الأخطاء أعلاه")
        print("EXE build failed. Please check the errors above")
        sys.exit(1)

if __name__ == "__main__":
    main()
