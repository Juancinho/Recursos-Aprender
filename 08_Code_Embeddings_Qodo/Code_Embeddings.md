# Code Embeddings

Un code embedding representa código en un vector para buscar por significado, no solo por texto exacto.

## Conecta con
- [[Qodo]]
- [[Busqueda_semantica_en_codigo]]
- [[Indexar_codigo_por_funciones_clases]]

## Text vs code
Texto general prioriza lenguaje natural. Code embeddings intentan capturar nombres, estructura, llamadas y patrones.

## Direcciones
Natural language -> code y code -> code.

## Riesgo
Puede recuperar código semánticamente parecido pero incorrecto para el repo actual.

## Checklist
- [ ] Puedo explicar el concepto sin leer la nota.
- [ ] He ejecutado al menos un comando o ejercicio relacionado.
- [ ] He escrito una duda concreta en [[Diario_Estudio_Template]].

## Ampliación curso: chunking de código

El chunking determina la calidad del índice. No es lo mismo indexar archivos enteros que funciones.

### Archivo entero

Ventaja: mucho contexto. Desventaja: mezcla responsabilidades. Una query puede recuperar el archivo correcto pero no la función exacta.

### Función/clase

Ventaja: precisión. Desventaja: puede perder contexto de imports, constantes o configuración.

### Chunk enriquecido

Una práctica mejor es indexar:

```text
file_path
imports relevantes
nombre de clase/función
docstring
firma
cuerpo
líneas
```

### AST

Para Python, `ast` permite extraer funciones/clases sin depender de regex frágiles. Para TypeScript o Java, conviene usar parser específico.

### Evaluación

Crea queries con respuesta conocida:

- "where is qdrant client created?"
- "where is git apply called?"
- "where is coverage calculated?"

Mide si el símbolo correcto aparece en top-5.

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
