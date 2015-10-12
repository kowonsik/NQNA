(추가 수정 중입니다. 잘못된 부분은 고쳐 주세요. 핵심 줄거리, 실행 내용)

### News Quatation Network Analysis 

뉴스기사 빅데이터 처리를 하여 내용 분석함
 - 전체적인 과제의 목표
   - 기사 내용 중 인용문의 사실성, 정확성을 분석함 
   - 언론 뉴스 노출 빈번도 등을 분석하면 빅데이터 처리만으로 신뢰도가 높은 인용문, 정보제공자를 찾아낼 수 있음을 가정함
 - 인용문은 인터뷰 내용 이나 제공한 정보가 인용부호로 만들어진것
 - 인용문을 언급한 정보원(정보제공자, 정보발언자)
 - 결국, 정보제공자가 신뢰성이 높은사람일 수록 기사의 신뢰도가 올라감
 - SW 로 정보의 충실도를 판단할 수 있음. 방대한 분량의 신문 정보를 SW를 이용하여 신속하게 분류, 통계 낼 수 있음

#### 개발 개요

   - 뉴스기사, 인용문, 정보원에 대한 연관도 분석을 위해, 세 가지 데이터가 서로 관련이 있음을 데이터 연결 그래프로 도식화
   - 빈번한 연결의 개념을 수치화 할 수 있도록 모델을 설계
   - 모델은 각 데이터가 뉴스기사에 포함되는 빈도수를 기준으로 연산하도록 정의하였으며, 포함 빈도에 따라 연관성 행렬을 구성하고, 이 행렬들의 원소 간에 거리(길이)를 연산하여 각 데이터 사이의 연관성 지표를 수치로 계산

![association](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/s-q-a_association.png)

#### 소프트웨어 입력 파일 및 연관도 도출 데이터 형식
![association](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/xls_files_with_arrow.png)

------

#### 10/13 까지 구현 해야하는 기능 항목

1. 위 그림의 A - Q - S 사이의 매트릭스를 구해서, 상호 의존도 행렬을 만들고 그 결과는 바이너리 파일로 저장
    * A (기사) Q (인용문) S (정보제공자)
    * Dr. Jung's SW output file이 제공될 것임
2. 여러개 바이너리 행렬 데이터를 이용하여, 각 행렬의 element 들 간의 의존도 그래프를 그리는 것이 목표임
    * ___현재 목표는 Q (인용문) 들을 상호 연관도를 네트워크 그래프로 그리는 것임___

<pre>
질문) A - Q - S 연관도 작성 방법은? 
    - 세가지에 대한 모든 연관도를 그리는 것은 많은 변수와 조건으로 인해 쉽지 않아 보임, 그래서 이번에는 부분별로 작업을 수행해서 상호 비교함
    - Q - A 의 연관도를 도식하고, S - A의 연관도와 비교함
    - S - A 는 Q - A 연결도를 만드는 것 보다 상대적으로 수월할 것으로 예상됨
</pre>

##### 기능 구현 내용
   * __입력 데이터 목록__  (배열, 현재 구현은 Dictionary 객체로 구현됨)
     * (형식:DICT) 인용문 ID : 인용 문장의 아이디
     * (형식:DICT) 레이블 ID (= 클러스터 ID) : Dr. Jung's 분석 SW 결과로 ID 할당
     * (형식:DICT) Examplar ID : 인용문 ID - 레이블 (클러스터)의 대표 인용문, 클러스터 헤드
     * (형식:2차원배열,행렬) Examplar ID 들 간의 연결 표시 행렬 
   
   * __각 인용문 간의 네트워크 연결 그래프 그리는 방법__
     * 파이썬의 NetworkX 패키지를 이용하여 그림
     * graph ((1,2),(5,10),(10,1)) 이런방법으로 호출하면, 1-2 연결, 5-10 연결, 10-1 연결로 각 노드번호를 연결하여 그래프를 그린다 - 여기서 (1,2)로 표시되는 노드번호는 인용문 ID, Examplar ID 임 - 모두 다 인용문 ID 임  

-------

- 인용문의 연결 그래프
   - 실행시 옵션을 주어 그래프의 상태 정보를 볼수 있도록 구현
   - 인용문의 연결은 상호 의존성이 있음을 의미
   - (의문) 인용문들이 서로 연결되어 있다면, 어떤 수치로 연결을 결정하는지?
   - (의문) 입력 되는 많은 인용문 데이터 중에, 어떤 인용문을 (검색 기준) 인용문으로 정하는 지?

````sh
- 옵션 예
- python -show q_id  # id만 표시
- python -show all   # 모두 표시
- python -show exemplar   # exemplar만 표시
- python -show label 1   # 1번 Label 만 표시
# 모든 노드에 대한 Degree of Neighbor의 랭킹을 매기고 가장 많은 2개의 exemplar를 표시
# Degree of Neighbor란 자신과 연결되어 있는 주변노드의 수를 의미 함
- python -show maxngb 2   

````
   - 같은 Label은 exemplar 중심으로 연결됨
   - 다른 Label에 연결될때는 exemplar 를 통해서 연결됨
   - node의 정보는 q_id와 인용문의 일부(10자정도)를 표시해주면 됨

-------

- 인용문의 연결 정보를 엑셀에 저장
   - 같은 Label(클러스터)의 id(node)의 depth는 0
   - 연결된 클러스터의 Depth는 1이며 클러스터 간에는 다수의 Path가 있어 모든 경우의 수를 다 고려하여 처리
   - 아래 그림을 보면 
   - Label 1에서 Label 2로 가는 Depth가 직접가는 1 이있고
   - Label 1에서 Label 4를 거쳐 Label 2로 가는 Depth가 2인경우가 있음

![cluster](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/cluster.png)

       - Sheet 1 : qid, q_label, q_exemplar
       - Sheet 2 : Label 연결 Matrix
       - Sheet 3 : Label 연결 Depth <= 1 인경우(Depth가 0 or 1인 경우가 있으면 1, 없으면 0을 넣으면 됨)
       - Sheet 4 : Label 연결 Depth <= 2 인경우(Depth가 0 or 1 or 2인 경우가 있으면 1, 없으면 0을 넣으면 됨)
       - Sheet 5 : Label 연결 Depth <= 3 인경우(Depth가 0 or 1 or 2 or 3인 경우가 있으면 1, 없으면 0을 넣으면 됨)
       

   - 아래 예시와 같이 다양한 경로를 가짐
   - exemplar 자신에게 돌아오는 경로는 아래 그림 결과에 상관없이 0으로 저장

![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/path.png)

   - 참고 그래프입니다(참고만;;)
![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/connection_path.png)
       - Sheet 1 : qid, q_label, q_exemplar
![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/id.png)
       - Sheet 2 : Label 연결 Matrix
![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/matrix.png)
       - Sheet 3 : Label 연결 Depth <= 1 인경우
![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/d1.png)
       - Sheet 4 : Label 연결 Depth <= 2 인경우
![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/d2.png)
       - Sheet 5 : Label 연결 Depth <= 3 인경우
![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/d3.png)

#### 연결도(네트워크)를 그리기 위한 입력 파일
   - 입력데이터는 Dr. Jung's Bin File 입니다. (아직 이 리포에는 없습니다.)
````sh
# 인용문 고유ID
# 10개를 예로 했지만 실제로는 3300개정도
q_id={0:23, 1:10, 2:39, 3:44, 4:14, 5:33, 6:21, 7:66, 8:88, 9:11}
>>>> (질문) 왜 q_id는  key : value 로 저장을 하는가? 그냥 아이디만 사용하면 될것 같은데....
>>>> (답변) 네..
>>>> (답변) 처음 시작을 디션어리로 해버려서;;

# 인용문 Label
# 같은 Label은 같은 클러스터를 구성한다고 보면 됨
# q_id의 수(3300)만큼 있고 각각의 Label을 표시
q_label={0:0, 1:4, 2:1, 3:2, 4:3, 5:4, 6:1, 7:2, 8:2, 9:1}
>>>> (질문) Label 은 어떤 기준 으로 결정 되는가? q_id 와 q_label은 key 값으로 구분 하는지?

>>>> (질문) 즉 q_lable[1], q_id[1] 이면, 인용문 10번은 레이블(클러스터 Id)가 4 라는 의미인지?
>>>> (답변1) 배열과 동일한 매핑임. q_id[5] 은 q_label[5]와 연결되어 있는 의미임. 
>>>>>>>>(숫자를 찾아서 코딩하기엔 한단계 더 들어가야 하기때문에 복잡하니, 배열로 바꿔주면 좋겠음) 
>>>> (답변2) 그리고 q_label[5]가 4이므로 q_id[5]인 33과 같은 클러스터(label)를 형성합니다(10번 & 33번)
>>>> q_id 와 q_label value 의 관계는.. 예를 들어.. q_id의 첫번재 value 23이 q_lable의 첫번째 value 인 0번과 매핑됩니다..
>>>> q_id value 10번과 33번의 자리(인덱스, 키)에  q_label(동일인덱스, 키)에 해당하는 value 4로 같으므로 같은 label

# Label의 대표 ID(클러스터 헤더)
# q_label 수 만큼 q_exemplar 존재
q_exemplar={0:23, 1:39, 2:44, 3:14, 4:33}

# Label의 연결도를 메트릭스로 표현(1: 연결, 0: 비연결)
# 5x5 배열 예지만 실제로는 q_label x q_label 배열임
G_q = np.matrix([\
    [1, 1, 1, 0, 0],\
    [1, 1, 1, 0, 1],\
    [1, 1, 1, 1, 0],\
    [0, 0, 1, 1, 0],\
    [0, 1, 0, 0, 1]])
    
````

#### 자료
   - 정박사님 NLP Git
    - https://github.com/deokwooj/NLP
    
    - 정보원의 정보를 Dictionary로 변환
       - https://github.com/deokwooj/NLP/blob/master/binfiles/NewsSrcObjs.p
    - 인용문의 정보를 Dictionary로 변환
       - https://github.com/deokwooj/NLP/blob/master/binfiles/NewsQuoObjs.p
       
    - q_id, q_label, q_exemplar, G_p(메트릭스)

#### 참고    
   - 정박사님 작성중인 논문
    - https://github.com/kowonsik/NQNA/blob/master/doc/icsc_nna.pdf
