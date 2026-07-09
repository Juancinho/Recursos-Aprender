# Ejercicio indexar repo Python

## Objetivo

Indexar un repo Python pequeño por funciones/clases, generar embeddings, meterlos en Qdrant y comparar contra `rg`.

## Comandos

```bash
python 13_Labs/code/code_embedding_indexer.py --repo .
```

Consultas:

- `where is vector search implemented?`
- `code that applies a patch`
- `function that calculates coverage`

## Entregable

- [ ] Top-5 semántico.
- [ ] Resultado equivalente con `rg`.
- [ ] Dos casos donde `rg` gana.
- [ ] Dos casos donde embeddings ayudan.

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
