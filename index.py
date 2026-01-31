from flask import Flask, request, send_file, render_template, abort
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import json
import io
import os

app = Flask(__name__)

# Route to Landing Page (Now Visual Redactor)
@app.route('/')
def home():
    return render_template('visual.html')

@app.route('/redact-visual', methods=['POST'])
def redact_visual():
    if 'pdf_file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['pdf_file']
    redactions_json = request.form.get('redactions')
    
    if not file or not redactions_json:
        return "Missing file or redaction data", 400

    try:
        redactions = json.loads(redactions_json) # { "1": [{x,y,w,h}], "2": ... }
        
        input_pdf = PyPDF2.PdfReader(file.stream)
        output_pdf = PyPDF2.PdfWriter()

        for i, page in enumerate(input_pdf.pages):
            # Page number in JSON is 1-based (from frontend logic usually, but let's check frontend code.
            # Frontend code: redactions[pageNum] where pageNum starts at 1.
            # Python enumerate starts at 0.
            page_num_str = str(i + 1)
            
            if page_num_str in redactions:
                packet = io.BytesIO()
                width = float(page.mediabox.width)
                height = float(page.mediabox.height)
                
                can = canvas.Canvas(packet, pagesize=(width, height))
                can.setFillColorRGB(0, 0, 0) # Black
                
                rects = redactions[page_num_str]
                for r in rects:
                    # r has x, y, w, h in 0-1 range
                    # Canvas origin is top-left. PDF origin is bottom-left.
                    # x is same.
                    # y in PDF = height - (y_in_canvas * height) - (h_in_canvas * height)
                    
                    # Frontend x,y is top-left of rect.
                    rect_width = r['w'] * width
                    rect_height = r['h'] * height
                    rect_x = r['x'] * width
                    
                    # Top-Left Y in PDF coord system = height - (r['y'] * height)
                    # Bottom-Left Y (which rect needs) = Top-Left Y - rect_height
                    
                    rect_y = height - (r['y'] * height) - rect_height
                    
                    can.rect(rect_x, rect_y, rect_width, rect_height, fill=1)
                
                can.save()
                packet.seek(0)
                overlay = PyPDF2.PdfReader(packet)
                page.merge_page(overlay.pages[0])
            
            output_pdf.add_page(page)

        output_buffer = io.BytesIO()
        output_pdf.write(output_buffer)
        output_buffer.seek(0)

        return send_file(
            output_buffer,
            as_attachment=True,
            download_name='redacted_visual.pdf',
            mimetype='application/pdf'
        )

    except Exception as e:
        return f"Error processing visual redaction: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
