# Entrypoint y Command

`ENTRYPOINT` define el ejecutable principal. `CMD` define argumentos por defecto. En Compose puedes sobreescribir `command` para cambiar cómo arranca el contenedor.

## Conecta con
- [[Docker]]
- [[OpenWebUI_Patch_al_arrancar]]

## Por qué importa
Si se aplica un patch al arrancar, normalmente hay un script wrapper que parchea archivos y después ejecuta el proceso real.

## Patrón
```sh
#!/bin/sh
set -e
cd /app
patch -p1 < /patches/company.patch
exec ./start.sh
```

## Riesgo
Si el script no usa `exec`, las señales de parada pueden no llegar bien al proceso final.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Ampliación curso: por qué entrypoint importa para patches

La imagen oficial define cómo arrancar la aplicación. Si la empresa quiere aplicar un patch antes de arrancar, necesita interceptar ese arranque. Eso suele hacerse con un entrypoint propio.

### Patrón robusto

```sh
#!/bin/sh
set -eu

echo "[startup] checking patch"
if [ -f /patches/company.patch ]; then
  cd /app
  git apply --check /patches/company.patch
  git apply /patches/company.patch
  echo "[startup] patch applied"
fi

exec /app/start.sh
```

### Por qué `exec` importa

`exec` reemplaza el shell por el proceso real. Así Docker envía señales de parada al proceso correcto. Sin `exec`, puedes tener paradas lentas o procesos huérfanos.

### Checklist para un entrypoint de empresa

- [ ] Usa `set -e` o equivalente para fallar si el patch falla.
- [ ] Loggea qué patch aplica.
- [ ] Comprueba antes con `git apply --check`.
- [ ] No oculta errores.
- [ ] Termina con `exec`.
- [ ] Permite saber versión base y versión del patch.

## Lección guiada

En Docker, cada concepto debe aterrizar en un comando observable. No basta con decir "contenedor": debes saber verlo, pararlo, inspeccionarlo y leer sus logs.

### Preguntas

- ¿Qué vive en la imagen y qué vive en el contenedor?
- ¿Qué parte se pierde al borrar el contenedor?
- ¿Qué URL usa mi host y qué URL usa otro contenedor?
- ¿Qué log confirma que el servicio arrancó?

### Práctica

```bash
docker ps
docker ps -a
docker logs <container>
docker exec -it <container> sh
docker compose ps
docker compose logs -f
```

### Evidencia

- [ ] He ejecutado al menos un comando relacionado con esta nota.
- [ ] Puedo explicar un fallo típico.
- [ ] Sé cómo conectarlo con [[Docker_para_OpenWebUI_Qdrant_LiteLLM]].
