# Diagrama de classes — Proxy

```mermaid
classDiagram
    class DadosUsuario {
        <<abstract>>
        +nome str
        +cpf str
        +endereco str
    }
    class Usuario {
        -__nome str
        -__cpf str
        -__endereco str
        +__init__(nome, cpf, endereco)
        +nome str
        +cpf str
        +endereco str
    }
    class UsuarioProxy {
        -__usuario Usuario
        +__init__(usuario)
        +nome str
        +cpf str
        +endereco str
    }
    class Principal {
        +main()$
    }
    DadosUsuario <|-- Usuario
    DadosUsuario <|-- UsuarioProxy
    UsuarioProxy --> Usuario : controla acesso
    Principal ..> Usuario : cria
    Principal ..> UsuarioProxy : consulta
```

`nome`, `cpf` e `endereco` são propriedades com métodos de leitura.
O Proxy delega a leitura do nome, mascara o CPF e lança `PermissionError`
ao tentar ler o endereço. O objeto real é mantido em um atributo privado.
