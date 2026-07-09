# README código de laboratorio

Estos scripts son didácticos. No están pensados como librería de producción, sino como piezas pequeñas para entender conceptos.

## Orden de ejecución

```bash
python 13_Labs/code/requirements_dataset.py
python 13_Labs/code/coverage_checker.py
python 13_Labs/code/embedding_thresholds.py
python 13_Labs/code/bm25_hybrid.py
python 13_Labs/code/qdrant_index_search.py
python 13_Labs/code/code_embedding_indexer.py --repo .
python 13_Labs/code/attention_requirements_from_scratch.py
python 13_Labs/code/attention_requirements_with_transformers.py
python 13_Labs/code/can_autoencoder.py
```

## Dependencias por grupo

### Básico

`requirements_dataset.py` y `coverage_checker.py` usan librería estándar.

### Retrieval

```bash
pip install pandas numpy scikit-learn sentence-transformers rank-bm25 qdrant-client
```

### Atención

```bash
pip install torch matplotlib pandas transformers
```

### Autoencoder CAN

```bash
pip install torch pandas numpy scikit-learn
```

## Cómo leer los scripts

- Empieza por `main()` si existe.
- Mira qué archivos crea en `13_Labs/outputs/`.
- Identifica inputs, transformación y outputs.
- Cambia un parámetro y observa qué ocurre.

## Cambios recomendados para aprender

- Añadir nuevos requisitos UDS.
- Cambiar thresholds.
- Añadir un módulo `braking`.
- Probar otra query BM25.
- Cambiar percentil 99 del autoencoder a 95.
- Comparar atención de otra pareja de requisitos.

## Actualización curso profundo


    # README código de laboratorio

    Estos scripts son didácticos. No están pensados como librería de producción, sino como piezas pequeñas para entender conceptos.

    ## Orden de ejecución

    ```bash
    python 13_Labs/code/requirements_dataset.py
    python 13_Labs/code/coverage_checker.py
    python 13_Labs/code/embedding_thresholds.py
    python 13_Labs/code/bm25_hybrid.py
    python 13_Labs/code/qdrant_index_search.py
    python 13_Labs/code/code_embedding_indexer.py --repo .
    python 13_Labs/code/attention_requirements_from_scratch.py
    python 13_Labs/code/attention_requirements_with_transformers.py
    python 13_Labs/code/can_autoencoder.py
    ```

    ## Dependencias por grupo

    ### Básico

    `requirements_dataset.py` y `coverage_checker.py` usan librería estándar.

    ### Retrieval

    ```bash
    pip install pandas numpy scikit-learn sentence-transformers rank-bm25 qdrant-client
    ```

    ### Atención

    ```bash
    pip install torch matplotlib pandas transformers
    ```

    ### Autoencoder CAN

    ```bash
    pip install torch pandas numpy scikit-learn
    ```

    ## Cómo leer los scripts

    - Empieza por `main()` si existe.
    - Mira qué archivos crea en `13_Labs/outputs/`.
    - Identifica inputs, transformación y outputs.
    - Cambia un parámetro y observa qué ocurre.

    ## Cambios recomendados para aprender

    - Añadir nuevos requisitos UDS.
    - Cambiar thresholds.
    - Añadir un módulo `braking`.
    - Probar otra query BM25.
    - Cambiar percentil 99 del autoencoder a 95.
    - Comparar atención de otra pareja de requisitos.

## Lección guiada

Un laboratorio se termina cuando puedes explicar entrada, transformación, salida y error típico.

### Antes de cerrar

- [ ] Sé qué archivo o servicio era input.
- [ ] Sé qué transformó el script/comando.
- [ ] Sé qué output generó.
- [ ] Sé qué dependencia podría faltar.
- [ ] Sé cómo modificar un parámetro para experimentar.
