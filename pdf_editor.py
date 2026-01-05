#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Editor Pro - محرر PDF الاحترافي
A comprehensive PDF editor with GUI support for Arabic language
برنامج شامل لتحرير ملفات PDF مع واجهة رسومية ودعم اللغة العربية
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from tkinter.scrolledtext import ScrolledText
import logging
from pathlib import Path
from typing import List, Optional, Tuple
import threading

# PDF processing libraries
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image, ImageTk
import fitz  # PyMuPDF
from pdf2image import convert_from_path

# Arabic text support
import arabic_reshaper
from bidi.algorithm import get_display

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pdf_editor.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class PDFEditor:
    """
    Main PDF Editor class with all PDF manipulation features
    الفئة الرئيسية لتحرير ملفات PDF مع جميع الميزات
    """
    
    def __init__(self, root):
        """Initialize the PDF Editor application"""
        self.root = root
        self.root.title("PDF Editor Pro - محرر PDF الاحترافي")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Configure style
        self.setup_styles()
        
        # Create main UI
        self.create_widgets()
        
        logger.info("PDF Editor Pro initialized successfully")
    
    def setup_styles(self):
        """Setup ttk styles for better appearance"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('TNotebook', background='#f0f0f0')
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10, 'bold'))
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground='#2c3e50')
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create all tabs
        self.create_add_text_tab()
        self.create_add_image_tab()
        self.create_merge_tab()
        self.create_split_tab()
        self.create_extract_tab()
        self.create_watermark_tab()
        self.create_convert_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("جاهز - Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    # ==================== Add Text Tab ====================
    def create_add_text_tab(self):
        """Create tab for adding text to PDF - تبويب إضافة نصوص"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="إضافة نص - Add Text")
        
        # Header
        header = ttk.Label(tab, text="إضافة نصوص إلى ملف PDF", style='Header.TLabel')
        header.pack(pady=10)
        
        # PDF file selection
        file_frame = ttk.LabelFrame(tab, text="اختيار الملف - File Selection", padding=10)
        file_frame.pack(fill='x', padx=20, pady=5)
        
        self.text_pdf_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.text_pdf_path, width=50).pack(side='left', padx=5)
        ttk.Button(file_frame, text="اختر PDF", command=self.browse_text_pdf).pack(side='left')
        
        # Text input
        text_frame = ttk.LabelFrame(tab, text="النص - Text Content", padding=10)
        text_frame.pack(fill='both', expand=True, padx=20, pady=5)
        
        self.text_content = ScrolledText(text_frame, height=5, width=50, font=('Arial', 11))
        self.text_content.pack(fill='both', expand=True)
        
        # Options
        options_frame = ttk.LabelFrame(tab, text="الخيارات - Options", padding=10)
        options_frame.pack(fill='x', padx=20, pady=5)
        
        # Page number
        page_frame = ttk.Frame(options_frame)
        page_frame.pack(fill='x', pady=2)
        ttk.Label(page_frame, text="رقم الصفحة - Page:").pack(side='left', padx=5)
        self.text_page_num = tk.IntVar(value=1)
        ttk.Spinbox(page_frame, from_=1, to=1000, textvariable=self.text_page_num, width=10).pack(side='left')
        
        # Position
        pos_frame = ttk.Frame(options_frame)
        pos_frame.pack(fill='x', pady=2)
        ttk.Label(pos_frame, text="الموضع - Position (X, Y):").pack(side='left', padx=5)
        self.text_x_pos = tk.IntVar(value=50)
        ttk.Spinbox(pos_frame, from_=0, to=1000, textvariable=self.text_x_pos, width=10).pack(side='left', padx=2)
        self.text_y_pos = tk.IntVar(value=50)
        ttk.Spinbox(pos_frame, from_=0, to=1000, textvariable=self.text_y_pos, width=10).pack(side='left', padx=2)
        
        # Font size
        font_frame = ttk.Frame(options_frame)
        font_frame.pack(fill='x', pady=2)
        ttk.Label(font_frame, text="حجم الخط - Font Size:").pack(side='left', padx=5)
        self.text_font_size = tk.IntVar(value=12)
        ttk.Spinbox(font_frame, from_=6, to=72, textvariable=self.text_font_size, width=10).pack(side='left')
        
        # Color
        color_frame = ttk.Frame(options_frame)
        color_frame.pack(fill='x', pady=2)
        ttk.Label(color_frame, text="اللون - Color:").pack(side='left', padx=5)
        self.text_color = tk.StringVar(value="#000000")
        ttk.Entry(color_frame, textvariable=self.text_color, width=15).pack(side='left', padx=5)
        ttk.Button(color_frame, text="اختر لون", command=self.choose_text_color).pack(side='left')
        
        # Execute button
        ttk.Button(tab, text="إضافة النص إلى PDF", command=self.add_text_to_pdf, 
                  style='TButton').pack(pady=10)
    
    def browse_text_pdf(self):
        """Browse for PDF file to add text"""
        filename = filedialog.askopenfilename(
            title="اختر ملف PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.text_pdf_path.set(filename)
    
    def choose_text_color(self):
        """Open color chooser dialog"""
        color = colorchooser.askcolor(title="اختر اللون")
        if color[1]:
            self.text_color.set(color[1])
    
    def add_text_to_pdf(self):
        """Add text to PDF file with Arabic support"""
        pdf_path = self.text_pdf_path.get()
        text = self.text_content.get("1.0", tk.END).strip()
        
        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار ملف PDF صحيح")
            return
        
        if not text:
            messagebox.showerror("خطأ - Error", "الرجاء إدخال النص المراد إضافته")
            return
        
        try:
            self.status_var.set("جاري إضافة النص... - Adding text...")
            self.root.update()
            
            # Process Arabic text
            reshaped_text = arabic_reshaper.reshape(text)
            bidi_text = get_display(reshaped_text)
            
            # Create output path
            output_path = pdf_path.replace('.pdf', '_with_text.pdf')
            
            # Open existing PDF
            doc = fitz.open(pdf_path)
            page_num = self.text_page_num.get() - 1
            
            if page_num >= len(doc):
                messagebox.showerror("خطأ - Error", f"رقم الصفحة غير صحيح. الملف يحتوي على {len(doc)} صفحة فقط")
                doc.close()
                return
            
            page = doc[page_num]
            
            # Parse color
            color_hex = self.text_color.get().lstrip('#')
            color_rgb = tuple(int(color_hex[i:i+2], 16) / 255 for i in (0, 2, 4))
            
            # Add text
            point = fitz.Point(self.text_x_pos.get(), self.text_y_pos.get())
            page.insert_text(
                point,
                bidi_text,
                fontsize=self.text_font_size.get(),
                color=color_rgb
            )
            
            # Save
            doc.save(output_path)
            doc.close()
            
            self.status_var.set("تم بنجاح - Success")
            messagebox.showinfo("نجح - Success", f"تم إضافة النص بنجاح!\nالملف المحفوظ: {output_path}")
            logger.info(f"Text added successfully to {output_path}")
            
        except Exception as e:
            self.status_var.set("فشل - Failed")
            messagebox.showerror("خطأ - Error", f"حدث خطأ: {str(e)}")
            logger.error(f"Error adding text: {str(e)}")
    
    # ==================== Add Image Tab ====================
    def create_add_image_tab(self):
        """Create tab for adding images to PDF - تبويب إضافة صور"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="إضافة صورة - Add Image")
        
        # Header
        header = ttk.Label(tab, text="إضافة صور إلى ملف PDF", style='Header.TLabel')
        header.pack(pady=10)
        
        # PDF file selection
        pdf_frame = ttk.LabelFrame(tab, text="ملف PDF - PDF File", padding=10)
        pdf_frame.pack(fill='x', padx=20, pady=5)
        
        self.image_pdf_path = tk.StringVar()
        ttk.Entry(pdf_frame, textvariable=self.image_pdf_path, width=50).pack(side='left', padx=5)
        ttk.Button(pdf_frame, text="اختر PDF", command=self.browse_image_pdf).pack(side='left')
        
        # Image file selection
        img_frame = ttk.LabelFrame(tab, text="ملف الصورة - Image File", padding=10)
        img_frame.pack(fill='x', padx=20, pady=5)
        
        self.image_path = tk.StringVar()
        ttk.Entry(img_frame, textvariable=self.image_path, width=50).pack(side='left', padx=5)
        ttk.Button(img_frame, text="اختر صورة", command=self.browse_image).pack(side='left')
        
        # Options
        options_frame = ttk.LabelFrame(tab, text="الخيارات - Options", padding=10)
        options_frame.pack(fill='x', padx=20, pady=5)
        
        # Page number
        page_frame = ttk.Frame(options_frame)
        page_frame.pack(fill='x', pady=2)
        ttk.Label(page_frame, text="رقم الصفحة - Page:").pack(side='left', padx=5)
        self.image_page_num = tk.IntVar(value=1)
        ttk.Spinbox(page_frame, from_=1, to=1000, textvariable=self.image_page_num, width=10).pack(side='left')
        
        # Position
        pos_frame = ttk.Frame(options_frame)
        pos_frame.pack(fill='x', pady=2)
        ttk.Label(pos_frame, text="الموضع - Position (X, Y):").pack(side='left', padx=5)
        self.image_x_pos = tk.IntVar(value=50)
        ttk.Spinbox(pos_frame, from_=0, to=1000, textvariable=self.image_x_pos, width=10).pack(side='left', padx=2)
        self.image_y_pos = tk.IntVar(value=50)
        ttk.Spinbox(pos_frame, from_=0, to=1000, textvariable=self.image_y_pos, width=10).pack(side='left', padx=2)
        
        # Size
        size_frame = ttk.Frame(options_frame)
        size_frame.pack(fill='x', pady=2)
        ttk.Label(size_frame, text="الحجم - Size (Width, Height):").pack(side='left', padx=5)
        self.image_width = tk.IntVar(value=100)
        ttk.Spinbox(size_frame, from_=10, to=1000, textvariable=self.image_width, width=10).pack(side='left', padx=2)
        self.image_height = tk.IntVar(value=100)
        ttk.Spinbox(size_frame, from_=10, to=1000, textvariable=self.image_height, width=10).pack(side='left', padx=2)
        
        # Execute button
        ttk.Button(tab, text="إضافة الصورة إلى PDF", command=self.add_image_to_pdf).pack(pady=10)
    
    def browse_image_pdf(self):
        """Browse for PDF file to add image"""
        filename = filedialog.askopenfilename(
            title="اختر ملف PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.image_pdf_path.set(filename)
    
    def browse_image(self):
        """Browse for image file"""
        filename = filedialog.askopenfilename(
            title="اختر صورة",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All files", "*.*")]
        )
        if filename:
            self.image_path.set(filename)
    
    def add_image_to_pdf(self):
        """Add image to PDF file"""
        pdf_path = self.image_pdf_path.get()
        image_path = self.image_path.get()
        
        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار ملف PDF صحيح")
            return
        
        if not image_path or not os.path.exists(image_path):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار ملف صورة صحيح")
            return
        
        try:
            self.status_var.set("جاري إضافة الصورة... - Adding image...")
            self.root.update()
            
            output_path = pdf_path.replace('.pdf', '_with_image.pdf')
            
            # Open PDF
            doc = fitz.open(pdf_path)
            page_num = self.image_page_num.get() - 1
            
            if page_num >= len(doc):
                messagebox.showerror("خطأ - Error", f"رقم الصفحة غير صحيح. الملف يحتوي على {len(doc)} صفحة فقط")
                doc.close()
                return
            
            page = doc[page_num]
            
            # Define rectangle for image
            rect = fitz.Rect(
                self.image_x_pos.get(),
                self.image_y_pos.get(),
                self.image_x_pos.get() + self.image_width.get(),
                self.image_y_pos.get() + self.image_height.get()
            )
            
            # Insert image
            page.insert_image(rect, filename=image_path)
            
            # Save
            doc.save(output_path)
            doc.close()
            
            self.status_var.set("تم بنجاح - Success")
            messagebox.showinfo("نجح - Success", f"تم إضافة الصورة بنجاح!\nالملف المحفوظ: {output_path}")
            logger.info(f"Image added successfully to {output_path}")
            
        except Exception as e:
            self.status_var.set("فشل - Failed")
            messagebox.showerror("خطأ - Error", f"حدث خطأ: {str(e)}")
            logger.error(f"Error adding image: {str(e)}")
    
    # ==================== Merge PDF Tab ====================
    def create_merge_tab(self):
        """Create tab for merging PDFs - تبويب دمج الملفات"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="دمج ملفات - Merge PDFs")
        
        # Header
        header = ttk.Label(tab, text="دمج ملفات PDF متعددة", style='Header.TLabel')
        header.pack(pady=10)
        
        # Files listbox
        files_frame = ttk.LabelFrame(tab, text="الملفات المحددة - Selected Files", padding=10)
        files_frame.pack(fill='both', expand=True, padx=20, pady=5)
        
        # Listbox with scrollbar
        list_frame = ttk.Frame(files_frame)
        list_frame.pack(fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.merge_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=10)
        self.merge_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.merge_listbox.yview)
        
        self.merge_files = []
        
        # Buttons
        btn_frame = ttk.Frame(files_frame)
        btn_frame.pack(fill='x', pady=5)
        
        ttk.Button(btn_frame, text="إضافة ملفات", command=self.add_merge_files).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="إزالة المحدد", command=self.remove_merge_file).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="مسح الكل", command=self.clear_merge_files).pack(side='left', padx=5)
        
        # Execute button
        ttk.Button(tab, text="دمج الملفات", command=self.merge_pdfs).pack(pady=10)
    
    def add_merge_files(self):
        """Add files to merge list"""
        filenames = filedialog.askopenfilenames(
            title="اختر ملفات PDF للدمج",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        for filename in filenames:
            if filename not in self.merge_files:
                self.merge_files.append(filename)
                self.merge_listbox.insert(tk.END, os.path.basename(filename))
    
    def remove_merge_file(self):
        """Remove selected file from merge list"""
        selection = self.merge_listbox.curselection()
        if selection:
            index = selection[0]
            self.merge_listbox.delete(index)
            self.merge_files.pop(index)
    
    def clear_merge_files(self):
        """Clear all files from merge list"""
        self.merge_listbox.delete(0, tk.END)
        self.merge_files.clear()
    
    def merge_pdfs(self):
        """Merge multiple PDF files"""
        if len(self.merge_files) < 2:
            messagebox.showerror("خطأ - Error", "الرجاء اختيار ملفين على الأقل للدمج")
            return
        
        # Ask for output file
        output_path = filedialog.asksaveasfilename(
            title="حفظ الملف المدموج",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if not output_path:
            return
        
        try:
            self.status_var.set("جاري دمج الملفات... - Merging PDFs...")
            self.root.update()
            
            merger = PyPDF2.PdfMerger()
            
            for pdf_file in self.merge_files:
                merger.append(pdf_file)
            
            merger.write(output_path)
            merger.close()
            
            self.status_var.set("تم بنجاح - Success")
            messagebox.showinfo("نجح - Success", f"تم دمج الملفات بنجاح!\nالملف المحفوظ: {output_path}")
            logger.info(f"PDFs merged successfully: {output_path}")
            
        except Exception as e:
            self.status_var.set("فشل - Failed")
            messagebox.showerror("خطأ - Error", f"حدث خطأ: {str(e)}")
            logger.error(f"Error merging PDFs: {str(e)}")
    
    # ==================== Split PDF Tab ====================
    def create_split_tab(self):
        """Create tab for splitting PDF - تبويب تقسيم الملفات"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="تقسيم ملف - Split PDF")
        
        # Header
        header = ttk.Label(tab, text="تقسيم ملف PDF إلى ملفات منفصلة", style='Header.TLabel')
        header.pack(pady=10)
        
        # File selection
        file_frame = ttk.LabelFrame(tab, text="اختيار الملف - File Selection", padding=10)
        file_frame.pack(fill='x', padx=20, pady=5)
        
        self.split_pdf_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.split_pdf_path, width=50).pack(side='left', padx=5)
        ttk.Button(file_frame, text="اختر PDF", command=self.browse_split_pdf).pack(side='left')
        
        # Split options
        options_frame = ttk.LabelFrame(tab, text="خيارات التقسيم - Split Options", padding=10)
        options_frame.pack(fill='x', padx=20, pady=5)
        
        self.split_mode = tk.StringVar(value="all")
        
        ttk.Radiobutton(options_frame, text="تقسيم كل صفحة في ملف منفصل - Split each page", 
                       variable=self.split_mode, value="all").pack(anchor='w', pady=2)
        
        range_frame = ttk.Frame(options_frame)
        range_frame.pack(fill='x', pady=2)
        ttk.Radiobutton(range_frame, text="تقسيم حسب النطاق - Split by range:", 
                       variable=self.split_mode, value="range").pack(side='left')
        
        ttk.Label(range_frame, text="من - From:").pack(side='left', padx=5)
        self.split_from = tk.IntVar(value=1)
        ttk.Spinbox(range_frame, from_=1, to=1000, textvariable=self.split_from, width=10).pack(side='left', padx=2)
        
        ttk.Label(range_frame, text="إلى - To:").pack(side='left', padx=5)
        self.split_to = tk.IntVar(value=1)
        ttk.Spinbox(range_frame, from_=1, to=1000, textvariable=self.split_to, width=10).pack(side='left', padx=2)
        
        # Output directory
        output_frame = ttk.LabelFrame(tab, text="مجلد الحفظ - Output Directory", padding=10)
        output_frame.pack(fill='x', padx=20, pady=5)
        
        self.split_output_dir = tk.StringVar()
        ttk.Entry(output_frame, textvariable=self.split_output_dir, width=50).pack(side='left', padx=5)
        ttk.Button(output_frame, text="اختر مجلد", command=self.browse_split_output).pack(side='left')
        
        # Execute button
        ttk.Button(tab, text="تقسيم الملف", command=self.split_pdf).pack(pady=10)
    
    def browse_split_pdf(self):
        """Browse for PDF file to split"""
        filename = filedialog.askopenfilename(
            title="اختر ملف PDF للتقسيم",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.split_pdf_path.set(filename)
    
    def browse_split_output(self):
        """Browse for output directory"""
        directory = filedialog.askdirectory(title="اختر مجلد الحفظ")
        if directory:
            self.split_output_dir.set(directory)
    
    def split_pdf(self):
        """Split PDF file"""
        pdf_path = self.split_pdf_path.get()
        output_dir = self.split_output_dir.get()
        
        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار ملف PDF صحيح")
            return
        
        if not output_dir or not os.path.exists(output_dir):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار مجلد الحفظ")
            return
        
        try:
            self.status_var.set("جاري تقسيم الملف... - Splitting PDF...")
            self.root.update()
            
            pdf_reader = PyPDF2.PdfReader(pdf_path)
            total_pages = len(pdf_reader.pages)
            
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            
            if self.split_mode.get() == "all":
                # Split each page
                for page_num in range(total_pages):
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[page_num])
                    
                    output_file = os.path.join(output_dir, f"{base_name}_page_{page_num + 1}.pdf")
                    with open(output_file, 'wb') as output_pdf:
                        pdf_writer.write(output_pdf)
                
                message = f"تم تقسيم الملف إلى {total_pages} ملف منفصل"
            else:
                # Split by range
                from_page = self.split_from.get() - 1
                to_page = self.split_to.get()
                
                if from_page < 0 or to_page > total_pages or from_page >= to_page:
                    messagebox.showerror("خطأ - Error", "نطاق الصفحات غير صحيح")
                    return
                
                pdf_writer = PyPDF2.PdfWriter()
                for page_num in range(from_page, to_page):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
                
                output_file = os.path.join(output_dir, f"{base_name}_pages_{from_page + 1}_to_{to_page}.pdf")
                with open(output_file, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
                
                message = f"تم استخراج الصفحات من {from_page + 1} إلى {to_page}"
            
            self.status_var.set("تم بنجاح - Success")
            messagebox.showinfo("نجح - Success", message)
            logger.info(f"PDF split successfully: {output_dir}")
            
        except Exception as e:
            self.status_var.set("فشل - Failed")
            messagebox.showerror("خطأ - Error", f"حدث خطأ: {str(e)}")
            logger.error(f"Error splitting PDF: {str(e)}")
    
    # ==================== Extract Pages Tab ====================
    def create_extract_tab(self):
        """Create tab for extracting pages - تبويب استخراج الصفحات"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="استخراج صفحات - Extract Pages")
        
        # Header
        header = ttk.Label(tab, text="استخراج صفحات معينة من PDF", style='Header.TLabel')
        header.pack(pady=10)
        
        # File selection
        file_frame = ttk.LabelFrame(tab, text="اختيار الملف - File Selection", padding=10)
        file_frame.pack(fill='x', padx=20, pady=5)
        
        self.extract_pdf_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.extract_pdf_path, width=50).pack(side='left', padx=5)
        ttk.Button(file_frame, text="اختر PDF", command=self.browse_extract_pdf).pack(side='left')
        
        # Page range input
        range_frame = ttk.LabelFrame(tab, text="نطاق الصفحات - Page Range", padding=10)
        range_frame.pack(fill='x', padx=20, pady=5)
        
        info_label = ttk.Label(range_frame, 
                              text="أدخل أرقام الصفحات (مثال: 1-5, 7, 9-12)\nEnter page numbers (e.g., 1-5, 7, 9-12)")
        info_label.pack(pady=5)
        
        self.extract_pages_entry = tk.StringVar()
        ttk.Entry(range_frame, textvariable=self.extract_pages_entry, width=40).pack(pady=5)
        
        # Execute button
        ttk.Button(tab, text="استخراج الصفحات", command=self.extract_pages).pack(pady=10)
    
    def browse_extract_pdf(self):
        """Browse for PDF file to extract pages"""
        filename = filedialog.askopenfilename(
            title="اختر ملف PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.extract_pdf_path.set(filename)
    
    def parse_page_range(self, range_str: str) -> List[int]:
        """Parse page range string like '1-5, 7, 9-12' into list of page numbers"""
        pages = []
        parts = range_str.replace(' ', '').split(',')
        
        for part in parts:
            if '-' in part:
                start, end = part.split('-')
                pages.extend(range(int(start), int(end) + 1))
            else:
                pages.append(int(part))
        
        return sorted(set(pages))  # Remove duplicates and sort
    
    def extract_pages(self):
        """Extract specific pages from PDF"""
        pdf_path = self.extract_pdf_path.get()
        pages_str = self.extract_pages_entry.get()
        
        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار ملف PDF صحيح")
            return
        
        if not pages_str:
            messagebox.showerror("خطأ - Error", "الرجاء إدخال أرقام الصفحات")
            return
        
        try:
            # Parse page range
            pages_to_extract = self.parse_page_range(pages_str)
            
            if not pages_to_extract:
                messagebox.showerror("خطأ - Error", "صيغة أرقام الصفحات غير صحيحة")
                return
            
            self.status_var.set("جاري استخراج الصفحات... - Extracting pages...")
            self.root.update()
            
            pdf_reader = PyPDF2.PdfReader(pdf_path)
            total_pages = len(pdf_reader.pages)
            
            # Validate page numbers
            for page_num in pages_to_extract:
                if page_num < 1 or page_num > total_pages:
                    messagebox.showerror("خطأ - Error", 
                                       f"رقم الصفحة {page_num} غير صحيح. الملف يحتوي على {total_pages} صفحة فقط")
                    return
            
            # Ask for output file
            output_path = filedialog.asksaveasfilename(
                title="حفظ الصفحات المستخرجة",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
            )
            
            if not output_path:
                return
            
            # Extract pages
            pdf_writer = PyPDF2.PdfWriter()
            for page_num in pages_to_extract:
                pdf_writer.add_page(pdf_reader.pages[page_num - 1])  # Convert to 0-based index
            
            with open(output_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            
            self.status_var.set("تم بنجاح - Success")
            messagebox.showinfo("نجح - Success", 
                              f"تم استخراج {len(pages_to_extract)} صفحة بنجاح!\nالملف المحفوظ: {output_path}")
            logger.info(f"Pages extracted successfully: {output_path}")
            
        except ValueError as e:
            self.status_var.set("فشل - Failed")
            messagebox.showerror("خطأ - Error", "صيغة أرقام الصفحات غير صحيحة")
            logger.error(f"Invalid page range format: {str(e)}")
        except Exception as e:
            self.status_var.set("فشل - Failed")
            messagebox.showerror("خطأ - Error", f"حدث خطأ: {str(e)}")
            logger.error(f"Error extracting pages: {str(e)}")
    
    # ==================== Watermark Tab ====================
    def create_watermark_tab(self):
        """Create tab for adding watermark - تبويب العلامة المائية"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="علامة مائية - Watermark")
        
        # Header
        header = ttk.Label(tab, text="إضافة علامة مائية إلى PDF", style='Header.TLabel')
        header.pack(pady=10)
        
        # File selection
        file_frame = ttk.LabelFrame(tab, text="اختيار الملف - File Selection", padding=10)
        file_frame.pack(fill='x', padx=20, pady=5)
        
        self.watermark_pdf_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.watermark_pdf_path, width=50).pack(side='left', padx=5)
        ttk.Button(file_frame, text="اختر PDF", command=self.browse_watermark_pdf).pack(side='left')
        
        # Watermark type
        type_frame = ttk.LabelFrame(tab, text="نوع العلامة المائية - Watermark Type", padding=10)
        type_frame.pack(fill='x', padx=20, pady=5)
        
        self.watermark_type = tk.StringVar(value="text")
        
        ttk.Radiobutton(type_frame, text="نص - Text", 
                       variable=self.watermark_type, value="text",
                       command=self.toggle_watermark_options).pack(anchor='w', pady=2)
        ttk.Radiobutton(type_frame, text="صورة - Image", 
                       variable=self.watermark_type, value="image",
                       command=self.toggle_watermark_options).pack(anchor='w', pady=2)
        
        # Text watermark options
        self.text_watermark_frame = ttk.LabelFrame(tab, text="خيارات النص - Text Options", padding=10)
        self.text_watermark_frame.pack(fill='x', padx=20, pady=5)
        
        ttk.Label(self.text_watermark_frame, text="النص - Text:").pack(anchor='w', pady=2)
        self.watermark_text = tk.StringVar(value="WATERMARK")
        ttk.Entry(self.text_watermark_frame, textvariable=self.watermark_text, width=40).pack(fill='x', pady=2)
        
        # Image watermark options
        self.image_watermark_frame = ttk.LabelFrame(tab, text="خيارات الصورة - Image Options", padding=10)
        
        img_select_frame = ttk.Frame(self.image_watermark_frame)
        img_select_frame.pack(fill='x', pady=2)
        
        self.watermark_image_path = tk.StringVar()
        ttk.Entry(img_select_frame, textvariable=self.watermark_image_path, width=40).pack(side='left', padx=5)
        ttk.Button(img_select_frame, text="اختر صورة", command=self.browse_watermark_image).pack(side='left')
        
        # Common options
        common_frame = ttk.LabelFrame(tab, text="خيارات عامة - Common Options", padding=10)
        common_frame.pack(fill='x', padx=20, pady=5)
        
        # Opacity
        opacity_frame = ttk.Frame(common_frame)
        opacity_frame.pack(fill='x', pady=2)
        ttk.Label(opacity_frame, text="الشفافية - Opacity (0-1):").pack(side='left', padx=5)
        self.watermark_opacity = tk.DoubleVar(value=0.3)
        ttk.Spinbox(opacity_frame, from_=0.0, to=1.0, increment=0.1, 
                   textvariable=self.watermark_opacity, width=10).pack(side='left')
        
        # Execute button
        ttk.Button(tab, text="إضافة العلامة المائية", command=self.add_watermark).pack(pady=10)
    
    def browse_watermark_pdf(self):
        """Browse for PDF file to add watermark"""
        filename = filedialog.askopenfilename(
            title="اختر ملف PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.watermark_pdf_path.set(filename)
    
    def browse_watermark_image(self):
        """Browse for watermark image"""
        filename = filedialog.askopenfilename(
            title="اختر صورة العلامة المائية",
            filetypes=[("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")]
        )
        if filename:
            self.watermark_image_path.set(filename)
    
    def toggle_watermark_options(self):
        """Toggle between text and image watermark options"""
        if self.watermark_type.get() == "text":
            self.text_watermark_frame.pack(fill='x', padx=20, pady=5)
            self.image_watermark_frame.pack_forget()
        else:
            self.text_watermark_frame.pack_forget()
            self.image_watermark_frame.pack(fill='x', padx=20, pady=5)
    
    def add_watermark(self):
        """Add watermark to PDF"""
        pdf_path = self.watermark_pdf_path.get()
        
        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار ملف PDF صحيح")
            return
        
        try:
            self.status_var.set("جاري إضافة العلامة المائية... - Adding watermark...")
            self.root.update()
            
            output_path = pdf_path.replace('.pdf', '_watermarked.pdf')
            doc = fitz.open(pdf_path)
            
            opacity = self.watermark_opacity.get()
            
            if self.watermark_type.get() == "text":
                # Text watermark
                text = self.watermark_text.get()
                if not text:
                    messagebox.showerror("خطأ - Error", "الرجاء إدخال نص العلامة المائية")
                    return
                
                # Process Arabic text
                reshaped_text = arabic_reshaper.reshape(text)
                bidi_text = get_display(reshaped_text)
                
                for page in doc:
                    # Get page dimensions
                    rect = page.rect
                    
                    # Add watermark at center
                    point = fitz.Point(rect.width / 2, rect.height / 2)
                    
                    # Insert text with rotation
                    page.insert_text(
                        point,
                        bidi_text,
                        fontsize=60,
                        color=(0.7, 0.7, 0.7),
                        rotate=45,
                        opacity=opacity
                    )
            else:
                # Image watermark
                image_path = self.watermark_image_path.get()
                if not image_path or not os.path.exists(image_path):
                    messagebox.showerror("خطأ - Error", "الرجاء اختيار صورة العلامة المائية")
                    return
                
                for page in doc:
                    # Get page dimensions
                    rect = page.rect
                    
                    # Calculate watermark size (30% of page)
                    wm_width = rect.width * 0.3
                    wm_height = rect.height * 0.3
                    
                    # Center position
                    x = (rect.width - wm_width) / 2
                    y = (rect.height - wm_height) / 2
                    
                    wm_rect = fitz.Rect(x, y, x + wm_width, y + wm_height)
                    
                    page.insert_image(wm_rect, filename=image_path, opacity=opacity)
            
            doc.save(output_path)
            doc.close()
            
            self.status_var.set("تم بنجاح - Success")
            messagebox.showinfo("نجح - Success", f"تم إضافة العلامة المائية بنجاح!\nالملف المحفوظ: {output_path}")
            logger.info(f"Watermark added successfully: {output_path}")
            
        except Exception as e:
            self.status_var.set("فشل - Failed")
            messagebox.showerror("خطأ - Error", f"حدث خطأ: {str(e)}")
            logger.error(f"Error adding watermark: {str(e)}")
    
    # ==================== Convert to Images Tab ====================
    def create_convert_tab(self):
        """Create tab for converting PDF to images - تبويب التحويل لصور"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="تحويل لصور - Convert to Images")
        
        # Header
        header = ttk.Label(tab, text="تحويل صفحات PDF إلى صور", style='Header.TLabel')
        header.pack(pady=10)
        
        # File selection
        file_frame = ttk.LabelFrame(tab, text="اختيار الملف - File Selection", padding=10)
        file_frame.pack(fill='x', padx=20, pady=5)
        
        self.convert_pdf_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.convert_pdf_path, width=50).pack(side='left', padx=5)
        ttk.Button(file_frame, text="اختر PDF", command=self.browse_convert_pdf).pack(side='left')
        
        # Options
        options_frame = ttk.LabelFrame(tab, text="خيارات التحويل - Conversion Options", padding=10)
        options_frame.pack(fill='x', padx=20, pady=5)
        
        # Image format
        format_frame = ttk.Frame(options_frame)
        format_frame.pack(fill='x', pady=2)
        ttk.Label(format_frame, text="صيغة الصورة - Image Format:").pack(side='left', padx=5)
        self.convert_format = tk.StringVar(value="PNG")
        ttk.Combobox(format_frame, textvariable=self.convert_format, 
                    values=["PNG", "JPG", "JPEG"], width=15, state='readonly').pack(side='left')
        
        # DPI (quality)
        dpi_frame = ttk.Frame(options_frame)
        dpi_frame.pack(fill='x', pady=2)
        ttk.Label(dpi_frame, text="الدقة - DPI (Quality):").pack(side='left', padx=5)
        self.convert_dpi = tk.IntVar(value=200)
        ttk.Spinbox(dpi_frame, from_=72, to=600, textvariable=self.convert_dpi, width=10).pack(side='left')
        
        # Output directory
        output_frame = ttk.LabelFrame(tab, text="مجلد الحفظ - Output Directory", padding=10)
        output_frame.pack(fill='x', padx=20, pady=5)
        
        self.convert_output_dir = tk.StringVar()
        ttk.Entry(output_frame, textvariable=self.convert_output_dir, width=50).pack(side='left', padx=5)
        ttk.Button(output_frame, text="اختر مجلد", command=self.browse_convert_output).pack(side='left')
        
        # Execute button
        ttk.Button(tab, text="تحويل إلى صور", command=self.convert_to_images).pack(pady=10)
    
    def browse_convert_pdf(self):
        """Browse for PDF file to convert"""
        filename = filedialog.askopenfilename(
            title="اختر ملف PDF للتحويل",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.convert_pdf_path.set(filename)
    
    def browse_convert_output(self):
        """Browse for output directory"""
        directory = filedialog.askdirectory(title="اختر مجلد الحفظ")
        if directory:
            self.convert_output_dir.set(directory)
    
    def convert_to_images(self):
        """Convert PDF pages to images"""
        pdf_path = self.convert_pdf_path.get()
        output_dir = self.convert_output_dir.get()
        
        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار ملف PDF صحيح")
            return
        
        if not output_dir or not os.path.exists(output_dir):
            messagebox.showerror("خطأ - Error", "الرجاء اختيار مجلد الحفظ")
            return
        
        try:
            self.status_var.set("جاري تحويل الصفحات... - Converting pages...")
            self.root.update()
            
            # Convert PDF to images
            dpi = self.convert_dpi.get()
            images = convert_from_path(pdf_path, dpi=dpi)
            
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            img_format = self.convert_format.get().lower()
            
            for i, image in enumerate(images, start=1):
                output_file = os.path.join(output_dir, f"{base_name}_page_{i}.{img_format}")
                image.save(output_file, img_format.upper())
            
            self.status_var.set("تم بنجاح - Success")
            messagebox.showinfo("نجح - Success", 
                              f"تم تحويل {len(images)} صفحة إلى صور بنجاح!\nالمجلد: {output_dir}")
            logger.info(f"PDF converted to images successfully: {output_dir}")
            
        except Exception as e:
            self.status_var.set("فشل - Failed")
            messagebox.showerror("خطأ - Error", f"حدث خطأ: {str(e)}")
            logger.error(f"Error converting PDF to images: {str(e)}")


def main():
    """Main entry point for the application"""
    try:
        root = tk.Tk()
        app = PDFEditor(root)
        root.mainloop()
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        messagebox.showerror("خطأ فادح - Critical Error", f"فشل تشغيل البرنامج: {str(e)}")


if __name__ == "__main__":
    main()
