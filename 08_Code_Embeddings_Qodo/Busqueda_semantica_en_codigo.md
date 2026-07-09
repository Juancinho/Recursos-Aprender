# Búsqueda semántica en código

Permite preguntar en lenguaje natural por una intención y recuperar funciones candidatas.

## Conecta con
- [[Code_Embeddings]]
- [[Grep_vs_Code_Embeddings]]

## Ejemplos
`where is vector search implemented?`, `code that applies a patch`, `function that filters by module`.

## Uso correcto
Primero candidatos, luego lectura humana y tests.

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
