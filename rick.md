graph TD
    A["VOCÊ <br/>(Despeja qualquer coisa: ideia, tarefa, divagação, fragmento)"] --> B["RICK (O Hub / CLI)"]
    
    subgraph IA [Triagem Inteligente via LLM]
        B --> C["O LLM lê, analisa o contexto e classifica"]
    end

    C --> D1["Divagação <br/>(Reflexões e teorias sem pé nem cabeça)"]
    C --> D2["Ideia <br/>(Hipóteses a maturar, ex: Dr. Cataplasma)"]
    C --> D3["Tarefa <br/>(Ações pragmáticas, ex: consertar Makefile)"]
    C --> D4["Fragmento <br/>(Pedaços soltos de código ou ficção)"]

    D1 --> E["BANCO DE DADOS <br/>(SQLite)"]
    D2 --> E
    D3 --> E
    D4 --> E

    E --> F["Monitor de Gaveta <br/>(Acompanha o tempo aberto)"]
    F --> G["'Ei, isso aqui tá aberto há 8 dias. <br/>Vai continuar ou vai arquivar?'"]
