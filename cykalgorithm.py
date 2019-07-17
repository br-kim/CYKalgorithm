# variable
rules = []
w = input().split(' ') # 문자열을 ' '으로 구분하여 입력한다.
roop = int(input())
for i in range(roop) :
    rules.append(input().split('->')) # 규칙을 ' '로 구분하여 입력한다.

table = [[['' for col in range(1)] for row in range(len(w))] for depth in range(len(w))]

# calculate bottom row
def cal_bottom(rules) :
    result3 = []
    for rule in rules :
        if(substr[0] == rule[1]) :
            result3.append([rule[1]]) 
    return result3

# product
def product(a,b):
    result = []
    for i in a :
        for j in b:
            result.append([i,j])
    return result

def fill_table(begin,end,table):
    result = []
    for i in range(begin,end) :
        result += product(table[begin][i],table[i+1][end])
    return result

def check_rule(table,rules):
    result = []
    for i in table[v][j] :
        for rule in rules :
            if(i == rule[1].split(' ')) and (rule[0] not in result) : # 생성 가능하고 중복되지 않을 경우
                result.append(rule[0]) #  가능한 결과에 추가
            
    return result

def print_table(table):
    for i in table : 
        print(i)

def check_table(table): #결과 출력 맨 끝에 S가 없다면 생성 불가능하다.
    if 'S' not in table[0][len(w)-1] :
        print('no')
    else:
        print('yes')

for i in range(1,len(w)+1) : #이전에 저장한 테이블을 가지고 위의 테이블을 채워나간다
    for s_begin in range(len(w)) :
        for s_end in range(s_begin,len(w)) :
            substr = w[s_begin:s_end+1]
            if len(substr) == i :
                if s_begin == s_end : 
                    table[s_begin][s_end] = cal_bottom(rules) # 한글자짜리는 문자열과 비교
                else:
                    table[s_begin][s_end] = fill_table(s_begin,s_end,table) #반복문을 통해 해당되는 행렬을 전부 product 후 합해준다.
    for v in range(len(table)) : #한 줄을 다 생성하고 나서 문법으로 변환 가능한지 확인
        for j in range(v,len(table[v])):
            # if i == 1: continue #첫번째는 문법 변환 x
            result1 = check_rule(table,rules)
            if v+i-1 == j : #바로 전에 채워진 테이블 줄에 대해서만 바꾼다
                if result1 != [] : #생성 가능한 문법으로 바꿔준다
                        table[v][j] = result1
                else : #생성 가능한 문법이 없으므로 공집합
                        table[v][j] = []

print_table(table)
check_table(table)