# Grep vs Code Embeddings

## Usa `rg` cuando

- Conoces el símbolo exacto.
- Buscas una variable de entorno.
- Buscas un endpoint.
- Buscas un literal de error.
- Quieres exhaustividad textual.

## Usa embeddings cuando

- No conoces el nombre.
- Buscas intención.
- Hay mucho naming inconsistente.
- Quieres encontrar código parecido a otro código.

## Regla práctica

Primero `rg` para hechos. Después embeddings para exploración semántica. Nunca aceptes un resultado semántico sin abrir el archivo y entenderlo.

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
