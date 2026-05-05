import sys
from pdf2image import convert_from_path
import Quartz
import Vision
from Cocoa import NSURL

def extract_text_from_pdf(pdf_path, output_txt_path):
    print(f"Converting {pdf_path} to images...")
    try:
        images = convert_from_path(pdf_path)
    except Exception as e:
        print(f"Could not read PDF {pdf_path}: {e}")
        return

    full_text = []
    
    for i, img in enumerate(images):
        print(f"Processing page {i+1}...")
        img_path = f"temp_page_{i}.jpg"
        img.save(img_path, "JPEG")
        
        # Use Vision Framework for OCR
        url = NSURL.fileURLWithPath_(img_path)
        request_handler = Vision.VNImageRequestHandler.alloc().initWithURL_options_(url, None)
        request = Vision.VNRecognizeTextRequest.alloc().init()
        
        # We can set language to French if needed
        request.setRecognitionLanguages_(["fr-FR", "en-US"])
        
        success, error = request_handler.performRequests_error_([request], None)
        if success:
            for observation in request.results():
                candidate = observation.topCandidates_(1).firstObject()
                if candidate:
                    full_text.append(candidate.string())
        else:
            print(f"OCR Error on page {i+1}: {error}")
            
    with open(output_txt_path, "w") as f:
        f.write("\n".join(full_text))
    print(f"Saved extracted text to {output_txt_path}")

files = [
    "Cours 2/2-regle_de_barre-RECTO.pdf",
    "Cours 2/2-regle_de_barre-VERSO.pdf",
    "Cours 2/3-Les_signaux-RECTO.pdf",
    "Cours 2/3-Les signaux-VERSO.pdf"
]

for pdf in files:
    out_name = pdf.split('/')[-1].replace('.pdf', '.txt')
    extract_text_from_pdf(pdf, out_name)
