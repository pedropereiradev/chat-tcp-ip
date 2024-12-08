# Chat TCP/IP em Python - Projeto de Automação e Programabilidade em Redes

## Descrição do Projeto
Este projeto implementa um sistema de chat baseado em TCP/IP utilizando Python, permitindo a comunicação em tempo real entre múltiplos clientes através de um servidor central. O sistema utiliza sockets e threads para gerenciar as conexões e a comunicação entre os usuários.

## Funcionalidades
- Conexão simultânea de múltiplos clientes
- Identificação de usuários por nome
- Broadcast de mensagens para todos os participantes
- Notificações de entrada e saída de usuários
- Tratamento de desconexões inesperadas

## Estrutura do Projeto
```
trabalho-final/
│
├── servidor.py    # Implementação do servidor
├── cliente.py     # Implementação do cliente
└── README.md      # Documentação do projeto
```

## Tecnologias Utilizadas
- Python 3.x
- Biblioteca `socket` para comunicação em rede
- Biblioteca `threading` para gerenciamento de múltiplas conexões

## Como Executar
1. Inicie o servidor:
```bash
python servidor.py
```

2. Em terminais diferentes, execute os clientes:
```bash
python cliente.py
```

3. Para cada cliente:
   - Digite um nome quando solicitado
   - Comece a enviar mensagens
   - Digite 'sair' para encerrar a conexão

## Detalhamento Técnico

### Servidor (servidor.py)
- **Arquitetura**: Servidor TCP multithreaded
- **Endereço**: localhost (127.0.0.1)
- **Porta**: 65432
- **Componentes principais**:
  - Dicionário de clientes ativos
  - Sistema de broadcast de mensagens
  - Gerenciamento de conexões por threads

### Cliente (cliente.py)
- Implementa interface de usuário via terminal
- Utiliza threads para recebimento assíncrono de mensagens
- Mantém conexão TCP persistente com o servidor

## Protocolo de Comunicação
1. **Conexão Inicial**:
   - Cliente conecta ao servidor
   - Servidor solicita nome do usuário
   - Cliente envia nome
   - Servidor anuncia entrada do novo usuário

2. **Troca de Mensagens**:
   - Mensagens são codificadas em UTF-8
   - Formato: `"[nome_usuario]: [mensagem]"`
   - Tamanho máximo de mensagem: 1024 bytes

3. **Desconexão**:
   - Cliente envia comando 'sair'
   - Servidor remove cliente da lista
   - Broadcast de notificação de saída

## Considerações de Implementação

### Tratamento de Erros
- Gerenciamento de desconexões abruptas
- Remoção automática de clientes inativos
- Tratamento de exceções na comunicação

### Limitações
- Interface baseada em terminal
- Sem persistência de mensagens
- Sem criptografia
- Execução apenas em rede local

### Possíveis Melhorias Futuras
- Interface gráfica
- Histórico de mensagens
- Suporte a mensagens privadas
- Criptografia das comunicações
- Suporte a emojis e formatação
- Transferência de arquivos

## Conclusão
Este projeto demonstra a implementação prática de conceitos fundamentais de redes de computadores, incluindo:
- Comunicação TCP/IP
- Programação com sockets
- Processamento multithreaded
- Protocolos de aplicação

O sistema desenvolvido serve como base para entender os princípios de comunicação em rede e pode ser expandido com funcionalidades adicionais.

## Autores
Pedro Pereira e Patrick Almeida

---
*Este projeto foi desenvolvido como trabalho de estudo de comunicação utilizando Socket na disciplina de Automação e Programabilidade de Redes.*
