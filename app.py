import streamlit as st
from datetime import datetime
from fpdf import FPDF

def generar_pdf(recibi_de, cantidad, concepto, recibido_por):
    pdf = FPDF(orientation='L', format=(120, 160))  # A6 horizontal (mitad de A4 aproximadamente)
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Título
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(140, 10, "Recibo de Pago", ln=True, align='C')
    pdf.ln(5)

    # Fecha actual
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    pdf.set_font("Arial", size=10)
    pdf.cell(140, 10, f"Fecha: {fecha_actual}", ln=True, align='L')
    pdf.ln(5)

    # Información del recibo
    pdf.cell(140, 10, f"Recibí de: {recibi_de}", ln=True, align='L')
    pdf.cell(140, 10, f"Cantidad en Soles: S/ {cantidad}", ln=True, align='L')
    pdf.cell(140, 10, f"Concepto: {concepto}", ln=True, align='L')
    pdf.cell(140, 10, f"Recibido por: {recibido_por}", ln=True, align='L')
    pdf.cell(140, 10, f"Firma del receptor del pago:", ln=True, align='L')

    # Guardar archivo temporal
    pdf_file = "/tmp/recibo_pago.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Interfaz de Streamlit
st.title("Generador de Recibos de Pago en PDF")

# Entradas del usuario
recibi_de = st.text_input("Recibí de", "")
cantidad = st.text_input("Cantidad en Soles", "")
concepto = st.text_area("Concepto", "")
recibido_por = st.text_input("Recibido por", "")

# Botón para generar PDF
if st.button("Generar Recibo de Pago"):
    if recibi_de and cantidad and concepto and recibido_por:
        try:
            pdf_file = generar_pdf(recibi_de, cantidad, concepto, recibido_por)

            # Descargar PDF
            with open(pdf_file, "rb") as file:
                st.download_button(
                    label="Descargar Recibo en PDF",
                    data=file,
                    file_name="recibo_pago.pdf",
                    mime="application/pdf",
                )
        except Exception as e:
            st.error(f"Error al generar el recibo: {e}")
    else:
        st.warning("Por favor, complete todos los campos antes de generar el recibo.")
