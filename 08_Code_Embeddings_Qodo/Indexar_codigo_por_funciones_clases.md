# Indexar código por funciones y clases

Indexar por archivo entero suele mezclar demasiadas responsabilidades. Por función/clase mejora precisión y metadata.

## Conecta con
- [[Code_Embeddings]]
- [[Qdrant]]

## Chunking
Usa AST cuando sea posible. Si no, usa heurísticas por `def`/`class`.

## Metadata
`file_path`, `symbol`, `start_line`, `end_line`, `commit`, `language`.

## Tradeoff
Chunks pequeños recuperan precisión; chunks grandes dan contexto.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

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
