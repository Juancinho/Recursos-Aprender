# Próximos pasos: primer día

1. Abrir Docker Desktop.
2. Ejecutar `docker version`.
3. Ejecutar `docker run hello-world`.
4. Levantar nginx.
5. Hacer `docker logs`.
6. Entrar con `docker exec`.
7. Escribir en Diario qué he entendido y qué no.

## Comandos concretos

```bash
docker version
docker run hello-world
docker run --name technica-nginx -p 8080:80 -d nginx:alpine
docker ps
docker logs technica-nginx
docker exec -it technica-nginx sh
docker stop technica-nginx
docker rm technica-nginx
```

## Diario mínimo

Abre [[Diario_Estudio_Template]] y responde:

- [ ] Qué es una imagen.
- [ ] Qué es un contenedor.
- [ ] Qué significa `8080:80`.
- [ ] Qué vi dentro del contenedor con `docker exec`.
- [ ] Qué error apareció, si apareció alguno.

## Lección guiada

Usa esta nota como punto de navegación. Antes de avanzar, identifica qué módulo estás estudiando, qué práctica vas a ejecutar y qué evidencia dejarás en el diario.

- [ ] He elegido una ruta concreta para hoy.
- [ ] Sé qué archivo abrir después.
- [ ] Sé qué comando, script o checklist usaré.
- [ ] He escrito una salida esperada antes de ejecutar nada.
