### News Source Network 

#### 개요

#### 목적

#### 구현 List

#### 제공 Raw Data
   - 정박사님께서 제공해주실 Raw Data 입니다
````sh
# 인용문 고유ID
# 10개를 예로 했지만 실제로는 3300개정도
q_id={0:23, 1:10, 2:39, 3:44, 4:14, 5:33, 6:21, 7:66, 8:88, 9:11}

# 인용문 Label
# 같은 Label은 같은 클러스터를 구성한다고 보면 됨
# q_id의 수만큼 있고 각각의 Label을 표시

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

#### To Do List

   - 참고 그래프입니다(참고만;;)
![connection](https://raw.githubusercontent.com/kowonsik/NQNA/master/png/connection_path.png)

#### 참고
   - 정박사님 NLP Git
    - https://github.com/deokwooj/NLP
    - 정보원의 정보를 Dictionary로 변환
       - https://github.com/deokwooj/NLP/blob/master/binfiles/NewsSrcObjs.p
    - 인용문의 정보를 Dictionary로 변환
       - https://github.com/deokwooj/NLP/blob/master/binfiles/NewsQuoObjs.p
    - 연관도 메트릭스 정보
    
   - 정박사님 작성중인 논문
    - https://github.com/kowonsik/NQNA/blob/master/doc/icsc_nna.pdf
