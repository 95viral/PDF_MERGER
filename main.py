import PyPDF2 as pd

merger = pd.PdfWriter()

pdfs = []
try:
    while True:
        pdf = input("Enter PDF file name (or 'done' to finish): ")
        if pdf.lower() == 'done':
            break
        pdfs.append(pdf)

    for pdf in pdfs:
        merger.append(pdf)
except Exception as e:
    print(f"An error occurred: {e}")

merger.write("merged-pdf.pdf")
merger.close()