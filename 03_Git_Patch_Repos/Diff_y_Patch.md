# Diff y Patch

Un diff describe cambios entre archivos. Un patch es un diff guardado para aplicarlo después.

## Comandos clave

```bash
git diff
git show <commit>
git log --oneline
git diff > changes.patch
git apply changes.patch
git apply --check changes.patch
```

## Qué significa aplicar un diff al arrancar un contenedor

Significa que el contenedor parte de una imagen base, por ejemplo la imagen oficial de [[OpenWebUI]], y durante el arranque ejecuta algo parecido a:

```sh
git apply /patches/company.patch
```

o:

```sh
patch -p1 < /patches/company.patch
```

Después arranca la aplicación. El contenedor final contiene cambios propios, pero la imagen base sigue siendo la oficial.

## Por qué hacerlo

- Mantenerse cerca de la imagen oficial.
- Evitar mantener un fork completo.
- Aplicar cambios internos pequeños.
- Probar modificaciones sin reconstruir una imagen compleja.

## Riesgos

> [!warning]
> Si OpenWebUI cambia el archivo base, el patch puede dejar de aplicar.

- El patch queda acoplado a líneas concretas.
- Puede aplicar con offset pero cambiar comportamiento inesperado.
- Es fácil olvidar documentar qué modifica.
- Si falla al arrancar, el servicio puede no estar disponible.

## Ejercicio rápido

```bash
mkdir patch-demo
cd patch-demo
git init
echo "hello" > app.txt
git add app.txt
git commit -m "base"
echo "hello technica" > app.txt
git diff > changes.patch
git checkout -- app.txt
git apply --check changes.patch
git apply changes.patch
cat app.txt
```

Rompe el patch cambiando la línea base:

```bash
git checkout -- app.txt
echo "hola" > app.txt
git apply --check changes.patch
```

## Checklist

- [ ] Sé generar un patch.
- [ ] Sé comprobarlo con `git apply --check`.
- [ ] Sé explicar por qué falla cuando cambia la base.

## Ampliación curso: leer un patch como un ingeniero

Un patch tiene cabeceras, rutas y hunks. Un hunk es un bloque de cambios con contexto.

```diff
diff --git a/app.py b/app.py
index 83db48f..f735c2a 100644
--- a/app.py
+++ b/app.py
@@ -10,6 +10,8 @@ def search(query):
     results = dense_search(query)
+    bm25_results = bm25_search(query)
+    results = fuse(results, bm25_results)
     return results
```

### Cómo interpretarlo

- `---` y `+++`: archivo antes/después.
- `@@`: zona aproximada del archivo.
- líneas con espacio: contexto.
- líneas con `-`: se eliminan.
- líneas con `+`: se añaden.

### Por qué un patch deja de aplicar

`git apply` busca el contexto. Si el archivo cambió demasiado, no sabe dónde insertar. Esto pasa mucho si actualizas OpenWebUI oficial y el patch tocaba una función interna que cambió.

### Estrategia de mantenimiento

1. Mantén patches pequeños.
2. Divide por funcionalidad: `hybrid-search.patch`, `qdrant-payload.patch`.
3. Añade test o grep de comprobación por patch.
4. Documenta versión base.
5. Revalida al subir versión de imagen.

### Ejercicio con diagnóstico

- [ ] Genera un patch.
- [ ] Cambia el archivo base para que falle.
- [ ] Ejecuta `git apply --check`.
- [ ] Lee exactamente qué hunk falló.
- [ ] Arregla el patch manualmente.

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
