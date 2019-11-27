# TaskGenerator
This program generate tasks by given utilization and total memory usage

## Input
자세한 내용은 파일 내부의 설명을 참고하세요.
- input_mem.txt: 메모리의 종류, 종류 별 실행률, 용량, active 상태의 전력소모량, idle 상태의 전력소모량 
- input_task.txt: 프로세서 코어의 개수, 태스크의 개수, 최악수행시간 범위, 총 메모리 용량, 목표 cpu utilization

## Run
생성하고자 하는 태스크셋에 대한 정보를 위 input 파일에 형식을 맞추어 입력하고, Main.py를 실행한다.<br>

## Output
생성된 태스크셋에 대한 정보가 task_generated.txt로 출력된다.

## Demo
Task Generator Demo: util = 50 인 태스크 100개 생성 결과
https://youtu.be/XJMImfe-JPs
