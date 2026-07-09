# Qodo

Qodo puede referirse a la plataforma de herramientas para desarrollo asistido por IA y a Qodo-Embed/code embeddings como modelo o capacidad orientada a código. En el contexto de la empresa, lo importante es preguntar si se usa como producto, como modelo de embeddings o como referencia para indexar código.

## Preguntas concretas

- ¿Usan Qodo como plataforma o solo Qodo-Embed?
- ¿Indexan repos internos?
- ¿El índice va a Qdrant?
- ¿Chunking por archivo, función o clase?
- ¿Qué metadata guardan?

## Relación con repos grandes

Los code embeddings ayudan a buscar por intención:

- "where is vector search implemented?"
- "code that applies a patch"
- "where are OpenAI-compatible calls made?"

Pero no sustituyen a `rg`. Ver [[Grep_vs_Code_Embeddings]].

## Ampliación curso: cómo encaja Qodo en un flujo real

Si Qodo se usa para embeddings de código, el valor no está en "tener vectores", sino en reducir tiempo de orientación en repos grandes.

### Flujo natural language -> code

1. Pregunta: "where is vector search implemented?"
2. Embedding de la pregunta.
3. Búsqueda en índice de funciones/clases.
4. Resultados con `file_path`, símbolo y líneas.
5. Lectura humana del código.
6. Confirmación con `rg` o tests.

### Flujo code -> code

Tomas una función que aplica patch o llama a Qdrant y buscas funciones parecidas. Sirve para encontrar duplicación conceptual o patrones repetidos.

### Qué metadata decide si el sistema es útil

- `file_path`: abrir rápido.
- `symbol`: función/clase.
- `start_line`, `end_line`: contexto exacto.
- `commit`: reproducibilidad.
- `language`: filtros.
- `imports`: dependencias.

### Riesgo principal

Un embedding puede devolver una función que "parece" resolver algo pero pertenece a otro flujo. Por eso siempre se verifica con lectura de llamadas, tests o ejecución.

## Lección guiada

En code embeddings, el objetivo es buscar intención en código sin abandonar las verificaciones exactas. `rg` y embeddings se complementan.

### Preguntas

- ¿Conozco el símbolo exacto? Usa `rg`.
- ¿Busco una intención? Usa embeddings.
- ¿El chunk es archivo, función o clase?
- ¿Qué metadata me permite abrir el sitio correcto?

### Práctica

```bash
python 13_Labs/code/code_embedding_indexer.py --repo .
rg -n "qdrant|patch|coverage|attention"
```

### Evidencia

- [ ] He comparado un resultado semántico con `rg`.
- [ ] Puedo explicar chunking por AST.
- [ ] Sé qué metadata guardaría en Qdrant.
