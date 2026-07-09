# Curso completo IA Technica

Esta nota funciona como temario narrativo. Si te pierdes entre carpetas, vuelve aquí.

## Bloque 1: infraestructura mínima

Empieza por [[Docker]]. El objetivo es ser capaz de levantar e inspeccionar servicios. No estudies OpenWebUI como aplicación hasta poder responder:

- [ ] ¿Qué contenedor está vivo?
- [ ] ¿Qué puerto expone?
- [ ] ¿Dónde están los logs?
- [ ] ¿Qué volumen guarda datos?
- [ ] ¿Qué variables conectan servicios?

## Bloque 2: cambios sobre software existente

Sigue con [[Diff_y_Patch]], [[Git_Apply]] y [[OpenWebUI_Patch_al_arrancar]]. El objetivo es entender cómo una empresa adapta una herramienta open source sin mantener un fork completo.

Pregunta central: si mañana OpenWebUI cambia de versión, ¿cómo sé si nuestras modificaciones siguen funcionando?

## Bloque 3: orientación en repos

Lee [[Como_leer_un_repo_grande_sin_IA]]. Esto es una habilidad profesional independiente de la IA. Un LLM puede ayudar, pero tú debes saber encontrar entrypoints, configuración, tests y llamadas externas.

## Bloque 4: dominio de requisitos

Lee [[Testing_basado_en_requisitos]]. Aquí pasas de texto a datos evaluables. Sin esta capa, embeddings y LLMs no tienen una tarea bien definida.

## Bloque 5: retrieval

Estudia [[Embeddings_para_requisitos]], [[BM25]], [[Hybrid_Search]], [[Qdrant]] y [[Evaluacion_Retrieval]]. El objetivo no es "usar RAG", sino medir si recuperas candidatos correctos.

## Bloque 6: interfaz y serving

Lee [[OpenWebUI]], [[Motor_de_inferencia]], [[LiteLLM]], [[vLLM]] y [[Qwen_Local]]. Aquí separas UI, gateway, motor y modelo.

## Bloque 7: código y agentes

Lee [[Qodo]], [[Code_Embeddings]], [[LangGraph]] y [[MCP]]. El objetivo es entender cómo buscar código por intención y cómo convertir un proceso en workflow auditable.

## Bloque 8: automoción y anomalías

Lee [[Wireshark]], [[CAN]], [[UDS]], [[DoIP]], [[Autoencoders]] y [[Features_para_CAN]]. Antes de entrenar modelos, aprende a leer los datos.

## Bloque 9: atención entre requisitos

Lee [[Atencion_desde_cero]], [[Self_Attention_vs_Cross_Attention]], [[Atencion_entre_dos_requisitos]] y [[Atencion_no_es_explicabilidad]]. Implementa, visualiza y compara contra BM25/embeddings.

## Examen final propuesto

Construye una demo pequeña:

1. Dataset de requisitos y tests.
2. Coverage básico.
3. BM25 + embeddings + hybrid.
4. Qdrant con filtros.
5. Informe de top-k y errores.
6. Heatmap de atención para un par UDS.
7. Mini autoencoder CAN sintético.
8. `MAPA_REPO.md` de la propia bóveda/scripts.

## Actualización curso profundo


    # Curso completo IA Technica

    Esta nota funciona como temario narrativo. Si te pierdes entre carpetas, vuelve aquí.

    ## Bloque 1: infraestructura mínima

    Empieza por [[Docker]]. El objetivo es ser capaz de levantar e inspeccionar servicios. No estudies OpenWebUI como aplicación hasta poder responder:

    - [ ] ¿Qué contenedor está vivo?
    - [ ] ¿Qué puerto expone?
    - [ ] ¿Dónde están los logs?
    - [ ] ¿Qué volumen guarda datos?
    - [ ] ¿Qué variables conectan servicios?

    ## Bloque 2: cambios sobre software existente

    Sigue con [[Diff_y_Patch]], [[Git_Apply]] y [[OpenWebUI_Patch_al_arrancar]]. El objetivo es entender cómo una empresa adapta una herramienta open source sin mantener un fork completo.

    Pregunta central: si mañana OpenWebUI cambia de versión, ¿cómo sé si nuestras modificaciones siguen funcionando?

    ## Bloque 3: orientación en repos

    Lee [[Como_leer_un_repo_grande_sin_IA]]. Esto es una habilidad profesional independiente de la IA. Un LLM puede ayudar, pero tú debes saber encontrar entrypoints, configuración, tests y llamadas externas.

    ## Bloque 4: dominio de requisitos

    Lee [[Testing_basado_en_requisitos]]. Aquí pasas de texto a datos evaluables. Sin esta capa, embeddings y LLMs no tienen una tarea bien definida.

    ## Bloque 5: retrieval

    Estudia [[Embeddings_para_requisitos]], [[BM25]], [[Hybrid_Search]], [[Qdrant]] y [[Evaluacion_Retrieval]]. El objetivo no es "usar RAG", sino medir si recuperas candidatos correctos.

    ## Bloque 6: interfaz y serving

    Lee [[OpenWebUI]], [[Motor_de_inferencia]], [[LiteLLM]], [[vLLM]] y [[Qwen_Local]]. Aquí separas UI, gateway, motor y modelo.

    ## Bloque 7: código y agentes

    Lee [[Qodo]], [[Code_Embeddings]], [[LangGraph]] y [[MCP]]. El objetivo es entender cómo buscar código por intención y cómo convertir un proceso en workflow auditable.

    ## Bloque 8: automoción y anomalías

    Lee [[Wireshark]], [[CAN]], [[UDS]], [[DoIP]], [[Autoencoders]] y [[Features_para_CAN]]. Antes de entrenar modelos, aprende a leer los datos.

    ## Bloque 9: atención entre requisitos

    Lee [[Atencion_desde_cero]], [[Self_Attention_vs_Cross_Attention]], [[Atencion_entre_dos_requisitos]] y [[Atencion_no_es_explicabilidad]]. Implementa, visualiza y compara contra BM25/embeddings.

    ## Examen final propuesto

    Construye una demo pequeña:

    1. Dataset de requisitos y tests.
    2. Coverage básico.
    3. BM25 + embeddings + hybrid.
    4. Qdrant con filtros.
    5. Informe de top-k y errores.
    6. Heatmap de atención para un par UDS.
    7. Mini autoencoder CAN sintético.
    8. `MAPA_REPO.md` de la propia bóveda/scripts.

## Lección guiada

Usa esta nota como punto de navegación. Antes de avanzar, identifica qué módulo estás estudiando, qué práctica vas a ejecutar y qué evidencia dejarás en el diario.

- [ ] He elegido una ruta concreta para hoy.
- [ ] Sé qué archivo abrir después.
- [ ] Sé qué comando, script o checklist usaré.
- [ ] He escrito una salida esperada antes de ejecutar nada.
