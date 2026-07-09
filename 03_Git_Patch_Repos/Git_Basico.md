# Git Básico

Git registra cambios entre versiones. Para tu caso, lo importante es leer historia, ver diferencias y entender qué se está aplicando encima de una base.

## Conecta con
- [[Diff_y_Patch]]
- [[Git_Apply]]

## Comandos
```bash
git status
git log --oneline --decorate -20
git show <commit>
git diff
git diff --staged
```

## Lectura
`git show` enseña un commit completo. `git diff` enseña cambios no confirmados. `git log` enseña historia.

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
