import markdown
from xhtml2pdf import pisa
import re
import base64

def md_to_pdf(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Function to replace mermaid blocks with images
    def replace_mermaid(match):
        code = match.group(1).strip()
        # Encode to base64 for mermaid.ink
        code_bytes = code.encode('ascii')
        base64_bytes = base64.b64encode(code_bytes)
        base64_string = base64_bytes.decode('ascii')
        # Request higher quality PNG with white background and scaling
        url = f"https://mermaid.ink/img/{base64_string}?type=png&bgColor=white&scale=2"
        return f'<div class="mermaid-container"><img src="{url}" alt="ER Diagram" /></div>'

    # Regex to find mermaid blocks
    pattern = r'```mermaid(.*?)```'
    text = re.sub(pattern, replace_mermaid, text, flags=re.DOTALL)

    # Convert to HTML
    # Note: explicit extensions for tables are crucial
    html = markdown.markdown(text, extensions=['tables', 'fenced_code'])
    
    # Add robust styling for xhtml2pdf
    full_html = f"""
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}
        body {{ 
            font-family: Helvetica, sans-serif; 
            font-size: 11pt; 
            line-height: 1.5;
        }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #34495e; padding-bottom: 5px; }}
        h2 {{ color: #2980b9; margin-top: 20px; border-bottom: 1px solid #eee; }}
        h3 {{ color: #16a085; margin-top: 15px; }}
        
        /* Table Styling */
        table {{ 
            width: 100%; 
            border: 1px solid #000000; 
            border-collapse: collapse; 
            margin-bottom: 20px; 
        }}
        th, td {{ 
            border: 1px solid #000000; 
            padding: 8px; 
            text-align: left; 
            vertical-align: top;
        }}
        th {{ 
            background-color: #f2f2f2; 
            font-weight: bold; 
        }}
        
        /* Code styling */
        code {{ 
            background-color: #f8f8f8; 
            padding: 2px 4px;
            font-family: monospace; 
            color: #d35400;
        }}
        pre {{
            background-color: #f8f8f8;
            padding: 10px;
            border: 1px solid #ddd;
            white-space: pre-wrap;
        }}
        
        /* Images */
        .mermaid-container {{
            text-align: center;
            margin: 20px 0;
            padding: 10px;
            border: 1px solid #eee;
        }}
        img {{ width: 100%; height: auto; }}
    </style>
    </head>
    <body>
    {html}
    </body>
    </html>
    """

    # Write PDF
    with open(output_file, "wb") as result_file:
        pisa_status = pisa.CreatePDF(
            full_html,                # the HTML to convert
            dest=result_file          # file handle to receive result
        )

    if pisa_status.err:
        print(f"Error converting to PDF: {pisa_status.err}")
    else:
        print(f"Successfully created {output_file}")

if __name__ == "__main__":
    md_to_pdf('solution_q1_q2_partB.md', 'solution.pdf')
