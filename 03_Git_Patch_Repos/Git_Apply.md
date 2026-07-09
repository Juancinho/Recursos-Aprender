# Git Apply

`git apply` aplica un patch al árbol de trabajo sin crear commit automáticamente. Es útil para reproducir cambios en otra copia o durante el arranque de un contenedor.

## Conecta con
- [[Diff_y_Patch]]
- [[OpenWebUI_Patch_al_arrancar]]

## Comandos
```bash
git apply --check changes.patch
git apply changes.patch
git apply --reject changes.patch
```

## Buenas prácticas
Primero `--check`. Después aplicar. Si falla, lee nombres de archivos y contexto. No fuerces sin entender.

## En contenedores
El script de arranque debería fallar claro si el patch no aplica, no arrancar a medias.

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
