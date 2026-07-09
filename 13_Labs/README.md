# README Laboratorios

Ejecuta los labs en orden. Los scripts crean salidas en `13_Labs/outputs/`.

## Orden recomendado

1. [[Lab_00_Setup]]
2. [[Lab_01_Docker_Nginx]]
3. [[Lab_02_Docker_Compose]]
4. [[Lab_03_Patch_al_arrancar]]
5. [[Lab_04_Dataset_Requisitos]]
6. [[Lab_05_Embeddings_Thresholds]]
7. [[Lab_06_BM25_Hybrid]]
8. [[Lab_07_Qdrant]]
9. [[Lab_08_OpenWebUI_Arquitectura]]
10. [[Lab_09_vLLM_LiteLLM]]
11. [[Lab_10_Code_Embeddings]]
12. [[Lab_11_Atencion_Requisitos]]
13. [[Lab_12_Wireshark_CAN]]
14. [[Lab_13_Autoencoder_CAN]]

## Dependencias Python habituales

```bash
pip install torch matplotlib pandas numpy scikit-learn sentence-transformers rank-bm25 qdrant-client transformers
```

Cada script intenta mostrar un mensaje claro si falta una dependencia.

## Ampliación curso: cómo ejecutar laboratorios como experimentos

Cada lab debe producir una observación. No ejecutes scripts como si fueran una instalación; ejecútalos como experimentos.

### Antes de ejecutar

- [ ] Lee el objetivo.
- [ ] Predice qué archivo o salida aparecerá.
- [ ] Mira dependencias.
- [ ] Ejecuta desde la raíz de la bóveda.

### Durante

- [ ] Copia errores importantes.
- [ ] No instales paquetes a ciegas sin saber para qué sirven.
- [ ] Si hay Docker, mira logs.

### Después

- [ ] Abre outputs.
- [ ] Escribe qué cambió.
- [ ] Relaciona salida con la nota teórica.
- [ ] Añade una mejora posible.

### Mapa scripts -> conceptos

| Script | Concepto |
|---|---|
| `requirements_dataset.py` | datos base de requisitos |
| `coverage_checker.py` | trazabilidad/cobertura |
| `embedding_thresholds.py` | similitud y thresholds |
| `bm25_hybrid.py` | lexical + dense |
| `qdrant_index_search.py` | vector DB + filtros |
| `code_embedding_indexer.py` | code embeddings |
| `attention_requirements_from_scratch.py` | Q/K/V desde cero |
| `attention_requirements_with_transformers.py` | atención real de Transformer |
| `can_autoencoder.py` | anomalías CAN |

## Lección guiada

Un laboratorio se termina cuando puedes explicar entrada, transformación, salida y error típico.

### Antes de cerrar

- [ ] Sé qué archivo o servicio era input.
- [ ] Sé qué transformó el script/comando.
- [ ] Sé qué output generó.
- [ ] Sé qué dependencia podría faltar.
- [ ] Sé cómo modificar un parámetro para experimentar.
