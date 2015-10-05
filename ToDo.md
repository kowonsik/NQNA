### News Quatation Network Analysis 

#### 개요

   - 뉴스기사, 인용문, 정보원에 대한 연관도 분석을 위해, 세 가지 데이터가 서로 관련이 있음을 데이터 연결 그래프로 도식화
   - 빈번한 연결의 개념을 수치화 할 수 있도록 모델을 설계
   - 모델은 각 데이터가 뉴스기사에 포함되는 빈도수를 기준으로 연산하도록 정의하였으며, 포함 빈도에 따라 연관성 행렬을 구성하고, 이 행렬들의 원소 간에 거리(길이)를 연산하여 각 데이터 사이의 연관성 지표를 수치로 계산


#### 구현 List(To Do List)

    1. 인용문의 연결 그래프
       - 실행시 옵션을 주어 그래프의 상태 정보를 볼수 있도록 구현

````sh
       - 옵션 예
         - python -show q_id  # id만 표시
         - python -show all   # 모두 표시
         - python -show exemplar   # exemplar만 표시
         # 모든 노드에 대한 Degree of Neighbor의 랭킹을 매기고 가장 많은 2개의 exemplar를 표시
         - python -show maxngb 2   
         - python -show label 1   # 1번 Label 만 표시
````

       - 같은 Label은 exemplar 중심으로 연결됨
       - 다른 Label에 연결될때는 exemplar 를 통해서 연결됨
       - node의 정보는 q_id와 인용문의 일부(10자정도)를 표시해주면 됨
       
    2. 인용문의 연결 정보를 엑셀에 저장
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
       

   - 참고 그래프입니다(참고만;;)
![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/connection_path.png)

#### 제공 Raw Data
   - 정박사님께서 제공해주실 Raw Data 입니다
````sh
# 인용문 고유ID
# 10개를 예로 했지만 실제로는 3300개정도
q_id={0:23, 1:10, 2:39, 3:44, 4:14, 5:33, 6:21, 7:66, 8:88, 9:11}

# 인용문 Label
# 같은 Label은 같은 클러스터를 구성한다고 보면 됨
# q_id의 수(3300)만큼 있고 각각의 Label을 표시

q_label={0:0, 1:4, 2:1, 3:2, 4:3, 5:4, 6:1, 7:2, 8:2, 9:1}

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
