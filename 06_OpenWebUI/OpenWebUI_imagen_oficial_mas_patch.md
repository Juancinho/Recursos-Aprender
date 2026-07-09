# OpenWebUI imagen oficial más patch

Patrón: usar imagen oficial para base estable y aplicar cambios internos durante arranque.

## Conecta con
- [[OpenWebUI]]
- [[Diff_y_Patch]]
- [[OpenWebUI_Patch_al_arrancar]]

## Ventaja
Menos mantenimiento que un fork grande.

## Riesgo
La versión oficial cambia y el patch deja de aplicar.

## Prueba mínima
El contenedor debe loggear versión base, patch aplicado y arranque correcto.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Ampliación curso: ventajas y deuda técnica del patrón imagen oficial + patch

Este patrón es pragmático, pero crea una deuda concreta: cada actualización de la imagen oficial exige revalidar el patch.

### Ventajas

- Aprovechas seguridad y mejoras de upstream.
- Evitas mantener fork completo.
- Puedes aislar cambios propios en un diff revisable.
- Facilita comparar "oficial vs modificado".

### Costes

- El patch depende de estructura interna.
- Puede no aplicar al cambiar versión.
- Puede aplicar pero romper semántica.
- Puede ser difícil depurar si se aplica en runtime y no en build.

### Alternativas

| Alternativa | Ventaja | Coste |
|---|---|---|
| Fork | control total | mantenimiento continuo |
| Imagen propia build-time | falla antes, reproducible | pipeline más complejo |
| Patch runtime | flexible | falla al arrancar |
| Plugin/extensión | menos invasivo | depende de puntos de extensión |

### Qué documentación debería existir por patch

- Nombre y propósito.
- Versión base de OpenWebUI.
- Archivos tocados.
- Cómo verificar que se aplicó.
- Riesgos al actualizar.
- Test manual o automático.

## Lección guiada

En OpenWebUI, separa interfaz, backend, retrieval, configuración y modelo. Cuando algo falla, ubica primero en qué tramo está el fallo.

### Preguntas

- ¿OpenWebUI llama al modelo directamente o vía LiteLLM?
- ¿Dónde está configurado Qdrant?
- ¿El patch se aplicó realmente?
- ¿Qué logs muestran retrieval?
- ¿Qué grep confirma símbolos propios?

### Práctica

```bash
docker compose logs -f openwebui
grep -R "hybrid_search" /app/backend/open_webui -n
grep -R "bm25" /app/backend/open_webui -n
grep -R "qdrant" /app/backend/open_webui -n
```

### Evidencia

- [ ] Puedo dibujar OpenWebUI -> Qdrant -> modelo.
- [ ] Puedo explicar imagen oficial + patch.
- [ ] Puedo hacer una checklist de inspección.
