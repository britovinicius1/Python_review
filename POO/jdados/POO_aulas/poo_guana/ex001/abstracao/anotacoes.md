
Abstração -> Pratica de ignorar o irrelevante e so focar istritamente no essencial
Exemplo: Controle remoto, vc nao precisa saber os detalhes internos do controle remoto
Pra dirigir um carro - vc nao precisa saber o funcionamento interno do motor do carro etc pra poder dirigir
Usuario nao precisa entender as minuncias
Vantagens:
- Maior legibilidade
- Padronização
- Simplificação
- Segurança (nao expoe os detalhes internos)

Existe a abstração de daados, que acontece quando ignoramos informações desnecessárias para o escpoto do proeto;
- se nao faz sentido de guardar peso e altura pra um projeto -> abstrai
Abração de projetos -> Existe a abstração de processos, quando não precisamos saber como um método faz seu trabalho, apenas sabe que ela existe pela interface.
(exemplo disso é usar o pandas)
 

Classe abstrata -> Não serve pra gerar objetos, servee de base pra todas as subclasses virar objeto
Metodo abstrato(abstract) -> que ta na calsse mae abstrata, mas a subclasse mas vai ter o metodo, se nao nem vai ter na classe. 


Uma classe abastrata nunca será instanciada (nunca virara um objeto), ja que ela será usada apenas como base para as subclasses.

Ao definir um conjunto de métodos abstratos, dizemos que estamos criando a interface pública da classe.

Uma classe abstrata pode ter métodos abstratos queu deverão ser obrigatoriamente implementada nas subclasses

Mas uma classe abstrata pode ter métodos concretos se eles fimcopmare da mesma maneira pra todas as subclasses(Don't repeat yourself )