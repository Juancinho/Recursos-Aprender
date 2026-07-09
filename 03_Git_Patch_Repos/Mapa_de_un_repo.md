# Mapa de un repo

Un `MAPA_REPO.md` es una brújula. No es documentación perfecta; es una vista útil para trabajar sin perderte.

## Conecta con
- [[Como_leer_un_repo_grande_sin_IA]]

## Plantilla
```md
# MAPA_REPO

## Cómo arrancar
## Estructura
## Entry points
## Configuración
## Flujo principal
## Tests
## Dudas
```

## Señal de calidad
Otra persona debería poder ubicar dónde tocar para cambiar retrieval, inferencia o configuración.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

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
