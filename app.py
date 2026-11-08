import streamlit as st

st.set_page_config(page_title="FlorIA Risk & FX", page_icon="🌸", layout="centered")

st.title("🌸 FlorIA Risk & FX")
st.subheader("Simulador Inteligente de Riesgo Cambiario e Insumos")
st.markdown("**Empresa:** Antioquia Flora & Export S.A.S. | **Ubicación:** Rionegro, Antioquia")

st.markdown("---")

st.sidebar.header("Parámetros de Simulación (Inputs)")
trm = st.sidebar.slider("TRM Proyectada (COP / USD)", 3500, 4800, 4200, 50)
inflacion_insumos = st.sidebar.slider("Inflación de Insumos (%)", 0.0, 20.0, 5.0, 0.5)
volumen_tallos = st.sidebar.number_input("Volumen Exportado (Tallos/mes)", 10000, 100000, 50000, 5000)

precio_usd = 0.80
ingresos_cop = volumen_tallos * precio_usd * trm
costo_unitario_base = 1680
costo_variable_total = volumen_tallos * costo_unitario_base * (1 + inflacion_insumos / 100)
costos_fijos = 42000000
utilidad_operativa = ingresos_cop - costo_variable_total - costos_fijos
margen_contribucion_unitario = (precio_usd * trm) - (costo_unitario_base * (1 + inflacion_insumos / 100))
punto_equilibrio = costos_fijos / margen_contribucion_unitario if margen_contribucion_unitario > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Ingresos Totales (COP)", f"${ingresos_cop:,.0f}")
col2.metric("Utilidad Operativa", f"${utilidad_operativa:,.0f}")
col3.metric("Punto de Equilibrio", f"{punto_equilibrio:,.0f} tallos")

st.markdown("### 🤖 Diagnóstico y Recomendación del Modelo de IA")

if trm < 3900 or utilidad_operativa < 15000000:
    nivel_riesgo = "🔴 ALTO RIESGO CAMBIARIO (Escenario Adverso)"
    recomendacion = "El modelo detecta que una TRM baja combinada con la inflación de insumos comprime severamente los márgenes. **Recomendación IA:** Adquirir contratos de cobertura cambiaria (Forward) sobre el 60% de las exportaciones y renegociar plazos con proveedores locales."
elif trm <= 4300 and utilidad_operativa < 35000000:
    nivel_riesgo = "🟡 RIESGO MODERADO (Escenario Base con Presión)"
    recomendacion = "El proyecto es rentable pero sensible a variaciones semanales. **Recomendación IA:** Mantener un fondo de caja de contingencia equivalente a 1.5 meses de costos fijos y optimizar rutas logísticas hacia el aeropuerto de Rionegro."
else:
    nivel_riesgo = "🟢 RIESGO BAJO / EXCELENTE RENTABILIDAD (Escenario Favorable)"
    recomendacion = "Condiciones macroeconómicas altamente favorables para el negocio. **Recomendación IA:** Destinar el 30% del excedente de utilidad a la implementación de agricultura de precisión e inversión en paneles solares para cuartos fríos."

st.markdown(f"**Clasificación de Riesgo:** {nivel_riesgo}")
st.info(recomendacion)