# Lab 14 - Grafo de requisitos con atencion

## Objetivo

Construir un grafo pequeño de requisitos:

- nodos = requisitos;
- candidatos = requisitos cercanos por similitud global;
- aristas = relaciones candidatas refinadas con atencion token-a-token;
- evidencia = pares de tokens que explican la arista.

Este lab implementa la idea de [[Grafo_de_requisitos_con_atencion]].

## Prerrequisitos

Minimo:

```bash
pip install pandas numpy matplotlib
```

Opcional para mejor visualizacion:

```bash
pip install networkx scikit-learn
```

El script tiene fallback si faltan `scikit-learn` o `networkx`.

## Pasos

1. Crea o reutiliza dataset:

```bash
python 13_Labs/code/requirements_dataset.py
```

2. Ejecuta el grafo:

```bash
python 13_Labs/code/requirements_attention_graph.py
```

3. Abre salidas:

```text
13_Labs/outputs/requirements_graph_nodes.csv
13_Labs/outputs/requirements_graph_edges.csv
13_Labs/outputs/requirements_graph.png
```

## Que deberias observar

En `edges.csv` veras columnas:

- `source`: requisito origen;
- `target`: requisito destino;
- `candidate_score`: similitud global;
- `attention_score`: fuerza media de alineamiento token-token;
- `weight`: score combinado;
- `evidence`: pares de tokens destacados.

## Interpretacion

Una arista fuerte no significa automaticamente que los requisitos sean duplicados. Significa:

```text
este par merece revision porque comparte señales globales y tokens alineados
```

La decision final puede ser:

- duplicate;
- related;
- covers;
- contradicts;
- same_module;
- unrelated.

## Errores comunes

- Pensar que PCA descubre relaciones: PCA solo ayuda a visualizar.
- Usar atencion como verdad causal: la atencion es evidencia auxiliar.
- No guardar evidencia: sin evidencia no puedes auditar el grafo.
- Usar todos contra todos sin top-k: escala mal y mete ruido.

## Entregable

- [ ] `requirements_graph_edges.csv` generado.
- [ ] 5 aristas revisadas manualmente.
- [ ] Una nota explicando si las aristas tienen sentido.
- [ ] Un threshold propuesto para ocultar ruido.

