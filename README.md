# CYKalgorithm
membership problem  
Chomsky 정규형인 문법에 의하여 생성되는 모든 언어에 대하여 소속성을 결정한다.
Input  

she eats a fish with a fork  
12  
S->NP VP  
VP->VP PP  
VP->V NP  
VP->eats  
PP->P NP  
NP->Det N  
NP->she  
V->eats  
P->with  
N->fish  
N->fork  
Det->a  

Output  
[['NP'], ['S'], [], ['S'], [], [], ['S']]  
[[''], ['VP', 'V'], [], ['VP'], [], [], ['VP']]  
[[''], [''], ['Det'], ['NP'], [], [], []]  
[[''], [''], [''], ['N'], [], [], []]  
[[''], [''], [''], [''], ['P'], [], ['PP']]  
[[''], [''], [''], [''], [''], ['Det'], ['NP']]  
[[''], [''], [''], [''], [''], [''], ['N']]  
yes
