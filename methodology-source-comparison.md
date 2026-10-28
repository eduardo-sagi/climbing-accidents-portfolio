# Comparação de fontes por país — acidentes em escalada

**Estado:** camada de análise separada; não altera o portfolio canônico.  
**Data da triagem:** 2026-10-28  
**Escopo:** escalada esportiva, boulder e tradicional/multilargo.  
**Regra central:** comparar perfis dentro de cada sistema; não somar contagens de populações incompatíveis.

## 1. Portfolio canônico preservado

O portfolio visual canônico permanece em `index.html`, sem nova seção conceitual. Esta matriz é um artefato de pesquisa para orientar a próxima rodada quantitativa.

- HTML canônico: `5719679aa88be58c1158da269a53e3df35be0fec9bb90c0872bf1aa741701ad4`
- ZIP canônico: `842f1950d234ce3ad1dd4340bc840e75c08e721afe2676a4eb7d09d475532a48`

## 2. Matriz internacional de fontes

| País/região | Fonte | Período/escala identificada | Modalidade/ambiente | Unidade de observação | Variáveis úteis | Comparabilidade | Gate |
|---|---|---|---|---|---|---|---|
| Suécia | Swedish Climbing Association/SKF + estudo publicado | 2008–2019; estudo com n=38 | Sport, boulder e trad; outdoor | Pessoa lesionada/lesão autorreportada com ligação a registro clínico | mecanismo, região corporal, fratura, modalidade | Boa para perfil de lesão entre modalidades; não é incidência nacional | Extrair tabelas completas e preservar denominador de seleção |
| Áustria | National Registry for Mountain Accidents | 2005–2018; n=2.992 emergências | Mistura de sport, boulder, gelo e alpina; outdoor | Emergência/ocorrência registrada | causa, consequência, gravidade, morte, resgate | Útil para gravidade e mecanismos; não misturar com lesões suecas | Filtrar linhas de modalidade antes de qualquer comparação |
| Alemanha/Áustria | DAV/KLEVER Kletterhallen-Unfallstatistik | 2024–2025; 261 acidentes avaliados em 2024 e 252 em 2025 | Boulder e escalada indoor | Acidente de academia com ambulância ou lesão moderada+ | quedas, operação de dispositivo, região corporal, gravidade, fatalidade | Forte para indoor; não representa outdoor nem todos os incidentes | Preservar relatórios anuais e confirmar universo de academias |
| Suíça | University Hospital Bern ED | abr/2012–dez/2018; n=78 pacientes | Escalada outdoor ampla; inclui boulder e sport, com necessidade de filtro | Paciente atendido em pronto-socorro | mecanismo, fratura, ISS, UIAA MedCom, internação, morte | Comparável somente a outras coortes hospitalares; não a relatos voluntários | Extrair tabela por modalidade, se disponível |
| França/Europa | SERAC/Camptocamp | lançado em 2015; quase 400 relatos até meados de 2020; 88 de escalada com um ou mais largos | Trad/multilargo, rocha alpina, incidentes e quase-acidentes | Relato voluntário participativo | tipo de incidente, fatores, consequências, quase-acidente | Bom para near miss e cadeia do evento; forte viés de participação | Mapear exportação, categorias e duplicidade |
| Reino Unido/Irlanda | BMC Incident & Near-Miss Reporting | série contínua; mais de 150 relatos recentes/históricos reportados pela BMC | Sport, trad, multilargo e near miss; outdoor e outros ambientes | Relato voluntário publicado após moderação | causa, atividade, lesão, gravidade, erro de segurança | Bom para near miss e mecanismos; não é censo | Exportar páginas e classificar modalidade/país |
| EUA/Canadá | AAC/ANAC | publicação anual desde 1948; cobertura contemporânea variável | Sport, trad, multilargo e outras escaladas; outdoor | Relato selecionado e publicado | mecanismo, contexto, desfecho, fatores contribuintes | Forte para casos graves e lições; seleção editorial impede taxa | Separar EUA/Canadá, ano e modalidade; deduplicar derivados |
| EUA/Canadá | ecaroom/climbing-accidents | dados derivados; cobertura útil predominantemente até 2018; 2.770 registros divulgados | Tags derivadas para sport/trad e outras | Registro editorial derivado | campos de atividade, localização, gravidade e narrativa | Reprodutível para exploração, mas não independente do ANAC | Rastrear cada linha à fonte AAC/ANAC e marcar duplicatas |
| Austrália | Australian Climbing Accident Register/ACAR | série online atual; histórico anterior heterogêneo | Escalada recreativa, acidentes e serious near miss; outdoor predominante | Acidente/near miss/resgate autorreportado | estilo, causa primária/secundária, lesão, desfecho | Bom para comparação de mecanismos; cobertura voluntária | Confirmar filtros, datas, licença e exportação |
| Nova Zelândia | NZAC Reporting / NZMSC | séries de segurança e tendências nacionais; janela exata por modalidade pendente | Escalada e outras atividades outdoor | Relato, resgate, fatalidade ou série de participação | fatalidade, resgate, tendência, exposição em alguns indicadores | Pode fornecer denominador nacional em alguns estratos, mas mistura atividades | Isolar rock climbing de montanhismo/tramping |
| Japão | JMSCA/JWAF Mountain Accident Database | base iniciada em 2003; 4.669 registros até 2023 | Acidentes de montanha amplos; sport/boulder precisam ser isolados | Pessoa/registro de acidente | 687 campos: local, tratamento, causa, resgate e contexto | Potencialmente rica, mas inadequada para agregado sem filtro | Obter relatório/dicionário e excluir montanhismo não técnico |
| Países Baixos | Dutch Injury Surveillance System | 1998–2001; cerca de 110 atendimentos/ano e 8/100.000 horas | Climbing injuries; definição histórica ampla | Atendimento em pronto-socorro | atendimentos e denominador de horas | Exemplo valioso de taxa com denominador, mas antigo e não harmonizado | Usar apenas como referência metodológica histórica |
| Internacional | UIAA Accident Data Reporting | catálogo de sistemas, não uma base homogênea | Sistemas nacionais variados | Depende do sistema | escopo, finalidade, método e links | Comparável como metadado de cobertura, não como contagem global | Usar como índice de fontes e atualizar a matriz |

## 3. Comparações que serão permitidas

### Comparações de composição interna

- proporção de quedas dentro de cada fonte;
- proporção de fraturas, entorses e contusões dentro de cada estudo;
- distribuição de lesões por região corporal;
- composição por modalidade dentro do mesmo dataset;
- gravidade e hospitalização dentro de coortes hospitalares;
- proporção de quase-acidentes dentro de sistemas que os coletam;
- tendência anual somente dentro da mesma série e definição.

### Comparações que exigem o mesmo universo

Uma comparação percentual entre países só entra no mesmo gráfico quando houver compatibilidade mínima em:

1. população;
2. unidade de observação;
3. definição de caso;
4. período;
5. ambiente;
6. modalidade;
7. regra de inclusão;
8. denominador ou interpretação explicitamente descritiva.

### Comparações proibidas

- somar n=38 da Suécia, n=2.992 da Áustria e n=430 pacientes da Alemanha;
- chamar relatos AAC/ANAC de incidência;
- comparar fatalidade de um registro de trauma grave com todos os atendimentos;
- misturar boulder indoor alemão com boulder outdoor sueco sem rotular o ambiente;
- usar a ausência de relatos como ausência de acidentes;
- tratar GitHub e AAC/ANAC como fontes independentes;
- produzir uma “taxa mundial” sem denominador comum.

## 4. Painéis estatísticos recomendados

1. **Pequenos múltiplos por fonte:** mecanismo, modalidade e gravidade, sempre com `n`, período e unidade.
2. **Barras percentuais internas:** queda, fratura, hospitalização e fatalidade dentro de cada dataset.
3. **Heatmap de cobertura:** país × fonte × modalidade × ambiente × desfecho disponível.
4. **Matriz de comparabilidade:** fonte × população × unidade × denominador × viés principal.
5. **Timeline de cobertura:** 2008–2025, distinguindo publicação, período observado e disponibilidade atual.
6. **Painel de quase-acidentes:** SERAC, BMC, ACAR, SKF e sistemas equivalentes, sem misturar com emergências hospitalares.
7. **Painel indoor:** DAV/KLEVER, estudos de visitas e estudos hospitalares de boulder.
8. **Painel outdoor:** SKF, AAC/ANAC, SERAC, ACAR e coortes hospitalares, separados por tipo de registro.

## 5. Próxima extração quantitativa

A próxima tabela-mestra deverá conter:

```text
source_id
país
fonte
período
modalidade
ambiente
unidade_observacional
n_total
n_acidentes
n_quase_acidentes
n_feridos
n_graves
n_hospitalizados
n_mortes
mecanismo
região_corporal
denominador
definição_de_caso
método_de_coleta
cobertura
licença
risco_de_duplicidade
referência
```

**Decisão metodológica:** o portfolio permanece como peça visual canônica; a camada comparativa será desenvolvida como análise auditável separada e só depois poderá alimentar novos plots, sem alterar a identidade visual aprovada.