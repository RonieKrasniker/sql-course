import re
import sys
import os

def generate_tex(input_file, output_tex, image_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tex_content = []
    
    # Preamble
    tex_content.append(r"""\documentclass{article}
\usepackage{fontspec}
\usepackage{xunicode}
\usepackage{xltxtra}
\usepackage[margin=2cm]{geometry}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{hyperref}
\usepackage{float}

\setmainfont{Arial} 
\setsansfont{Arial}
\setmonofont{Courier New}

\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegray},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codeturquoise},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}
\lstset{style=mystyle}

\title{Database Systems Assignment \#3}
\author{Student ID: 318828175}
\date{}

\begin{document}
\maketitle
""")

    in_mermaid = False
    in_table = False
    table_lines = []
    
    def process_inline(text):
        text = text.replace("&", r"\&").replace("%", r"\%").replace("$", r"\$").replace("#", r"\#").replace("_", r"\_")
        text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
        text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
        return text

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # 1. Handle Mermaid Code Block
        if line.strip().startswith('```mermaid'):
            in_mermaid = True
            tex_content.append(r"\section*{ER Diagram (Mermaid Code)}")
            tex_content.append(r"\begin{lstlisting}[language=java]") 
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                tex_content.append(lines[i].rstrip())
                i += 1
            
            # Finished mermaid block
            tex_content.append(r"\end{lstlisting}")
            
            # Embed Image (Assumes erd.png exists locally)
            if os.path.exists(image_file):
                tex_content.append(r"\section*{ER Diagram (Visualization)}")
                tex_content.append(r"\begin{figure}[H]")
                tex_content.append(r"\centering")
                tex_content.append(f"\\includegraphics[width=0.95\\textwidth]{{{image_file}}}")
                tex_content.append(r"\caption{Visualized ER Diagram}")
                tex_content.append(r"\end{figure}")
            else:
                tex_content.append(r"\textbf{Error: erd.png not found. Please run npm mermaid-cli.}")
            
            # Skip the closing backticks line if we haven't consumed it
            if i < len(lines) and lines[i].strip().startswith('```'):
                 i += 1
            continue

        # 2. Handle Tables (Basic)
        if "|" in line and not in_table:
            if i + 1 < len(lines) and re.match(r'^\s*\|?[:\s-]+\|', lines[i+1]):
                in_table = True
                table_lines = []
        
        if in_table:
            if not line.strip() or not "|" in line:
                in_table = False
                if table_lines:
                    header_line = table_lines[0]
                    if header_line.startswith('|'): header_line = header_line[1:]
                    if header_line.endswith('|'): header_line = header_line[:-1]
                    headers = [h.strip() for h in header_line.split('|')]
                    col_count = len(headers)
                    
                    tex_content.append(r"\begin{center}")
                    tex_content.append(r"\begin{longtable}{" + "|" + "l|" * col_count + "}")
                    tex_content.append(r"\hline")
                    tex_content.append(" & ".join([r"\textbf{" + h + "}" for h in headers]) + r" \\ \hline")
                    tex_content.append(r"\endhead")
                    
                    for row in table_lines[2:]:
                        r_line = row.strip()
                        if r_line.startswith('|'): r_line = r_line[1:]
                        if r_line.endswith('|'): r_line = r_line[:-1]
                        cols = r_line.split('|')
                        
                        cols = [process_inline(c.strip()) for c in cols]
                        if len(cols) == col_count:
                             tex_content.append(" & ".join(cols) + r" \\ \hline")
                    
                    tex_content.append(r"\end{longtable}")
                    tex_content.append(r"\end{center}") 
                table_lines = []
            else:
                table_lines.append(line)
                i += 1
                continue
        
        # 3. Headers
        if line.startswith('# '):
             tex_content.append(r"\section{" + process_inline(line[2:]) + "}")
        elif line.startswith('## '):
             tex_content.append(r"\subsection{" + process_inline(line[3:]) + "}")
        elif line.startswith('### '):
             tex_content.append(r"\subsubsection{" + process_inline(line[4:]) + "}")
        
        # 4. Lists
        elif line.strip().startswith('* ') or line.strip().startswith('- '):
            tex_content.append(r"\begin{itemize}")
            tex_content.append(r"\item " + process_inline(line.strip()[2:]))
            tex_content.append(r"\end{itemize}")
        
        # 5. Normal text
        else:
            if line.strip():
                tex_content.append(process_inline(line) + r"\\")
            else:
                tex_content.append(r"\vspace{0.2cm}") 
        i += 1
        
    tex_content.append(r"\end{document}")
    
    with open(output_tex, 'w', encoding='utf-8') as f:
        f.write("\n".join(tex_content))
    print(f"Generated {output_tex}")

if __name__ == "__main__":
    generate_tex('solution_q1_q2_partB.md', 'solution.tex', 'erd.png')
