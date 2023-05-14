# 1을 선택하면 아래 1을 제외한 케이스 중 최댓값, 몇번째 선택했는지 남기기

def solution(land):

    answer = 0

    # 최댓값, 몇번째 라인인지 고르기

    case=[[land[0][0],0],[land[0][1],1],[land[0][2],2],[land[0][3],3]]

    

    for i in range(1,len(land)):

        for j in range(len(case)):

            

            if case[j][1]==0:

            

                sum1=case[j][0]+land[i][1]

                sum2=case[j][0]+land[i][2]

                sum3=case[j][0]+land[i][3]

                case[j][0]=max(sum1,sum2,sum3)

                

                if sum1 > sum2 and sum1> sum3:

                    case[j][1]=1

                    

                elif sum2> sum1 and sum2> sum3:

                    case[j][1]=2

                    

                elif sum3> sum1 and sum3> sum2:

                    case[j][1]=3

                    

            elif case[j][1]==1:  

                

                sum1=case[j][1]+land[i][0]

                sum2=case[j][1]+land[i][2]

                sum3=case[j][1]+land[i][3]

                case[j][0]=max(sum1,sum2,sum3)

                

                if sum1 > sum2 and sum1> sum3:

                    case[j][1]=0

                elif sum2> sum1 and sum2> sum3:

                    case[j][1]=2

                elif sum3> sum1 and sum3> sum2:

                    case[j][1]=3

            

            elif case[j][1]==2:

                

                sum1=case[j][2]+land[i][0]

                sum2=case[j][2]+land[i][1]

                sum3=case[j][2]+land[i][3]

                case[j][0]=max(sum1,sum2,sum3)

                

                if sum1 > sum2 and sum1> sum3:

                    case[j][1]=0

                elif sum2> sum1 and sum2> sum3:

                    case[j][1]=1

                elif sum3> sum1 and sum3> sum2:

                    case[j][1]=3

                    

            elif case[j][1]==3:

                sum1=case[j][3]+land[i][0]

                sum2=case[j][3]+land[i][1]

                sum3=case[j][3]+land[i][2]

                case[j][0]=max(sum1,sum2,sum3)

                

                if sum1 > sum2 and sum1> sum3:

                    case[j][1]=0

                elif sum2> sum1 and sum2> sum3:

                    case[j][1]=1

                elif sum3> sum1 and sum3> sum2:

                    case[j][1]=2

                    

    for c in range(len(case)):

        if case[c][0]> answer:

            answer=case[c][0]

    return answer
