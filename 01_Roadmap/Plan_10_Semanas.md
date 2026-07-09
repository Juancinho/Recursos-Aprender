# Plan 10 Semanas

| Semana | Tema | Objetivos | Teoría | Práctica | Entregable | Checklist | Señales de que ya lo entiendo |
|---|---|---|---|---|---|---|---|
| 1 | Docker | Levantar e inspeccionar servicios | [[Docker]], [[Imagen_vs_Contenedor]], [[Puertos_Volumenes_Redes]] | [[Lab_01_Docker_Nginx]], [[Lab_02_Docker_Compose]] | Capturas/comandos en diario | `docker ps`, logs, exec | Puedo explicar `HOST:CONTENEDOR` y recuperar un contenedor caído |
| 2 | Git/diff/patch/repos grandes | Entender cambios aplicados sobre base oficial | [[Diff_y_Patch]], [[Git_Apply]], [[Como_leer_un_repo_grande_sin_IA]] | [[Lab_03_Patch_al_arrancar]] | `changes.patch` y `MAPA_REPO.md` | generar, aplicar, romper patch | Sé diagnosticar por qué un patch no aplica |
| 3 | Testing basado en requisitos | Modelar requisitos, tests y cobertura | [[Testing_basado_en_requisitos]], [[Trazabilidad]] | [[Lab_04_Dataset_Requisitos]] | `requirements.csv`, `tests.csv`, coverage | gaps, duplicados, contradicciones | Sé decir qué test cubre qué requisito y qué falta |
| 4 | Embeddings + thresholds | Medir similitud y errores | [[Embeddings_para_requisitos]], [[Thresholds_Falsos_Positivos_Falsos_Negativos]] | [[Lab_05_Embeddings_Thresholds]] | matriz de similitud | thresholds 0.5-0.9 | Entiendo FP/FN al mover threshold |
| 5 | BM25 + hybrid search | Combinar lexical y semántico | [[BM25]], [[Hybrid_Search]], [[RRF_Reranking]] | [[Lab_06_BM25_Hybrid]] | ranking comparado | alpha y RRF | Sé cuándo BM25 gana a embeddings |
| 6 | Qdrant | Indexar y filtrar vectores | [[Qdrant]], [[Qdrant_Colecciones_Points_Payload]] | [[Lab_07_Qdrant]] | colección `requirements` | points, payload, filtros | Puedo buscar por vector y filtrar por `module` |
| 7 | OpenWebUI parcheado | Entender integración y customización | [[OpenWebUI]], [[OpenWebUI_imagen_oficial_mas_patch]] | [[Lab_08_OpenWebUI_Arquitectura]] | mapa de servicios | inspección, grep | Sé comprobar si hay `hybrid_search` o `bm25` |
| 8 | vLLM/LiteLLM/Qwen | Entender serving local | [[Motor_de_inferencia]], [[KV_Cache_Batching_Streaming]] | [[Lab_09_vLLM_LiteLLM]] | curl OpenAI-compatible | streaming, batching | Distingo modelo, gateway y engine |
| 9 | Qodo + LangGraph/MCP | Buscar código y diseñar workflows | [[Qodo]], [[Code_Embeddings]], [[LangGraph]], [[MCP]] | [[Lab_10_Code_Embeddings]] | índice de repo pequeño | grep vs embeddings | Sé cuándo usar búsqueda exacta o semántica |
| 10 | Wireshark/CAN/autoencoders | Leer paquetes y detectar anomalías | [[Wireshark]], [[CAN]], [[UDS]], [[Autoencoders]] | [[Lab_12_Wireshark_CAN]], [[Lab_13_Autoencoder_CAN]] | detector sintético | features, threshold | Puedo explicar un falso positivo CAN |

## Ampliación curso: criterio de profundidad por semana

### Semana 1: Docker
No basta con levantar nginx. Debes poder reconstruir el estado de un servicio desde cero:
configuración -> imagen -> contenedor -> proceso -> logs -> red -> volumen.

### Semana 2: Git/diff/patch/repos
El objetivo no es aprender Git entero. Es dominar la unidad de cambio. Un patch representa una hipótesis: "si cambio estas líneas, obtengo esta funcionalidad". Debes poder comprobar si esa hipótesis sigue siendo válida cuando cambia la base.

### Semana 3: requirements testing
Aprende a convertir texto ambiguo en entidades: requisito, condición, acción, resultado esperado, test, evidencia. La IA ayuda después, no antes.

### Semana 4-6: retrieval
Aquí el foco es evaluación. Si no hay golden set, no sabes si un cambio mejora o solo parece mejorar. Guarda ejemplos de falsos positivos y falsos negativos; son más valiosos que una métrica media sin contexto.

### Semana 7-8: OpenWebUI e inferencia
Separa UI, backend, gateway y engine. Cuando algo falla, pregunta: ¿falló la llamada HTTP, el retrieval, el prompt, el servidor de modelo, la GPU o el streaming?

### Semana 9: Qodo/LangGraph/MCP
Trátalo como ingeniería de herramientas. Un workflow bueno tiene pasos pequeños, estado explícito, validación y revisión humana.

### Semana 10: automoción/anomalías
No empieces entrenando modelos. Primero lee frames. Si no sabes qué significa `can_id`, `dlc`, `delta_time` o `NRC`, el autoencoder será una caja negra sobre columnas.

## Lección guiada

Esta nota pertenece al plan de estudio. No la leas como una lista pasiva: conviértela en agenda.

### Preguntas

- ¿Qué bloque reduce más incertidumbre esta semana?
- ¿Qué entregable demostraría que lo entiendo?
- ¿Qué tema debo posponer aunque sea interesante?

### Evidencia de dominio

- [ ] Puedo explicar por qué este paso va antes que el siguiente.
- [ ] Tengo un entregable pequeño asociado.
- [ ] He marcado una duda para preguntar en la empresa.
