"""
Analyze the CEEM brand guidelines PDF structure to understand the exact layout
"""
import pdfplumber
import sys

def analyze_pdf_structure(pdf_path):
    """Extract structure and content from PDF guidelines"""
    print(f"Analyzing PDF: {pdf_path}")
    print("=" * 80)
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Total Pages: {len(pdf.pages)}")
        print()
        
        for i, page in enumerate(pdf.pages):  # All pages
            print(f"\n--- PAGE {i+1} ---")
            
            # Extract text
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                # Print first few lines to understand structure
                for line in lines[:10]:
                    if line.strip():
                        try:
                            print(f"  {line.strip()}")
                        except UnicodeEncodeError:
                            print(f"  [UNICODE TEXT]")
            
            # Check for images
            images = page.images
            if images:
                print(f"  [IMAGES: {len(images)} found]")
            
            if i >= 25:  # First 25 pages to see full structure
                break

if __name__ == "__main__":
    pdf_path = r"c:\Users\NadaH\Downloads\brand_agent\CEEM GUIDELINES (2).pdf"
    try:
        analyze_pdf_structure(pdf_path)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
