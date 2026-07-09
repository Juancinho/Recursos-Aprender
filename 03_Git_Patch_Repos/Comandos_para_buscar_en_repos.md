# Comandos para buscar en repos

## Archivos

```bash
rg --files
rg --files -g "*.py"
rg --files -g "docker-compose*.yml"
```

## Texto técnico

```bash
rg -n "qdrant|bm25|hybrid|embedding|rerank"
rg -n "litellm|vllm|openai|chat/completions"
rg -n "patch|git apply|diff"
rg -n "can|uds|doip|pcap|wireshark"
```

## Python

```bash
rg -n "^def |^class "
rg -n "FastAPI|APIRouter|BaseModel|pydantic"
rg -n "pytest|unittest"
```

## JavaScript/TypeScript

```bash
rg -n "function |const .*=>|class "
rg -n "fetch\(|axios|useQuery"
rg -n "describe\(|it\("
```

## Lección guiada

En Git/patch/repos, el objetivo es orientarte y controlar cambios. Cada diff debe responder: qué cambia, por qué, dónde y cómo verifico que no se rompió.

### Preguntas

- ¿Qué archivo cambió?
- ¿Qué comportamiento cambia?
- ¿Qué contexto necesita el patch para aplicar?
- ¿Qué comando prueba que aplica limpio?
- ¿Qué búsqueda con `rg` confirma el cambio?

### Práctica

```bash
git diff
git show <commit>
git apply --check changes.patch
rg -n "qdrant|bm25|hybrid|patch|entrypoint"
```

### Evidencia

- [ ] Puedo crear o leer un patch.
- [ ] Puedo explicar un fallo de hunk.
- [ ] Puedo añadir una entrada útil a un `MAPA_REPO.md`.
