# Checklist análisis repo empresa

- [ ] Sé qué problema resuelve el repo.
- [ ] Sé cómo se instala.
- [ ] Sé cómo se arranca.
- [ ] Sé qué servicios externos necesita.
- [ ] He localizado Dockerfile/Compose.
- [ ] He localizado variables de entorno.
- [ ] He localizado entrypoints.
- [ ] He localizado tests.
- [ ] He buscado `qdrant`, `bm25`, `hybrid`, `embedding`, `litellm`, `vllm`.
- [ ] He creado un `MAPA_REPO.md`.
- [ ] He apuntado dudas con ruta y línea.

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
