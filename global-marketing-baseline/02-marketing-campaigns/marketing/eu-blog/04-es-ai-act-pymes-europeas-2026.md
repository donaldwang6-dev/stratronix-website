# BLOG 04 — ES — AI Act europeo 2026: lo que las PYME deben saber

> **Autor:** JERRY (marketing STRATRONIX) · **Revisión pendiente:** Donald Wang (CEO)
> **Estado:** BORRADOR v0.1 · 2026-07-23 · **Volumen:** ~1.100 palabras
> **Distribución:** Silicon News Spain · The Spain Business · EU-Startups (Guest Post)
> **Cumplimiento:** regla 31 (sin fabricación) — solo fuentes jurídicas públicas

---

## La realidad 2026 para los adoptantes europeos de IA

El Reglamento europeo de IA (Reglamento 2024/1689) entró en vigor por fases a lo largo de 2025 y 2026. Para las pequeñas y medianas empresas europeas, la pregunta práctica en julio de 2026 ya no es *debemos adoptar IA*, sino *bajo qué reglas*. Este artículo resume lo que está en vigor, lo que cambia el 2 de agosto de 2026, y cómo un appliance de IA on-premise — categoría a menudo abreviada como PAA (Private AI-Agent Appliance) — encaja en el marco regulatorio.

## Lo que está en vigor hoy (julio 2026)

Tres bloques del Reglamento IA ya son vinculantes:

| Bloque | Fecha de entrada en vigor | Contenido |
|--------|---------------------------|-----------|
| **Prácticas prohibidas (art. 5)** | 2 de febrero de 2025 | Puntuación social, IA manipulativa, captura no dirigida de rostros, identificación biométrica en tiempo real (con excepciones estrechas) |
| **Obligaciones para IA de uso general (GPAI) (art. 50 + anexo XI)** | 2 de agosto de 2025 | Los proveedores de modelos frontera deben publicar resúmenes de datos de entrenamiento, políticas de derechos de autor y evaluaciones de riesgo sistémico por encima de 10²⁵ FLOPs |
| **Obligaciones de transparencia (art. 50)** | 2 de agosto de 2026 | Los proveedores y responsables del despliegue de sistemas de IA que interactúan con personas, generan medios sintéticos o realizan reconocimiento emocional deben revelar la implicación de la IA |

## Lo que cambia el 2 de agosto de 2026

A partir de agosto de 2026, el régimen de clasificación de alto riesgo (anexo III) se aplica a los sistemas utilizados en:

- **Infraestructuras críticas** (agua, gas, electricidad, tráfico)
- **Educación y formación profesional** (admisiones, evaluaciones, integridad de exámenes)
- **Empleo** (filtrado de CV, asignación de tareas, supervisión)
- **Servicios esenciales públicos y privados** (scoring crediticio, tarificación de seguros, despacho de emergencias, elegibilidad de prestaciones públicas)
- **Aplicación de la ley y migración** (evaluaciones de riesgo, polígrafos, fiabilidad probatoria)
- **Justicia y procesos democráticos** (asistencia judicial, influencia sobre votantes)

Los sistemas de alto riesgo deben cumplir requisitos de calidad de datos, documentación técnica, supervisión humana, robustez, ciberseguridad y evaluación de la conformidad antes de ser introducidos en el mercado de la UE o puestos en servicio.

## Donde las pilas de IA solo en la nube tienen dificultades

La IA alojada en la nube por proveedores no europeos responde mal a tres preguntas bajo este régimen:

1. **¿Dónde residen físicamente los datos?** — Si el camino de inferencia cruza fronteras (EE. UU., China, Singapur), se aplican los mecanismos de transferencia del Capítulo V del RGPD.
2. **¿Quién es proveedor y quién es responsable del despliegue?** — El artículo 25 reasigna la responsabilidad a lo largo de la cadena. Una PYME española que utiliza la API de OpenAI puede seguir siendo clasificada como responsable del despliegue de un sistema de alto riesgo.
3. **¿Qué exige el artículo 14 (supervisión humana) cuando el modelo es una API alojada?** — La intervención práctica, la anulación y el registro son más difíciles con puntos de conexión sin estado.

## IA on-premise como palanca de cumplimiento

Un appliance de hardware que ejecuta un modelo de lenguaje grande completamente dentro de la sala de datos del cliente — sin llamadas API salientes ni salida de datos de entrenamiento externos — cambia la respuesta operativa a las tres preguntas:

- **Ubicación de los datos:** 100 % dentro de la red de la empresa. Los pesos del modelo están en el dispositivo; los prompts y salidas nunca abandonan el appliance.
- **Línea proveedor/responsable del despliegue:** La PYME europea se convierte a la vez en proveedor y responsable del despliegue de su propia instancia, simplificando la documentación. Un proveedor como STRATRONIX entrega el appliance como hardware, no como servicio continuo.
- **Supervisión humana del artículo 14:** Como el modelo se ejecuta localmente, las organizaciones pueden implementar flujos de aprobación explícitos, registro, pistas de auditoría y rollback sin depender de APIs remotas.

## Lista de comprobación práctica para una PYME europea que despliega IA en 2026

1. **Clasifique su caso de uso** respecto al anexo III antes de la adquisición.
2. **Mapee los flujos de datos.** Si un prompt sale de la UE, debe gestionar un mecanismo de transferencia.
3. **Decida proveedor frente a responsable del despliegue.** Documente el límite en su política de IA.
4. **Exija humano en el bucle** para cualquier resultado de decisión de alto riesgo.
5. **Conserve registros.** La retención de cinco años es la hipótesis de trabajo para sistemas de alto riesgo.
6. **Elija una arquitectura que soporte el artículo 14** — la inferencia local lo hace sustancialmente más fácil.

## Qué ofrece STRATRONIX

STRATRONIX (Stratronix Technology (Shenzhen) Company, Limited) fabrica el STA-100 Private AI-Agent Appliance, un dispositivo de hardware 1U que ejecuta modelos de lenguaje de 7B / 13B / 70B parámetros on-premise. El sistema operativo OpenClaw acompañante es open source bajo BSD-3-Clause, por lo que la ruta de inferencia es auditable. El appliance soporta las 24 lenguas oficiales de la UE más inglés, chino, japonés, coreano, ruso y árabe.

El dispositivo se fabrica en Shenzhen, China, y se envía directamente a clientes europeos a través de la tienda en store.stratonix.ai. STRATRONIX es una empresa pequeña; este artículo no afirma que el STA-100 esté "certificado por el AI Act europeo" por un organismo notificado, porque tal certificación aún no existe para appliances LLM de uso general. La afirmación es más estrecha: el appliance da a los clientes europeos el control total del entorno de inferencia, lo cual es un prerrequisito técnico para la mayoría de los pasos de cumplimiento anteriores.

## Lecturas recomendadas

- **Reglamento (UE) 2024/1689** — texto completo en EUR-Lex (eur-lex.europa.eu)
- **Página del AI Act en la Comisión Europea** — ec.europa.eu/digital-strategy/ai-act
- **RGPD / LOPDGDD** — texto completo en EUR-Lex y aepd.es
- **AEPD — IA y protección de datos** — aepd.es

---

**Sobre el autor**

JERRY es el agente de marketing de STRATRONIX. Este artículo es contenido editorial y no constituye asesoramiento jurídico. Las PYME deben consultar asesoramiento cualificado antes de desplegar IA en casos de uso regulados.

**Contacto para asociaciones europeas:** store.stratonix.ai · +86 13632968417