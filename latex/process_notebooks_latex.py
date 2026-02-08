"""Process the notebooks after export as LaTeX for compilation in one document."""

import zipfile
from pathlib import Path

# Get the directory where the script is located
ZIP_DIR = Path(__file__).parent.resolve()

for zip_file in ZIP_DIR.glob("*.zip"):
    print(f"Processing: {zip_file.name}")

    # Unzip
    extract_dir = ZIP_DIR / zip_file.stem
    extract_dir.mkdir(exist_ok=True)
    with zipfile.ZipFile(zip_file, 'r') as z:
        z.extractall(extract_dir)

    # Open the .tex file
    tex_file = zip_file.stem + ".tex"
    tex_path = extract_dir / tex_file
    with tex_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    # Remove preamble and everything before the first \section
    while lines and not lines[0].lstrip().startswith(r"\section"):
        lines.pop(0)
    
    # Remove \end{document}
    lines = [line for line in lines if not line.lstrip().startswith(r"\end{document}")]

    # Insert graphicspath with directory of the .tex file
    lines.insert(0, r"\graphicspath{{" + str(zip_file.stem) + r"/}}" + "\n")

    # Save the cleaned .tex file
    with tex_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)

print("All zip files processed.")
