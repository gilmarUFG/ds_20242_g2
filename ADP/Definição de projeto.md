# EcoAlerta - Sistema de Reporte de Árvores com risco SocioAmbiental
----
### Atividade de Definição do Projeto
 

#### Definição e Escopo
---- 

O projeto tem como objetivo a produção de uma solução de software que facilite à população reportar árvores doentes com risco de queda ou danos à cidade e facilite aos agentes da Agência Municipal de Meio Ambiente a priorização e atendimento das ocorrências registradas. Os reportes realizados serão automaticamente categorizados pelo sistema de acordo com o grau de risco, auxiliando a AMMA a priorizar os casos reportados e, assim, realizar ações preventivas e específicas, poupando recursos humanos e financeiros.

O usuário que identificar uma árvore que gere algum risco, tanto às demais árvores quanto à estrutura da cidade, poderá reportar ao sistema, identificando os problemas (ex.: galhos quebrados, sinais de doença, inclinação perigosa) , localidade, e foto da árvore. Dessa forma, o sistema calculará automaticamente um "índice de risco" para a árvore, utilizando critérios como a localização (próxima a vias movimentadas, escolas, etc.), o tipo de problema reportado e a condição climática (ventos fortes na região, por exemplo).

Assim que um relatório é enviado, o sistema automaticamente calcula um "índice de risco" que varia de 1 a 10 para cada árvore reportada. Com esse índice, a AMMA pode visualizar uma lista das árvores reportadas, organizadas de acordo com o grau de risco. Isso permite que as intervenções sejam priorizadas conforme a gravidade da situação, otimizando a alocação de recursos e a eficiência das ações preventivas.

#### Resumo do Escopo
---- 

O projeto é uma solução de software que possibilita à população reportar árvores doentes ou em risco de causar acidentes na cidade. Com base nesses relatórios, o sistema calcula automaticamente um "índice de risco", auxiliando a AMMA na priorização das intervenções de acordo com a gravidade de cada caso, otimizando o uso de recursos e promovendo ações preventivas mais eficazes.

#### Relação com outros sistemas
----
Atualmente as solicitações de retiradas de árvores são realizadas abrindo um processo no site da prefeitura, conhecido como PED. Não é utilizado nenhum sistema para priorização de riscos ou distribuição dos processos abertos entre os servidores da Agência Municipal do Meio Ambiente, responsáveis por analisar se as solicitações de poda e estirpação podem ou não ser encaminhadas para a empresa responsável pela realização das mesmas. Sistemas relacionados que poderiam se encaixar como facilitadores para solucionar o problema que o software desenvolvido se propõe a solucionar são softwares de gestão e priorização de processos.

#### Fontes de requisitos
---- 
A elicitação de requisitos foi realizada junto a servidores da AMMA e cidadãos da população em geral através da aplicação de formulários.

#### Equipe
---- 
AUGUSTO BORGES DE MOURA - Líder de desenvolvimento, Desenvolvedor Full Stack  
ESTER ADAIANNE OLIVEIRA FERREIRA - Product Owner, Desenvolvedora Full Stack  
LÍBNA RAFFAELY DE JESUS COSTA - Designer, Desenvolvedora Front End  
PHABLO TAVARES PAIXÃO - Analista de requisitos, Desenvolvedor Front End  
VICTOR GABRIEL PACHECO GONTIJO - Designer, Desenvolvedor Back End  

#### Cronograma
----
**18/10/2024** - Sprint Planning  
**01/11/2024** - Entrega da primeira iteração  
**02/11/2024** - Sprint Review  
**04/11/2024** - Sprint Planning  
**29/11/2024** - Entrega da 2a iteração  
**30/11/224** - Sprint Review  
**02/12/2024** - Sprint Planning  
**13/12/2024** - Entrega final do MVP  

#### Prévia do backlog do produto
----
HU001 - Reportar árvore com risco  
HU002 - Consultar relatórios de reportes anteriores  
HU003 - Verificar os processos abertos
HU004 - Verificar índice de ocorrências por localidade/época  
HU005 - Login com a matrícula de servidor  
HU006 - Cadastro de fatores de risco para priorização de processos  
HU007 - Acessar o andamento do caso reportado  
HU008 - Alterar status de andamento do processo  
HU009 - Atualizar o relatório com imagens da ação realizada  
HU0010 - Login de cidadão

#### MVP e entregáveis
---- 
MVP:
- Cadastro do Usuário
- Cadastro do Servidor
- Abertura do Reporte (poda e estirpação)
- Histórico de Reportes para usuário
- Histórico de  Reportes para Servidor
- Localidade dos Reportes para servidor

Entregáveis:
- Documentação inicial: descrição do problema, objetivos e requisitos.
- Protótipo de interface: telas principais
  
