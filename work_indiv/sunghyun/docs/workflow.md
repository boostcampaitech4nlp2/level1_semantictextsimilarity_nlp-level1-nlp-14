# Work Flow Doucmentation
#### NLP_14조_번역해조_T4126_염성현
- - -
## 0. Thoughts
10/26 : Data 접근 + Model 접근
- Data 접근 : Augmentation + Feature Extraction + Tokenization + 전처리
    - Augmentation : Label 5 데이터 때문이라도 필요하지 않을까?
    - Feature Extraction : 각 라벨이 담고 있는 정보는 무엇일까? 부가적인 내용의 의미는?
    - Tokenization : BPE? 한국어에 맞는 방법은?
    - 전처리 : 불용어 처리, 대체 단어 탐색
        -> 필요한가?
        -> Embedding 측면으로 접근한다면?  
        #
- Model 접근 : Regression/Classification & proba threshold + Ensemble(WBF?, Weighted box fusion) + hyperparameter tuning
    - Regression이 Base, 경향성을 강화시키고 threshold를 주려면 Classification
    - Ensemble : 다양한 Ensemble 방법이 존재, 잘 짜여진 단일 모델이 Ensemble 보다 좋을 수 있다.
    - Hyperparameter tuning : Ray? wandb.sweep?
- Competition에 대한 고찰
    - 일반적인 대회   
        -> 당연히 성능, 순위가 중요, 타 대회 코드나 모듈에 의존   
    - 부스트 캠프 대회    
        -> 교육 과정, podium의 의미?, 과정과 기록, Struggle, 잘하는 걸 증명하기만 하는 것은 별 의미가 없다. 의존하느냐 협업하느냐.   
    - 코드 공유의 의미    
        -> 고도화 시키지 않은 코드는 공유해도 무방, podium에 들지 못할 가능성, 스스로를 어필하는 방법.   
- - -
## 1.EDA
- - -
### 1-1.EDA &insights

[EDA File](../codes/simpler_eda.ipynb "to file")
- Raw data
    - 비문법적 표현, 인터넷 용어가 많이 보인다.
    - 단어의 분절(split)이 잘 되지 않은 문장들이 보인다.
    - 출현 횟수가 1 또는 적은 단어들이 많이 보인다.  
    #
- Label
    - 0 라벨 데이터의 숫자가 많고 그 비율 또한 상당히 높다.
    - 5 라벨 데이터의 숫자와 비율은 반면에 매우 적고 매우 낮다.
    - 0 라벨 데이터에 치우치거나 5 라벨 데이터 예측이 잘 안되는 것이 우려된다.
    - 5 라벨 최대 토큰 개수가 문장 길이에 비해 매우 적게 나왔다.   
        -> 단어의 분절화가 잘 이루어지지 않았거나 비문법적 표현이 많이 사용되었을 가능성이 있다.  
        #
- Sentence Length, Token Counts
    - 문장 길이는 40, 토큰 개수는 10을 기준으로 데이터 수가 급격히 줄어들었다.
    - 데이터의 치우침이 있는 것 같아 보인다. skewness 확인해 볼 필요성.  
    #
- Correlation
    - 약 0.8의 문장 길이 및 토큰 상관 계수
    - 두 문장 사이의 관계에서 이것이 유의미한 것인가는 더 따져봐야 함  
    #
- Source
    - 총 3가지 유형의 데이터 셋, 그러나 rtt와 sampled가 나뉘어 6개의 데이터셋이 있다.
    - 유형 별 train 성능을 비교해보는 것도 유의미할 것 같다.  
    # 
- Most tokens, n-gram
    - 전처리가 되지 않아 현재로서는 큰 의미를 갖지 못하는 것 같다.
    - 불용어 처리도 필요해 보이고 다양한 tokenization 방법론을 사용해 봐야할 것 같다.

### 1-2.Further

- 비문법적 표현 및 인터넷 용어 처리
- 불용어 처리
- 다양한 tokenization 방법 적용
- Data Augmentation, Data Filtering
    - 라벨 별 혹은 문장 길이 별 데이터 비율을 맞춰주는 것 고려
    - 라벨 별 혹은 문장 길이 별 데이터 filtering, 각각의 proba에 대해 각기 다른 threshold를 주는 것 고려
    - 출현 횟수가 적은 token에 대한 처리 고려

